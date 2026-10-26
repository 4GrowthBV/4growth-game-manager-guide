---
type: Runbook
title: "TK-20 Leaderboard aanmaken & exporteren"
description: "Zo maak je een eigen leaderboard over één of meer campagnes, en exporteer je de stand naar Excel."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-20 — Leaderboard aanmaken & exporteren

> **Voor game managers.** Zo maak je een eigen leaderboard over één of meer campagnes, en exporteer je de stand naar Excel.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Een handmatig leaderboard is een ranglijst die jíj samenstelt.** Anders dan het automatische scorebord (spelerskant: "Scorebord") dat elke campagne standaard heeft, bepaal jij hier zelf: welke campagnes tellen mee, welke periode telt, en wie de lijst ziet (via labels). Ideaal voor een teamcompetitie of een actiemaand.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Leaderboards** → knop **Toevoegen** |
| **Wanneer inzetten** | Competitie over meerdere campagnes, een afgebakende actieperiode, of een ranglijst per doelgroep (label) |
| **Wat je nodig hebt** | Naam (per taal), de campagnes die meetellen, en eventueel labels om te filteren |
| **Meerdere campagnes** | Scores uit de gekozen campagnes worden **opgeteld** tot één ranglijst |
| **Labels** | Bepalen **wie het leaderboard ziet** — alleen spelers met het gekozen label |
| **Verschil met scorebord** | Campagne-scorebord = automatisch, per campagne (uitzetten via campagne-vinkje "Verberg scorebord", TK-06). Leaderboard = handmatig, zelf samengesteld |
| **Waar spelers het zien** | Als knop **Leaderboards** in de hoofdnavigatie van de speler-app — niet als tegel op het dashboard |
| **Export** | XLSX (Excel), rechtstreeks vanuit de leaderboard-lijst |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Open het **Control Panel** → **Leaderboards** → **Toevoegen**.
2. Vul de **Naam** in — per beschikbare taal (tabjes boven het veld). Kies een naam die spelers begrijpen, bijv. "Zomercompetitie 2026".
3. Stel de **zichtbaarheidsperiode** in: **Beschikbaar van** / **Beschikbaar tot**. Dit bepaalt wannéér spelers het leaderboard zien.
4. Stel de **scoreperiode** in: **Score van** / **Score tot**. Dit bepaalt welke scores meetellen. Alleen punten die in deze periode zijn behaald, komen in de ranglijst.
5. Kies de **campagnes** die meetellen. Meerdere campagnes mag: de scores die een speler daarin haalde worden **bij elkaar opgeteld**.
6. Optioneel: filter op **labels** (tags). Zo werkt dat:
   - Het label bepaalt **wie het leaderboard te zien krijgt**. Heeft een speler het label `manager`, en filtert dit leaderboard op `manager`, dan ziet die speler het.
   - Combineer dat met campagnes die dezelfde doelgroep bedienen, dan krijg je één ranglijst met de opgetelde scores van díe campagnes, zichtbaar voor precies díe groep.
   - Spelers zonder het label zien dit leaderboard niet, maar kunnen wél een ander leaderboard zien dat op hún label filtert.
7. **Opslaan.** Het leaderboard verschijnt in de lijst.
8. Meerdere leaderboards? Bepaal de **volgorde** waarin spelers ze zien via de volgorde-functie in de lijst (**Volgorde opslaan**).
9. Exporteren: kies bij het leaderboard **Exporteren** → je krijgt een **XLSX**-bestand met de actuele stand.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Labels sturen zichtbaarheid, niet alleen deelname.** Wie het label niet heeft, ziet het leaderboard helemaal niet. Gebruik dat bewust: het is de manier om per doelgroep een eigen ranglijst te maken zonder dat groepen elkaar zien.
- **Zichtbaarheid ≠ scoreperiode.** Twee verschillende dingen: je kunt een leaderboard tot eind december tonen, terwijl alleen scores uit november meetellen. Stel beide bewust in.
- **Scoreperiode vergeten = lege of oneerlijke lijst.** Begint je actie op 1 september? Zet "Score van" op 1 september, anders tellen oude scores mee.
- **Label-filter? Check de labels eerst.** Controleer de labeltoewijzing (TK-05) vóór de start — een speler zonder label mist de hele ranglijst.
- **Meertalig? Beide talen invullen.** Een lege taal toont een lege naam bij spelers met die taalinstelling.
- **Prijsuitreiking? Exporteer op de einddatum.** De export toont de stand van dát moment — plan je export direct na afloop van de scoreperiode.

---

## ✅ Checklist vóór livegang

- [ ] Naam in alle talen van de organisatie
- [ ] Zichtbaarheidsperiode klopt met de communicatie naar spelers
- [ ] Scoreperiode klopt met start en einde van de actie
- [ ] Juiste campagnes aangevinkt (scores worden opgeteld)
- [ ] Label-filter bewust gekozen (of bewust leeg gelaten)
- [ ] Gecontroleerd dat de bedoelde doelgroep het label daadwerkelijk heeft
- [ ] Volgorde van leaderboards logisch voor de speler

---

## 🔍 Klaar? Zo controleer je

Open de spelersomgeving (menu → **Bekijk app**) en kijk bovenin de hoofdnavigatie bij **Leaderboards**: staat jouw leaderboard er, klopt de naam, en verschijnen scores nadat je met een testaccount een module hebt gespeeld in een meetellende campagne? Test bij een label-filter ook met een account zónder dat label — die hoort het leaderboard niet te zien.

---

*Grondslag: LearnStrike-platform, stand april 2026 · werking van labels, het optellen van scores over campagnes en de plek in de spelersnavigatie geverifieerd door 4Growth op 30-08-2026. Verwante kaarten: TK-05 (labels), TK-06 (campagne, scorebord aan/uit), TK-21 (spelersdashboard), TK-23 (exports).*
