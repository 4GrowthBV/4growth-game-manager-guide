---
type: Runbook
title: "TK-16 Create a battle (Battle Arena)"
description: "How to set up a battle: a one-on-one knowledge duel in which players challenge each other in a micro game."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# ⚔️ Task card TK-16 — Create a battle (Battle Arena)

> **For game managers.** How to set up a battle: a one-on-one knowledge duel in which players challenge each other in a micro game.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**A battle is a duel between two players in the Battle Arena.** The challenger plays a micro game and the opponent gets the same game. The winner earns bonus points. You decide where the questions come from, how the points work and when the battle runs.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Battles** → **Add battle** |
| **When to use** | Activating and repeating knowledge in a playful way; extra buzz alongside a Campaign or during a tournament |
| **Question source** | A Campaign (the system picks a random Micro game) or one or more individual Micro games |
| **Response time** | The time the challenged player has to **accept** the challenge — not the playing time per question |
| **Period** | **Available from/until** — must not overlap with another battle |
| **Watch out** | For a tournament Campaign, the battle has to fall entirely within the tournament period |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Battles** → **Add battle**.
2. Fill in the basics: **Name** and **Description** (per language) and an **Image**.
3. Choose the **question source**:
   - **Random Micro game from Campaign** — pick a Campaign and the system will draw a random Micro game from it for each battle round. Note: a Campaign with "Anonymous users" access cannot be selected here.
   - **Individual Micro games** — select one or more Micro games yourself.
4. Set the points:
   - **Win bonus** — the bonus points for the winner.
   - **Percentage of the win bonus the loser receives** (0–50%) — consolation points that keep losers motivated.
   - **Factor for beating a higher-ranked player** (100–500) — an extra reward for anyone who beats a stronger opponent.
5. Set the rules of play:
   - **Response time** (in seconds) — the window within which the challenged player has to **accept** the challenge. Once that time runs out, the challenge expires. So this is not the time per question; you set that in the Micro game or quiz itself.
   - **Daily limit** — the maximum number of battles per player per day (leave empty for unlimited).
   - **Simultaneous open sessions** — how many battles a player may have running at the same time (leave empty for unlimited).
6. Choose **Available from** and **Available until**:
   - The period must **not overlap** with another battle — only one can run at a time.
   - Does the battle belong to a tournament Campaign? Then the whole battle period has to fall **within the tournament period** (TK-14).
7. Handy: tick **Add dashboard tile** so the battle appears on the player dashboard straight away. Turn on **Enable fullscreen mode** for the Micro game if you want to.
8. Click **Save**. Players can now challenge each other in the Battle Arena as soon as the period starts.
9. Want to stop early? Open the battle and choose **Stop battle**.

---

## ⭐ Golden rules & common mistakes

- **Response time is accept time.** Don't set it too short: a player has to notice the challenge coming in. A day or more is more realistic for most audiences than a few minutes.
- **One battle at a time.** The system rejects overlapping periods. Schedule battles one after the other, not on top of each other.
- **Give the loser something.** A loser percentage of 20–30% keeps players in the game; 0% puts them off after a couple of defeats.
- **A daily limit pays off.** Without one, keen players can skew the ranking by battling endlessly.
- **Campaign as the source? Check the Micro games.** Every Micro game in the Campaign can come up — including that half-finished test game. If that's a risk, use individual Micro games instead.
- **Battle points count as a bonus** on top of the Campaign score. Exactly how those bonus points feed through into a Leaderboard is **[still to verify]**.

---

## ✅ Checklist before you start

- [ ] Name, description (all languages) and image filled in
- [ ] Question source chosen deliberately and played through yourself
- [ ] Win bonus, loser percentage and factor set
- [ ] Response time generous enough to accept a challenge
- [ ] Daily limit and open sessions as you want them
- [ ] Period checked: no overlap with other battles, and within any tournament period
- [ ] Dashboard tile arranged (automatically or via TK-21)

---

## 🔍 Done? How to check

Open the player environment (menu → **View app**) with two test accounts. Challenge account B from account A, play the battle through and check: did both players get the right Micro game, are the bonus points correct for winner and loser, and does the result show up in the battle Leaderboard?

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | How do battle bonus points count towards a Leaderboard — with the Campaign score or separately? | Play a battle through with a test account and compare the Leaderboard standings before and after | 4Growth |

---

*Basis: LearnStrike platform, as of April 2026 · meaning of response time verified by 4Growth on 30-08-2026. Related cards: TK-06 (Campaign), TK-14 (tournament), TK-17 (Daily challenge), TK-21 (dashboard).*
