---
type: Runbook
title: "TK-01 Gebruiker toevoegen & beheren"
description: "Zo maak je handmatig een gebruiker aan, pas je gegevens aan en beheer je 2FA — zonder technische kennis."
tags: [taakkaart, gebruikers, nl]
timestamp: 2026-08-30
lifecycle: active
---

# 👤 Taakkaart TK-01 — Gebruiker toevoegen & beheren

> **Voor game managers.** Zo maak je handmatig een gebruiker aan, pas je gegevens aan en beheer je 2FA — zonder technische kennis.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

> ⚠️ **Let op:** dit onderdeel van LearnStrike is na april 2026 gewijzigd. Deze kaart wordt bijgewerkt. Twijfel je, mail support@4growth.com.

---

**Elke speler is een gebruiker in jouw organisatie.** Handmatig aanmaken is handig voor enkele gebruikers of een testaccount. Voor grotere groepen: importeren (TK-02) of uitnodigen per e-mail (TK-03).

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Gebruikers** → knop **+ Gebruiker toevoegen** |
| **Wanneer inzetten** | Eén of enkele gebruikers direct aanmaken; testaccounts; snelle correcties |
| **Wat je nodig hebt** | Naam + e-mailadres (verplicht); eventueel wachtwoord, taal, labels |
| **Alternatieven** | Veel gebruikers tegelijk? → Import (TK-02). Gebruiker zelf laten registreren? → Uitnodigen (TK-03) |
| **Let op** | E-mailadres moet uniek zijn binnen het platform |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

💡 **Zoek je een knop en zie je hem niet?** Veel acties in het Control Panel zitten onder de **drie puntjes** — op de gebruikerspagina staan die naast de knop **+ Gebruiker toevoegen**. Daar vind je onder meer uitnodigen, exporteren en labels in bulk toewijzen.

---

## 🚀 Stappenplan

**Aanmaken:**

1. Open Control Panel → **Gebruikers**.
2. Klik op **+ Gebruiker toevoegen** en vul in:
   - **Naam** (verplicht) en **E-mail adres** (verplicht, uniek).
   - **Taal** — bepaalt de taal van de speler-app voor deze gebruiker.
   - **Labels (Tags)** — koppel direct de juiste doelgroep-labels (zie TK-05).
   - **Wachtwoord** + bevestiging.
   - **Nickname** (2–25 tekens) — alleen zichtbaar én verplicht als jouw organisatie nicknames vereist.
   - **Avatar** — profielfoto uploaden (afbeelding, max 4 MB), optioneel.
   - **Rollen** — vink **Manager** aan voor een collega-beheerder. De optie **Administrator** zie je alleen als je eigen rol dat toestaat.
3. Klik **Opslaan**. De gebruiker staat nu in de lijst.

**Bewerken (in deelvormen):**

4. Zoek de gebruiker in de lijst via het zoekveld **Zoeken...** of de filters **Gebruikersrollen**, **Labels** en **Gebruikersstatus**, en open de gebruiker. Je bewerkt gegevens in aparte deelvormen — elk met een eigen opslaan-knop:
   - **Profiel** — naam, e-mail, nickname, avatar.
   - **Wachtwoord** — nieuw wachtwoord instellen.
   - **Taal** — taalvoorkeur wijzigen.
   - **Rollen** — Manager/Administrator aan- of uitzetten.
   - **Labels** — labels toevoegen of weghalen.

**2FA beheren:**

5. Op de gebruikerspagina zie je de status van **tweestapsverificatie (Two-factor)**. Je kunt deze inschakelen, bevestigen, uitschakelen of **resetten**. Reset bij "ik kom er niet meer in"-meldingen; wat de gebruiker daarna precies te zien krijgt is **[nog te toetsen]**. Controleer vóór een reset via een ander kanaal, bijvoorbeeld telefonisch, dat de melder echt de gebruiker is.

**Data inzien:**

6. Via de gebruikerspagina bekijk je de **gebruikersdata** en de **onboarding-antwoorden** (wat de gebruiker bij de startvragen heeft ingevuld). Voortgang per campagne vind je onder de **inzichten per gebruiker**.

**Verwijderen:**

7. Verwijder een gebruiker via de verwijderknop bij de gebruiker. **Verwijderen is definitief** — er is geen herstelfunctie voor gebruikers.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Labels direct meegeven.** Zonder labels ziet de gebruiker mogelijk geen campagnes die op labels gefilterd zijn (TK-05).
- **Taal bewust kiezen.** Een verkeerde taal betekent een speler-app in de verkeerde taal.
- **Manager-rol = beheertoegang.** Geef deze alleen aan collega's die echt in het Control Panel moeten werken; zij moeten dan ook 2FA instellen.
- **Nickname vergeten?** Als je organisatie nicknames vereist en het veld is leeg, kan de gebruiker niet goed spelen — vul het meteen in.
- **Verwijderen kun je niet terugdraaien.** Twijfel je? Haal liever eerst de labels weg zodat de gebruiker geen content meer ziet.

---

## ✅ Checklist

- [ ] Naam + uniek e-mailadres ingevuld
- [ ] Taal gekozen
- [ ] Juiste labels gekoppeld
- [ ] Wachtwoord gedeeld via een veilig kanaal (niet in dezelfde e-mail als de inlognaam)
- [ ] Rol alleen verhoogd als dat echt nodig is
- [ ] Nickname ingevuld (indien vereist)

---

## 🔍 Klaar? Zo controleer je

Open de gebruiker in de lijst: kloppen naam, e-mail, taal en labels? Laat de gebruiker inloggen en controleer of de juiste campagnes zichtbaar zijn. Voor een beheerder: controleer dat het Control Panel bereikbaar is en 2FA wordt gevraagd.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Wat ziet een gebruiker na een 2FA-reset — moet die bij de eerstvolgende login opnieuw een authenticator koppelen? | Reset 2FA op een testaccount en log daarmee in | 4Growth |

---

*Grondslag: LearnStrike-platform, stand april 2026 · UI geverifieerd door 4Growth op 30-08-2026 in de live omgeving. Verwante kaarten: TK-02 (importeren), TK-03 (uitnodigen), TK-04 (exporteren), TK-05 (labels).*
