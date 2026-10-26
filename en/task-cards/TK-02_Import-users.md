---
type: Runbook
title: "TK-02 Import users"
description: "How to add a whole group of users to the platform in one go from an Excel or CSV file — no technical knowledge needed."
tags: [task-card, users, en]
timestamp: 2026-08-30
lifecycle: active
---

# 📥 Task card TK-02 — Import users

> **For game managers.** How to add a whole group of users to the platform in one go from an Excel or CSV file — no technical knowledge needed.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**The import runs in 3 steps: upload → map columns → process.** Ideal at the start of a programme or with a new intake of participants. For one or two users, creating them by hand is quicker (TK-01).

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Users** → **three dots** next to **+ Add user** → **Import** |
| **When to use** | Adding groups of users at once (a new class, department or programme) |
| **What you need** | A file in **csv, xls or xlsx**, up to **8 MB** |
| **Columns** | Name, e-mail, password, language, tags — you decide which column is what |
| **Result** | A processing report listing any errors per row |
| **Permissions** | Manager role (or higher), 2FA enabled |

⚠️ **Watch out with Excel on US regional settings.** The template assumes separate columns, but with a US language or separator setting those columns don't always come through properly and the upload fails. See the tip below on opening a CSV in Excel.

---

## 🚀 Step by step

**First: prepare your file in Excel**

1. Build a sheet with one row per user and clear column headers, for example: `Name | E-mail | Password | Language | Tags`.
2. Tips:
   - **E-mail is the key**: every address has to be valid and unique. Remove duplicate rows (Excel: Data → Remove Duplicates).
   - **Language** as a language code: `nl` or `en`.
   - **Tags**: use exactly the same tag names as in the Control Panel (TK-05). Which separator to use for several tags in one cell is **[still to verify]**.
   - The **password** column is optional. What happens if you leave it out is **[still to verify]**.
   - No blank rows in between; no merged cells; save as .xlsx or .csv.

**Working with a CSV? This keeps your columns intact**

3. Don't open the CSV by double-clicking it — go through **Excel → Data tab → From Text/CSV**. Choose **semicolon (;)** as the delimiter and **UTF-8** as the file origin. Save it as **CSV UTF-8 (\*.csv)**. That keeps the columns separated, even on a machine with US settings.

**Step 1 — Upload**

4. Open the Control Panel → **Users** → **three dots** → **Import**.
5. Pick your file (csv/xls/xlsx, max 8 MB) and upload it.

**Step 2 — Map the columns**

6. You'll see a preview of your file. For each column, say what it contains:
   - **None** — skip the column
   - **Name** · **Email** · **Password** · **Language** · **Tags**
7. Tick **Skip header** if your first row contains column headers (nearly always the case).

**Step 3 — Process**

8. Start the processing. You'll then see the result, with **an error message per row** if something went wrong (an invalid e-mail address, for instance).
9. Fix the errors in your Excel file and re-import only the corrected rows. Whether rows with an existing e-mail address are skipped or updated is **[still to verify]**.

---

## ⭐ Golden rules & common mistakes

- **Test with 2-3 rows first.** Is the column mapping right, and do the tags come through? Only then do the whole list. As long as the points below are open, this matters even more.
- **Seeing one long line instead of separate columns in step 2?** Excel read the delimiter wrong. Go back to step 3 above and reopen the CSV via Data → From Text/CSV.
- **Forgetting to skip the header** turns your column headers into a "user". Always check this in step 2.
- **Create the tags first** in the Control Panel (TK-05), so the spelling matches exactly.
- **Mind the Excel formatting**: e-mail addresses may not contain spaces; check for invisible spaces when copying from other systems.
- **Privacy**: the import file contains personal data (and possibly passwords). Store it securely and delete it once the import is done.

---

## ✅ Checklist before importing

- [ ] File is csv/xls/xlsx and smaller than 8 MB
- [ ] CSV opened and saved via Data → From Text/CSV, semicolon, UTF-8
- [ ] One row per user, no duplicates or blank rows
- [ ] E-mail addresses checked (valid, unique, no spaces)
- [ ] Language codes correct (nl/en)
- [ ] Tag names exactly the same as the tags in the Control Panel
- [ ] Test import with a few rows done

---

## 🔍 Done? How to check

Look at the processing report: zero errors? Then open the Control Panel → **Users** and spot-check a few users: are the name, language and tags right? Have one imported user log in as a final check.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | Which separator do you use for several tags in one cell — a comma or a semicolon? | Import a test row with two tags in one cell, first with a comma, then with a semicolon | 4Growth |
| 2 | What happens if the password column is missing? Does the user get an e-mail to choose a password themselves, or can they not log in at all? | Import one test user without a password column and try to log in | 4Growth |
| 3 | Is a row with an existing e-mail address skipped or updated? | Import three rows, one of them an existing address with a changed name, and see what happens to that user | 4Growth |
| 4 | Exactly which Excel settings break the import, and does the Data → From Text/CSV route always fix it? | Try an import on a machine with US regional settings, with and without the import route from step 3 | 4Growth |

*This card will be updated as soon as the tests are done.*

---

*Basis: LearnStrike platform, as of April 2026 · button location verified by 4Growth on 30-08-2026; the Excel issue is known from practice but has not been tested systematically. Related cards: TK-01 (create by hand), TK-03 (invite), TK-05 (tags).*
