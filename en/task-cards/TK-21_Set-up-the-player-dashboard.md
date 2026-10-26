---
type: Runbook
title: "TK-21 Set up the player dashboard"
description: "How to decide what players see on their home screen: sections with tiles for campaigns, battles and more."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-21 — Set up the player dashboard

> **For game managers.** How to decide what players see on their home screen: sections with tiles for campaigns, battles and more.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**The dashboard is the shop window of your player environment.** You build it from **sections** (rows with a heading) that hold **tiles**. A tile always points to content: a campaign, a battle, a daily challenge or a direct-play micro game. A tidy dashboard is the difference between "where do I start?" and playing straight away.

ℹ️ **A leaderboard is not a tile.** If a leaderboard is switched on, a **Leaderboards** button appears at the top of the main navigation in the player app. So you don't need to make a tile for it — and you can't — see TK-20.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Dashboard layout** |
| **When to use** | With every new campaign, battle or daily challenge, and periodically as a clean-up round |
| **What you need** | Section name + description (per language); the items the tiles point to must already exist |
| **Tile types** | Campaign · Battle · Daily challenge · Direct-play micro game |
| **Not a tile type** | Leaderboard — that shows up as a button in the main navigation |
| **Order** | Use **Dashboard layout** to decide which section a tile sits in and in what order |
| **Automatic** | Organisation setting: add new items as a tile automatically (on/off per type) |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

**A. Create sections**

1. Open the **Control Panel** → **Dashboard layout**.
2. Create a **section**: fill in **Name** and **Description** — for each available language (tabs above the field). For example "New this month" or "Your learning paths".
3. **Save.** Repeat for every row you want on the dashboard.

**B. Add and order tiles**

4. Open a section and choose **Add** (tile).
5. Pick the **type**: campaign, battle, daily challenge or direct-play micro game.
6. Pick the specific item (which campaign, for instance). The drop-down only lists items that already exist.
7. **Save.** Then use **Dashboard layout** to decide which section each tile belongs to and in what order the tiles appear. Put your most important content at the top.

**C. Clear out orphaned tiles**

8. Go to the overview of orphaned tiles: tiles whose source (a deleted campaign, for example) no longer exists. The exact name of this menu item is **[still to verify]**.
9. Delete these tiles — they do nothing for players and they look sloppy.

**D. Add tiles automatically**

10. Want every new item to get a tile by itself? Go to **Admin → Organisations → [your organisation] → Gameplay → Dashboard** and switch it on per type: automatic tile for a new campaign / battle / daily challenge / direct-play micro game.

---

## ⭐ Golden rules & common mistakes

- **Think like a new player.** What should someone logging in for the first time see first? Put that at the top.
- **Looking for the leaderboard on the dashboard?** It isn't there — it lives in the main navigation as soon as you activate a leaderboard (TK-20).
- **Automatic on = clean up yourself.** With the automatic setting the dashboard fills up on its own. Schedule a regular clean-up.
- **A tile doesn't make hidden content visible.** The campaign's own access rules (tags, publication status, TK-06) still apply. What a player sees for a tile pointing to a draft campaign is **[still to verify]**.
- **Multilingual? Fill in both languages** for section names and descriptions.
- **Deleting a campaign? Check for orphaned tiles.** Otherwise a dead tile is left behind.

---

## ✅ Checklist

- [ ] Sections have clear names in every language
- [ ] The most important content is at the top
- [ ] Every tile points to an existing, published item
- [ ] Tile order set via Dashboard layout
- [ ] No orphaned tiles in the overview
- [ ] Automatic tile setting deliberately switched on or off
- [ ] Dashboard checked on mobile and desktop

---

## 🔍 Done? How to check

Open the player environment (menu → **View app**): are all sections and tiles there, in the right order, with the right texts? Click every tile — does it take you to the right item? Also check with an account from a specific target group (tag) that it only sees the intended content, and see whether the Leaderboards button is in the main navigation if you activated a leaderboard.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | What exactly is the menu item for orphaned tiles called in the interface? | Look it up in the Control Panel under Dashboard layout | 4Growth |
| 2 | What does a player see for a tile pointing to a draft campaign — is the tile hidden or empty? | Create a tile for a draft campaign and view the dashboard with a player account | 4Growth |

---

*Basis: LearnStrike platform, as of April 2026 · verified by 4Growth on 30-08-2026: leaderboards are not a tile type but a button in the main navigation, and tile order is handled through Dashboard layout. Related cards: TK-06 (campaign), TK-16 (battles), TK-17 (daily challenges), TK-18 (direct play), TK-20 (leaderboards).*
