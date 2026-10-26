---
type: Runbook
title: "TK-22 Set up achievements & certificates"
description: "How to decide which achievements players can earn (and what they are worth), and how certificates are awarded."
tags: [task-card, insights, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-22 — Set up achievements & certificates

> **For game managers.** How to decide which achievements players can earn (and what they are worth), and how certificates are awarded.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**Achievements and certificates are your reward buttons.** Achievements are badges with bonus points for behaviour you want to encourage (playing early, keeping it up, winning battles). Certificates are the formal proof of completing a campaign. You set both up at two levels: organisation-wide and per campaign.

---

## 📌 Highlights

| | |
|---|---|
| **Where (achievements per campaign)** | Control Panel → **Campaigns** → open the campaign → **three dots** to the right of the title → **Achievements** |
| **Where (achievements organisation-wide)** | **Admin → Organisations → [your organisation] → Gameplay → Achievements** |
| **Where (certificate on/off)** | Per campaign: the **Awards certificate** checkbox (TK-06) |
| **Where (certificate design)** | **Admin → Organisations** → click the organisation name → **Organisation settings** → **PDF templates** |
| **Adjustable per achievement** | **Once** · **Points** (score award) · **Configuration** (number of streak days, threshold in minutes, and so on) · switch off |
| **Worth knowing** | Some achievements are **secret** — players only see them once they earn them |
| **Player** | Can download the certificate and receive it by email |
| **Permissions** | Manager role (or higher), 2FA enabled |

💡 **The Achievements button is a bit hidden.** Open a campaign in the Control Panel and you'll see **three dots** to the right of the title — that's where Achievements sits, alongside duplicate and copy.

---

## 🚀 Step by step

**A. Set up achievements organisation-wide**

1. Go to **Admin → Organisations → [your organisation] → Gameplay → Achievements**.
2. You'll see the list of available achievements. Standard examples (from the system settings):
   - **Early Bird** — playing between 04:00 and 08:30 (500 points)
   - **Streaks** — playing daily: runs of 3, 10, 20, 30, 60 and 90 days
   - **Battle runs** — winning battles in a row (3 or 7 wins, for instance)
   - Plus campaign completed (2,500 pts), challenge completed (1,500 pts), and secret achievements (we're not giving those away here)
3. For each achievement you can adjust:
   - **Once** — can a player earn it a single time or more often?
   - **Points** (score award) — how many bonus points does it give?
   - **Configuration** — the threshold, for example the number of streak days or a minimum play time in minutes (only for achievements that have such a setting).
   - **Switch off** — take it out of the list for your organisation.
4. **Save.**

**B. Fine-tune achievements per campaign**

5. Open **Campaigns** → the campaign → click the **three dots** to the right of the title → **Achievements**.
6. Adjust the same settings (once, points, configuration, switch off) — for this campaign only. Handy when a short campaign doesn't need a 90-day streak, for example.

**C. Switch certificates on**

7. Per campaign: tick **Awards certificate** in the campaign settings (TK-06).
8. Want this as the default for all new campaigns? That's an organisation setting; exactly which tab holds that checkbox is **[still to verify]**.

**D. Set up the certificate design (PDF templates)**

9. Go to **Admin → Organisations**. In the overview, click the **name of the organisation** (the blue text, to the left of "Current organisation").
10. You land in **Organisation settings**. Choose **PDF templates**.
11. This is where you design every PDF the platform issues — certificates, but also survey and questionnaire reports. Adjust texts and colours.
12. Done: on completion the player gets a PDF certificate and can **download it or email it to themselves**.

ℹ️ **PDF templates is new functionality.** Walk through the design once from start to finish before you use it with a client, and look at the result as a player.

---

## ⭐ Golden rules & common mistakes

- **Award points with care.** Achievement bonus points count towards scores and leaderboards. Set them very high and you distort the competition.
- **Match the configuration to your run time.** Nobody can hit a 60-day streak in a three-week campaign — switch it off or lower the threshold.
- **Don't give away secret achievements** in your communication — the surprise is exactly what makes them work.
- **A certificate is a promise.** Only tick the box if the campaign genuinely assesses a completed learning achievement, and check the PDF design before go-live.
- **Organisation-wide first, then per campaign.** Set your general preferences at organisation level; use campaign level only for exceptions.
- **Duplicating a campaign?** Check afterwards whether the achievement settings came along — that hasn't been established yet (TK-08).

---

## ✅ Checklist

- [ ] Achievements list reviewed: anything that doesn't fit switched off
- [ ] Points per achievement in line with your scoring model (10,000 per module)
- [ ] Configurations (streak days, minutes) achievable within the run time
- [ ] Certificate checkbox deliberately on or off per campaign
- [ ] PDF template for the certificate checked: texts and colours
- [ ] Certificate viewed and emailed as a player

---

## 🔍 Done? How to check

Play with a test account: complete a challenge and check whether the achievement shows up with the right number of points. Complete a campaign with a certificate and look at the PDF — are the name, date, texts and colours correct? Test emailing the certificate too.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | Which tab holds the organisation setting "new campaigns award certificates by default"? | Walk through Organisation settings and record the location | 4Growth |

---

*Basis: LearnStrike platform, as of April 2026 · the location of the achievements button and the route to PDF templates verified by 4Growth on 30-08-2026 in the live environment. Related cards: TK-06 (campaign certificate checkbox), TK-08 (duplicating), TK-16 (battles), TK-23 (Achievements/Certificates export).*
