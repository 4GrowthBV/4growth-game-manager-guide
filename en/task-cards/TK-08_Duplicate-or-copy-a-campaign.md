---
type: Runbook
title: "TK-08 Duplicate or copy a campaign"
description: "How to reuse an existing campaign: as a copy inside your own organisation, or as a transfer request to another organisation."
tags: [task-card, content, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🎯 Task card TK-08 — Duplicate or copy a campaign

> **For game managers.** How to reuse an existing campaign: as a copy inside your own organisation, or as a transfer request to another organisation.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**Two routes, two purposes.** **Duplicate campaign** makes a copy inside your own organisation — a handy starting point for a new group or a variant. **Copy campaign** sends a transfer request to another organisation, which has to accept it first.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → open the campaign → **three dots** to the right of the title → **Duplicate campaign** or **Copy campaign** |
| **When to use** | A new edition of an existing journey; the same content for another organisation or subdomain |
| **What you need** | For copying: the subdomain of the receiving organisation (e.g. yourcompany) |
| **What comes along** | All settings of the campaign, including linked skills |
| **Acceptance** | Copying runs through a request: the receiving organisation **accepts or declines** (in bulk too) |
| **Micro games** | Option: **skip** micro games the receiver has no access to |
| **Permissions** | Manager role (or higher), 2FA active |

💡 **Looking for a button and can't find it?** Many actions in the Control Panel sit under the **three dots** to the right of the title. That goes for these two as well.

---

## 🚀 Step by step

**Route A — Duplicating (within your own organisation)**

1. Open the **Control Panel** → **Campaigns** and click the campaign open.
2. Click the **three dots** to the right of the campaign title and choose **Duplicate campaign**.
3. A copy appears in your campaign list as a **Draft** (not published). All settings from the original come along, including the linked skills. Whether the **achievement settings** come along too is **[still to verify]**.
4. Adjust the name, texts and settings, and publish when you are ready (TK-06, step 10).

**Route B — Copying to another organisation (transfer request)**

1. Open the campaign → **three dots** → **Copy campaign**.
2. Enter the **subdomain** of the receiving organisation (required) — the part before `.learnstrike.app`.
3. Decide whether you want to **skip missing micro games** (checkbox). On = the copy goes ahead, but micro game modules the receiver has no access to are left out. Off = the request may fail on this; exactly what happens then is **[still to verify]**.
4. Click **Send copy request**.
5. **The receiver** sees the request in the Control Panel under **Transfer requests** and chooses **accept** or **decline** — per request or in bulk.
6. Once accepted, the campaign sits in the receiving organisation as a copy; the manager there adjusts and publishes it themselves.

---

## ⭐ Golden rules & common mistakes

- **A copy is a snapshot.** If you change the original later, the copy does **not** change with it (and vice versa).
- **Double-check the subdomain.** A typo means the request lands at the wrong organisation, or at none at all.
- **Go through the achievements in the copy.** As long as point 1 below is open: after duplicating, check the achievement settings yourself.
- **Think about micro game access up front.** If the receiving organisation does not have the same micro games, use the skip missing micro games option — and fill the gaps manually afterwards.
- **Copying publishes nothing.** The receiver has to check, adjust and publish the campaign themselves.
- **Agree on it first.** Warn your contact at the receiving organisation that a request is coming — otherwise it just sits there unnoticed.
- **Progress never comes along.** Player scores and progress stay with the original; a copy always starts empty.

---

## ✅ Checklist

- [ ] Right route chosen: duplicate (own organisation) or copy (another organisation)
- [ ] For copying: subdomain checked (spelling!)
- [ ] Decision made: skip missing micro games yes/no
- [ ] Receiver informed about the request
- [ ] After duplicating: achievements and skills checked in the copy
- [ ] Name and texts adjusted (no leftover references to the old version)
- [ ] Copy played through yourself before publishing

---

## 🔍 Done? How to check

For duplicating: is the copy in your campaign list as a Draft, and is the content right? Put the two campaigns side by side and walk through challenges, modules, skills and achievements. For copying: ask the receiver to confirm that the request arrived under **Transfer requests** and, after accepting, to check that all challenges and modules are complete — paying extra attention to any skipped micro game modules.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | Do the achievement settings come along when duplicating? | Duplicate a campaign that has achievements set up and compare both campaigns at achievement level | 4Growth |
| 2 | What happens to a transfer request when "skip missing micro games" is **off** and the receiver is missing a micro game? | Send a request to an organisation without that micro game and record the error message | 4Growth |

*This card will be updated as soon as the tests are finished.*

---

*Basis: LearnStrike platform, as of April 2026 · UI and behaviour verified by 4Growth on 30-08-2026 in the live environment. Related cards: TK-06 (create/publish a campaign), TK-07 (challenges), TK-09 (micro game module), TK-22 (achievements).*
