---
type: Runbook
title: "TK-24 Set up onboarding, skills & profile"
description: "Three setup jobs in one card: onboarding questions for new users, managing skills, and filling the player profile with handouts."
tags: [task-card, insights, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-24 — Set up onboarding, skills & profile

> **For game managers.** Three setup jobs in one card: onboarding questions for new users, managing skills, and filling the player profile with handouts.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

> ⚠️ **Heads-up:** this part of LearnStrike has changed since April 2026. This card is being updated. In doubt? Email support@4growth.com.

---

**These three settings shape the first impression and the profile of your players.** Onboarding questions segment new users automatically with tags. Skills make learning results visible in a graph. And through the profile settings you give players documents and take aways.

---

## 📌 Highlights

| | |
|---|---|
| **Where (onboarding)** | **Admin → Organisations → [your organisation] → Users → Onboarding** |
| **Where (skills)** | Control Panel → **Skills** |
| **Where (profile)** | **Admin → Organisations → [your organisation] → Profile** → Settings / Take aways / Handouts |
| **When to use** | At the start of a new organisation or target group; after that, with every new learning path that needs segmentation or reference material |
| **Smart move** | Onboarding answer = automatic tag → drives campaign access (TK-06) and leaderboard filters (TK-20) |
| **Watch out** | Onboarding questions are expected to apply to **new** users only — see "Still to verify" |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

**A. Onboarding questions — segmenting new users automatically**

1. Go to **Admin → Organisations → [your organisation] → Users → Onboarding**.
2. Create a **question** — for each available language (for example "Which department do you work in?").
3. Decide whether the question is **mandatory** (checkbox).
4. Add at least **2 answers** (per language too) and link an **assigned tag** to each answer. If a new user picks "Kitchen", they automatically get the "Kitchen" tag.
5. Put multiple questions in the **order** you want and **save**.
6. Check: do the tags already exist (TK-05)? If not, create them first.
7. Adding a question to an organisation that already has users? Assume existing users will **not** be shown the question after the fact, and assign their tags manually or in bulk (TK-05). Whether it really works that way is **[still to verify]**.

**B. Skills — making learning results visible**

8. Go to Control Panel → **Skills** → **Add**.
9. Fill in **Name** and **Description** — per language. For example "Communication", "Hygiene", "Safety".
10. Tick **"show in graph"** if the skill should appear in the spider graph in the player profile.
11. Then link the skill to content: you do that on the **module**, **quiz question** or **survey item** itself (in its edit screen). The scores then feed the graph.

**C. Profile — sections, take aways and handouts**

12. Go to **Admin → Organisations → [your organisation] → Profile**.
13. **Settings** tab: decide which **profile sections** players see. Exactly which sections can be switched on and off is **[still to verify]**.
14. **Take aways** tab: settings for take aways (insights and answers players keep from modules and see again in their profile).
15. **Handouts** tab: reference documents for players.
    - First create **categories** (name + description, per language).
    - Add **handouts** per category: name, description and a **file** (pdf, doc/docx, xls/xlsx, ppt/pptx).
    - Tick the **visible** checkbox per handout and set the **order**.

---

## ⭐ Golden rules & common mistakes

- **Keep onboarding short.** One to three questions; every extra question costs you sign-ups. Only ask what you genuinely use for segmentation.
- **Set your onboarding up in time.** A question you add once the group is already in is expected to come too late — set up the onboarding before you invite or import users.
- **Agree on tag names first.** The tags from onboarding have to match your campaign access and leaderboard filters exactly — otherwise you're segmenting into thin air.
- **Not every skill belongs in the graph.** Five to eight skills make a readable spider graph; more turns it into a tangle.
- **Handouts are not an archive.** Only current, directly usable documents; use the visible checkbox to hide outdated material temporarily instead of leaving everything in place.

---

## ✅ Checklist

- [ ] Onboarding set up before the first users arrive
- [ ] Onboarding questions in every language, with the mandatory checkbox chosen deliberately
- [ ] Every answer linked to an existing tag
- [ ] Existing users: tags assigned manually or in bulk (TK-05)
- [ ] Skills created and linked to modules/questions
- [ ] "Show in graph" only on for the core skills
- [ ] Handout categories sensibly organised, files uploaded and set to visible
- [ ] Order of questions, skills and handouts checked

---

## 🔍 Done? How to check

Register a test account: do you get the onboarding questions in the right order and language, and does the account carry the right tag after answering (check under Users)? Then open the player profile: does the spider graph appear after playing a linked module, and can the handouts be opened and downloaded?

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | Are existing users still shown a new onboarding question, or does it only apply to new users? | Add an onboarding question to an organisation with existing users and log in with one of those existing accounts | 4Growth |
| 2 | Which profile sections can you switch on and off exactly under Profile → Settings? | Walk through the tab and record the options | 4Growth |

*This card will be updated as soon as the tests are done.*

---

*Basis: LearnStrike platform, as of April 2026 · reviewed by 4Growth on 30-08-2026; the assumption that onboarding only applies to new users has not been tested yet. Related cards: TK-01 (users), TK-05 (tags, bulk assignment), TK-06 (access via tags), TK-20 (leaderboard filters).*
