---
type: Runbook
title: "TK-21 Spelersdashboard inrichten"
description: "Zo bepaal je wat spelers zien op hun startscherm: secties met tegels voor campagnes, battles en meer."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-21 — Spelersdashboard inrichten

> **Voor game managers.** Zo bepaal je wat spelers zien op hun startscherm: secties met tegels voor campagnes, battles en meer.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Het dashboard is de etalage van je spelersomgeving.** Je bouwt het op uit **secties** (rijen met een kop) waarin **tegels** staan. Een tegel bevat altijd content: een campagne, battle, daily challenge of direct-play microgame. Een opgeruimd dashboard maakt het verschil tussen "waar moet ik beginnen?" en direct spelen.

ℹ️ **Een leaderboard is geen tegel.** Staat er een leaderboard aan, dan verschijnt er bovenin de hoofdnavigatie van de speler-app een knop **Leaderboards**. Je hoeft (en kunt) daar dus geen tegel voor maken — zie TK-20.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Dashboard indeling** |
| **Wanneer inzetten** | Bij elke nieuwe campagne, battle of daily challenge, en periodiek als opruimbeurt |
| **Wat je nodig hebt** | Sectienaam + omschrijving (per taal); de items waarnaar tegels verwijzen moeten al bestaan |
| **Tegeltypen** | Campagne · Battle · Daily challenge · Direct-play microgame |
| **Geen tegeltype** | Leaderboard — dat verschijnt als knop in de hoofdnavigatie |
| **Volgorde** | Via **Dashboard indeling** bepaal je in welke sectie een tegel staat en in welke volgorde |
| **Automatisch** | Organisatie-instelling: nieuwe items automatisch als tegel toevoegen (per type aan/uit) |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

**A. Secties aanmaken**

1. Open het **Control Panel** → **Dashboard indeling**.
2. Maak een **sectie** aan: vul **Naam** en **Omschrijving** in — per beschikbare taal (tabjes boven het veld). Bijv. "Nieuw deze maand" of "Jouw leertrajecten".
3. **Opslaan.** Herhaal voor elke gewenste rij op het dashboard.

**B. Tegels toevoegen en ordenen**

4. Open een sectie en kies **Toevoegen** (tegel).
5. Kies het **type**: campagne, battle, daily challenge of direct-play microgame.
6. Kies het specifieke item (bijv. welke campagne). De keuzelijst toont alleen bestaande items.
7. **Opslaan.** Via **Dashboard indeling** bepaal je vervolgens onder welke sectie elke tegel valt en in welke volgorde de tegels staan. Zet de belangrijkste content bovenaan.

**C. Wees-tegels opruimen**

8. Ga naar het overzicht met wees-tegels: tegels waarvan de bron (bijvoorbeeld een verwijderde campagne) niet meer bestaat. De exacte naam van dit menu-item is **[nog te toetsen]**.
9. Verwijder deze tegels — spelers hebben er niets aan en het oogt slordig.

**D. Automatisch tegels laten toevoegen**

10. Wil je dat elk nieuw item vanzelf een tegel krijgt? Ga naar **Admin → Organisaties → [jouw organisatie] → Gameplay → Dashboard** en zet per type aan: automatisch tegel bij nieuwe campagne / battle / daily challenge / direct-play microgame.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Denk vanuit de nieuwe speler.** Wat moet iemand die voor het eerst inlogt als eerste zien? Zet dat bovenaan.
- **Zoek je het leaderboard op het dashboard?** Dat staat er niet — het zit in de hoofdnavigatie zodra je een leaderboard activeert (TK-20).
- **Automatisch aan = zelf opruimen.** Met de automatische instelling groeit het dashboard vanzelf vol. Plan een periodieke opruimbeurt.
- **Een tegel maakt niets zichtbaar dat verborgen is.** Toegangsregels van de campagne zelf (labels, publicatiestatus, TK-06) blijven gelden. Wat een speler ziet bij een tegel naar een conceptcampagne is **[nog te toetsen]**.
- **Meertalig? Beide talen invullen** bij sectienamen en omschrijvingen.
- **Verwijder je een campagne? Check op wees-tegels.** Anders blijft er een dode tegel achter.

---

## ✅ Checklist

- [ ] Secties hebben duidelijke namen in alle talen
- [ ] Belangrijkste content staat bovenaan
- [ ] Elke tegel verwijst naar een bestaand, gepubliceerd item
- [ ] Volgorde van tegels ingesteld via Dashboard indeling
- [ ] Geen wees-tegels in het overzicht
- [ ] Automatische tegel-instelling bewust aan of uit gezet
- [ ] Dashboard bekeken op mobiel én desktop

---

## 🔍 Klaar? Zo controleer je

Open de spelersomgeving (menu → **Bekijk app**): staan alle secties en tegels er, in de juiste volgorde, met de juiste teksten? Klik elke tegel aan — kom je op het juiste item uit? Controleer ook met een account uit een specifieke doelgroep (label) dat die alleen de bedoelde content ziet, en kijk of de knop Leaderboards in de hoofdnavigatie staat als je een leaderboard hebt geactiveerd.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Hoe heet het menu-item voor wees-tegels precies in de Nederlandse interface? | Opzoeken in het Control Panel bij Dashboard indeling | 4Growth |
| 2 | Wat ziet een speler bij een tegel die verwijst naar een campagne in concept — is de tegel verborgen of leeg? | Maak een tegel naar een conceptcampagne en bekijk het dashboard met een spelersaccount | 4Growth |

---

*Grondslag: LearnStrike-platform, stand april 2026 · geverifieerd door 4Growth op 30-08-2026: leaderboards zijn geen tegeltype maar een knop in de hoofdnavigatie, en de volgorde van tegels regel je via Dashboard indeling. Verwante kaarten: TK-06 (campagne), TK-16 (battles), TK-17 (daily challenges), TK-18 (direct play), TK-20 (leaderboards).*
