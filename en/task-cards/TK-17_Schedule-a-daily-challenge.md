---
type: Runbook
title: "TK-17 Schedule a daily challenge"
description: "How to schedule a Daily challenge: a single Micro game players can play every day — separate from any Campaign."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# 📅 Task card TK-17 — Schedule a daily challenge

> **For game managers.** How to schedule a Daily challenge: a single Micro game players can play every day — separate from any Campaign.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**A Daily challenge is a stand-alone Micro game with an availability period.** No Campaign or Challenge around it — players open it straight from the dashboard. Ideal as a daily return moment: a quick game, a better score, a streak to keep alive.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Daily challenges** → **Add daily challenge** |
| **When to use** | Building a daily playing habit, keeping knowledge warm between Campaigns, encouraging streaks |
| **What you need** | A Micro game (from **Micro games**), a name and description, an image, an availability period |
| **Number of attempts** | **Unlimited** — a player may play as often as they like |
| **Date rules** | **Available from** cannot be in the past; **Available until** (optional) has to be after the start date |
| **Watch out** | Active Daily challenges must **not overlap** — only one at a time |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Daily challenges** → **Add daily challenge**.
2. Fill in the basics: **Name** and **Description** (per language) and an **Image**.
3. Choose the **Micro game** (required). Play it yourself first: this is what players will be served every day.
4. Set the period:
   - **Available from** (required) — cannot be in the past.
   - **Available until** (optional) — has to be after the start date. Leave it empty and the challenge runs until you switch it off.
5. Tick **Active**. Note: only one active Daily challenge may run at a time — if the period overlaps with another active Daily challenge, the system refuses to save.
6. Turn on **Enable fullscreen mode** if the Micro game should fill the screen (recommended on mobile).
7. Handy: tick **Add dashboard tile** so the Daily challenge appears on the player dashboard right away (otherwise see TK-21).
8. Click **Save**. From the start date onwards, players can play the Daily challenge.
9. Lining up the next one? Create it now with a start date after the end date of the current one — that way your programming runs on seamlessly.

---

## ⭐ Golden rules & common mistakes

- **Unlimited play is a deliberate choice.** Players may play as often as they want: repetition strengthens the learning effect, and chasing a better score is exactly what you want to see. Communicate it that way too — "try to beat your score" works better than "you get one shot".
- **One at a time.** Two active Daily challenges with overlapping periods is not possible. To switch: set the old one to inactive or give it an end date, and let the new one start after that.
- **"Daily" is in the playing, not in the scheduling.** A single Daily challenge can be available for weeks; players come back each day for a better score.
- **Plan ahead.** The start date cannot be in the past, so create the Daily challenge well in advance.
- **Pick a short, fast Micro game.** A Daily challenge should be playable in one to three minutes, otherwise the daily rhythm fades.
- **Don't forget the dashboard tile.** Without a tile (or an automatic organisation setting), players simply won't find the Daily challenge.

---

## ✅ Checklist before you activate

- [ ] Name, description (all languages) and image filled in
- [ ] Micro game chosen and played through yourself
- [ ] Start date in the future; end date correct (or deliberately empty)
- [ ] No overlap with another active Daily challenge
- [ ] Active tickbox on
- [ ] Dashboard tile arranged (automatically or via TK-21)

---

## 🔍 Done? How to check

After the start date, open the player environment (menu → **View app**): is the Daily challenge tile on the dashboard, does the Micro game open (in fullscreen if you set that), and is the score recorded? Play it twice in a row to confirm that repeat play works. When you switch challenges, also check that the old Daily challenge has disappeared cleanly.

---

*Basis: LearnStrike platform, as of April 2026 · the unlimited number of attempts is a deliberate design choice, confirmed by the Product Owner on 30-08-2026. Related cards: TK-16 (battle), TK-18 (Direct Play & public micro game), TK-21 (dashboard).*
