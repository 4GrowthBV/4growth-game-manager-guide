---
type: Runbook
title: "TK-15 Set up leagues on a campaign"
description: "How to set up a league competition: players play in small poules and are promoted or relegated between levels every week."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🥇 Task card TK-15 — Set up leagues on a campaign

> **For game managers.** How to set up a league competition: players play in small poules and are promoted or relegated between levels every week.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**Leagues split players into poules across four levels: Welcome → Bronze → Silver → Gold.** Every week (on a day and time you choose) the best players in a poule are promoted to a higher level and the lowest are relegated. That way everyone plays against players at their own level — motivating for front-runners and stragglers alike.

⚠️ **Leagues is new functionality and still in its test phase.** Only use leagues with large groups — rule of thumb: **more than 150 active participants**. Several settings in this card have not been confirmed yet; see the "Still to verify" block at the bottom. Talk to 4Growth before you use leagues with a client.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → campaign → **Edit** → **Enable leagues** |
| **When to use** | Long-running campaigns with a lot of players (more than 150), where you want to encourage weekly competition and repeat play |
| **What you need** | A campaign with enough active players; a poule size; a switch day and time; promotion and relegation settings |
| **Levels** | Welcome → Bronze → Silver → Gold |
| **Rhythm** | Promotion/relegation **weekly**, on a fixed day and time |
| **Status** | New, still in its test phase — not suitable for small groups yet |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Campaigns** → open the campaign → **Edit**.
2. Tick **Enable leagues**. Extra fields appear.
3. Set the **Ideal poule size**: the number of players per poule the system aims for. Rule of thumb: 10–20 players — big enough for competition, small enough to stand a chance of promotion. Whether this is also the platform's own recommendation is **[still to verify]**.
4. Under **Promotion / relegation every:** choose the **day** (Monday to Sunday) and the **time** of the weekly switch. Pick a quiet moment, for example Sunday evening or early Monday morning.
5. Set the promotion and relegation settings per level:
   - **Promotion from Bronze** — how many players per poule move up to Silver.
   - **Promotion from Silver** — how many players move up to Gold.
   - **Relegation from Silver** — how many players drop back to Bronze.
   - **Relegation from Gold** — how many players drop back to Silver.
   - We suspect you enter a **percentage** here rather than a number of players, but that is **[still to verify]**. Look at the field itself to see whether there is a percentage sign before you fill it in.
6. Fill in the **League explanation** (a multilingual field): short rules for players — what the levels are, when the switch happens, and what you have to do to be promoted. Fill this in per language (tabs above the field).
7. Click **Save**.
8. Here is how it works from then on: for each level the system builds poules of roughly the ideal size. At the end of each week that week's score counts: the best are promoted, the lowest are relegated, and the poules are rearranged. Which level new players enter at, and exactly how the rearranging works, is **[still to verify]**.

---

## ⭐ Golden rules & common mistakes

- **Leagues need volume.** Below 150 active participants there are barely enough players to fill a poule per level, and too little happens to be motivating.
- **Talk it through before you use it with a client.** The functionality is new; go through the settings together with 4Growth.
- **Write the league explanation before the start.** Players who don't understand why they are being relegated drop out. Spell out the switch day and the rules.
- **Multilingual? Fill in every language.** An empty language means players with that language setting see no explanation at all.
- **Don't combine it with a short tournament.** Leagues run on a weekly rhythm; a one-week tournament gets nothing out of them. Pick one form of competition per campaign — whether leagues and tournament mode can technically run together is **[still to verify]**.
- **Don't change settings halfway through a week.** Make your adjustments just after a switch moment.

---

## ✅ Checklist before you activate

- [ ] More than 150 active players in the campaign
- [ ] Use discussed with 4Growth
- [ ] Ideal poule size chosen deliberately
- [ ] Switch day and time set (a quiet moment)
- [ ] Promotion and relegation settings filled in (watch out: a number or a percentage — check the field)
- [ ] League explanation written in every language
- [ ] Players informed about the rules

---

## 🔍 Done? How to check

Look at the campaign in the player environment (menu → **View app**): do you see the league view with the poule and level, and is the explanation right? After the first switch moment, check whether promotions and relegations have been applied and whether the poules have been rearranged. Ask two or three players whether the rules were clear.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | Do you enter a **number of players** or a **percentage** for promotion and relegation? | Open the field in the Control Panel and see whether a unit or percentage sign is shown; ask the development partner if needed | Product Owner |
| 2 | Which level do new players start at — always Welcome? | Add a new player to a campaign with leagues and see which poule they end up in | Product Owner |
| 3 | Can leagues and tournament mode be switched on at the same time on one campaign? | Switch both on in a test campaign and see whether the platform allows it | Product Owner |
| 4 | Which poule size does the platform recommend, and how does the rearranging work at each switch moment? | Request documentation from the development partner and follow one switch moment | Product Owner |

*This card will be updated once the tests are finished and the documentation is in.*

---

*Basis: LearnStrike platform, as of April 2026 · reviewed by 4Growth on 30-08-2026; how it works in practice has not been verified yet. Related cards: TK-06 (campaign), TK-14 (tournament), TK-20 (leaderboard).*
