---
type: Runbook
title: "TK-16 Battle aanmaken (Battle Arena)"
description: "Zo zet je een battle op: een 1-op-1 kennisduel waarin spelers elkaar uitdagen in een microgame."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# ⚔️ Taakkaart TK-16 — Battle aanmaken (Battle Arena)

> **Voor game managers.** Zo zet je een battle op: een 1-op-1 kennisduel waarin spelers elkaar uitdagen in een microgame.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Een battle is een duel tussen twee spelers in de Battle Arena.** De uitdager speelt een microgame, de tegenstander krijgt dezelfde game. De winnaar krijgt bonuspunten. Jij bepaalt de vragenbron, de punten en de periode.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Battles** → **Battle toevoegen** |
| **Wanneer inzetten** | Kennis activeren en herhalen op een speelse manier; extra reuring naast een campagne of tijdens een toernooi |
| **Vragenbron** | Een campagne (systeem kiest willekeurige microgame) óf één of meer losse microgames |
| **Reactietijd** | De tijd die de uitgedaagde speler heeft om de uitdaging **aan te nemen** — niet de speeltijd per vraag |
| **Periode** | **Beschikbaar vanaf/tot** — mag niet overlappen met een andere battle |
| **Let op** | Bij een toernooicampagne moet de battle volledig binnen de toernooiperiode vallen |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Open het **Control Panel** → **Battles** → **Battle toevoegen**.
2. Vul de basis in: **Naam** en **Omschrijving** (per taal) en een **Afbeelding**.
3. Kies de **vragenbron**:
   - **Willekeurige microgame uit campagne** — kies een campagne; per battle-ronde pakt het systeem een willekeurige microgame daaruit. Let op: een campagne met toegang "Anonieme gebruikers" kun je hier niet kiezen.
   - **Losse microgames** — selecteer zelf één of meer microgames.
4. Stel de punten in:
   - **Winst bonus** — bonuspunten voor de winnaar.
   - **Percentage van de winstbonus die de verliezer ontvangt** (0–50%) — troostpunten, houdt verliezers gemotiveerd.
   - **Score factor bij winst op hoger gerankte speler** (100–500) — extra beloning voor wie een sterkere tegenstander verslaat.
5. Stel het spelverloop in:
   - **Reactietijd** (in seconden) — de termijn waarbinnen de uitgedaagde speler de uitdaging moet **accepteren**. Loopt die tijd af, dan vervalt de uitdaging. Dit is dus níet de tijd per vraag; die stel je in de microgame of quiz zelf in.
   - **Daglimiet** — maximum aantal battles per speler per dag (leeg = onbeperkt).
   - **Gelijktijdig open sessies** — hoeveel battles een speler tegelijk open mag hebben staan (leeg = onbeperkt).
6. Kies **Beschikbaar vanaf** en **Beschikbaar tot**:
   - De periode mag **niet overlappen** met een andere battle — er kan er maar één tegelijk lopen.
   - Hoort de battle bij een toernooicampagne? Dan moet de hele battle-periode **binnen de toernooiperiode** vallen (TK-14).
7. Handig: vink **Dashboardtegel toevoegen** aan zodat de battle direct op het spelersdashboard staat. Zet eventueel **Schermvullend** aan voor de microgame.
8. Klik **Opslaan**. Spelers kunnen elkaar nu uitdagen in de Battle Arena zodra de periode ingaat.
9. Eerder stoppen? Open de battle en kies **Battle stoppen**.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Reactietijd is accepteertijd.** Zet hem niet te kort: een speler moet de uitdaging wel zien binnenkomen. Een dag of langer is voor de meeste doelgroepen realistischer dan een paar minuten.
- **Eén battle tegelijk.** Overlappende periodes weigert het systeem. Plan battles achter elkaar, niet door elkaar.
- **Geef de verliezer iets.** Een verliezerspercentage van 20–30% houdt spelers in het spel; 0% schrikt af na een paar verliespartijen.
- **Daglimiet instellen loont.** Zonder limiet kunnen fanatieke spelers het klassement scheeftrekken door eindeloos te battelen.
- **Campagne als bron? Check de microgames.** Elke microgame in de campagne kan voorbijkomen — ook die halfaffe testgame. Gebruik anders losse microgames als bron.
- **Battle-punten tellen als bonus** bovenop de campagnescore. Hoe die bonuspunten precies doorwerken in een leaderboard is **[nog te toetsen]**.

---

## ✅ Checklist vóór de start

- [ ] Naam, omschrijving (alle talen) en afbeelding ingevuld
- [ ] Vragenbron bewust gekozen en zelf gespeeld
- [ ] Winst bonus, verliezerspercentage en score factor ingesteld
- [ ] Reactietijd ruim genoeg om een uitdaging te kunnen accepteren
- [ ] Daglimiet en open sessies naar wens
- [ ] Periode gecheckt: geen overlap met andere battles, binnen eventuele toernooiperiode
- [ ] Dashboardtegel geregeld (automatisch of via TK-21)

---

## 🔍 Klaar? Zo controleer je

Open de spelersomgeving (menu → **Bekijk app**) met twee testaccounts. Daag met account A account B uit, speel de battle uit en controleer: kregen beide spelers de juiste microgame, kloppen de bonuspunten voor winnaar en verliezer, en verschijnt het resultaat in het battle-scorebord?

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Hoe tellen battle-bonuspunten mee in een leaderboard — bij de campagnescore of apart? | Speel een battle uit met een testaccount en vergelijk de leaderboardstand voor en na | 4Growth |

---

*Grondslag: LearnStrike-platform, stand april 2026 · betekenis van reactietijd geverifieerd door 4Growth op 30-08-2026. Verwante kaarten: TK-06 (campagne), TK-14 (toernooi), TK-17 (daily challenge), TK-21 (dashboard).*
