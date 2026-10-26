---
type: Runbook
title: "TK-10 Module Quiz toevoegen"
description: "Zo bouw je een quiz-module met vragen, feedback en een slagingsdrempel — zonder technische kennis."
tags: [taakkaart, content, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Taakkaart TK-10 — Module Quiz toevoegen

> **Voor game managers.** Zo bouw je een quiz-module met vragen, feedback en een slagingsdrempel — zonder technische kennis.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Een quiz toetst kennis direct in het platform** — geen Unity of aparte tool nodig. Je maakt vragen (enkel- of meerkeuze) met feedback per vraag, stelt tijd en slagingsdrempel in, en kunt vragen in bulk aanleveren via Excel.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Campagnes** → [campagne] → [challenge] → **Module toevoegen** → type **Quiz** |
| **Wanneer inzetten** | Kennischeck na een leeractiviteit; toetsmoment binnen een challenge |
| **Wat je nodig hebt** | Vragen + antwoorden (per taal), feedbackteksten, eventueel afbeeldingen per vraag |
| **Slagingsdrempel** | Percentage goede antwoorden (0–100%) dat nodig is om te slagen |
| **Tijd per vraag** | 15, 30, 45, 60, 75 of 90 seconden — standaard **30 seconden** |
| **Willekeurige selectie** | Toon 1–200 vragen per beurt, willekeurig gekozen uit je totale vragenset |
| **Bulk** | Vragen importeren/exporteren via **Excel** (incl. template om te downloaden) |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

---

## 🚀 Stappenplan

1. Open het **Control Panel** → **Campagnes** → [campagne] → [challenge] → **Module toevoegen** → **Quiz**.
2. Vul de algemene module-instellingen in — naam, omschrijving, score-factor, vaardigheden, herspeelbaar, begin-/eindscherm — zie TK-09, stap 4–7.
3. Stel de quiz-instellingen in:
   - **Drempel** (Threshold): percentage goede antwoorden om te slagen (0–100%).
   - **Tijd per vraag**: kies uit **15, 30, 45, 60, 75 of 90 seconden**. De standaardinstelling is 30 seconden.
   - **Aantal te tonen vragen** (1–200): het platform kiest per speelbeurt willekeurig dit aantal uit je vragenset. Handig i.c.m. herspeelbaar: elke beurt andere vragen.
4. Voeg vragen toe via **Vraag toevoegen**. Per vraag:
   - **Vraagtype**: enkelkeuze (één goed antwoord) of meerkeuze (meerdere goede antwoorden).
   - **Vraagtekst** (per taal) en optioneel een **afbeelding**.
   - **Antwoorden** via **Antwoord toevoegen** (per taal); vink per antwoord aan of het **goed** is.
   - **Feedback goed** en **Feedback fout** (per taal): korte uitleg die de speler na het antwoorden ziet — dit is je duidingsmoment (Kolb stap 3).
   - Optioneel: **Vaardigheden** per vraag.
5. Veel vragen? Gebruik de **Excel-route**:
   - Download eerst de **template** (bij de quizvragen: template downloaden).
   - Vul de template met je vragen en **importeer** het bestand.
   - Bestaande vragen kun je ook **exporteren**, extern bewerken en opnieuw importeren.
6. Klik **Opslaan** en versleep de module naar de juiste plek in de challenge.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Feedback is het leren.** Schrijf bij élke vraag inhoudelijke feedback — ook bij goed ("Klopt, want…"). Een quiz zonder feedback is een toets, geen leermiddel.
- **Stem de tijd af op de vraag.** 30 seconden werkt voor een korte kennisvraag; een vraag met een afbeelding of een langere casus verdient 45 tot 90 seconden. Lees de vraag zelf hardop voor en tel mee.
- **Meer vragen dan getoond = herhaling loont.** Maak bijv. 20 vragen en toon er 10; herspelen blijft dan interessant.
- **Drempel realistisch kiezen.** 70–80% is gebruikelijk; 100% frustreert bij tijdsdruk.
- **Meerkeuze goed uitleggen.** Spelers verwachten vaak één goed antwoord; maak in de vraagtekst duidelijk dat er meerdere goede antwoorden zijn.
- **Excel-import: gebruik altijd de template.** Eigen kolomindelingen mislukken. Controleer na import steekproefsgewijs een paar vragen in de UI.
- **Meertalig? Alles per taal** — vragen, antwoorden én feedbackteksten.

---

## ✅ Checklist

- [ ] Algemene module-instellingen ingevuld (zie TK-09)
- [ ] Drempel, tijd per vraag en aantal te tonen vragen ingesteld
- [ ] Elke vraag heeft feedback goed én fout
- [ ] Goede antwoorden correct aangevinkt (dubbelcheck bij meerkeuze!)
- [ ] Alle teksten in alle talen
- [ ] Bij Excel-import: template gebruikt en import gecontroleerd
- [ ] Vaardigheden gekoppeld (module en/of per vraag)

---

## 🔍 Klaar? Zo controleer je

Speel de quiz zelf in de spelersomgeving (menu → **Bekijk app**). Beantwoord bewust vragen goed én fout: klopt de feedback, telt de tijd goed af, en klopt de slagen/zakken-uitkomst met je drempel? Speel twee keer bij willekeurige selectie: krijg je andere vragen?

---

*Grondslag: LearnStrike-platform, stand april 2026 · tijdsopties en standaardwaarde geverifieerd door 4Growth op 30-08-2026 in de live omgeving. Verwante kaarten: TK-09 (algemene module-instellingen), TK-07 (challenge), TK-12 (questionnaire).*
