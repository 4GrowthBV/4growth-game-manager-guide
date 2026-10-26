# Technische referentie — ZIP-anatomie en content-JSON (v2)

> Voor Claude, niet voor de gebruiker. Geverifieerd op exports (editor 1.31-1.33): PUZ194-TFC, PUZ173-MC3D, PUZ156-TGMC4E, PUM13-2-TGC, LOA24, PUZ159 (vaste rondes), MIX11 (container), MIX27. Kernprincipe: **klonen-en-vullen** — nooit from scratch, nooit Configuration.json wijzigen.

## ZIP-anatomie
```
manifest.json          documentatie/metadata (ZIP-structuur is leidend)
Configuration.json     spelstructuur — NOOIT wijzigen (script bewaakt byte-gelijkheid)
Localisation.csv       alle game-teksten: Key;nl[;en] — alleen wáárden vullen, keys/guids nooit
[SUBGAME/]{ronde-uuid}_{n}/   map per ronde; MIX-containers hebben een submap per sub-game
├── BackgroundImage/   achtergrond (niet aanraken)
├── Expansion/         Expansion_{ronde-uuid}_{taal}.csv — vragenpool, per taal één bestand
└── ExpansionImage/    PNG's waar beeld-kolommen naar verwijzen (naam zonder .png)
```
- Encoding gegenereerde bestanden: **UTF-8-BOM, `;`, CRLF** (declaratie in manifest; import tolereert meer).
- Games kunnen **meerdere pool-rondes** hebben (LOA24: 12, PUM13: 4) — content per ronde-uuid.
- Feedback-rondes (toelichtingsschermen) hebben geen pool; teksten via Localisation (`TextKey`/`QuestionKey`).
- Exports kunnen vervuilde key-namen of lege pools bevatten; keys intact laten, waarden vullen.

## Speltypes en schema's (autodetectie door het script)
| Code | Speltype | Pool-formaat |
|---|---|---|
| tf | Waar/Niet waar | flat `Description;Feedback;Target;Image`; Target = exacte target-naam (bv. `tar correct`/`tar false`); labels (WAAR/NIET WAAR) in Localisation |
| mc3/mc4 | Meerkeuze | flat `Description;Feedback;Image;Correct;Distractor01…05`; aantal gevulde distractors = aantal targets − 1 |
| loa | Locate & Answer | flat 23 kolommen: `ZoomedText;SpotImage;ZoomedImage;NotAnsweredSprite;CorrectAnsweredSprite;CorrectText;CorrectFeedback;CorrectImage;Distractor01Text/Feedback/Image…05` — beeld-kolommen erven standaard van de eerste skelet-rij van die ronde |
| pum | Puzzle Motion | secties `[TARGETS]` (TargetName;Description;Feedback;Image;TargetFullImage — namen/beelden liggen vast, labels aanpasbaar) + `[AGENTS]` of `[DRAGGABLES]` (Description;Feedback;GoodFeedback;Image;Target01…05) |
| sort | Sort-to-target / PUZ-Complex | sectie `[DRAGGABLES]` (zelfde kolommen als AGENTS); Target-verwijzing naar target-objectnamen uit Configuration |
| vast | Vaste rondes | géén pool: content = Localisation-waarden op de bestaande structuur (aantallen liggen vast!) |
MIX-container: mix van bovenstaande, per ronde gedetecteerd. `[AGENTS]` en `[DRAGGABLES]` zijn dezelfde sectie (AGENTS = oudere marker); het script behoudt de marker van het skelet.

## Content-JSON (input voor scripts/generate_zip.py)
```json
{"talen": ["nl"],
 "localisation": {"<exacte key>": {"nl": "…", "en": "…"}},
 "items": [...],                     // kortschrift: alleen bij precies één tf/mc-ronde
 "rondes": [{"uuid": "<ronde-uuid>", ...}]}
```
Per speltype in een ronde-object:
- **tf**: `items: [{stelling:{nl:..}, waar:true|false, feedback:{nl:..}}]`
- **mc**: `items: [{vraag, correct, distractors:[..], feedback}]` (alle waarden `{taal: tekst}`)
- **loa**: `items: [{vraag:{..}, correct:{tekst:{..}, feedback:{..}}, distractors:[{tekst,feedback},1-5], spot_beeld?, zoom_beeld?}]` — beeldvelden weglaten = skelet-beeld hergebruiken
- **pum**: `targets?: [{name:"tar-x", label:{nl:..}, feedback?:{..}}]` (alleen labels van bestáánde targets; namen/aantal liggen vast) + `agents: [{tekst:{..}, feedback:{..}, goed_feedback?, target:"tar-x" (of targets:[..]), beeld?}]`
- **sort**: `draggables: [{tekst:{..}, feedback:{..}, goed_feedback?, target:"target 1", beeld?}]`
- **vast**: geen rondes/items; alléén `localisation`. Let op: bij vaste-rondes-games moet het aantal content-elementen exact passen op de bestaande keys (per ronde N draggables/targets) — lees Localisation.csv en map 1-op-1.

Werkwijze: altijd eerst `--inspect` (geeft per ronde: uuid, speltype, targets, talen, pool-bestanden); daarna Localisation.csv uit het ZIP lezen voor de exacte keys. Vul minimaal de game-level teksten (titel-key, Introduction, LearningGoal, GameplayTime, TotalRounds, Tip, Debriefing, succes/faal-keys), de QuestionKeys en de toelichtingsscherm-TextKeys. Geen puntkomma's in teksten.

## Script-gebruik
```
python scripts/generate_zip.py --inspect skelet.zip
python scripts/generate_zip.py skelet.zip content.json out.zip [--images map]
```
- Rondes die je niet in `rondes` opneemt blijven onaangeroerd (skelet-content blijft staan) — benoem dat in het controle-overzicht.
- `--images`: PNG's genormaliseerd naar 320×216, round-robin gekoppeld bij tf/mc; bij pum/sort/loa liever expliciete `beeld`-velden met bestaande skelet-assetnamen.
- Taal-aanvulling (taal niet in skelet): experimenteel; los vangnet-CSV wordt naast de ZIP geschreven; alle gevulde rondes krijgen beide talen.
- Het script valideert (structuur, encoding, markers/kopregels, target/beeld-refs, feedback gevuld, taal-pariteit, Localisation-keys, Configuration byte-gelijk) en weigert bij fouten. Vertaal de uitkomst naar gewone taal voor de gebruiker.

## Bekende valkuilen
1. Import in dezelfde game/context doen als waaruit geëxporteerd is.
2. PUM/sort: target-namen letterlijk overnemen (hoofdlettergevoelig); beelden alleen uit bestaande skelet-assets.
3. LOA: elke ronde heeft eigen zoom-beelden — items per ronde moeten inhoudelijk bij dát beeld passen; standaard erven ze de beeldverwijzingen van de eerste skelet-rij.
4. Vaste-rondes-games: alleen teksten vervangen; structuurwijziging = Game Designer.
5. Test-eerst-regel: altijd eerst in een testomgeving importeren en volledig uitspelen.
6. GameplayTime afstemmen op omvang (2:00 bij 15 items, 3:00 bij 20).
