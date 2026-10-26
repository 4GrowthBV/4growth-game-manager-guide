---
type: Runbook
title: "TK-05 Labels beheren & bulk toewijzen"
description: "Zo maak en beheer je Labels (Tags) en wijs je ze in één keer toe aan een groep gebruikers — zonder technische kennis."
tags: [taakkaart, gebruikers, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 🏷️ Taakkaart TK-05 — Labels beheren & bulk toewijzen

> **Voor game managers.** Zo maak en beheer je Labels (Tags) en wijs je ze in één keer toe aan een groep gebruikers — zonder technische kennis.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

> ⚠️ **Let op:** dit onderdeel van LearnStrike is na april 2026 gewijzigd. Deze kaart wordt bijgewerkt. Twijfel je, mail support@4growth.com.

---

**Labels zijn hét middel om gebruikers te groeperen.** Ze bepalen wie welke campagne ziet (toegang), wie in welk leaderboard meetelt en welke labels de onboarding automatisch uitdeelt. Goed labelbeheer = de basis van elk gericht leertraject.

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Labels** (beheren) · bulk toewijzen via **Gebruikers** → **drie puntjes** naast **+ Gebruiker toevoegen** |
| **Wanneer inzetten** | Vóór elke campagne met beperkte toegang; bij nieuwe doelgroepen, afdelingen of lichtingen |
| **Waarvoor** | Campagne-toegang (TK-06), leaderboard-filters (TK-20), onboarding-toekenning (TK-24) |
| **Velden** | Naam (per taal, uniek binnen de organisatie) + omschrijving |
| **Bulk toevoegen** | Labels in één keer aan meerdere gebruikers toewijzen |
| **Bulk weghalen** | Via export → labelkolom aanpassen → import (TK-04, TK-02) |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

💡 **Zoek je de bulk-functie en zie je hem niet?** Die staat niet bij Labels maar op de gebruikerspagina, onder de **drie puntjes** rechts naast **+ Gebruiker toevoegen**.

---

## 🚀 Stappenplan

**Label aanmaken, bewerken, verwijderen:**

1. Open Control Panel → **Labels**.
2. Klik op label toevoegen en vul in:
   - **Naam** — per beschikbare taal; moet uniek zijn binnen je organisatie.
   - **Omschrijving** — leg vast waarvoor het label dient (bijv. "Alle medewerkers vestiging Utrecht — toegang campagne Hygiëne").
3. Bewerken en verwijderen doe je vanuit de labellijst. Verwijderd label per ongeluk? Gebruik **Herstellen (Restore)**.
4. Bij een label zie je de **toegekende gebruikers** — handig om te controleren wie het label heeft.

**Labels in bulk toewijzen aan gebruikers:**

5. Open Control Panel → **Gebruikers** → **drie puntjes** naast **+ Gebruiker toevoegen** en kies de bulk-optie voor labels.
6. Kies de gebruikers en de labels die je wilt toekennen, en bevestig. Alle geselecteerde gebruikers krijgen de labels in één keer.

**Labels weghalen bij een groep:**

7. Voor het verwijderen van labels bij meerdere gebruikers gebruik je de route **exporteren → aanpassen → importeren**: exporteer de gebruikerslijst (TK-04), haal in de kolom **Tags** de labels weg die eraf moeten, en importeer het bestand terug (TK-02).
8. Andere manieren om labels toe te kennen: per gebruiker (TK-01), via de import-kolom "tags" (TK-02), of automatisch via onboarding-antwoorden (TK-24).

**Waarom labels zo belangrijk zijn:**

- **Campagne-toegang** — bij toegang "Geregistreerde gebruikers" kun je een campagne beperken tot gebruikers met bepaalde labels (TK-06). Geen label = campagne onzichtbaar.
- **Leaderboard-filters** — een leaderboard toont alleen spelers met bepaalde labels, en is alleen zichtbaar voor gebruikers met dat label (TK-20).
- **Onboarding** — antwoorden op onboardingvragen kennen automatisch labels toe; zo segmenteren nieuwe gebruikers zichzelf (TK-24).

---

## ⭐ Gouden regels & naamgevingsadvies

- **Eerst labels, dan campagnes.** Maak labels aan vóór je een campagne met labeltoegang publiceert — anders ziet niemand hem.
- **Kies een vaste naamconventie**, bijvoorbeeld met een voorvoegsel per doel:
- `afd-utrecht`, `afd-zuid` — organisatie-eenheden
- `groep-2026a` — lichtingen/klassen
- `traject-hygiene` — campagne-specifieke toegang
- **Kort en herkenbaar.** Geen lange zinnen; wel consistent (altijd kleine letters, altijd hetzelfde koppelteken).
- **Geen dubbelingen.** Check de lijst voordat je een nieuw label aanmaakt — "Utrecht" en "afd-utrecht" naast elkaar zorgt voor gemiste gebruikers.
- **Omschrijving altijd invullen.** Over een half jaar weet niemand meer waar "groep-x" voor was.
- **Verwijder niet zomaar.** Een label kan in gebruik zijn voor campagne-toegang, leaderboards of onboarding — controleer dat eerst.

---

## ✅ Checklist

- [ ] Labelnaam volgt de naamconventie en is uniek
- [ ] Omschrijving ingevuld (doel + doelgroep)
- [ ] Naam in alle talen van de organisatie ingevuld
- [ ] Juiste gebruikers toegewezen (bulk of via import)
- [ ] Gecontroleerd waar het label gebruikt wordt vóór wijzigen/verwijderen

---

## 🔍 Klaar? Zo controleer je

Open het label en bekijk de toegekende gebruikers: klopt de groep? Test daarna de werking: log in (of kijk mee) met een gebruiker mét het label en één zónder — ziet alleen de eerste de label-gebonden campagne of het gefilterde leaderboard?

---

*Grondslag: LearnStrike-platform, stand april 2026 · knoplocatie en de export/import-route voor het weghalen van labels geverifieerd door 4Growth op 30-08-2026 in de live omgeving. Verwante kaarten: TK-01 (gebruiker beheren), TK-02 (importeren), TK-04 (exporteren), TK-06 (campagne-toegang), TK-20 (leaderboard), TK-24 (onboarding).*
