---
type: Runbook
title: "TK-11 Add a Survey module"
description: "How to build a survey module for reflection, evaluation or measurement — no technical knowledge required."
tags: [task-card, content, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-11 — Add a Survey module

> **For game managers.** How to build a survey module for reflection, evaluation or measurement — no technical knowledge required.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

> ⚠️ **Heads-up:** this part of LearnStrike has changed since April 2026. This card is being updated. In doubt? Email support@4growth.com.

---

**A survey has no right or wrong answers** — it is the reflection and measurement module (Kolb step 4: transfer to practice). You build it in two layers: first the module itself, then the individual questions (survey entries). Answers can be exported afterwards and can be sent to the player as a PDF.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → [campaign] → [challenge] → **Add module** → type **Survey** |
| **When to use** | Reflection questions, evaluations, baseline and follow-up measurements, intentions for the workplace |
| **Question types** | Open, single choice, multiple choice, slider, statement (a statement with a scale) |
| **PDF** | Your own PDF text + the option **show all answers in the PDF** (the player takes their answers with them) |
| **Results** | Exportable via Insights (see TK-23) |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Open the **Control Panel** → **Campaigns** → [campaign] → [challenge] → **Add module** → **Survey**.
2. Fill in the general module settings — name, description, factor, skills, start and end screen — see TK-09, steps 4–7.
3. Configure the survey settings:
   - **PDF text** (per language, max 10,000 characters): the supporting text in the PDF the player receives.
   - **Show all answers in the PDF**: on = the player gets their own answers in the PDF — powerful for reflection and for conversations with their manager.
4. Save, then add **questions** (survey entries). Pick a type for each question:
   - **Open**: a free text answer.
   - **Single choice**: pick one option; per option a text (per language) and optionally an image.
   - **Multiple choice**: several options can be picked; otherwise the same as single choice.
   - **Slider**: slide along a scale (minimum ≥ 1, maximum up to 10).
   - **Statement**: a statement with a scale, plus a **minimum text** and a **maximum text** for the two ends (for example "Strongly disagree" ↔ "Strongly agree", max 255 characters).
5. Per question you can also set:
   - **Question text** (per language, required), **image**, **skills**.
   - **Optional**: the player may skip the question.
   - For choice questions: the **"other"** option — the player can fill in an answer of their own.
6. Put the questions in the right **order** (drag & drop).
7. Done? Check the module and drag it to the right position in the challenge.

---

## ⭐ Golden rules & common mistakes

- **Keep it short.** 5–8 questions is plenty for reflection; long surveys make people drop out.
- **Use open questions sparingly.** One good open question ("What will you do differently tomorrow?") works better than five.
- **Don't forget the statement texts.** Without a minimum and maximum text the player has no idea what the ends of the scale mean.
- **Use the "other" option deliberately** — only if you are genuinely going to read those free answers (via the export).
- **Match the PDF settings to your privacy rules.** Answers in the PDF are visible to everyone the player forwards it to.
- **Measuring before and after?** Duplicate the survey questions exactly for the baseline and follow-up measurement; only then are the results comparable.
- **Deleted questions** can be brought back with **Restore**.

---

## ✅ Checklist

- [ ] General module settings filled in (see TK-09)
- [ ] PDF text written and a choice made: answers in the PDF yes/no
- [ ] Per question: the right type, text in every language
- [ ] Statements: minimum and maximum text filled in
- [ ] Optional or required chosen deliberately per question
- [ ] "Other" option wherever it adds value
- [ ] Questions in a logical order
- [ ] Agreed who reads the results (TK-23)

---

## 🔍 Done? How to check

Fill in the survey yourself in the player environment (menu → **View app**). Check: do all question types work, are the scales and texts right, and does the PDF look good? Then check in **Insights** whether your test answers show up in the export (TK-23).

---

*Basis: LearnStrike platform, as of April 2026. Related cards: TK-09 (general module settings), TK-12 (questionnaire), TK-23 (exporting results).*
