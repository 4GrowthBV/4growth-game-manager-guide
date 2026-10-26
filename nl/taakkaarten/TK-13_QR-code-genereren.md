---
type: Runbook
title: "TK-13 QR-code genereren voor een challenge"
description: "Zo gebruik je de QR-code waarmee spelers direct een challenge starten — ideaal voor posters en werkplekkaarten."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 📱 Taakkaart TK-13 — QR-code genereren voor een challenge

> **Voor game managers.** Zo gebruik je de QR-code waarmee spelers direct een challenge starten — ideaal voor posters en werkplekkaarten.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Elke challenge krijgt automatisch een eigen QR-code.** Je hoeft niets aan te maken: open de challenge en de code staat er al. Spelers scannen hem met hun telefoon en komen direct bij die challenge uit. Op mobiel opent de link de app (via een zogenaamde deeplink); anders opent de browser.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → open de campagne → open de challenge (bewerken) → de QR-code staat **bovenin het scherm** |
| **Aanmaken** | Niet nodig — bij elke challenge wordt standaard een unieke QR-code gegenereerd |
| **Wanneer inzetten** | Posters, werkplekkaarten, presentaties, flyers — overal waar spelers snel moeten kunnen starten |
| **Wat je nodig hebt** | Een bestaande challenge (TK-07); verder niets |
| **Formaat** | Download als **SVG** (standaard) of **PNG**; standaardgrootte 2048 px |
| **Link** | Loopt via het voorkeursdomein van je organisatie, of via een Branch.io-deeplink die op mobiel de app opent |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Log in en open het **Control Panel** (menu rechtsboven).
2. Ga naar **Campagnes** en open de campagne waar de challenge in zit.
3. Open de **challenge** waarvoor je de QR-code wilt (bewerken).
4. **Bovenin het scherm** staat de QR-code, met de tekst: *"Gebruik deze QR code om spelers direct te laten spelen."*
5. Download de code:
   - **Download SVG** — standaard en aan te raden: oneindig schaalbaar, dus altijd scherp op posters en in presentaties.
   - **Download PNG** — voor tools die geen SVG accepteren (bijv. sommige chat- of officeprogramma's). De PNG-download werkt op productie, zowel op macOS als op Windows.
6. Plaats de QR-code in je materiaal. De standaardgrootte is 2048 px — ruim genoeg voor A3-posters.
7. Test de code: scan hem zelf met je telefoon. Op mobiel opent de app (via de Branch.io-deeplink); op desktop opent de browser via het voorkeursdomein van je organisatie.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **QR = challenge, niet campagne.** Wil je spelers naar een heel leertraject sturen? Kies dan de eerste challenge, of gebruik een gewone link naar de campagne.
- **Check de toegang van de campagne.** Staat de campagne op "Geregistreerde gebruikers" met labels? Dan moet de scanner wél kunnen inloggen en het juiste label hebben (TK-06, TK-05).
- **Publiceer eerst.** Een QR-code naar een challenge in een concept-campagne werkt niet voor spelers.
- **Print groot genoeg.** Vuistregel: minimaal 2×2 cm op leesafstand van 20 cm; op posters liever 5×5 cm of groter.
- **Speel-op-volgorde aan?** Dan kan een speler een latere challenge pas starten als de eerdere af zijn. Wat een speler ziet als die een nog vergrendelde challenge scant, is **[nog te toetsen]**.

---

## ✅ Checklist vóór verspreiden

- [ ] Campagne is gepubliceerd en toegankelijk voor de doelgroep
- [ ] QR-code gedownload (SVG voor druk, PNG voor office/chat)
- [ ] Zelf gescand met een telefoon: opent de app en de juiste challenge
- [ ] Ook getest op desktop (browser)
- [ ] Groot genoeg afgedrukt en met voldoende witruimte eromheen

---

## 🔍 Klaar? Zo controleer je

Scan de afgedrukte (niet de digitale) versie met minimaal twee verschillende telefoons. Controleer: opent de app of browser, kom je bij de júiste challenge uit, en kun je direct spelen? Test ook met een account uit de doelgroep, niet alleen met je manager-account.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Wat ziet een speler die een QR-code scant van een challenge die nog vergrendeld is door "speel op volgorde"? | Zet speel-op-volgorde aan, scan de QR van challenge 2 met een account dat challenge 1 nog niet af heeft | 4Growth |

---

*Grondslag: LearnStrike-platform, stand april 2026 · plek in de UI en werking van de PNG-download geverifieerd door 4Growth op 30-08-2026 op macOS en Windows. Verwante kaarten: TK-05 (labels), TK-06 (campagne), TK-07 (challenge), TK-18 (Direct Play & gedeelde micro game).*
