---
type: Runbook
title: "TK-12 Module Questionnaire toevoegen"
description: "Zo zet je een questionnaire op: een vragenlijst die uitmondt in een profiel of resultaat per speler. Dit is het meest complexe moduletype — plan er tijd voor in."
tags: [taakkaart, content, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-12 — Module Questionnaire toevoegen

> **Voor game managers.** Zo zet je een questionnaire op: een vragenlijst die uitmondt in een profiel of resultaat per speler. Dit is het meest complexe moduletype — plan er tijd voor in.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Een questionnaire is méér dan een survey.** Antwoorden tellen op per categorie en leiden tot een **resultaat of profiel** (bijv. een stressprofiel of interesseprofiel). Het verschil in één zin: quiz = goed/fout, survey = vrije antwoorden, questionnaire = antwoorden → categorieën → profiel.

ℹ️ Waar deze typen vandaan komen. De questionnaire-typen in LearnStrike zijn gebaseerd op bestaande, breed gebruikte vragenlijsten. Overweeg je een questionnaire voor een andere context, stem het type dan af met 4Growth.

⚠️ **Doe de eerste keer niet alleen.** Elk type heeft zijn eigen instellingen, waardes en scoringslogica. Werk je eerste questionnaire samen met 4Growth of een ervaren collega uit.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → [campagne] → [challenge] → **Module toevoegen** → type **Questionnaire** |
| **Wanneer inzetten** | Zelfscans, profieltests, gevalideerde vragenlijsten (bijv. stress- of interessetest) |
| **Typen** | hypothesis, multiple_choice, bat, coping, zeven_domeinen, stress_test, riasec |
| **Herkomst** | Gebaseerd op bestaande vragenlijsten |
| **Scoring** | Verschilt **per type** — de keuze van het type bepaalt hoe antwoorden meetellen |
| **Flow** | 1. Type kiezen → 2. Instellingen van dat type → 3. Categorieën → 4. Vragen → 5. Resultaten |
| **Vergelijken** | Kan resultaten vergelijken met een eerdere questionnaire (voor- en nameting) |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

*Globaal stappenplan — de schermen verschillen per questionnaire-type.*

1. Open het **Control Panel** → **Campagnes** → [campagne] → [challenge] → **Module toevoegen** → **Questionnaire**.
2. Vul de algemene module-instellingen in — naam, omschrijving, score-factor, vaardigheden, begin-/eindscherm — zie TK-09, stap 4–7.
3. Kies het **Questionnaire type**. De beschikbare typen: **hypothesis**, **multiple_choice**, **bat**, **coping**, **zeven_domeinen**, **stress_test**, **riasec** (interesseprofiel).
4. Zodra je een type hebt gekozen, verschijnen de **instellingen en waardes die bij dat type horen**. Vul die in. Elk type heeft een eigen set — vandaar dat de eerste keer samen met 4Growth verstandig is.
5. Volg daarna de opbouw-flow in deze volgorde:
   1. **Categorieën aanmaken** (Create categories) — de "assen" waarop gescoord wordt, bijv. zeven domeinen of RIASEC-letters.
   2. **Vragen aanmaken** (Create questions) — per vraag koppel je antwoorden aan categorieën.
   3. **Resultaten aanmaken** (Create results) — de profielen/uitslagen die de speler te zien krijgt, met tekst per categorie of scorebereik.
6. Optioneel: stel **vergelijken met een eerdere questionnaire** in — de speler ziet dan zijn ontwikkeling ten opzichte van een eerdere afname (voor-/nameting). Naar verwachting moeten beide questionnaires dezelfde opzet (type en categorieën) hebben; dat is **[nog te toetsen]**.
7. Klik **Opslaan** en test de hele flow zelf, van eerste vraag tot resultaatscherm.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Het type bepaalt de scoring.** Hoe zwaar een antwoord meetelt en hoe het resultaat tot stand komt, hangt af van het gekozen type. Ga niet uit van je ervaring met een ander type.
- **Kies het type vooraf, definitief.** Of je het type na aanmaken nog kunt wijzigen is **[nog te toetsen]** — ga er voorlopig van uit dat het niet kan en dat wisselen betekent: opnieuw beginnen.
- **Werk in de vaste volgorde: categorieën → vragen → resultaten.** Vragen kun je pas goed koppelen als de categorieën staan; resultaten pas als de vragen staan.
- **Gebruik gevalideerde vragenlijsten waar ze bestaan.** Typen als stress_test en riasec zijn gebaseerd op bestaande methodieken; verzin geen eigen varianten zonder inhoudelijk expert.
- **Schrijf resultaatteksten voor de speler, niet voor de onderzoeker.** Positief, concreet en met een handelingsperspectief.
- **Voor-/nameting? Eerst plannen.** Zet beide questionnaires identiek op vóór de eerste afname — achteraf repareren kan niet.
- **Test met verschillende antwoordpatronen** — extreem hoog, extreem laag en gemiddeld — zodat je elk mogelijk profiel één keer gezien hebt.

---

## ✅ Checklist

- [ ] Type bewust gekozen en afgestemd met 4Growth of een inhoudsexpert
- [ ] Type-specifieke instellingen en waardes ingevuld
- [ ] Algemene module-instellingen ingevuld (zie TK-09)
- [ ] Categorieën compleet en juist benoemd
- [ ] Alle vragen gekoppeld aan de juiste categorieën
- [ ] Resultaten/profielen voor élke mogelijke uitkomst geschreven
- [ ] Alle teksten in alle talen
- [ ] Bij voor-/nameting: vergelijking ingesteld en identieke opzet gecontroleerd
- [ ] Volledige flow zelf getest met minimaal drie antwoordpatronen

---

## 🔍 Klaar? Zo controleer je

Doorloop de questionnaire meermaals in de spelersomgeving (menu → **Bekijk app**) met bewust verschillende antwoorden. Controleer per doorloop: klopt het getoonde profiel/resultaat met wat je op basis van de antwoorden verwacht? Laat bij gevalideerde tests een inhoudsexpert het resultaat toetsen vóór publicatie.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Hoe werkt de scoring per questionnaire-type precies, en hoe stel je de resultaatregels (drempels, combinaties) in? | Documentatie opvragen via 4Growth en per type vastleggen; daarna deze kaart uitbreiden of splitsen per type | Product Owner |
| 2 | Kun je het type van een questionnaire na aanmaken nog wijzigen? | Maak een testquestionnaire en probeer het type te veranderen | Product Owner |
| 3 | Welke voorwaarden gelden voor het vergelijken met een eerdere questionnaire? | Zet twee questionnaires op en probeer de vergelijking in te stellen | Product Owner |

*Dit is het meest complexe moduletype en tegelijk het minst gedocumenteerde. Deze kaart wordt uitgebreid zodra de scoringslogica per type is uitgezocht.*

---

*Grondslag: LearnStrike-platform, stand april 2026 · herkomst van de typen en de type-afhankelijke instellingen zijn beschreven door de Product Owner op 30-08-2026; de scoringslogica per type is nog niet vastgelegd. Verwante kaarten: TK-09 (algemene module-instellingen), TK-10 (quiz), TK-11 (survey).*
