#!/usr/bin/env python3
"""Microgame Maker — universele ZIP-generator v2 (klonen-en-vullen).

Ondersteunde LearnStrike-speltypes (autodetectie per ronde):
  tf     Waar/Niet-waar          flat: Description;Feedback;Target;Image
  mc3/4  Meerkeuze               flat: Description;Feedback;Image;Correct;Distractor01..05
  loa    Locate & Answer         flat: ZoomedText;SpotImage;...;Distractor05Image (23 kolommen)
  pum    Puzzle Motion           secties: [TARGETS] + [AGENTS]/[DRAGGABLES]
  sort   Sort-to-target/Complex  secties: [DRAGGABLES] (Target01..05 -> target-namen)
  vast   Vaste rondes            geen pool; alleen teksten (Localisation) vervangen
MIX-containers: bovenstaande per ronde, submap-prefix uit het ZIP.

Gebruik:
  python generate_zip.py --inspect skelet.zip
  python generate_zip.py skelet.zip content.json out.zip [--images map]

Content-JSON:
  {"talen": ["nl"], "localisation": {"<exacte key>": {"nl": "..."}},
   "items": [...]                       # kortschrift: single-pool tf/mc
   "rondes": [{"uuid": "...", ...}]}    # multi-ronde; velden per speltype:
     tf:   items: [{stelling:{nl:..}, waar:true, feedback:{nl:..}}]
     mc:   items: [{vraag, correct, distractors:[..], feedback}]  (alle {taal:tekst})
     loa:  items: [{vraag:{nl:..}, correct:{tekst:{nl:..},feedback:{nl:..}},
                    distractors:[{tekst,feedback}...], spot_beeld?, zoom_beeld?}]
     pum:  targets?: [{name, label:{nl:..}, feedback?:{nl:..}}]   (labels op bestaande targets)
           agents: [{tekst:{nl:..}, feedback:{nl:..}, goed_feedback?, target:"tar-x", beeld?}]
     sort: draggables: [{tekst:{nl:..}, feedback:{nl:..}, goed_feedback?, target:"target 1", beeld?}]
     vast: (geen rondes/items; alleen localisation)
Principes: Configuration.json blijft byte-gelijk; Localisation-keys onaangetast;
UTF-8-BOM / ';' / CRLF; het script valideert en weigert bij fouten.
"""
import json, sys, zipfile, io, os, re, copy

BOM = "﻿"
CRLF = "\r\n"
TF_HEADER = "Description;Feedback;Target;Image"
MC_HEADER = "Description;Feedback;Image;Correct;Distractor01;Distractor02;Distractor03;Distractor04;Distractor05"
AG_HEADER = "Description;Feedback;GoodFeedback;Image;Target01;Target02;Target03;Target04;Target05"
LOA_COLS = ["ZoomedText","SpotImage","ZoomedImage","NotAnsweredSprite","CorrectAnsweredSprite",
            "CorrectText","CorrectFeedback","CorrectImage"] + \
           [f"Distractor0{i}{s}" for i in range(1,6) for s in ("Text","Feedback","Image")]
LOA_HEADER = ";".join(LOA_COLS)
TRUE_HINTS = ("correct","waar","true","juist","feit")
FALSE_HINTS = ("false","fout","niet","onwaar","fabel")

def esc(v):
    v = (v or "").replace("\r"," ").replace("\n"," ").strip()
    if '"' in v or ";" in v:
        v = '"' + v.replace('"','""') + '"'
    return v

def txt(d, lang):
    if d is None: return ""
    if isinstance(d, str): return d
    return d.get(lang, "")

def parse_csv_text(raw):
    return raw.decode("utf-8-sig").replace("\r\n","\n").rstrip("\n").split("\n")

def parse_sections(lines):
    out = []
    cur = None
    for ln in lines:
        if ln.startswith("["):
            cur = {"marker": ln.strip(), "header": None, "rows": []}
            out.append(cur)
        elif cur is not None:
            if cur["header"] is None: cur["header"] = ln
            else: cur["rows"].append(ln)
    return out

# ---------------------------------------------------------------- inspectie
def collect_rounds(cfg):
    mp = cfg.get("missionPackage", {})
    out = [(r, mp.get("$type","")) for r in (mp.get("rounds") or [])]
    for m in (mp.get("missions") or []):
        sub = m.get("missionPackage") or {}
        for r in (sub.get("rounds") or []):
            out.append((r, m.get("$type","") or sub.get("$type","")))
    return out

def inspect(skelet_path):
    z = zipfile.ZipFile(skelet_path)
    names = z.namelist()
    mani = json.loads(z.read("manifest.json").decode("utf-8-sig"))
    cfg = json.loads(z.read("Configuration.json").decode("utf-8-sig"))
    info = {"bestand": os.path.basename(skelet_path),
            "identifier": mani.get("identifier", {}),
            "skelet_talen": mani.get("localisation", {}).get("languages", []),
            "rondes": []}
    for r, mtype in collect_rounds(cfg):
        if r.get("isFeedbackRound"): continue
        uuid = r["id"]
        prefix = None
        for n in names:
            m = re.match(rf"(.*{re.escape(uuid)}_\d+)/", n)
            if m: prefix = m.group(1); break
        csvs = {}
        if prefix:
            for n in names:
                m = re.match(rf"{re.escape(prefix)}/Expansion/Expansion_{re.escape(uuid)}_(\w+)\.csv$", n)
                if m: csvs[m.group(1)] = n
        exp_cfg = r.get("expansion")
        targets = [t.get("objectName","") for t in r.get("targets",[])]
        rt = None
        if csvs:
            lines = parse_csv_text(z.read(sorted(csvs.values())[0]))
            if lines[0].startswith("["):
                markers = [s["marker"] for s in parse_sections(lines)]
                rt = "pum" if "[TARGETS]" in markers else "sort"
            else:
                h = lines[0]
                if h == TF_HEADER: rt = "tf"
                elif h == MC_HEADER: rt = f"mc{len(targets)}"
                elif h.startswith("ZoomedText"): rt = "loa"
        elif exp_cfg:
            et = exp_cfg.get("$type","")
            if "Statements" in et: rt = "tf"
            elif "MultipleChoice" in et: rt = f"mc{len(targets)}"
            elif "LocateAndAnswer" in et: rt = "loa"
            elif "Complex" in et: rt = "sort"
            elif "PuzzleMotion" in mtype: rt = "pum"
        elif "PuzzleMotion" in mtype and prefix:
            rt = "pum"
        rec = {"uuid": uuid, "naam": r.get("objectName"), "map": prefix,
               "speltype": rt or "vast", "pool_bestanden": csvs, "targets": targets}
        if rt == "tf":
            rec["target_waar"] = next((t for t in targets if any(h in t.lower() for h in TRUE_HINTS)), None)
            rec["target_nietwaar"] = next((t for t in targets if t != rec["target_waar"] and any(h in t.lower() for h in FALSE_HINTS)), None)
        info["rondes"].append(rec)
    pool = [r for r in info["rondes"] if r["speltype"] != "vast"]
    info["game_type"] = ("vaste-rondes" if not pool else
                         "mix" if len({r["speltype"][:2] for r in pool}) > 1 else pool[0]["speltype"])
    loc = parse_csv_text(z.read("Localisation.csv"))
    info["localisation_header"] = loc[0]
    info["aantal_tekst_keys"] = len(loc) - 1
    return z, names, mani, info

# ---------------------------------------------------------------- bouwers
def rows_tf(items, rec, lang, images):
    rows = []
    for i, it in enumerate(items):
        tgt = rec["target_waar"] if it["waar"] else rec["target_nietwaar"]
        img = images[i % len(images)] if images else ""
        rows.append(";".join([esc(txt(it.get("stelling") or it.get("tekst"), lang)),
                              esc(txt(it["feedback"], lang)), tgt, img]))
    return [TF_HEADER] + rows

def rows_mc(items, rec, lang, images):
    n_dis = len(rec["targets"]) - 1
    rows = []
    for i, it in enumerate(items):
        dis = it["distractors"]
        if len(dis) != n_dis:
            raise SystemExit(f"FOUT: ronde {rec['uuid'][:8]} item {i+1}: {len(dis)} foute opties, vereist {n_dis}.")
        img = images[i % len(images)] if images else ""
        d = [esc(txt(x, lang)) for x in dis] + [""] * (5 - n_dis)
        rows.append(";".join([esc(txt(it["vraag"], lang)), esc(txt(it["feedback"], lang)),
                              img, esc(txt(it["correct"], lang))] + d))
    return [MC_HEADER] + rows

def rows_loa(items, rec, lang, skelet_lines):
    defaults = dict.fromkeys(("SpotImage","ZoomedImage","NotAnsweredSprite","CorrectAnsweredSprite"), "")
    if skelet_lines and len(skelet_lines) > 1:
        hdr = skelet_lines[0].split(";")
        first = skelet_lines[1].split(";")
        for k in defaults:
            if k in hdr and hdr.index(k) < len(first):
                defaults[k] = first[hdr.index(k)]
    rows = []
    for it in items:
        vals = {c: "" for c in LOA_COLS}
        vals.update(defaults)
        vals["ZoomedText"] = txt(it["vraag"], lang)
        vals["SpotImage"] = it.get("spot_beeld", defaults["SpotImage"])
        vals["ZoomedImage"] = it.get("zoom_beeld", defaults["ZoomedImage"])
        cor = it["correct"]
        vals["CorrectText"] = txt(cor.get("tekst"), lang)
        vals["CorrectFeedback"] = txt(cor.get("feedback"), lang)
        vals["CorrectImage"] = cor.get("beeld", "")
        dis = it.get("distractors", [])
        if not 1 <= len(dis) <= 5:
            raise SystemExit(f"FOUT: LOA-item '{vals['ZoomedText'][:30]}': 1-5 distractors vereist.")
        for i, d in enumerate(dis, 1):
            vals[f"Distractor0{i}Text"] = txt(d.get("tekst"), lang)
            vals[f"Distractor0{i}Feedback"] = txt(d.get("feedback"), lang)
            vals[f"Distractor0{i}Image"] = d.get("beeld", "")
        rows.append(";".join(esc(vals[c]) if vals[c] else "" for c in LOA_COLS))
    return [LOA_HEADER] + rows

def rows_agents(lst, valid_targets, lang, images, kind):
    rows = []
    for i, a in enumerate(lst):
        tgts = a.get("targets") or [a.get("target")]
        for t in tgts:
            if t not in valid_targets:
                raise SystemExit(f"FOUT: {kind} {i+1}: target '{t}' bestaat niet (geldig: {sorted(valid_targets)}).")
        img = a.get("beeld", images[i % len(images)] if images else "")
        t5 = [tgts[j] if j < len(tgts) else "" for j in range(5)]
        rows.append(";".join([esc(txt(a["tekst"], lang)), esc(txt(a["feedback"], lang)),
                              esc(txt(a.get("goed_feedback"), lang)), img] + t5))
    return rows

def build_sectioned(skelet_lines, payload, rec, lang, images):
    secs = parse_sections(skelet_lines)
    tnames = set()
    for s in secs:
        if s["marker"] == "[TARGETS]":
            tnames = {r.split(";")[0] for r in s["rows"] if r.strip()}
    valid = tnames or set(rec["targets"])
    out = []
    for s in secs:
        out.append(s["marker"])
        out.append(s["header"])
        if s["marker"] == "[TARGETS]" and payload.get("targets"):
            skelnames = {r.split(";")[0] for r in s["rows"]}
            byname = {}
            for t in payload["targets"]:
                if t["name"] not in skelnames:
                    raise SystemExit(f"FOUT: target '{t['name']}' bestaat niet in het skelet (namen liggen vast).")
                byname[t["name"]] = t
            for r in s["rows"]:
                cols = r.split(";")
                ov = byname.get(cols[0])
                if ov:
                    if len(cols) > 1:
                        nieuw = esc(txt(ov.get("label"), lang))
                        if nieuw: cols[1] = nieuw
                    if len(cols) > 2 and ov.get("feedback") is not None:
                        cols[2] = esc(txt(ov["feedback"], lang))
                out.append(";".join(cols))
        elif s["marker"] in ("[AGENTS]","[DRAGGABLES]") and (payload.get("agents") or payload.get("draggables")):
            lst = payload.get("agents") or payload.get("draggables")
            out.extend(rows_agents(lst, valid, lang, images, s["marker"].strip("[]").lower()))
        else:
            out.extend(s["rows"])
    return out

# ---------------------------------------------------------------- overige
def build_localisation(orig, loc_updates, talen):
    text = parse_csv_text(orig)
    hdr = text[0].split(";")
    assert hdr[0] == "Key", f"Onverwachte header: {text[0]}"
    skelet_talen = hdr[1:]
    out_talen = list(dict.fromkeys(skelet_talen + [t for t in talen if t not in skelet_talen]))
    out = ["Key;" + ";".join(out_talen)]
    for line in text[1:]:
        parts = line.split(";")
        key = parts[0]
        vals = {t: (parts[i+1] if i+1 < len(parts) else "") for i, t in enumerate(skelet_talen)}
        upd = loc_updates.get(key, {})
        out.append(";".join([key] + [esc(upd.get(t, vals.get(t, ""))) for t in out_talen]))
    return out

def prep_images(img_dir, staging):
    files = sorted(f for f in os.listdir(img_dir) if f.lower().endswith(".png"))
    if not files: raise SystemExit(f"FOUT: geen PNG's in {img_dir}.")
    os.makedirs(staging, exist_ok=True)
    try:
        from PIL import Image
        pil = True
    except ImportError:
        pil = False
    names = []
    for i, f in enumerate(files, 1):
        name = f"beeld-{i}"
        dst = os.path.join(staging, name + ".png")
        if pil:
            im = Image.open(os.path.join(img_dir, f)).convert("RGBA")
            t = (320, 216)
            r = max(t[0]/im.width, t[1]/im.height)
            im = im.resize((round(im.width*r), round(im.height*r)), Image.LANCZOS)
            l, tp = (im.width-t[0])//2, (im.height-t[1])//2
            im.crop((l, tp, l+t[0], tp+t[1])).save(dst, "PNG")
        else:
            import shutil; shutil.copy(os.path.join(img_dir, f), dst)
        names.append(name)
    return names, staging

# ---------------------------------------------------------------- main
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--inspect" in sys.argv:
        _,_,_, info = inspect(args[0])
        print(json.dumps(info, ensure_ascii=False, indent=2)); return

    skelet, content_path, out_zip = args[:3]
    img_dir = sys.argv[sys.argv.index("--images")+1] if "--images" in sys.argv else None
    content = json.load(open(content_path, encoding="utf-8"))
    talen = content.get("talen", ["nl"])
    z, names, mani, info = inspect(skelet)
    by_uuid = {r["uuid"]: r for r in info["rondes"]}

    rondes = content.get("rondes")
    if rondes is None and content.get("items"):
        pool = [r for r in info["rondes"] if r["speltype"] == "tf" or r["speltype"].startswith("mc")]
        if len(pool) != 1:
            raise SystemExit("FOUT: kortschrift 'items' kan alleen bij precies een tf/mc-pool-ronde; gebruik 'rondes'.")
        rondes = [{"uuid": pool[0]["uuid"], "items": content["items"]}]
    rondes = rondes or []
    if info["game_type"] == "vaste-rondes" and rondes:
        raise SystemExit("FOUT: dit is een vaste-rondes-game; alleen 'localisation' is toegestaan.")

    images, staging = ([], None)
    if img_dir:
        images, staging = prep_images(img_dir, os.path.join(os.path.dirname(out_zip) or ".", "_beeld_staging"))

    new_files = {}
    touched = []
    for ro in rondes:
        rec = by_uuid.get(ro["uuid"])
        if not rec: raise SystemExit(f"FOUT: ronde {ro['uuid']} bestaat niet in dit game-bestand.")
        if rec["speltype"] == "vast": raise SystemExit(f"FOUT: ronde {ro['uuid'][:8]} heeft geen vragenpool.")
        touched.append(rec)
        skel_lines = None
        src = sorted(rec["pool_bestanden"].values())
        if src: skel_lines = parse_csv_text(z.read(src[0]))
        for t in talen:
            if rec["speltype"] == "tf":
                lines = rows_tf(ro["items"], rec, t, images)
            elif rec["speltype"].startswith("mc"):
                lines = rows_mc(ro["items"], rec, t, images)
            elif rec["speltype"] == "loa":
                lines = rows_loa(ro["items"], rec, t, skel_lines)
            elif rec["speltype"] in ("pum","sort"):
                if not skel_lines:
                    raise SystemExit(f"FOUT: ronde {ro['uuid'][:8]} ({rec['speltype']}) heeft geen skelet-CSV om op voort te bouwen.")
                lines = build_sectioned(skel_lines, ro, rec, t, images)
            else:
                raise SystemExit(f"FOUT: onbekend speltype {rec['speltype']}.")
            new_files[f"{rec['map']}/Expansion/Expansion_{rec['uuid']}_{t}.csv"] = BOM + CRLF.join(lines) + CRLF

    for t in talen:
        if t not in mani["localisation"]["languages"]:
            mani["localisation"]["languages"].append(t)
    for r in mani.get("rounds", []):
        rec = by_uuid.get(r.get("uuid"))
        if rec and rec in touched:
            exp = r.get("expansion") or {}
            base = copy.deepcopy(next(iter(exp.values()))) if exp else {"structure":"flat","encoding":"UTF-8-BOM","delimiter":";","lineEnding":"CRLF"}
            for t in talen:
                blok = copy.deepcopy(exp.get(t) or base)
                blok["csv"] = f"Expansion/Expansion_{rec['uuid']}_{t}.csv"
                exp[t] = blok
            r["expansion"] = exp
            r.setdefault("folders", {})["expansion"] = "Expansion"

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zout:
        done = set()
        for name in names:
            if name in new_files:
                zout.writestr(name, new_files[name].encode("utf-8")); done.add(name)
            elif name == "Localisation.csv":
                loc = build_localisation(z.read(name), content.get("localisation", {}), talen)
                zout.writestr(name, (BOM + CRLF.join(loc) + CRLF).encode("utf-8"))
            elif name == "manifest.json":
                zout.writestr(name, json.dumps(mani, ensure_ascii=False, indent=2).encode("utf-8"))
            else:
                zout.writestr(name, z.read(name))
        for name, body in new_files.items():
            if name not in done: zout.writestr(name, body.encode("utf-8"))
        for rec in {r["map"]: r for r in touched}.values():
            for img in images:
                zout.writestr(f"{rec['map']}/ExpansionImage/{img}.png",
                              open(os.path.join(staging, img + ".png"), "rb").read())
    open(out_zip, "wb").write(buf.getvalue())

    for t in talen:
        if t not in info["skelet_talen"]:
            for name, body in new_files.items():
                if name.endswith(f"_{t}.csv"):
                    p = os.path.join(os.path.dirname(out_zip) or ".", "Vangnet_" + os.path.basename(name))
                    open(p, "wb").write(body.encode("utf-8"))

    # ------------------------------------------------------------ validatie
    import csv as csvmod
    rep = []
    zv = zipfile.ZipFile(out_zip)
    def check(label, ok): rep.append(("OK " if ok else "FOUT") + " | " + label)

    extra = (set(new_files) - set(names)) | {f"{rec['map']}/ExpansionImage/{i}.png" for rec in {r['map']: r for r in touched}.values() for i in images}
    check("structuur: alleen content toegevoegd/vervangen", set(zv.namelist()) == set(names) | extra)
    check("spelstructuur (Configuration.json) ongewijzigd", zv.read("Configuration.json") == z.read("Configuration.json"))

    for rec in touched:
        n_ref = None
        for t in talen:
            path = f"{rec['map']}/Expansion/Expansion_{rec['uuid']}_{t}.csv"
            raw = zv.read(path)
            rid = f"{rec['speltype']} {rec['uuid'][:8]} {t}"
            check(f"{rid}: UTF-8-BOM + CRLF", raw.startswith(b"\xef\xbb\xbf") and b"\r\n" in raw)
            lines = parse_csv_text(raw)
            if rec["speltype"] in ("pum","sort"):
                secs = parse_sections(lines)
                skel_secs = parse_sections(parse_csv_text(z.read(sorted(rec["pool_bestanden"].values())[0])))
                check(f"{rid}: sectie-markers en kopregels behouden",
                      [(s["marker"], s["header"]) for s in secs] == [(s["marker"], s["header"]) for s in skel_secs])
                tn = {r.split(";")[0] for s in secs if s["marker"] == "[TARGETS]" for r in s["rows"]}
                valid = tn or set(rec["targets"])
                ag = next((s for s in secs if s["marker"] in ("[AGENTS]","[DRAGGABLES]")), None)
                rows = list(csvmod.reader(io.StringIO("\n".join(ag["rows"])), delimiter=";")) if ag else []
                check(f"{rid}: alle target-verwijzingen geldig",
                      all(all((c in valid) for c in r[4:9] if c.strip()) for r in rows))
                check(f"{rid}: uitleg (feedback) overal gevuld", all(len(r) > 1 and r[1].strip() for r in rows))
                n = len(rows)
            else:
                parsed = list(csvmod.reader(io.StringIO("\n".join(lines)), delimiter=";"))
                hdr, data = ";".join(parsed[0]), parsed[1:]
                want = {"tf": TF_HEADER, "loa": LOA_HEADER}.get(rec["speltype"], MC_HEADER)
                check(f"{rid}: kopregel exact", hdr == want)
                ncol = len(want.split(";"))
                check(f"{rid}: {ncol} kolommen per rij", all(len(r) == ncol for r in parsed))
                if rec["speltype"] == "tf":
                    check(f"{rid}: targets geldig", all(r[2] in (rec["target_waar"], rec["target_nietwaar"]) for r in data))
                    check(f"{rid}: uitleg gevuld", all(r[1].strip() for r in data))
                elif rec["speltype"].startswith("mc"):
                    nd = len(rec["targets"]) - 1
                    check(f"{rid}: correct + {nd} distractors", all(r[3].strip() and all(r[4+i].strip() for i in range(nd)) and not any(r[4+i].strip() for i in range(nd,5)) for r in data))
                    check(f"{rid}: uitleg gevuld", all(r[1].strip() for r in data))
                    check(f"{rid}: geen dubbele opties", all(len({r[3].strip().lower()} | {r[4+i].strip().lower() for i in range(nd)}) == nd+1 for r in data))
                else:
                    check(f"{rid}: vraag + correct gevuld", all(r[0].strip() and r[5].strip() for r in data))
                    check(f"{rid}: uitleg bij correct gevuld", all(r[6].strip() for r in data))
                    check(f"{rid}: minimaal 1 distractor", all(r[8].strip() for r in data))
                n = len(data)
            if n_ref is None: n_ref = n
            else: check(f"{rec['uuid'][:8]}: talen even veel rijen", n == n_ref)

    locraw = zv.read("Localisation.csv")
    locrows = parse_csv_text(locraw)
    orig_rows = parse_csv_text(z.read("Localisation.csv"))
    check("teksten: UTF-8-BOM", locraw.startswith(b"\xef\xbb\xbf"))
    check("teksten: zelfde aantal regels als skelet", len(locrows) == len(orig_rows))
    check("teksten: alle keys ongewijzigd", [r.split(";")[0] for r in locrows] == [r.split(";")[0] for r in orig_rows])
    m2 = json.loads(zv.read("manifest.json").decode("utf-8-sig"))
    check("registratie talen in manifest", all(t in m2["localisation"]["languages"] for t in talen))

    rep.append(f"INFO | game={info['game_type']} | rondes gevuld: {len(touched)} | talen={'+'.join(talen)} | beeld={len(images) or 'geen'}")
    print("\n".join(rep))
    sys.exit(0 if not any(r.startswith("FOUT") for r in rep) else 1)

if __name__ == "__main__":
    main()
