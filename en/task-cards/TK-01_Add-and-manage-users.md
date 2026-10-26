---
type: Runbook
title: "TK-01 Add & manage users"
description: "How to create a user by hand, edit their details and manage 2FA — no technical knowledge needed."
tags: [task-card, users, en]
timestamp: 2026-08-30
lifecycle: active
---

# 👤 Task card TK-01 — Add & manage users

> **For game managers.** How to create a user by hand, edit their details and manage 2FA — no technical knowledge needed.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

> ⚠️ **Heads-up:** this part of LearnStrike has changed since April 2026. This card is being updated. In doubt? Email support@4growth.com.

---

**Every player is a user in your organisation.** Creating one by hand is handy for a single user or a test account. For larger groups: import them (TK-02) or invite them by e-mail (TK-03).

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Users** → button **+ Add user** |
| **When to use** | Creating one or a few users straight away; test accounts; quick corrections |
| **What you need** | Name + e-mail address (required); optionally password, language, tags |
| **Alternatives** | Many users at once? → Import (TK-02). Want users to register themselves? → Invite (TK-03) |
| **Watch out** | The e-mail address has to be unique within the platform |
| **Permissions** | Manager role (or higher), 2FA enabled |

💡 **Looking for a button you can't find?** A lot of Control Panel actions sit behind the **three dots** — on the users page you'll find them next to the **+ Add user** button. That's where inviting, exporting and bulk-assigning tags live.

---

## 🚀 Step by step

**Creating:**

1. Open the Control Panel → **Users**.
2. Click **+ Add user** and fill in:
   - **Name** (required) and **E-mail address** (required, unique).
   - **Language** — sets the language of the player app for this user.
   - **Tags** — attach the right audience tags straight away (see TK-05).
   - **Password** + confirmation.
   - **Nickname** (2–25 characters) — only shown, and only required, if your organisation uses nicknames.
   - **Avatar** — upload a profile picture (image, max 4 MB), optional.
   - **Roles** — tick **Manager** for a fellow administrator. You'll only see the **Administrator** option if your own role allows it.
3. Click **Save**. The user now appears in the list.

**Editing (in separate sections):**

4. Find the user in the list using the **Search...** field or the **User roles**, **Tags** and **User status** filters, and open them. You edit details in separate sections, each with its own save button:
   - **Profile** — name, e-mail, nickname, avatar.
   - **Password** — set a new password.
   - **Language** — change the language preference.
   - **Roles** — switch Manager/Administrator on or off.
   - **Tags** — add or remove tags.

**Managing 2FA:**

5. The user page shows the status of **two-factor authentication**. You can enable, confirm, disable or **reset** it. Reset it when someone reports they can't get in; exactly what the user sees afterwards is **[still to verify]**. Before resetting, check through another channel, by phone for example, that the person asking really is the user.

**Viewing data:**

6. From the user page you can view the **user data** and the **onboarding answers** (what the user filled in on the opening questions). Progress per campaign lives under **Insights** per user.

**Deleting:**

7. Delete a user with the delete button on that user. **Deleting is permanent** — there is no restore function for users.

---

## ⭐ Golden rules & common mistakes

- **Assign tags right away.** Without tags a user may not see campaigns that are filtered on tags (TK-05).
- **Pick the language deliberately.** The wrong language means a player app in the wrong language.
- **Manager role = admin access.** Only give it to colleagues who genuinely need to work in the Control Panel; they'll have to set up 2FA as well.
- **Forgot the nickname?** If your organisation requires nicknames and the field is empty, the user can't play properly — fill it in straight away.
- **Deleting can't be undone.** Not sure? Remove the tags first so the user no longer sees any content.

---

## ✅ Checklist

- [ ] Name + unique e-mail address filled in
- [ ] Language chosen
- [ ] Right tags attached
- [ ] Password shared through a secure channel (not in the same e-mail as the login name)
- [ ] Role only raised where it's genuinely needed
- [ ] Nickname filled in (if required)

---

## 🔍 Done? How to check

Open the user in the list: are the name, e-mail, language and tags right? Have the user log in and check that the right campaigns show up. For an administrator: check that the Control Panel opens and that 2FA is requested.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | What does a user see after a 2FA reset — do they have to link an authenticator again at their next login? | Reset 2FA on a test account and log in with it | 4Growth |

---

*Basis: LearnStrike platform, as of April 2026 · UI verified by 4Growth on 30-08-2026 in the live environment. Related cards: TK-02 (import), TK-03 (invite), TK-04 (export), TK-05 (tags).*
