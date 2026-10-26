---
type: Runbook
title: "TK-02 Gebruikers importeren"
description: "Zo zet je in één keer een hele groep gebruikers in het platform via een Excel- of CSV-bestand — zonder technische kennis."
tags: [taakkaart, gebruikers, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 📥 Taakkaart TK-02 — Gebruikers importeren

> **Voor game managers.** Zo zet je in één keer een hele groep gebruikers in het platform via een Excel- of CSV-bestand — zonder technische kennis.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**De import werkt in 3 stappen: uploaden → kolommen toewijzen → verwerken.** Ideaal bij de start van een traject of een nieuwe lichting deelnemers. Voor één of twee gebruikers is handmatig aanmaken sneller (TK-01).

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Gebruikers** → **drie puntjes** naast **+ Gebruiker toevoegen** → **Importeren** |
| **Wanneer inzetten** | Groepen gebruikers tegelijk toevoegen (nieuwe klas, afdeling, traject) |
| **Wat je nodig hebt** | Bestand in **csv, xls of xlsx**, maximaal **8 MB** |
| **Kolommen** | Naam, e-mail, wachtwoord, taal, labels — jij bepaalt zelf welke kolom wat is |
| **Resultaat** | Verwerkingsrapport met eventuele fouten per rij |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

⚠️ **Let op bij Excel met Amerikaanse regio-instellingen.** De template gaat uit van losse kolommen, maar bij een Amerikaanse taal- of scheidingsteken-instelling worden die kolommen niet altijd goed weergegeven en mislukt de upload. Zie de tip hieronder over het openen van een CSV in Excel.

---

## 🚀 Stappenplan

**Vooraf: bereid je bestand voor in Excel**

1. Maak een werkblad met één rij per gebruiker en duidelijke kolomkoppen, bijvoorbeeld: `Naam | E-mail | Wachtwoord | Taal | Labels`.
2. Tips:
   - **E-mail is de sleutel**: elk adres moet geldig en uniek zijn. Verwijder dubbele rijen (Excel: Gegevens → Duplicaten verwijderen).
   - **Taal** als taalcode: `nl` of `en`.
   - **Labels**: gebruik exact dezelfde labelnamen als in het Control Panel (TK-05). Het scheidingsteken bij meerdere labels in één cel is **[nog te toetsen]**.
   - **Wachtwoord**-kolom is optioneel. Wat er gebeurt als je die kolom weglaat, is **[nog te toetsen]**.
   - Geen lege rijen tussendoor; geen samengevoegde cellen; sla op als .xlsx of .csv.

**Werk je met een CSV? Zo houd je de kolommen heel**

3. Open de CSV niet met dubbelklikken, maar via **Excel → tabblad Gegevens → Van tekst/CSV**. Kies scheidingsteken **puntkomma (;)** en bestandsherkomst **UTF-8**. Bewaren doe je als **CSV UTF-8 (\*.csv)**. Zo blijven de kolommen gescheiden, ook op een machine met Amerikaanse instellingen.

**Stap 1 — Uploaden**

4. Open Control Panel → **Gebruikers** → **drie puntjes** → **Importeren**.
5. Kies je bestand (csv/xls/xlsx, max 8 MB) en upload.

**Stap 2 — Kolommen toewijzen**

6. Je ziet een voorbeeldweergave van je bestand. Wijs per kolom toe wat erin staat:
   - **Geen (none)** — kolom overslaan
   - **Naam (name)** · **E-mail (email)** · **Wachtwoord (password)** · **Taal (language)** · **Labels (tags)**
7. Vink **Sla kopregel over (skip header)** aan als je eerste rij kolomkoppen bevat (bijna altijd het geval).

**Stap 3 — Verwerken**

8. Start de verwerking. Daarna zie je het resultaat, met **per rij een foutmelding** als er iets misging (bijv. ongeldig e-mailadres).
9. Los fouten op in je Excel-bestand en importeer alleen de gecorrigeerde rijen opnieuw. Of rijen met een al bestaand e-mailadres worden overgeslagen of bijgewerkt, is **[nog te toetsen]**.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Test eerst met 2-3 rijen.** Klopt de kolomtoewijzing en komen de labels goed door? Dan pas de hele lijst. Zolang de punten hieronder openstaan is dit extra belangrijk.
- **Zie je in stap 2 geen losse kolommen maar één lange regel?** Dan las Excel het scheidingsteken verkeerd. Ga terug naar stap 3 hierboven en open de CSV opnieuw via Gegevens → Van tekst/CSV.
- **Kopregel vergeten over te slaan** = je kolomkoppen worden een "gebruiker". Altijd even checken in stap 2.
- **Labels vooraf aanmaken** in het Control Panel (TK-05), zodat de spelling exact overeenkomt.
- **Let op Excel-opmaak**: e-mailadressen mogen geen spaties bevatten; controleer op onzichtbare spaties bij kopiëren uit andere systemen.
- **Privacy**: het importbestand bevat persoonsgegevens (en mogelijk wachtwoorden). Bewaar het beveiligd en verwijder het na de import.

---

## ✅ Checklist vóór de import

- [ ] Bestand is csv/xls/xlsx en kleiner dan 8 MB
- [ ] CSV geopend en bewaard via Gegevens → Van tekst/CSV, puntkomma, UTF-8
- [ ] Eén rij per gebruiker, geen duplicaten of lege rijen
- [ ] E-mailadressen gecontroleerd (geldig, uniek, geen spaties)
- [ ] Taalcodes correct (nl/en)
- [ ] Labelnamen exact gelijk aan de labels in het Control Panel
- [ ] Testimport met enkele rijen gedaan

---

## 🔍 Klaar? Zo controleer je

Bekijk het verwerkingsrapport: nul fouten? Open dan Control Panel → **Gebruikers** en controleer steekproefsgewijs enkele gebruikers: kloppen naam, taal en labels? Laat één geïmporteerde gebruiker inloggen als eindcontrole.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Welk scheidingsteken gebruik je voor meerdere labels in één cel — komma of puntkomma? | Importeer een testrij met twee labels in één cel, eerst met komma, dan met puntkomma | 4Growth |
| 2 | Wat gebeurt er als de wachtwoordkolom ontbreekt? Krijgt de gebruiker een e-mail om zelf een wachtwoord te kiezen, of kan die niet inloggen? | Importeer één testgebruiker zonder wachtwoordkolom en probeer in te loggen | 4Growth |
| 3 | Wordt een rij met een bestaand e-mailadres overgeslagen of bijgewerkt? | Importeer drie rijen waarvan één bestaand adres met een gewijzigde naam, en kijk wat er met die gebruiker gebeurt | 4Growth |
| 4 | Bij welke Excel-instellingen loopt de import precies stuk, en helpt de route Gegevens → Van tekst/CSV altijd? | Import proberen op een machine met Amerikaanse regio-instelling, met en zonder de importroute uit stap 3 | 4Growth |

*Deze kaart wordt bijgewerkt zodra de tests zijn afgerond.*

---

*Grondslag: LearnStrike-platform, stand april 2026 · knoplocatie geverifieerd door 4Growth op 30-08-2026; het Excel-probleem is bekend uit de praktijk maar nog niet systematisch getest. Verwante kaarten: TK-01 (handmatig aanmaken), TK-03 (uitnodigen), TK-05 (labels).*
