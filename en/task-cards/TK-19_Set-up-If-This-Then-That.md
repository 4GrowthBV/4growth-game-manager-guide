---
type: Runbook
title: "TK-19 Set up If This Then That"
description: "How to send players automatically to the right next step after a Challenge — based on their score or their answers."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-19 — Set up If This Then That

> **For game managers.** How to send players automatically to the right next step after a Challenge — based on their score or their answers.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**If This Then That (IFTTT) lets you build tailored learning routes.** For each Challenge you set rules: "if the player scores or answers this, then they go there." That way a player with a low quiz score gets a repeat Challenge, while a player with a high score gets extra depth.

⚠️ **If This Then That is fairly new functionality.** Its place in the interface is settled, but a separate manual is still coming on exactly how it works — how rules are evaluated and what happens when no rule matches. Always test your set-up yourself before you let players loose on it.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → [campaign] → open the Challenge → **three dots** to the right of the title → **Set up If This Then That** |
| **When to use** | Differentiated learning routes: repetition on a low score, depth on a high score, routing on a survey or questionnaire outcome |
| **What you need** | A Challenge with at least one quiz, survey or questionnaire module; the destination Challenges have to exist already |
| **A rule consists of** | A label (name) + one or more conditions + a destination (another Challenge or an external URL) + an order |
| **Condition types** | Module score · survey answer given · questionnaire category score (% or points) · questionnaire outcome category |
| **Permissions** | Manager role (or higher), 2FA enabled |

💡 **Looking for If This Then That and can't find it?** It isn't shown as a tab — it sits under the **three dots** to the right of the title when you open a Challenge in the Control Panel.

---

## 🚀 Step by step

1. Open the **Control Panel** → **Campaigns** → pick your Campaign → open the Challenge that the next step should follow.
2. Click the **three dots** to the right of the title and choose **Set up If This Then That**.
3. Create a new **rule** and give it a recognisable **label**, e.g. "Low score → repeat". This label is for you, to keep your rules apart.
4. Set the **condition(s)**. Pick a type per condition:
   - **Module score** — the score achieved on a specific module (a quiz, for example), with a threshold (lower than 6,000 points, say).
   - **Survey answer given** — the player picked a particular answer in a survey module.
   - **Questionnaire category score** — the score on a category from a questionnaire, in **%** or in **points**.
   - **Questionnaire outcome category** — the category the questionnaire produced as its outcome (a profile type, for example).
5. Choose the **destination**:
   - **Another Challenge** — a repeat or deep-dive Challenge, for instance. Whether you can also route to a Challenge in a *different* Campaign is **[still to verify]**.
   - **External URL** — a page in your LMS or a sign-up form, for instance.
6. Repeat steps 3–5 for every route. An example set-up:
   - Rule 1: quiz module score < 6,000 → Challenge "Basics refresher".
   - Rule 2: quiz module score ≥ 8,000 → Challenge "Advanced deep dive".
7. Put the rules in the right **order**. The order in which the platform evaluates the rules, and which rule wins when several match, is **[still to verify]** — for now, assume the topmost matching rule wins, and test that.
8. **Save** and test it through yourself (see below).

---

## ⭐ Golden rules & common mistakes

- **Test every path yourself before going live.** As long as the behaviour isn't fully documented, playing through with a test account is your only certainty.
- **Build the destinations first.** You can only route to a Challenge that already exists — so build your repeat and deep-dive Challenges first.
- **Cover every outcome.** What happens when no rule matches is **[still to verify]**. So build your rules such that one always matches, and test the "no rule matches" scenario anyway.
- **Keep it simple.** Two or three clear routes work better than ten rules that overlap.
- **Mind your score thresholds.** A module yields 10,000 points by default; choose thresholds that fit that, and don't leave a "gap" between rules (for example < 6,000 and ≥ 8,000, but nothing for 6,000–8,000).
- **Deleting a destination Challenge?** Then check the rules pointing to it as well.

---

## ✅ Checklist before you go live

- [ ] Destination Challenges exist and are filled
- [ ] Every rule has a clear label
- [ ] Score thresholds connect up (no gaps, no overlap)
- [ ] Order of rules chosen deliberately
- [ ] Every path played through yourself with a test account
- [ ] "No rule matches" scenario tested
- [ ] External URLs checked (right link, opens properly on mobile)

---

## 🔍 Done? How to check

Play the Challenge through yourself with a test account. Score deliberately low once and high once: do you end up on the right follow-up Challenge (or URL) in both cases? For survey and questionnaire conditions, test every answer and every outcome category at least once. Also play out an outcome that no rule covers, and record what happens then.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | In what order are rules evaluated, and which one wins when several match? | Part of the If This Then That manual — work it out and record it | Product Owner |
| 2 | What happens when no rule matches — does the player get the normal next step? | Play out an outcome that falls outside every rule and record the behaviour | Product Owner |
| 3 | Can you route to a Challenge in another Campaign, or only within the same Campaign? | Try to pick a Challenge from another Campaign as the destination | Product Owner |

*A separate manual on "how If This Then That works" is coming for these points. This card will be updated afterwards.*

---

*Basis: LearnStrike platform, as of April 2026 · place in the UI verified by 4Growth on 30-08-2026; how the rules behave is not yet documented. Related cards: TK-07 (Challenge), TK-10 (quiz), TK-11 (survey/reflection), TK-06 (Campaign).*
