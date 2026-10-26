---
type: Runbook
title: "TK-25 Add text and video modules"
description: "How to add the three simple module types: Text, YouTube/Vimeo video and Gamified video (HiHaHo) — no technical knowledge needed."
tags: [task-card, content, en]
timestamp: 2026-09-30
lifecycle: active
---

# 🎯 Task card TK-25 — Add text and video modules

> **For game managers.** How to add the three simple module types: Text, YouTube/Vimeo video and Gamified video (HiHaHo) — no technical knowledge needed.
> **Status:** v1.1 · 30-09-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**These are the "telling" modules.** Perfect for introducing a learning goal (Kolb step 1) or making sense of things after a game (step 3). Text and YouTube/Vimeo are non-interactive; Gamified video (via HiHaHo) is interactive — but it's only available if the HiHaHo integration is active for your organisation. How to build and publish such a video in HiHaHo is covered in TK-26.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → [campaign] → [challenge] → **Add module** → type **Text**, **YouTube**, **Vimeo** or **Gamified video** |
| **When to use** | Introduction, explanation, sense-making, instruction video |
| **Text** | Content per language + an optional image |
| **YouTube / Vimeo** | All you need is a valid video URL from that platform |
| **Gamified video** | Pick a HiHaHo video from the folders assigned to your organisation; requires an active HiHaHo integration and a published video (see TK-26) |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Campaigns** → [campaign] → [challenge] → **Add module** and pick the type.
2. Always fill in the general module settings — name, description, factor, skills, start/end screen — see TK-09, steps 4–7.

**Type Text**

3. Fill in the **Content** (mandatory, per language): the text the player reads.
4. Optionally add an **image** alongside the text.
5. Want to give players an idea of how long it takes? Put the reading time in brackets in the module **title** yourself, for example "Why hand hygiene works (3 min)". The platform has no separate field for reading time and doesn't calculate it either.

**Type YouTube or Vimeo**

3. Paste the **video URL** into the URL field. The platform checks that it is a valid YouTube or Vimeo link.
4. Note: the video has to be public or accessible via link — private videos stay black for players.

**Type Gamified video (HiHaHo)**

3. Don't see this type in the list? Then the **HiHaHo integration** isn't active for your organisation — ask 4Growth about it.
4. Pick the **video** from the list. You only see videos from the HiHaHo **folders assigned to your organisation**. The list is synchronised from HiHaHo automatically, but not instantly: a new video can take a few hours to appear [still to verify].
5. Only published videos come through. If the video is set to **Only me** in HiHaHo, it won't appear in the list [still to verify].
6. You build the interaction (questions, hotspots) and the score in HiHaHo itself, not in the Control Panel. HiHaHo decides through its end score screen whether the module is passed.

**To finish (all types)**

7. Click **Save** and drag the module to the right spot in the challenge.

---

## ⭐ Golden rules & common mistakes

- **Short is strong.** Text modules of 150–300 words work best; split long stories across several modules or challenges.
- **Put the reading time in the title.** Players are less likely to drop out if they know up front that something takes two minutes. Reckon on roughly 200 words per minute.
- **Text and video are not a play experience** — use them as a run-up to or a debrief around a game or quiz, never as a whole challenge.
- **Always test the video URL yourself** in an incognito window: private or region-blocked videos may well play for you but not for the player.
- **Multilingual? Your videos too.** One shared video with Dutch narration doesn't work for players in another language; consider a separate solution per language.
- **HiHaHo video not showing up?** Run through this list: is it in the right folder, is it published (not "Only me"), is the folder linked to your organisation, and has the synchronisation run yet? An administrator can also start the import straight away. See TK-26.
- **Keep the factor low.** Watching and reading is not a performance; a low factor keeps the leaderboard fair towards games and quizzes. The factor is a percentage of the default score of 10,000 points that every module carries — it has nothing to do with time or length.

---

## ✅ Checklist

- [ ] Right type chosen (Text / YouTube / Vimeo / Gamified video)
- [ ] General module settings filled in (see TK-09)
- [ ] Text: content in every language + an image where it helps
- [ ] Text: reading time added to the title if the text is on the longer side
- [ ] Video: URL tested in an incognito window
- [ ] Gamified video: right HiHaHo video chosen, published, and the interaction finished in HiHaHo
- [ ] Factor set appropriately (low)
- [ ] Module in the right spot in the challenge

---

## 🔍 Done? How to check

Open the module in the player environment (menu → **View app**). Text: readable, right language, image showing? Video: does it play straight away, on mobile too? Gamified video: do the interaction moments work, and does the player land neatly on the module's end screen afterwards?

---

## 🔎 Still to verify

| Point | How we verify it | Who |
|---|---|---|
| How quickly a new HiHaHo video appears in the list, and whether videos set to "Only me" are skipped | Publish test videos and compare after the synchronisation (see TK-26) | 4Growth (ticket) |

---

*Basis: LearnStrike platform, as of April 2026 · verified by 4Growth on 30-08-2026: there is no reading time setting in the platform, and the factor is a percentage of the default score of 10,000 points · extended on 30-09-2026 with synchronisation, publishing and scoring via HiHaHo (sources: see TK-26). Related cards: TK-26 (create & manage a gamified video), TK-09 (general module settings), TK-07 (challenge), TK-10 (quiz).*
