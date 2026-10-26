---
type: Runbook
title: "TK-14 Toernooi opzetten"
description: "Zo maak je van een campagne een toernooi met een vaste begin- en einddatum — voor een korte, intensieve competitie."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🏆 Taakkaart TK-14 — Toernooi opzetten

> **Voor game managers.** Zo maak je van een campagne een toernooi met een vaste begin- en einddatum — voor een korte, intensieve competitie.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Een toernooi is geen apart campagnetype, maar een instelling op een gewone campagne.** Je zet **Toernooimodus inschakelen** (Enable tournament mode) aan en kiest een periode. Spelers strijden binnen die periode om de hoogste score; daarna is de campagne niet meer speelbaar.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → campagne → **Wijzigen** → **Toernooimodus inschakelen** |
| **Wanneer inzetten** | Kick-offs, themaweken, campagnes met een deadline — alles waar tijdsdruk en competitie het spel spannender maken |
| **Wat je nodig hebt** | Een campagne met challenges en modules (TK-06, TK-07); begin- en einddatum |
| **Spelregels datums** | Einddatum ná begindatum; begindatum niet in het verleden |
| **Wat spelers zien** | TOERNOOI-badge, scorebord, status **Gepland** / **Lopend** / **Beëindigd** |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Zet eerst de campagne volledig op: challenges, modules, alles doorgespeeld (TK-06 t/m TK-12). Bij een toernooi telt elke dag — de inhoud moet af zijn vóór de start.
2. Open het **Control Panel** → **Campagnes** → open de campagne → **Wijzigen**.
3. Vink **Toernooimodus inschakelen** aan.
4. Vul in: **Toernooi begint op** en **Toernooi eindigt op** (datum + tijd).
   - De einddatum moet ná de begindatum liggen.
   - De begindatum mag niet in het verleden liggen.
5. Controleer het scorebord: laat **Verberg scorebord** úit — een toernooi zonder ranglijst mist zijn doel.
6. Klik **Opslaan** en publiceer de campagne (TK-06, stap 10).
7. Wat spelers nu zien:
   - Een **TOERNOOI**-badge op de campagne.
   - De toernooistatus: **Gepland** (nog niet gestart), **Lopend** (bezig) of **Beëindigd** (afgelopen), met de looptijd.
   - Het scorebord met de tussenstand.
8. Na de einddatum is de campagne **niet meer speelbaar** — spelers krijgen de melding *"Toernooi afgelopen"*. De resultaten en het scorebord blijven wél zichtbaar.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Plan royaal, start niet vandaag.** De begindatum mag niet in het verleden liggen; kies een startmoment waarop je de aankondiging al hebt verstuurd.
- **Content wijzigen tijdens een lopend toernooi = oneerlijk.** Spelers die al gespeeld hebben, hadden andere inhoud. Zet alles klaar vóór de start.
- **Combineer met een battle? Let op de periode.** Een battle gekoppeld aan een toernooicampagne moet volledig bínnen de toernooiperiode vallen — anders weigert het systeem de battle (TK-16).
- **Extra leaderboard nodig?** Het campagne-scorebord toont deze campagne. Wil je een ranglijst over meerdere campagnes of gefilterd op labels, maak dan een apart leaderboard (TK-20).
- **De melding "Toernooi afgelopen" is per organisatie aan te passen** via Talen → Vertalingen (vertaalsleutel voor toernooi-einde).

---

## ✅ Checklist vóór de start

- [ ] Campagne compleet en zelf doorgespeeld
- [ ] Toernooimodus aan, begin- en einddatum gecontroleerd (incl. tijdstip en tijdzone)
- [ ] Scorebord zichtbaar (Verberg scorebord uit)
- [ ] Campagne gepubliceerd vóór de startdatum
- [ ] Eventuele battles vallen binnen de toernooiperiode
- [ ] Aankondiging naar spelers gepland (met einddatum erin!)

---

## 🔍 Klaar? Zo controleer je

Bekijk de campagne in de spelersomgeving (menu → **Bekijk app**): zie je de TOERNOOI-badge en de status **Gepland** met de juiste startdatum? Controleer na de start of de status op **Lopend** springt en de scores op het scorebord binnenkomen. Zet voor een test eventueel een korte proef-toernooiperiode op een kopie van de campagne (TK-08).

---

*Grondslag: LearnStrike-platform, stand april 2026 · UI nog niet geverifieerd in live omgeving. Verwante kaarten: TK-06 (campagne), TK-08 (dupliceren), TK-15 (leagues), TK-16 (battle), TK-20 (leaderboard).*
