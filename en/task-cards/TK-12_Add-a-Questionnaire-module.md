---
type: Runbook
title: "TK-12 Add a Questionnaire module"
description: "How to set up a questionnaire: a list of questions that results in a profile or outcome per player. This is the most complex module type — plan time for it."
tags: [task-card, content, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-12 — Add a Questionnaire module

> **For game managers.** How to set up a questionnaire: a list of questions that results in a profile or outcome per player. This is the most complex module type — plan time for it.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**A questionnaire is more than a survey.** Answers add up per category and lead to a **result or profile** (a stress profile or an interest profile, for example). The difference in one sentence: quiz = right/wrong, survey = free answers, questionnaire = answers → categories → profile.

ℹ️ Where these types come from. The questionnaire types in LearnStrike are based on existing, widely used questionnaires. Considering a questionnaire for a different context? Discuss the type with 4Growth first.

⚠️ **Don't do your first one on your own.** Every type has its own settings, values and scoring logic. Build your first questionnaire together with 4Growth or an experienced colleague.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → [campaign] → [challenge] → **Add module** → type **Questionnaire** |
| **When to use** | Self-scans, profile tests, validated questionnaires (a stress test or interest test, for example) |
| **Types** | hypothesis, multiple_choice, bat, coping, zeven_domeinen, stress_test, riasec |
| **Origin** | Based on existing questionnaires |
| **Scoring** | Differs **per type** — the type you choose determines how answers count |
| **Flow** | 1. Choose a type → 2. Settings for that type → 3. Categories → 4. Questions → 5. Results |
| **Comparing** | Results can be compared with an earlier questionnaire (baseline and follow-up measurement) |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

*A broad outline — the screens differ per questionnaire type.*

1. Open the **Control Panel** → **Campaigns** → [campaign] → [challenge] → **Add module** → **Questionnaire**.
2. Fill in the general module settings — name, description, factor, skills, start and end screen — see TK-09, steps 4–7.
3. Choose the **questionnaire type**. The available types: **hypothesis**, **multiple_choice**, **bat**, **coping**, **zeven_domeinen**, **stress_test**, **riasec** (interest profile).
4. As soon as you pick a type, the **settings and values that belong to that type** appear. Fill those in. Every type has its own set — which is exactly why doing your first one together with 4Growth is a good idea.
5. Then follow the build flow in this order:
   1. **Create categories** — the "axes" you score on, for example the seven domains or the RIASEC letters.
   2. **Create questions** — for each question you link the answers to categories.
   3. **Create results** — the profiles/outcomes the player gets to see, with a text per category or score range.
6. Optional: set up **comparison with an earlier questionnaire** — the player then sees how they have developed compared to an earlier session (baseline and follow-up). We expect both questionnaires need the same setup (type and categories); this is **[still to verify]**.
7. Click **Save** and test the whole flow yourself, from the first question to the results screen.

---

## ⭐ Golden rules & common mistakes

- **The type determines the scoring.** How heavily an answer counts and how the result is calculated depends on the type you choose. Don't assume what you learned from another type applies.
- **Choose the type up front, for good.** Whether you can still change the type after creating the module is **[still to verify]** — for now, assume you cannot, and that switching means starting over.
- **Work in a fixed order: categories → questions → results.** You can only link questions properly once the categories are in place, and only write results once the questions are in place.
- **Use validated questionnaires where they exist.** Types such as stress_test and riasec are based on established methods; don't invent your own variants without a subject-matter expert.
- **Write result texts for the player, not for the researcher.** Positive, concrete, and with something they can act on.
- **Baseline and follow-up? Plan it first.** Set both questionnaires up identically before the first session — you cannot repair this afterwards.
- **Test with different answer patterns** — extremely high, extremely low and average — so you have seen every possible profile at least once.

---

## ✅ Checklist

- [ ] Type chosen deliberately and discussed with 4Growth or a subject-matter expert
- [ ] Type-specific settings and values filled in
- [ ] General module settings filled in (see TK-09)
- [ ] Categories complete and correctly named
- [ ] All questions linked to the right categories
- [ ] Results/profiles written for every possible outcome
- [ ] All texts in every language
- [ ] For baseline and follow-up: comparison set up and identical setup checked
- [ ] Complete flow tested yourself with at least three answer patterns

---

## 🔍 Done? How to check

Go through the questionnaire several times in the player environment (menu → **View app**), deliberately giving different answers. Check each run: does the profile or result shown match what you would expect from those answers? For validated tests, have a subject-matter expert review the result before you publish.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | How exactly does scoring work per questionnaire type, and how do you set the result rules (thresholds, combinations)? | Request documentation through 4Growth and record it per type; then expand this card or split it per type | Product Owner |
| 2 | Can you still change the type of a questionnaire after creating it? | Create a test questionnaire and try to change the type | Product Owner |
| 3 | What conditions apply to comparing with an earlier questionnaire? | Set up two questionnaires and try to configure the comparison | Product Owner |

*This is the most complex module type and at the same time the least documented. This card will be expanded once the scoring logic per type has been worked out.*

---

*Basis: LearnStrike platform, as of April 2026 · the origin of the types and the type-dependent settings were described by the Product Owner on 30-08-2026; the scoring logic per type has not been recorded yet. Related cards: TK-09 (general module settings), TK-10 (quiz), TK-11 (survey).*
