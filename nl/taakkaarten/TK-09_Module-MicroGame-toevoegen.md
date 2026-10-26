---
type: Runbook
title: "TK-09 Module MicroGame toevoegen"
description: "Zo voeg je een MicroGame-module toe aan een challenge en stel je de module-instellingen in — zonder technische kennis."
tags: [taakkaart, content, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-09 — Module MicroGame toevoegen

> **Voor game managers.** Zo voeg je een MicroGame-module toe aan een challenge en stel je de module-instellingen in — zonder technische kennis.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Een module is één leeractiviteit binnen een challenge.** Deze kaart legt óók de **algemene module-instellingen** uit (score-factor, vaardigheden, herspeelbaar, start-/eindscherm) — die gelden voor álle moduletypen en komen in TK-10 t/m TK-12 en TK-25 terug. De inhoud ván de microgame (vragen, plaatjes, levels) regel je niet hier, maar in de game zelf: zie de taakkaarten **Template Games** (Unity / Configuration Editor).

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → [campagne] → [challenge] → **Module toevoegen** → type **MicroGame** |
| **Wanneer inzetten** | De "Doen"-stap van een challenge: oefenen via een game |
| **Wat je nodig hebt** | Een bestaande, gevulde microgame (beschikbaar voor jouw organisatie); naam + omschrijving per taal |
| **Punten** | Score-factor: basis **10.000 punten** per module, instelbaar **0–500%** |
| **Sterren** | Sterrendrempels (1–5) stel je in bij de **microgame**, niet bij de module |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Open het **Control Panel** → **Campagnes** → [campagne] → klik de challenge open.
2. Klik **Module toevoegen** en kies type **MicroGame**.
3. Kies de **Micro game** uit de lijst met games die voor jouw organisatie beschikbaar zijn. Zie je de juiste game niet? Dan is hij (nog) niet aan je organisatie toegewezen — vraag dit na bij 4Growth.
4. Vul de basis in: **Naam** (verplicht) en **Omschrijving** — per taal. Optioneel een **Afbeelding**; bij dit type kun je ook de afbeelding van de microgame zelf gebruiken.
5. Stel de **algemene module-instellingen** in (gelden voor alle moduletypen):
   - **Factor** (score-factor): percentage van de basisscore van 10.000 punten, 0–500%. 100% = 10.000 punten, 200% = 20.000. Zo maak je zwaardere modules meer waard.
   - **Vaardigheden** (Skills): koppel één of meer vaardigheden — die voeden de skill-grafiek in het spelersprofiel.
   - **Herspeelbaar** (Replayable): speler mag opnieuw spelen om zijn score te verbeteren.
   - **Hervatbaar** (Resumable) + **Maximale hervattingsperiode** (1–365 dagen): speler mag later verder waar hij was gebleven.
6. Richt het **beginscherm** en **eindscherm** in:
   - **Layout**: tekst **onder**, **links** of **rechts** van de afbeelding.
   - Per scherm: **titel**, **beschrijving** en **afbeelding**.
   - **Eindscherm knop label**: tekst op de doorgaan-knop (max 100 tekens), bijv. "Volgende" of "Naar de reflectie".
7. Optioneel: vink **Schermvullend** (fullscreen) aan — de game vult dan het hele scherm. Aan te raden bij games met veel beeldelementen.
8. Klik **Opslaan** en versleep de module zo nodig naar de juiste plek in de challenge.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Eerst de game, dan de module.** Controleer dat de microgame gevuld en getest is vóór je hem in een challenge hangt (zie taakkaarten Template Games).
- **Score-factor bewust kiezen.** Houd het simpel: 100% als standaard, hoger alleen voor zwaardere of belangrijkere modules. Grote verschillen maken het scorebord onnavolgbaar.
- **Herspeelbaar aan = Kolb-stap 5 (Repeat).** Zet dit standaard aan bij microgames, tenzij het een eenmalige toets is.
- **Vaardigheden vergeten = lege skill-grafiek.** Koppel altijd minimaal één vaardigheid als je organisatie met skills werkt.
- **Gearchiveerde microgames** zijn niet kiesbaar voor nieuwe modules, maar blijven speelbaar in bestaande.
- **Verwijderd ≠ weg.** Verwijderde modules kun je via **Herstellen** terughalen.

---

## ✅ Checklist

- [ ] Juiste microgame gekozen (inhoud gecontroleerd en zelf getest)
- [ ] Naam + omschrijving in alle talen
- [ ] Score-factor bewust ingesteld
- [ ] Vaardigheden gekoppeld
- [ ] Herspeelbaar/hervatbaar naar wens (incl. hervattingsperiode)
- [ ] Begin- en eindscherm: layout, titel, beschrijving, afbeelding
- [ ] Eindscherm-knoplabel logisch geformuleerd
- [ ] Module op de juiste plek in de challenge

---

## 🔍 Klaar? Zo controleer je

Speel de module zelf door in de spelersomgeving (menu → **Bekijk app**) of via de module-preview. Controleer: start de game, kloppen begin- en eindscherm, krijg je punten en sterren, en werkt opnieuw spelen als herspeelbaar aanstaat?

---

*Grondslag: LearnStrike-platform, stand april 2026. Verwante kaarten: TK-07 (challenge), TK-10 (quiz), TK-11 (survey), TK-12 (questionnaire), TK-25 (tekst & video), Template Games-taakkaarten (game-inhoud).*
