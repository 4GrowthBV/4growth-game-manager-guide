---
type: Runbook
title: "TK-09 Add a MicroGame module"
description: "How to add a MicroGame module to a challenge and set up the module settings — no technical knowledge needed."
tags: [task-card, content, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-09 — Add a MicroGame module

> **For game managers.** How to add a MicroGame module to a challenge and set up the module settings — no technical knowledge needed.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**A module is a single learning activity within a challenge.** This card **also** explains the **general module settings** (factor, skills, replayable, start/end screen) — they apply to every module type and come back in TK-10 through TK-12 and TK-25. The content **of** the micro game (questions, images, levels) is not set here but in the game itself: see the **Template Games** task cards (Unity / Configuration Editor).

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → [campaign] → [challenge] → **Add module** → type **MicroGame** |
| **When to use** | The "Do" step of a challenge: practising through a game |
| **What you need** | An existing, filled micro game (available to your organisation); name + description per language |
| **Points** | Factor: a base of **10,000 points** per module, adjustable **0–500%** |
| **Stars** | Star thresholds (1–5) are set on the **micro game**, not on the module |
| **Permissions** | Manager role (or higher), 2FA active |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Campaigns** → [campaign] → click the challenge open.
2. Click **Add module** and choose the type **MicroGame**.
3. Pick the **Micro game** from the list of games available to your organisation. Can't find the game you want? Then it has not been assigned to your organisation (yet) — check with 4Growth.
4. Fill in the basics: **Name** (required) and **Description** — per language. Optionally an **Image**; for this type you can also use the image of the micro game itself.
5. Set the **general module settings** (these apply to every module type):
   - **Factor**: a percentage of the base score of 10,000 points, 0–500%. 100% = 10,000 points, 200% = 20,000. This is how you make heavier modules worth more.
   - **Skills**: link one or more skills — they feed the skill graph in the player profile.
   - **Replayable**: the player may play again to improve their score.
   - **Resumable** + **Maximum resume period** (1–365 days): the player may pick up later where they left off.
6. Set up the **start screen** and **end screen**:
   - **Layout**: text **below**, **left of** or **right of** the image.
   - Per screen: **title**, **description** and **image**.
   - **End screen button label**: the text on the continue button (max 100 characters), e.g. "Next" or "On to the reflection".
7. Optional: tick **Enable fullscreen mode** — the game then fills the whole screen. Recommended for games with a lot of visual elements.
8. Click **Save** and drag the module into the right position in the challenge if needed.

---

## ⭐ Golden rules & common mistakes

- **Game first, module second.** Check that the micro game is filled and tested before you hang it in a challenge (see the Template Games task cards).
- **Choose the factor deliberately.** Keep it simple: 100% as standard, higher only for heavier or more important modules. Big differences make the leaderboard impossible to follow.
- **Replayable on = Kolb step 5 (Repeat).** Switch this on by default for micro games, unless it is a one-off test.
- **Forgetting skills = an empty skill graph.** Always link at least one skill if your organisation works with skills.
- **Archived micro games** cannot be chosen for new modules, but stay playable in existing ones.
- **Deleted is not gone.** You can bring deleted modules back with **Restore**.

---

## ✅ Checklist

- [ ] Right micro game chosen (content checked and tested yourself)
- [ ] Name + description in every language
- [ ] Factor set deliberately
- [ ] Skills linked
- [ ] Replayable/resumable as intended (including the resume period)
- [ ] Start and end screen: layout, title, description, image
- [ ] End screen button label worded sensibly
- [ ] Module in the right position in the challenge

---

## 🔍 Done? How to check

Play the module through yourself in the player environment (menu → **View app**) or through the module preview. Check: does the game start, are the start and end screens right, do you get points and stars, and does playing again work when replayable is switched on?

---

*Basis: LearnStrike platform, as of April 2026. Related cards: TK-07 (challenge), TK-10 (quiz), TK-11 (survey), TK-12 (questionnaire), TK-25 (text & video), Template Games task cards (game content).*
