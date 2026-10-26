---
type: Runbook
title: "TK-15 Leagues instellen op een campagne"
description: "Zo zet je een league-competitie op: spelers spelen in kleine poules en promoveren of degraderen wekelijks tussen niveaus."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🥇 Taakkaart TK-15 — Leagues instellen op een campagne

> **Voor game managers.** Zo zet je een league-competitie op: spelers spelen in kleine poules en promoveren of degraderen wekelijks tussen niveaus.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Leagues verdelen spelers in poules op vier niveaus: Welcome → Bronze → Silver → Gold.** Elke week (op een dag en tijd die jij kiest) promoveren de besten van een poule naar een hoger niveau en degraderen de laagsten. Zo speelt iedereen tegen spelers van eigen niveau — motiverend voor koplopers én achterblijvers.

⚠️ **Leagues is nieuwe functionaliteit en nog in testfase.** Zet leagues alleen in bij grote groepen — vuistregel: **meer dan 150 actieve deelnemers**. Verschillende instellingen in deze kaart zijn nog niet bevestigd; zie het blok "Nog te toetsen" onderaan. Overleg met 4Growth voordat je leagues bij een klant inzet.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → campagne → **Wijzigen** → **Leagues aanzetten** (Enable leagues) |
| **Wanneer inzetten** | Langlopende campagnes met veel spelers (meer dan 150), waar je wekelijkse competitie en herhaald spelen wilt stimuleren |
| **Wat je nodig hebt** | Een campagne met voldoende actieve spelers; poulegrootte; wisseldag en -tijd; promotie-/degradatie-instellingen |
| **Niveaus** | Welcome → Bronze → Silver → Gold |
| **Ritme** | Promotie/degradatie **wekelijks**, op een vaste dag en tijd |
| **Status** | Nieuw, nog in testfase — nog niet geschikt voor kleine groepen |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Open het **Control Panel** → **Campagnes** → open de campagne → **Wijzigen**.
2. Vink **Leagues aanzetten** aan. Er verschijnen extra velden.
3. Stel de **Ideale poule grootte** in: het aantal spelers per poule waar het systeem naar streeft. Vuistregel: 10–20 spelers — groot genoeg voor competitie, klein genoeg om kans te maken op promotie. Of dit ook de aanbeveling van het platform zelf is, is **[nog te toetsen]**.
4. Kies bij **Promotie / degradatie elke:** de **dag** (maandag t/m zondag) en het **tijdstip** waarop wekelijks gewisseld wordt. Kies een rustig moment, bijv. zondagavond of maandagochtend vroeg.
5. Stel de promotie- en degradatie-instellingen per niveau in:
   - **Promotie vanuit Bronze** — hoeveel spelers per poule stijgen naar Silver.
   - **Promotie vanuit Silver** — hoeveel spelers stijgen naar Gold.
   - **Degradatie vanuit Silver** — hoeveel spelers zakken terug naar Bronze.
   - **Degradatie vanuit Gold** — hoeveel spelers zakken terug naar Silver.
   - Wij vermoeden dat je hier een **percentage** invult en geen aantal spelers, maar dat is **[nog te toetsen]**. Kijk in het veld zelf of er een procentteken staat voor je het invult.
6. Vul de **League-uitleg** in (meertalig veld): korte spelregels voor spelers — wat zijn de niveaus, wanneer wordt gewisseld, wat moet je doen om te promoveren. Vul dit per taal in (tabjes boven het veld).
7. Klik **Opslaan**.
8. Zo werkt het daarna: per niveau maakt het systeem poules van ongeveer de ideale grootte. Aan het eind van elke week telt de score van die week: de besten promoveren, de laagsten degraderen, en de poules worden opnieuw ingedeeld. Op welk niveau nieuwe spelers instromen en hoe de herindeling precies verloopt, is **[nog te toetsen]**.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Leagues hebben massa nodig.** Onder de 150 actieve deelnemers is er per niveau nauwelijks een poule te vullen en gebeurt er te weinig om motiverend te zijn.
- **Overleg vóór je het bij een klant inzet.** De functionaliteit is nieuw; loop de instellingen samen met 4Growth door.
- **Schrijf de league-uitleg vóór de start.** Spelers die niet snappen waarom ze degraderen, haken af. Leg wisseldag en spelregels expliciet uit.
- **Meertalig? Alle talen invullen.** Een lege taal toont lege uitleg bij spelers met die taalinstelling.
- **Niet combineren met een kort toernooi.** Leagues zijn een wekelijks ritme; een toernooi van één week heeft er niets aan. Kies één competitievorm per campagne — of leagues en toernooimodus technisch samen kunnen, is **[nog te toetsen]**.
- **Wijzig instellingen niet middenin een week.** Doe aanpassingen vlak ná een wisselmoment.

---

## ✅ Checklist vóór activeren

- [ ] Meer dan 150 actieve spelers in de campagne
- [ ] Inzet afgestemd met 4Growth
- [ ] Ideale poulegrootte bewust gekozen
- [ ] Wisseldag en -tijd ingesteld (rustig moment)
- [ ] Promotie-/degradatie-instellingen ingevuld (let op: aantal of percentage — check het veld)
- [ ] League-uitleg geschreven in alle talen
- [ ] Spelers geïnformeerd over de spelregels

---

## 🔍 Klaar? Zo controleer je

Bekijk de campagne in de spelersomgeving (menu → **Bekijk app**): zie je de league-weergave met poule en niveau, en klopt de uitleg? Controleer na het eerste wisselmoment of promoties en degradaties zijn doorgevoerd en of de poules opnieuw zijn ingedeeld. Vraag twee of drie spelers of de spelregels duidelijk waren.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Vul je bij promotie en degradatie een **aantal spelers** of een **percentage** in? | Open het veld in het Control Panel en kijk of er een eenheid of procentteken bij staat; zo nodig navragen bij de ontwikkelpartner | Product Owner |
| 2 | Op welk niveau starten nieuwe spelers — altijd in Welcome? | Voeg een nieuwe speler toe aan een campagne met leagues en kijk in welke poule die terechtkomt | Product Owner |
| 3 | Kunnen leagues en toernooimodus tegelijk aanstaan op één campagne? | Beide aanzetten op een testcampagne en kijken of het platform dat toestaat | Product Owner |
| 4 | Welke poulegrootte adviseert het platform, en hoe verloopt de herindeling per wisselmoment? | Documentatie opvragen bij de ontwikkelpartner en één wisselmoment meelopen | Product Owner |

*Deze kaart wordt bijgewerkt zodra de tests zijn afgerond en de documentatie binnen is.*

---

*Grondslag: LearnStrike-platform, stand april 2026 · beoordeeld door 4Growth op 30-08-2026; werking in de praktijk nog niet geverifieerd. Verwante kaarten: TK-06 (campagne), TK-14 (toernooi), TK-20 (leaderboard).*
