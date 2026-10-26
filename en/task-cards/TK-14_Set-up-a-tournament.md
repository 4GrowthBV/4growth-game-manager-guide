---
type: Runbook
title: "TK-14 Set up a tournament"
description: "How to turn a campaign into a tournament with a fixed start and end date — for a short, intense competition."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🏆 Task card TK-14 — Set up a tournament

> **For game managers.** How to turn a campaign into a tournament with a fixed start and end date — for a short, intense competition.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**A tournament is not a separate campaign type, but a setting on an ordinary campaign.** You switch on **Enable tournament mode** and choose a period. Players compete for the highest score within that period; after it, the campaign can no longer be played.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → campaign → **Edit** → **Enable tournament mode** |
| **When to use** | Kick-offs, theme weeks, campaigns with a deadline — anywhere time pressure and competition make the game more exciting |
| **What you need** | A campaign with challenges and modules (TK-06, TK-07); a start and end date |
| **Date rules** | The end date must be after the start date; the start date cannot be in the past |
| **What players see** | A TOURNAMENT badge, the leaderboard, and the status **Scheduled** / **Running** / **Finished** |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Build the campaign completely first: challenges, modules, everything played through (TK-06 through TK-12). In a tournament every day counts — the content has to be finished before the start.
2. Open the **Control Panel** → **Campaigns** → open the campaign → **Edit**.
3. Tick **Enable tournament mode**.
4. Fill in: **Tournament starts on** and **Tournament ends on** (date + time).
   - The end date has to be after the start date.
   - The start date cannot be in the past.
5. Check the leaderboard: leave **Hide leaderboard** off — a tournament without a ranking misses the point.
6. Click **Save** and publish the campaign (TK-06, step 10).
7. What players see now:
   - A **TOURNAMENT** badge on the campaign.
   - The tournament status: **Scheduled** (not started yet), **Running** (in progress) or **Finished** (over), with the running time.
   - The leaderboard with the current standings.
8. After the end date the campaign **can no longer be played** — players get the message *"Tournament finished"*. The results and the leaderboard do stay visible.

---

## ⭐ Golden rules & common mistakes

- **Plan with room to spare, don't start today.** The start date cannot be in the past; pick a start moment by which you have already sent the announcement.
- **Changing content during a running tournament = unfair.** Players who already played had different content. Get everything ready before the start.
- **Combining it with a battle? Mind the period.** A battle linked to a tournament campaign has to fall entirely within the tournament period — otherwise the system rejects the battle (TK-16).
- **Need an extra leaderboard?** The campaign leaderboard shows this campaign only. If you want a ranking across several campaigns or filtered by tags, create a separate leaderboard (TK-20).
- **The "Tournament finished" message can be adjusted per organisation** via Languages → Translations (the translation key for the end of a tournament).

---

## ✅ Checklist before the start

- [ ] Campaign complete and played through by you
- [ ] Tournament mode on, start and end date checked (including time and time zone)
- [ ] Leaderboard visible (Hide leaderboard off)
- [ ] Campaign published before the start date
- [ ] Any battles fall within the tournament period
- [ ] Announcement to players scheduled (with the end date in it!)

---

## 🔍 Done? How to check

Look at the campaign in the player environment (menu → **View app**): do you see the TOURNAMENT badge and the status **Scheduled** with the right start date? After the start, check whether the status switches to **Running** and whether scores are coming in on the leaderboard. To test, you can set up a short trial tournament period on a copy of the campaign (TK-08).

---

*Basis: LearnStrike platform, as of April 2026 · UI not yet verified in a live environment. Related cards: TK-06 (campaign), TK-08 (duplicating), TK-15 (leagues), TK-16 (battle), TK-20 (leaderboard).*
