---
type: Runbook
title: "TK-04 Export users"
description: "How to download an overview of all your users as an Excel file — and handle it with care."
tags: [task-card, users, en]
timestamp: 2026-08-30
lifecycle: active
---

# 📤 Task card TK-04 — Export users

> **For game managers.** How to download an overview of all your users as an Excel file — and handle it with care.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**The export gives you an Excel file (XLSX) with every user in your organisation in one click.** Handy for checks, reporting, or as the basis for a tag clean-up. Do note: the file contains personal data.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Users** → **three dots** next to **+ Add user** → **Export** |
| **When to use** | An overview or check of users, tags and roles; input for reporting or a clean-up |
| **Format** | XLSX (Excel) |
| **Columns** | Name, Nickname, Email, Language, Tags, IsDemo, IsManager, IsAdministrator |
| **Watch out** | Personal data — handle the file in line with the GDPR |
| **Permissions** | Manager role (or higher), 2FA enabled |

💡 **Looking for the export button and can't see it?** It sits behind the **three dots** to the right of **+ Add user**, together with inviting, importing and bulk-assigning tags.

---

## 🚀 Step by step

1. Open the Control Panel → **Users**.
2. Click the **three dots** next to **+ Add user** and choose **Export**. The XLSX file downloads.
3. Open the file in Excel. Per user you'll see:
   - **Name** — name
   - **Nickname** — screen name (if used)
   - **Email** — e-mail address
   - **Language** — language preference (nl/en)
   - **Tags** — the tags assigned
   - **IsDemo** — guest user yes/no
   - **IsManager** — manager role yes/no
   - **IsAdministrator** — administrator role yes/no
4. Use Excel filters for your analysis — for example: every user without tags, or every account with a manager role.

Progress and scores are *not* in here. For those you use the exports under Insights (TK-23): progress per campaign, survey answers and the full combined export.

**The export is also your route for removing tags.** To strip tags from a group of users, export the list, edit the tag column and import it back (TK-02, TK-05).

---

## ⭐ Golden rules & GDPR care

- **Only export with a purpose.** Don't make a "just in case" export — every copy of personal data is a risk.
- **Store it securely.** Keep the file in the secure organisation environment only (your business OneDrive, for instance), never on a private device or a USB stick.
- **Don't share it casually.** Don't forward it to people outside the organisation; within the team, share it only with those who really need it.
- **Delete it when you're done.** Analysis finished? Delete the export (including from your recycle bin and downloads folder).
- **A role check comes free.** Do the IsManager/IsAdministrator columns show accounts that no longer need that role? Adjust it (TK-01).

---

## ✅ Checklist

- [ ] A clear purpose for the export
- [ ] File saved in a secure location
- [ ] Only shared with those who need it
- [ ] Deleted after use (including the downloads folder and recycle bin)

---

## 🔍 Done? How to check

Open the file and compare the number of rows with the number of users in the Control Panel — do they match? Spot-check: are the tags and roles of a few users you know correct?

---

*Basis: LearnStrike platform, as of April 2026 · button location verified by 4Growth on 30-08-2026 in the live environment. Related cards: TK-01 (manage a user), TK-02 (import), TK-05 (tags), TK-23 (insights and exports).*
