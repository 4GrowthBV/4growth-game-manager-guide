---
type: Runbook
title: "TK-10 Add a Quiz module"
description: "How to build a quiz module with questions, feedback and a pass threshold — no technical knowledge needed."
tags: [task-card, content, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-10 — Add a Quiz module

> **For game managers.** How to build a quiz module with questions, feedback and a pass threshold — no technical knowledge needed.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**A quiz tests knowledge directly in the platform** — no Unity, no separate tool. You create questions (single or multiple choice) with feedback per question, set the time and the pass threshold, and you can deliver questions in bulk through Excel.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → [campaign] → [challenge] → **Add module** → type **Quiz** |
| **When to use** | A knowledge check after a learning activity; a testing moment within a challenge |
| **What you need** | Questions + answers (per language), feedback texts, images per question if you want them |
| **Pass threshold** | The percentage of correct answers (0–100%) needed to pass |
| **Time per question** | 15, 30, 45, 60, 75 or 90 seconds — **30 seconds** by default |
| **Random selection** | Show 1–200 questions per round, picked at random from your full question set |
| **Bulk** | Import/export questions through **Excel** (including a template to download) |
| **Permissions** | Manager role (or higher), 2FA active |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Campaigns** → [campaign] → [challenge] → **Add module** → **Quiz**.
2. Fill in the general module settings — name, description, factor, skills, replayable, start/end screen — see TK-09, steps 4–7.
3. Set the quiz settings:
   - **Threshold**: the percentage of correct answers needed to pass (0–100%).
   - **Time per question**: choose from **15, 30, 45, 60, 75 or 90 seconds**. The default is 30 seconds.
   - **Number of questions to show** (1–200): each round, the platform picks this many questions at random from your set. Handy in combination with replayable: different questions every round.
4. Add questions through **Add question**. Per question:
   - **Question type**: single choice (one correct answer) or multiple choice (several correct answers).
   - **Question text** (per language) and optionally an **image**.
   - **Answers** through **Add answer** (per language); tick per answer whether it is **correct**.
   - **Feedback correct** and **Feedback incorrect** (per language): a short explanation the player sees after answering — this is your sense-making moment (Kolb step 3).
   - Optional: **Skills** per question.
5. Lots of questions? Use the **Excel route**:
   - First download the **template** (with the quiz questions: download template).
   - Fill the template with your questions and **import** the file.
   - You can also **export** existing questions, edit them outside the platform and import them again.
6. Click **Save** and drag the module into the right position in the challenge.

---

## ⭐ Golden rules & common mistakes

- **Feedback is where the learning happens.** Write substantive feedback for **every** question — including the correct one ("That's right, because…"). A quiz without feedback is a test, not a learning tool.
- **Match the time to the question.** 30 seconds works for a short knowledge question; a question with an image or a longer case deserves 45 to 90 seconds. Read the question out loud yourself and count along.
- **More questions than you show = repetition pays off.** Create 20 questions and show 10, for example; replaying then stays interesting.
- **Pick a realistic threshold.** 70–80% is common; 100% is frustrating under time pressure.
- **Explain multiple choice properly.** Players usually expect one correct answer; make it clear in the question text that there are several.
- **Excel import: always use the template.** Your own column layouts will fail. After importing, spot-check a few questions in the UI.
- **Multilingual? Everything per language** — questions, answers and feedback texts.

---

## ✅ Checklist

- [ ] General module settings filled in (see TK-09)
- [ ] Threshold, time per question and number of questions to show all set
- [ ] Every question has feedback for correct **and** incorrect
- [ ] Correct answers ticked properly (double-check with multiple choice!)
- [ ] All texts in every language
- [ ] For an Excel import: template used and import checked
- [ ] Skills linked (on the module and/or per question)

---

## 🔍 Done? How to check

Play the quiz yourself in the player environment (menu → **View app**). Answer some questions correctly and some deliberately wrong: is the feedback right, does the clock count down properly, and does the pass/fail outcome match your threshold? With random selection, play twice: do you get different questions?

---

*Basis: LearnStrike platform, as of April 2026 · time options and default value verified by 4Growth on 30-08-2026 in the live environment. Related cards: TK-09 (general module settings), TK-07 (challenge), TK-12 (questionnaire).*
