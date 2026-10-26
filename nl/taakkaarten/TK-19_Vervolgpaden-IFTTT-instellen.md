---
type: Runbook
title: "TK-19 Vervolgpaden (If This Then That) instellen"
description: "Zo stuur je spelers na een challenge automatisch naar de juiste vervolgstap — op basis van hun score of antwoorden."
tags: [taakkaart, spelvormen, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-19 — Vervolgpaden (If This Then That) instellen

> **Voor game managers.** Zo stuur je spelers na een challenge automatisch naar de juiste vervolgstap — op basis van hun score of antwoorden.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Met vervolgpaden (If This Then That, kort: IFTTT) maak je leerroutes op maat.** Per challenge stel je regels in: "áls de speler dit scoort of antwoordt, dán gaat hij daarheen." Zo krijgt een speler met een lage quizscore een herhalingschallenge, en een speler met een hoge score juist verdieping.

⚠️ **Vervolgpaden is vrij nieuwe functionaliteit.** De plek in de interface staat vast, maar over de precieze werking — hoe regels worden afgelopen en wat er gebeurt als geen regel past — komt nog een aparte handleiding. Test je opzet altijd zelf door voordat je hem op spelers loslaat.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → [campagne] → open de challenge → **drie puntjes** rechts van de titel → **Vervolgpaden instellen** |
| **Wanneer inzetten** | Gedifferentieerde leerroutes: herhalen bij lage score, verdiepen bij hoge score, routeren op survey- of questionnaire-uitkomst |
| **Wat je nodig hebt** | Een challenge met minimaal één quiz-, survey- of questionnaire-module; de bestemmingschallenges moeten al bestaan |
| **Een regel bestaat uit** | Label (naam) + één of meer voorwaarden + bestemming (andere challenge óf externe URL) + volgorde |
| **Voorwaardetypen** | Modulescore · gegeven survey-antwoord · questionnaire-categoriescore (% of punten) · questionnaire-uitkomstcategorie |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

💡 **Zoek je vervolgpaden en zie je ze niet?** Ze staan niet als tabblad in beeld, maar onder de **drie puntjes** rechts van de titel wanneer je een challenge opent in het Control Panel.

---

## 🚀 Stappenplan

1. Open het **Control Panel** → **Campagnes** → kies je campagne → open de challenge waar het vervolgpad ná moet komen.
2. Klik op de **drie puntjes** rechts van de titel en kies **Vervolgpaden instellen**.
3. Maak een nieuwe **regel** aan en geef hem een herkenbaar **label**, bijv. "Lage score → herhaling". Dit label is voor jezelf, om je regels uit elkaar te houden.
4. Stel de **voorwaarde(n)** in. Kies per voorwaarde een type:
   - **Modulescore** — de behaalde score op een specifieke module (bijv. quiz), met een grens (bijv. lager dan 6.000 punten).
   - **Gegeven survey-antwoord** — de speler koos een bepaald antwoord in een survey-module.
   - **Questionnaire-categoriescore** — de score op een categorie uit een vragenlijst (questionnaire), in **%** of in **punten**.
   - **Questionnaire-uitkomstcategorie** — de categorie die als uitkomst uit de vragenlijst kwam (bijv. een profieltype).
5. Kies de **bestemming**:
   - **Andere challenge** — bijv. een herhalings- of verdiepingschallenge. Of je ook naar een challenge in een ándere campagne kunt routeren, is **[nog te toetsen]**.
   - **Externe URL** — bijv. een pagina in je LMS of een aanmeldformulier.
6. Herhaal stap 3–5 voor elke route. Voorbeeld-opzet:
   - Regel 1: modulescore quiz < 6.000 → challenge "Herhaling basiskennis".
   - Regel 2: modulescore quiz ≥ 8.000 → challenge "Verdieping voor gevorderden".
7. Zet de regels in de juiste **volgorde**. In welke volgorde het platform de regels afloopt en welke regel wint als er meerdere passen, is **[nog te toetsen]** — ga er voorlopig van uit dat de bovenste passende regel wint, en test dat.
8. **Opslaan** en zelf doortesten (zie onder).

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Test elk pad zelf voor je live gaat.** Zolang de werking niet volledig is gedocumenteerd, is doorspelen met een testaccount je enige zekerheid.
- **Maak eerst de bestemmingen.** Je kunt pas routeren naar een challenge die al bestaat — bouw dus eerst je herhalings- en verdiepingschallenges.
- **Dek alle uitkomsten af.** Wat er gebeurt als géén regel klopt, is **[nog te toetsen]**. Bouw daarom je regels zo dat er altijd één past, en test het scenario "geen regel klopt" hoe dan ook.
- **Houd het simpel.** Twee of drie duidelijke routes werken beter dan tien regels die elkaar overlappen.
- **Let op scoregrenzen.** Een module levert standaard 10.000 punten; kies grenzen die daarbij passen en laat geen "gat" tussen regels vallen (bijv. wél <6.000 en ≥8.000, maar niets voor 6.000–8.000).
- **Verwijder je een bestemmingschallenge?** Controleer dan ook de regels die ernaartoe wijzen.

---

## ✅ Checklist vóór livegang

- [ ] Bestemmingschallenges bestaan en zijn gevuld
- [ ] Elke regel heeft een duidelijk label
- [ ] Scoregrenzen sluiten op elkaar aan (geen gaten, geen overlap)
- [ ] Volgorde van regels bewust gekozen
- [ ] Elk pad zelf doorgespeeld met een testaccount
- [ ] Scenario "geen regel klopt" getest
- [ ] Externe URL's gecontroleerd (juiste link, opent goed op mobiel)

---

## 🔍 Klaar? Zo controleer je

Speel de challenge zelf door met een testaccount. Scoor één keer bewust laag en één keer hoog: kom je in beide gevallen op de juiste vervolgchallenge (of URL) uit? Test bij survey- en questionnaire-voorwaarden elk antwoord en elke uitkomstcategorie minstens één keer. Speel ook een keer een uitkomst die door géén enkele regel gedekt wordt en leg vast wat er dan gebeurt.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | In welke volgorde worden regels geëvalueerd, en welke wint als er meerdere passen? | Onderdeel van de handleiding vervolgpaden — uitzoeken en vastleggen | Product Owner |
| 2 | Wat gebeurt er als geen enkele regel past — krijgt de speler het normale vervolg? | Speel een uitkomst die buiten alle regels valt en leg het gedrag vast | Product Owner |
| 3 | Kun je routeren naar een challenge in een andere campagne, of alleen binnen dezelfde campagne? | Probeer bij bestemming een challenge uit een andere campagne te kiezen | Product Owner |

*Voor deze punten komt een aparte handleiding "werking vervolgpaden". Deze kaart wordt daarna bijgewerkt.*

---

*Grondslag: LearnStrike-platform, stand april 2026 · plek in de UI geverifieerd door 4Growth op 30-08-2026; werking van de regels nog niet gedocumenteerd. Verwante kaarten: TK-07 (challenge), TK-10 (quiz), TK-11 (survey/reflectie), TK-06 (campagne).*
