---
type: Runbook
title: "TK-03 Invite users"
description: "How to invite someone to the platform by e-mail — the invitee finishes setting up the account themselves."
tags: [task-card, users, en]
timestamp: 2026-08-30
lifecycle: active
---

# ✉️ Task card TK-03 — Invite users

> **For game managers.** How to invite someone to the platform by e-mail — the invitee finishes setting up the account themselves.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**Inviting is the clean route for new colleagues and administrators.** You only set the e-mail address and the role; the invitee picks their own name and password. For large groups without an e-mail flow: import (TK-02).

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Users** → **three dots** next to the **+ Add user** button → **Invite** |
| **When to use** | New users who should finish their own account; new managers/administrators |
| **What you need** | An e-mail address + a role per invitee |
| **Roles** | **User** · **Manager**. You'll only see the **Administrator** option if your own role allows it |
| **Management** | Resend or withdraw an invite as long as it hasn't been accepted |
| **Permissions** | Manager role (or higher), 2FA enabled |

💡 **Looking for the Invite button and can't see it?** It isn't on the page itself, but behind the **three dots** to the right of **+ Add user**. The same three dots also hold exporting and bulk-assigning tags.

---

## 🚀 Step by step

**Inviting:**

1. Open the Control Panel → **Users**.
2. Click the **three dots** next to **+ Add user** and choose **Invite**.
3. Fill in:
   - The **e-mail address** of the invitee.
   - The **role**: **User** (player), **Manager** (manages the organisation's users and campaigns) or **Administrator** (platform administration by 4Growth; you'll only see that option if your own role allows it).
4. Send it. The invitee receives an e-mail with a personal acceptance link.

**What the invitee sees and does (acceptance flow):**

5. The invitee clicks the link in the e-mail and lands on an acceptance page in your organisation's environment.
6. There they finish the account: setting a name and a password. Which other fields that page holds (language or nickname, for instance) is **[still to verify]**.
7. Once accepted, the account is active with the role you chose, and the invite disappears from the open list.

**Managing open invites:**

8. **Resend** — e-mail not delivered or lost? Send the same invite again.
9. **Withdraw** — delete the invite; the link stops working. Use this after a typo in the e-mail address, or when someone shouldn't get access after all.

---

## ⭐ Golden rules & common mistakes

- **Pick the lowest role that does the job.** Torn between User and Manager? Choose User — you can always raise it later (TK-01).
- **Administrator almost never.** That role is for platform administration by 4Growth. You'll only see the option if your own role allows it.
- **Typo in the e-mail address?** Withdraw and invite again — don't just carry on editing.
- **Tags are a separate job.** An invite doesn't include tags; assign them after acceptance (TK-01/TK-05), otherwise the new user may not see tag-restricted campaigns.
- **Send a reminder after a few days.** Not accepted? Resend it rather than creating a second invite. Whether an invite expires after a while is **[still to verify]** — for now, don't assume an old link still works.

---

## ✅ Checklist

- [ ] E-mail address checked (right person, no typo)
- [ ] Role chosen deliberately (default: User)
- [ ] Invitee told that an e-mail is coming (check spam too)
- [ ] After acceptance: tags assigned (TK-05)
- [ ] Open invites cleaned up regularly (withdraw whatever is no longer needed)

---

## 🔍 Done? How to check

Check in the invite list whether the status updated after acceptance, and whether the new user appears in the Control Panel → **Users** with the right role. For a Manager: have them log in to the Control Panel and set up 2FA.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | Does an invite have an expiry date, and if so, how long is it valid? | Ask the development partner — hard to test without a long wait | Product Owner |
| 2 | Which fields exactly are on the acceptance page the invitee gets to see? | Invite a test address and walk through the acceptance yourself | 4Growth |

*This card will be updated as soon as the answers come in.*

---

*Basis: LearnStrike platform, as of April 2026 · button location verified by 4Growth on 30-08-2026 in the live environment. Related cards: TK-01 (create by hand), TK-02 (import), TK-05 (tags).*
