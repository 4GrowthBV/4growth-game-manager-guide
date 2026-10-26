---
type: Runbook
title: "TK-20 Create and export a leaderboard"
description: "How to build your own Leaderboard across one or more Campaigns, and export the standings to Excel."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-20 — Create and export a leaderboard

> **For game managers.** How to build your own Leaderboard across one or more Campaigns, and export the standings to Excel.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**A manual Leaderboard is a ranking that you put together yourself.** Unlike the automatic Leaderboard that every Campaign has by default (players see it as **Leaderboard**), here you decide: which Campaigns count, which period counts, and who gets to see the list (through tags). Ideal for a team competition or a themed month.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Leaderboards** → **Add** button |
| **When to use** | Competition across several Campaigns, a fixed campaign period, or a ranking per audience (tag) |
| **What you need** | A name (per language), the Campaigns that count, and optionally tags to filter on |
| **Several Campaigns** | Scores from the Campaigns you pick are **added together** into a single ranking |
| **Tags** | Determine **who sees the Leaderboard** — only players with the chosen tag |
| **Difference from the Campaign leaderboard** | The Campaign leaderboard is automatic, one per Campaign (switch it off with the Campaign tickbox "Hide leaderboard", TK-06). A Leaderboard you create is manual, put together by you |
| **Where players see it** | As the **Leaderboards** button in the main navigation of the player app — not as a tile on the dashboard |
| **Export** | XLSX (Excel), straight from the Leaderboard list |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Leaderboards** → **Add**.
2. Fill in the **Name** — per available language (tabs above the field). Pick a name players understand, e.g. "Summer competition 2026".
3. Set the **visibility period**: **Available from** / **Available until**. This decides *when* players see the Leaderboard.
4. Set the **score period**: **Score from** / **Score until**. This decides which scores count. Only points earned within this period make it into the ranking.
5. Choose the **Campaigns** that count. Several Campaigns is fine: the scores a player earned in them are **added together**.
6. Optional: filter by **tags**. Here's how that works:
   - The tag decides **who gets to see the Leaderboard**. If a player has the tag `manager`, and this Leaderboard filters on `manager`, that player sees it.
   - Combine that with Campaigns aimed at the same audience and you get one ranking with the combined scores of *those* Campaigns, visible to exactly *that* group.
   - Players without the tag don't see this Leaderboard, but they can still see another Leaderboard that filters on *their* tag.
7. **Save.** The Leaderboard appears in the list.
8. Several Leaderboards? Decide the **order** in which players see them using the ordering function in the list (**Save order**).
9. Exporting: choose **Export** on the Leaderboard and you get an **XLSX** file with the current standings.

---

## ⭐ Golden rules & common mistakes

- **Tags steer visibility, not just participation.** Anyone without the tag doesn't see the Leaderboard at all. Use that deliberately: it's how you give each audience its own ranking without the groups seeing each other.
- **Visibility ≠ score period.** These are two different things: you can show a Leaderboard until the end of December while only November scores count. Set both deliberately.
- **Forget the score period and you get an empty or unfair list.** Does your campaign start on 1 September? Then set "Score from" to 1 September, otherwise old scores count too.
- **Filtering on tags? Check the tags first.** Check tag assignment (TK-05) before the start — a player without the tag misses the whole ranking.
- **Multilingual? Fill in both languages.** An empty language shows an empty name to players with that language setting.
- **Handing out prizes? Export on the end date.** The export shows the standings at that moment — so plan your export right after the score period ends.

---

## ✅ Checklist before you go live

- [ ] Name filled in for every language the organisation uses
- [ ] Visibility period matches what you told players
- [ ] Score period matches the start and end of the campaign
- [ ] Right Campaigns ticked (scores are added together)
- [ ] Tag filter chosen deliberately (or deliberately left empty)
- [ ] Checked that the intended audience actually has the tag
- [ ] Order of Leaderboards makes sense for the player

---

## 🔍 Done? How to check

Open the player environment (menu → **View app**) and look at **Leaderboards** in the main navigation at the top: is your Leaderboard there, is the name right, and do scores appear after you play a module with a test account in a Campaign that counts? If you use a tag filter, also test with an account *without* that tag — it shouldn't see the Leaderboard at all.

---

*Basis: LearnStrike platform, as of April 2026 · how tags work, the adding up of scores across Campaigns and the place in the player navigation verified by 4Growth on 30-08-2026. Related cards: TK-05 (tags), TK-06 (Campaign, leaderboard on/off), TK-21 (player dashboard), TK-23 (exports).*
