---
type: Runbook
title: "TK-05 Manage tags & bulk assign"
description: "How to create and manage tags and assign them to a whole group of users in one go — no technical knowledge needed."
tags: [task-card, users, en]
timestamp: 2026-08-30
lifecycle: active
---

# 🏷️ Task card TK-05 — Manage tags & bulk assign

> **For game managers.** How to create and manage tags and assign them to a whole group of users in one go — no technical knowledge needed.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

> ⚠️ **Heads-up:** this part of LearnStrike has changed since April 2026. This card is being updated. In doubt? Email support@4growth.com.

---

Tags are *the* way to group users. They decide who sees which campaign (access), who counts towards which leaderboard, and which tags the onboarding hands out automatically. Good tag management is the foundation of every targeted learning programme.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Tags** (managing) · bulk assigning via **Users** → **three dots** next to **+ Add user** |
| **When to use** | Before every campaign with restricted access; with new audiences, departments or intakes |
| **What for** | Campaign access (TK-06), leaderboard filters (TK-20), onboarding assignment (TK-24) |
| **Fields** | Name (per language, unique within the organisation) + description |
| **Bulk add** | Assign tags to several users at once |
| **Bulk remove** | Via export → edit the tag column → import (TK-04, TK-02) |
| **Permissions** | Manager role (or higher), 2FA enabled |

💡 **Looking for the bulk function and can't see it?** It isn't under Tags but on the users page, behind the **three dots** to the right of **+ Add user**.

---

## 🚀 Step by step

**Creating, editing and deleting a tag:**

1. Open the Control Panel → **Tags**.
2. Click add tag and fill in:
   - **Name** — for every available language; it has to be unique within your organisation.
   - **Description** — record what the tag is for (e.g. "All staff at the Utrecht site — access to the Hygiene campaign").
3. You edit and delete from the tag list. Deleted a tag by mistake? Use **Restore**.
4. Each tag shows the **users assigned** to it — handy for checking who has it.

**Bulk-assigning tags to users:**

5. Open the Control Panel → **Users** → **three dots** next to **+ Add user** and choose the bulk option for tags.
6. Pick the users and the tags you want to assign, and confirm. All the selected users get the tags in one go.

**Removing tags from a group:**

7. To remove tags from several users, use the **export → edit → import** route: export the user list (TK-04), strip the tags you want gone from the **Tags** column, and import the file back (TK-02).
8. Other ways to assign tags: per user (TK-01), through the "tags" import column (TK-02), or automatically from onboarding answers (TK-24).

**Why tags matter so much:**

- **Campaign access** — with access set to "Registered users" you can limit a campaign to users with particular tags (TK-06). No tag means the campaign is invisible.
- **Leaderboard filters** — a leaderboard shows only players with particular tags, and is only visible to users with that tag (TK-20).
- **Onboarding** — answers to onboarding questions assign tags automatically, so new users segment themselves (TK-24).

---

## ⭐ Golden rules & naming advice

- **Tags first, campaigns second.** Create your tags before you publish a campaign with tag-based access — otherwise nobody sees it.
- **Settle on a fixed naming convention**, for example with a prefix per purpose:
- `dept-utrecht`, `dept-south` — organisational units
- `group-2026a` — intakes/classes
- `programme-hygiene` — campaign-specific access
- **Short and recognisable.** No long sentences; be consistent (always lower case, always the same hyphen).
- **No near-duplicates.** Check the list before you create a new tag — "Utrecht" sitting next to "dept-utrecht" means users get missed.
- **Always fill in the description.** Six months from now nobody remembers what "group-x" was for.
- **Don't just delete.** A tag may be in use for campaign access, leaderboards or onboarding — check that first.

---

## ✅ Checklist

- [ ] Tag name follows the naming convention and is unique
- [ ] Description filled in (purpose + audience)
- [ ] Name filled in for every language the organisation uses
- [ ] Right users assigned (bulk or via import)
- [ ] Checked where the tag is used before changing or deleting it

---

## 🔍 Done? How to check

Open the tag and look at the users assigned: is that the right group? Then test how it works: log in (or look along) with a user *with* the tag and one *without* — does only the first see the tag-restricted campaign or the filtered leaderboard?

---

*Basis: LearnStrike platform, as of April 2026 · button location and the export/import route for removing tags verified by 4Growth on 30-08-2026 in the live environment. Related cards: TK-01 (manage a user), TK-02 (import), TK-04 (export), TK-06 (campaign access), TK-20 (leaderboard), TK-24 (onboarding).*
