---
type: Runbook
title: "TK-22 Achievements & certificaten instellen"
description: "Zo bepaal je welke achievements spelers kunnen verdienen (en wat ze opleveren), en hoe certificaten worden uitgereikt."
tags: [taakkaart, inzicht, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-22 — Achievements & certificaten instellen

> **Voor game managers.** Zo bepaal je welke achievements spelers kunnen verdienen (en wat ze opleveren), en hoe certificaten worden uitgereikt.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Achievements en certificaten zijn je beloningsknoppen.** Achievements zijn badges met bonuspunten voor gedrag dat je wilt stimuleren (vroeg spelen, volhouden, battles winnen). Certificaten zijn het formele bewijs bij het afronden van een campagne. Beide stel je in op twee niveaus: organisatiebreed en per campagne.

---

## 📌 Highlights

| | |
|---|---|
| **Waar (achievements per campagne)** | Control Panel → **Campagnes** → open de campagne → **drie puntjes** rechts van de titel → **Achievements** |
| **Waar (achievements organisatiebreed)** | **Admin → Organisaties → [jouw organisatie] → Gameplay → Achievements** |
| **Waar (certificaat aan/uit)** | Per campagne: vinkje **Reikt certificaat uit** (TK-06) |
| **Waar (opmaak certificaat)** | **Admin → Organisaties** → klik de organisatienaam aan → **Organisatie settings** → **PDF sjablonen** |
| **Per achievement instelbaar** | **Eenmalig** (once) · **Punten** (score award) · **Configuratie** (bijv. aantal streak-dagen, drempel in minuten) · uitschakelen |
| **Bijzonder** | Er bestaan **geheime** achievements — spelers zien die pas als ze ze verdienen |
| **Speler** | Kan het certificaat downloaden en per e-mail ontvangen |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

💡 **De knop Achievements zit een beetje verstopt.** Open je een campagne in het Control Panel, dan staan rechts van de titel **drie puntjes** — daar vind je Achievements, naast onder meer dupliceren en kopiëren.

---

## 🚀 Stappenplan

**A. Achievements organisatiebreed instellen**

1. Ga naar **Admin → Organisaties → [jouw organisatie] → Gameplay → Achievements**.
2. Je ziet de lijst met beschikbare achievements. Standaardvoorbeelden (uit de systeeminstellingen):
   - **Early Bird** — spelen tussen 04:00 en 08:30 (500 punten)
   - **Streaks** — dagelijks spelen: reeksen van 3, 10, 20, 30, 60 en 90 dagen
   - **Battle-reeksen** — battles op rij winnen (bijv. 3 of 7 wins)
   - Verder o.a. campagne afgerond (2.500 pt), challenge afgerond (1.500 pt), en geheime achievements (die verklappen we hier niet)
3. Per achievement kun je aanpassen:
   - **Eenmalig** (once) — kan de speler hem één keer of vaker verdienen?
   - **Punten** (score award) — hoeveel bonuspunten levert hij op?
   - **Configuratie** — de drempel, bijv. aantal streak-dagen of minimale speelduur in minuten (alleen bij achievements die zo'n instelling hebben).
   - **Uitschakelen** — haal hem uit de lijst voor jouw organisatie.
4. **Opslaan.**

**B. Achievements per campagne bijstellen**

5. Open **Campagnes** → de campagne → klik de **drie puntjes** rechts van de titel → **Achievements**.
6. Pas dezelfde instellingen (eenmalig, punten, configuratie, uitschakelen) aan — alleen voor déze campagne. Handig als een korte campagne bijv. geen 90-dagen-streak nodig heeft.

**C. Certificaten aanzetten**

7. Per campagne: vink **Reikt certificaat uit** aan in de campagne-instellingen (TK-06).
8. Wil je dit standaard voor alle nieuwe campagnes? Dat is een organisatie-instelling; onder welk tabblad dat vinkje precies staat is **[nog te toetsen]**.

**D. Opmaak van het certificaat instellen (PDF sjablonen)**

9. Ga naar **Admin → Organisaties**. Klik in het overzicht de **naam van de organisatie** aan (de blauwe tekst, links naast "Huidige organisatie").
10. Je komt in **Organisatie settings**. Kies **PDF sjablonen**.
11. Hier maak je de opmaak van álle PDF's die het platform uitgeeft — certificaten, maar ook survey- en questionnaire-rapporten. Pas teksten en kleuren aan.
12. Klaar: de speler krijgt bij afronden een PDF-certificaat en kan dit **downloaden of naar zichzelf mailen**.

ℹ️ **PDF sjablonen is nieuwe functionaliteit.** Loop de opmaak een keer helemaal door voordat je hem bij een klant gebruikt, en bekijk het resultaat als speler.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Punten met beleid.** Achievement-bonuspunten tellen mee in scores en leaderboards. Zet je ze erg hoog, dan verstoor je de competitie.
- **Configuratie past bij je looptijd.** Een 60-dagen-streak in een campagne van drie weken kan niemand halen — schakel uit of verlaag de drempel.
- **Geheime achievements niet verklappen** in je communicatie — de verrassing is juist de kracht.
- **Certificaat = belofte.** Zet het vinkje alleen aan als de campagne echt een afgeronde leerprestatie toetst; controleer de PDF-opmaak vóór livegang.
- **Organisatiebreed eerst, dan per campagne.** Wijzig algemene voorkeuren op organisatieniveau; gebruik campagneniveau alleen voor uitzonderingen.
- **Dupliceer je een campagne?** Controleer daarna of de achievement-instellingen zijn meegekomen — dat is nog niet vastgesteld (TK-08).

---

## ✅ Checklist

- [ ] Achievements-lijst doorgelopen: alles wat niet past uitgeschakeld
- [ ] Punten per achievement passend bij je puntenmodel (10.000 per module)
- [ ] Configuraties (streak-dagen, minuten) haalbaar binnen de looptijd
- [ ] Certificaat-vinkje per campagne bewust aan/uit
- [ ] PDF-sjabloon voor het certificaat gecontroleerd: teksten en kleuren
- [ ] Certificaat als speler bekeken en gemaild

---

## 🔍 Klaar? Zo controleer je

Speel met een testaccount: rond een challenge af en controleer of de achievement met de juiste punten verschijnt. Rond een campagne met certificaat af en bekijk de PDF — kloppen naam, datum, teksten en kleuren? Test ook het mailen van het certificaat.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Onder welk tabblad staat de organisatie-instelling "nieuwe campagnes reiken standaard certificaten uit"? | Doorloop Organisatie settings en leg de plek vast | 4Growth |

---

*Grondslag: LearnStrike-platform, stand april 2026 · plek van de achievements-knop en de route naar PDF sjablonen geverifieerd door 4Growth op 30-08-2026 in de live omgeving. Verwante kaarten: TK-06 (campagne-vinkje certificaat), TK-08 (dupliceren), TK-16 (battles), TK-23 (export Achievements/Certificates).*
