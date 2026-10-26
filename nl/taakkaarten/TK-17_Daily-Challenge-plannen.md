---
type: Runbook
title: "TK-17 Daily Challenge plannen"
description: "Zo plan je een daily challenge: één losse microgame die spelers dagelijks kunnen spelen — los van campagnes."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 📅 Taakkaart TK-17 — Daily Challenge plannen

> **Voor game managers.** Zo plan je een daily challenge: één losse microgame die spelers dagelijks kunnen spelen — los van campagnes.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Een daily challenge is een losse microgame met een beschikbaarheidsperiode.** Geen campagne of challenge eromheen — spelers openen hem direct vanaf het dashboard. Ideaal als dagelijks terugkeermoment: even snel spelen, score verbeteren, streak vasthouden.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Daily challenges** → **Daily challenge toevoegen** |
| **Wanneer inzetten** | Dagelijks speelritueel opbouwen, kennis warm houden tussen campagnes door, streaks stimuleren |
| **Wat je nodig hebt** | Een microgame (uit **Micro games**), naam + omschrijving, afbeelding, beschikbaarheidsperiode |
| **Aantal pogingen** | **Onbeperkt** — een speler mag zo vaak spelen als hij wil |
| **Spelregels datums** | **Beschikbaar vanaf** niet in het verleden; **Beschikbaar tot** (optioneel) ná de startdatum |
| **Let op** | Actieve daily challenges mogen elkaar **niet overlappen** — één tegelijk |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Open het **Control Panel** → **Daily challenges** → **Daily challenge toevoegen**.
2. Vul de basis in: **Naam** en **Omschrijving** (per taal) en een **Afbeelding**.
3. Kies de **microgame** (verplicht). Speel hem zelf eerst: dit is wat spelers dagelijks voorgeschoteld krijgen.
4. Stel de periode in:
   - **Beschikbaar vanaf** (verplicht) — mag niet in het verleden liggen.
   - **Beschikbaar tot** (optioneel) — moet ná de startdatum liggen. Leeg = loopt door tot je hem uitzet.
5. Zet het vinkje **Actief** aan. Let op: er mag maar één actieve daily challenge tegelijk lopen — overlapt de periode met een andere actieve daily challenge, dan weigert het systeem het opslaan.
6. Zet **Schermvullend** aan als de microgame beeldvullend moet spelen (aan te raden op mobiel).
7. Handig: vink **Dashboardtegel toevoegen** aan zodat de daily challenge direct op het spelersdashboard verschijnt (anders: TK-21).
8. Klik **Opslaan**. Vanaf de startdatum kunnen spelers de daily challenge spelen.
9. Volgende daily challenge klaarzetten? Maak hem alvast aan met een startdatum ná de einddatum van de huidige — zo sluit de programmering naadloos aan.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Onbeperkt spelen is een bewuste keuze.** Spelers mogen zo vaak spelen als ze willen: herhaling versterkt het leereffect, en het jagen op een betere score is precies wat je wilt zien. Communiceer dat ook zo naar spelers — "probeer je score te verbeteren" werkt beter dan "je hebt één kans".
- **Eén tegelijk.** Twee actieve daily challenges met overlappende periodes kan niet. Wil je wisselen: zet de oude op inactief of geef hem een einddatum, en laat de nieuwe daarna starten.
- **"Daily" zit in het spelen, niet in het plannen.** Eén daily challenge kan weken beschikbaar zijn; spelers komen elke dag terug voor een betere score.
- **Plan vooruit.** De startdatum mag niet in het verleden liggen; maak de daily challenge dus ruim van tevoren aan.
- **Kies een korte, snelle microgame.** Een daily challenge moet in 1–3 minuten te spelen zijn, anders verwatert het dagelijkse ritme.
- **Vergeet de dashboardtegel niet.** Zonder tegel (of automatische organisatie-instelling) vinden spelers de daily challenge niet.

---

## ✅ Checklist vóór activeren

- [ ] Naam, omschrijving (alle talen) en afbeelding ingevuld
- [ ] Microgame gekozen en zelf gespeeld
- [ ] Startdatum in de toekomst; einddatum klopt (of bewust leeg)
- [ ] Geen overlap met een andere actieve daily challenge
- [ ] Actief-vinkje aan
- [ ] Dashboardtegel geregeld (automatisch of via TK-21)

---

## 🔍 Klaar? Zo controleer je

Open na de startdatum de spelersomgeving (menu → **Bekijk app**): staat de daily challenge-tegel op het dashboard, opent de microgame (schermvullend indien ingesteld) en wordt de score geregistreerd? Speel hem twee keer achter elkaar om te bevestigen dat herhaald spelen werkt. Controleer bij een wissel ook of de oude daily challenge netjes verdwenen is.

---

*Grondslag: LearnStrike-platform, stand april 2026 · het onbeperkte aantal pogingen is een bewuste ontwerpkeuze, bevestigd door de Product Owner op 30-08-2026. Verwante kaarten: TK-16 (battle), TK-18 (Direct Play & gedeelde micro game), TK-21 (dashboard).*
