---
type: Runbook
title: "TK-03 Gebruikers uitnodigen"
description: "Zo nodig je iemand per e-mail uit voor het platform — de genodigde maakt zelf het account af."
tags: [taakkaart, gebruikers, nl]
timestamp: 2026-08-30
lifecycle: active
---

# ✉️ Taakkaart TK-03 — Gebruikers uitnodigen

> **Voor game managers.** Zo nodig je iemand per e-mail uit voor het platform — de genodigde maakt zelf het account af.
> **Status:** v1.0 · 30-08-2026 · onderdeel LearnStrike Kennisbank · taal: NL.

---

**Uitnodigen is de nette route voor nieuwe collega's en beheerders.** Jij bepaalt alleen e-mailadres en rol; de genodigde kiest zelf naam en wachtwoord. Voor grote groepen zonder e-mailflow: import (TK-02).

---

## 📌 Highlights

| | |
|---|---|
| **Waar** | Control Panel → **Gebruikers** → **drie puntjes** naast de knop **+ Gebruiker toevoegen** → **Uitnodigen** |
| **Wanneer inzetten** | Nieuwe gebruikers die zelf hun account moeten afronden; nieuwe managers/beheerders |
| **Wat je nodig hebt** | E-mailadres + rol per genodigde |
| **Rollen** | **Gebruiker (User)** · **Manager**. De optie **Administrator** zie je alleen als je eigen rol dat toestaat |
| **Beheer** | Uitnodiging opnieuw versturen of intrekken zolang die niet is geaccepteerd |
| **Rechten** | Rol Manager (of hoger), 2FA actief |

💡 **Zoek je de knop Uitnodigen en zie je hem niet?** Hij staat niet los op de pagina, maar onder de **drie puntjes** rechts naast **+ Gebruiker toevoegen**. Onder diezelfde drie puntjes vind je ook exporteren en labels in bulk toewijzen.

---

## 🚀 Stappenplan

**Uitnodigen:**

1. Open Control Panel → **Gebruikers**.
2. Klik op de **drie puntjes** naast **+ Gebruiker toevoegen** en kies **Uitnodigen**.
3. Vul in:
   - **E-mail adres** van de genodigde.
   - **Rol**: **Gebruiker** (speler), **Manager** (beheert gebruikers en campagnes van de organisatie) of **Administrator** (platformbeheer door 4Growth; die optie zie je alleen als je eigen rol dat toestaat).
4. Verstuur. De genodigde ontvangt een e-mail met een persoonlijke acceptatielink.

**Wat de genodigde ziet en doet (acceptatieflow):**

5. De genodigde klikt op de link in de e-mail en komt op een acceptatiepagina in de omgeving van jouw organisatie.
6. Daar rondt de genodigde het account af: naam en wachtwoord instellen. Welke velden er verder op die pagina staan (bijvoorbeeld taal of nickname) is **[nog te toetsen]**.
7. Na acceptatie is het account actief met de rol die jij hebt gekozen, en verdwijnt de uitnodiging uit de openstaande lijst.

**Beheren van openstaande uitnodigingen:**

8. **Opnieuw versturen (resend)** — e-mail niet aangekomen of kwijt? Verstuur dezelfde uitnodiging opnieuw.
9. **Intrekken** — verwijder de uitnodiging; de link werkt daarna niet meer. Gebruik dit bij een typefout in het e-mailadres of als iemand toch geen toegang mag krijgen.

---

## ⭐ Gouden regels & veelgemaakte fouten

- **Kies de laagste rol die volstaat.** Twijfel tussen Gebruiker en Manager? Kies Gebruiker — verhogen kan altijd nog (TK-01).
- **Administrator bijna nooit.** Die rol is voor platformbeheer door 4Growth. Je ziet de optie alleen als je eigen rol dat toestaat.
- **Typefout in e-mailadres?** Intrekken en opnieuw uitnodigen — bewerk niet zomaar door.
- **Labels regel je apart.** Een uitnodiging bevat geen labels; ken die na acceptatie toe (TK-01/TK-05), anders ziet de nieuwe gebruiker mogelijk geen label-gebonden campagnes.
- **Herinner na een paar dagen.** Niet geaccepteerd? Verstuur opnieuw in plaats van een tweede uitnodiging aan te maken. Of een uitnodiging na verloop van tijd vervalt, is **[nog te toetsen]** — ga er voorlopig niet van uit dat een oude link nog werkt.

---

## ✅ Checklist

- [ ] E-mailadres gecontroleerd (juiste persoon, geen typefout)
- [ ] Rol bewust gekozen (standaard: Gebruiker)
- [ ] Genodigde geïnformeerd dat er een e-mail aankomt (check ook spam)
- [ ] Na acceptatie: labels toegekend (TK-05)
- [ ] Openstaande uitnodigingen periodiek opgeschoond (intrekken wat niet meer nodig is)

---

## 🔍 Klaar? Zo controleer je

Controleer in de lijst met uitnodigingen of de status is bijgewerkt na acceptatie, en of de nieuwe gebruiker in Control Panel → **Gebruikers** staat met de juiste rol. Bij een Manager: laat diegene inloggen op het Control Panel en 2FA instellen.

---

## 🔎 Nog te toetsen

| # | Wat | Hoe te checken | Wie |
|---|---|---|---|
| 1 | Heeft een uitnodiging een vervaldatum, en zo ja: hoe lang is die geldig? | Navragen bij de ontwikkelpartner — lastig te testen zonder lang te wachten | Product Owner |
| 2 | Welke velden staan er precies op de acceptatiepagina die de genodigde te zien krijgt? | Nodig een testadres uit en doorloop de acceptatie zelf | 4Growth |

*Deze kaart wordt bijgewerkt zodra de antwoorden binnen zijn.*

---

*Grondslag: LearnStrike-platform, stand april 2026 · knoplocatie geverifieerd door 4Growth op 30-08-2026 in de live omgeving. Verwante kaarten: TK-01 (handmatig aanmaken), TK-02 (importeren), TK-05 (labels).*
