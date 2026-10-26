---
type: Runbook
title: "TK-04 Gebruikers exporteren"
description: "Zo download je een overzicht van alle gebruikers als Excel-bestand — en ga je daar zorgvuldig mee om."
tags: [taakkaart, gebruikers, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 📤 Taakkaart TK-04 — Gebruikers exporteren

> **Voor game managers.** Zo download je een overzicht van alle gebruikers als Excel-bestand — en ga je daar zorgvuldig mee om.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**De export geeft je in één klik een Excel-bestand (XLSX) met alle gebruikers van je organisatie.** Handig voor controles, rapportages of als basis voor een label-opschoning. Let op: het bestand bevat persoonsgegevens.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Gebruikers** → **drie puntjes** naast **+ Gebruiker toevoegen** → **Exporteren** |
| **Wanneer inzetten** | Overzicht/controle van gebruikers, labels en rollen; input voor rapportage of opschoning |
| **Formaat** | XLSX (Excel) |
| **Kolommen** | Name, Nickname, Email, Language, Tags, IsDemo, IsManager, IsAdministrator |
| **Let op** | Persoonsgegevens — behandel het bestand volgens de AVG |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

💡 **Zoek je de exportknop en zie je hem niet?** Hij staat onder de **drie puntjes** rechts naast **+ Gebruiker toevoegen**, samen met uitnodigen, importeren en labels in bulk toewijzen.

---

## 🚀 Stappenplan

1. Open Control Panel → **Gebruikers**.
2. Klik op de **drie puntjes** naast **+ Gebruiker toevoegen** en kies **Exporteren**. Het XLSX-bestand wordt gedownload.
3. Open het bestand in Excel. Je ziet per gebruiker:
   - **Name** — naam
   - **Nickname** — schermnaam (indien gebruikt)
   - **Email** — e-mailadres
   - **Language** — taalvoorkeur (nl/en)
   - **Tags** — toegekende Labels (Tags)
   - **IsDemo** — gast-gebruiker ja/nee
   - **IsManager** — manager-rol ja/nee
   - **IsAdministrator** — administrator-rol ja/nee
4. Gebruik filters in Excel voor je analyse — bijvoorbeeld: alle gebruikers zonder labels, of alle accounts met een manager-rol.

**Voortgang en scores zitten hier níet in.** Daarvoor gebruik je de exports onder **Inzichten** (TK-23): voortgang per campagne, survey-antwoorden en de volledige totaalexport.

**De export is ook je route om labels weg te halen.** Wil je bij een groep gebruikers labels verwijderen, dan exporteer je de lijst, past de labelkolom aan en importeert die terug (TK-02, TK-05).

---

## ⭐ Gouden regels & AVG-zorgvuldigheid

- **Exporteer alleen met een doel.** Maak geen "export voor de zekerheid" — elke kopie van persoonsgegevens is een risico.
- **Bewaar veilig.** Zet het bestand alleen in de beveiligde organisatie-omgeving (bijv. je zakelijke OneDrive), nooit op een privé-apparaat of USB-stick.
- **Deel niet zomaar.** Niet doormailen naar externen; deel binnen het team alleen met wie het echt nodig heeft.
- **Verwijder na gebruik.** Klaar met je analyse? Verwijder de export (ook uit je prullenbak en downloads-map).
- **Rollen-check als bijvangst.** Zie je in de kolommen IsManager/IsAdministrator accounts die die rol niet meer nodig hebben? Pas dit aan (TK-01).

---

## ✅ Checklist

- [ ] Duidelijk doel voor de export
- [ ] Bestand opgeslagen op een beveiligde plek
- [ ] Alleen gedeeld met wie het nodig heeft
- [ ] Na gebruik verwijderd (incl. downloads-map en prullenbak)

---

## 🔍 Klaar? Zo controleer je

Open het bestand en vergelijk het aantal rijen met het aantal gebruikers in het Control Panel — komt dat overeen? Steekproef: kloppen labels en rollen van een paar bekende gebruikers?

---

*Grondslag: LearnStrike-platform, stand april 2026 · knoplocatie geverifieerd door 4Growth op 30-08-2026 in de live omgeving. Verwante kaarten: TK-01 (gebruiker beheren), TK-02 (importeren), TK-05 (labels), TK-23 (inzichten en exports).*
