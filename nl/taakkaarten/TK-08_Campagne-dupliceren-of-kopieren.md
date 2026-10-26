---
type: Runbook
title: "TK-08 Campagne dupliceren of kopiëren"
description: "Zo hergebruik je een bestaande campagne: als kopie binnen je eigen organisatie, of via een kopieerverzoek naar een andere organisatie."
tags: [taakkaart, content, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-08 — Campagne dupliceren of kopiëren

> **Voor game managers.** Zo hergebruik je een bestaande campagne: als kopie binnen je eigen organisatie, of via een kopieerverzoek naar een andere organisatie.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Twee routes, twee doelen.** **Dupliceer campagne** (Duplicate campaign) maakt een kopie binnen je eigen organisatie — handig als startpunt voor een nieuwe groep of variant. **Kopieer campagne** (Copy campaign) stuurt een kopieerverzoek (transfer request) naar een andere organisatie, die het verzoek eerst moet accepteren.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → open de campagne → **drie puntjes** rechts van de titel → **Dupliceer campagne** of **Kopieer campagne** |
| **Wanneer inzetten** | Nieuwe editie van een bestaand traject; zelfde content voor een andere organisatie of subdomein |
| **Wat je nodig hebt** | Bij kopiëren: het subdomein van de doelorganisatie (bijv. jouwbedrijf) |
| **Wat er meekomt** | Alle instellingen van de campagne, inclusief gekoppelde vaardigheden (skills) |
| **Acceptatie** | Kopiëren gaat via een verzoek: de ontvangende organisatie **accepteert of weigert** (ook in bulk) |
| **Microgames** | Optie: microgames waar de ontvanger geen toegang toe heeft **overslaan** |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

💡 **Zoek je een knop en zie je hem niet?** Veel acties in het Control Panel zitten onder de **drie puntjes** rechts van de titel. Dat geldt ook hier.

---

## 🚀 Stappenplan

**Route A — Dupliceren (binnen eigen organisatie)**

1. Open het **Control Panel** → **Campagnes** en klik de campagne open.
2. Klik op de **drie puntjes** rechts van de campagnetitel en kies **Dupliceer campagne** (Duplicate campaign).
3. Er verschijnt een kopie in je campagnelijst, als **Concept** (niet gepubliceerd). Alle instellingen van het origineel komen mee, inclusief de gekoppelde vaardigheden. Of de **achievement-instellingen** ook meekomen, is **[nog te toetsen]**.
4. Pas naam, teksten en instellingen aan en publiceer als je klaar bent (TK-06, stap 10).

**Route B — Kopiëren naar een andere organisatie (kopieerverzoek)**

1. Open de campagne → **drie puntjes** → **Kopieer campagne** (Copy campaign).
2. Vul het **subdomein** van de doelorganisatie in (verplicht) — het deel vóór `.learnstrike.app`.
3. Kies of je **ontbrekende microgames wilt overslaan** (checkbox). Aan = de kopie gaat door, maar microgame-modules waar de ontvanger geen toegang toe heeft worden weggelaten. Uit = het verzoek kan hierop stuklopen; wat er dan precies gebeurt is **[nog te toetsen]**.
4. Klik **Kopieerverzoek versturen** (Send copy request).
5. **De ontvanger** ziet het verzoek in het Control Panel bij **Kopieerverzoeken** (Transfer requests) en kiest **accepteren** of **weigeren** — per verzoek of in bulk.
6. Na acceptatie staat de campagne als kopie in de doelorganisatie; de ontvangende manager past hem daar aan en publiceert zelf.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Een kopie is een momentopname.** Wijzig je later het origineel, dan verandert de kopie níet mee (en andersom).
- **Controleer het subdomein extra goed.** Een typefout betekent dat het verzoek bij de verkeerde of bij geen enkele organisatie terechtkomt.
- **Loop de achievements na in de kopie.** Zolang punt 1 hieronder openstaat: controleer na het dupliceren zelf of de achievement-instellingen kloppen.
- **Denk vooraf na over microgame-toegang.** Heeft de doelorganisatie niet dezelfde microgames, gebruik dan de optie ontbrekende microgames overslaan — en vul de gaten daarna handmatig.
- **Kopiëren publiceert niets.** De ontvanger moet de campagne zelf controleren, aanpassen en publiceren.
- **Spreek het af.** Waarschuw je contactpersoon bij de ontvangende organisatie dat er een verzoek aankomt — anders blijft het onopgemerkt staan.
- **Voortgang gaat nooit mee.** Spelerscores en voortgang blijven bij het origineel; een kopie start altijd leeg.

---

## ✅ Checklist

- [ ] Juiste route gekozen: dupliceren (eigen organisatie) of kopiëren (andere organisatie)
- [ ] Bij kopiëren: subdomein gecontroleerd (spelling!)
- [ ] Keuze gemaakt: ontbrekende microgames overslaan ja/nee
- [ ] Ontvanger geïnformeerd over het verzoek
- [ ] Na dupliceren: achievements en vaardigheden nagelopen in de kopie
- [ ] Naam en teksten aangepast (geen "oude" verwijzingen)
- [ ] Kopie zelf doorgespeeld vóór publicatie

---

## 🔍 Klaar? Zo controleer je

Bij dupliceren: staat de kopie als Concept in je campagnelijst en klopt de inhoud? Zet de twee campagnes naast elkaar en loop challenges, modules, vaardigheden en achievements langs. Bij kopiëren: vraag de ontvanger te bevestigen dat het verzoek binnenkwam bij **Kopieerverzoeken** en na acceptatie te controleren of alle challenges en modules compleet zijn — let extra op overgeslagen microgame-modules.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Komen de achievement-instellingen mee bij dupliceren? | Dupliceer een campagne met ingestelde achievements en vergelijk beide campagnes op achievement-niveau | 4Growth |
| 2 | Wat gebeurt er bij een kopieerverzoek als "ontbrekende microgames overslaan" **uit** staat en de ontvanger mist een microgame? | Verzoek versturen naar een organisatie zonder die microgame en de foutmelding vastleggen | 4Growth |

*Deze kaart wordt bijgewerkt zodra de tests zijn afgerond.*

---

*Grondslag: LearnStrike-platform, stand april 2026 · UI en gedrag geverifieerd door 4Growth op 30-08-2026 in de live omgeving. Verwante kaarten: TK-06 (campagne aanmaken/publiceren), TK-07 (challenges), TK-09 (microgame-module), TK-22 (achievements).*
