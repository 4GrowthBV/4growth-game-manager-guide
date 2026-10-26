---
type: Runbook
title: "TK-13 Generate a QR code for a challenge"
description: "How to use the QR code that lets players start a challenge straight away — ideal for posters and workplace cards."
tags: [task-card, game-modes, en]
timestamp: 2026-08-30
lifecycle: active
---

# 📱 Task card TK-13 — Generate a QR code for a challenge

> **For game managers.** How to use the QR code that lets players start a challenge straight away — ideal for posters and workplace cards.
> **Status:** v1.0 · 30-08-2026 · part of the LearnStrike Knowledge Base · language: EN.

---

**Every challenge automatically gets its own QR code.** There is nothing to create: open the challenge and the code is already there. Players scan it with their phone and land directly on that challenge. On mobile the link opens the app (through what is called a deeplink); otherwise the browser opens.

---

## 📌 Highlights

| | |
|---|---|
| **Where** | Control Panel → **Campaigns** → open the campaign → open the challenge (edit) → the QR code is **at the top of the screen** |
| **Creating one** | Not needed — every challenge gets a unique QR code by default |
| **When to use** | Posters, workplace cards, presentations, flyers — anywhere players need to get started quickly |
| **What you need** | An existing challenge (TK-07); nothing else |
| **Format** | Download as **SVG** (the default) or **PNG**; default size 2048 px |
| **Link** | Runs through your organisation's preferred domain, or through a Branch.io deeplink that opens the app on mobile |
| **Permissions** | Manager role (or higher), 2FA enabled |

---

## 🚀 Step by step

1. Log in and open the **Control Panel** (menu, top right).
2. Go to **Campaigns** and open the campaign the challenge sits in.
3. Open the **challenge** you want the QR code for (edit).
4. **At the top of the screen** you will find the QR code, with the text: *"Use this QR code to let players play straight away."*
5. Download the code:
   - **Download SVG** — the default and the one to go for: infinitely scalable, so always sharp on posters and in presentations.
   - **Download PNG** — for tools that don't accept SVG (some chat or office programs, for instance). The PNG download works in production, on both macOS and Windows.
6. Place the QR code in your material. The default size is 2048 px — more than enough for A3 posters.
7. Test the code: scan it yourself with your phone. On mobile the app opens (through the Branch.io deeplink); on desktop the browser opens through your organisation's preferred domain.

---

## ⭐ Golden rules & common mistakes

- **A QR code points to a challenge, not a campaign.** Want to send players into a whole learning journey? Pick the first challenge, or use a normal link to the campaign.
- **Check who can access the campaign.** Is the campaign set to "Registered users" with tags? Then whoever scans it has to be able to log in and have the right tag (TK-06, TK-05).
- **Publish first.** A QR code pointing to a challenge in a draft campaign won't work for players.
- **Print it big enough.** Rule of thumb: at least 2×2 cm when read from 20 cm away; on posters go for 5×5 cm or larger.
- **Play in order switched on?** Then a player can only start a later challenge once the earlier ones are finished. What a player sees when they scan a challenge that is still locked is **[still to verify]**.

---

## ✅ Checklist before you distribute

- [ ] Campaign is published and accessible to the target group
- [ ] QR code downloaded (SVG for print, PNG for office/chat)
- [ ] Scanned it yourself with a phone: opens the app and the right challenge
- [ ] Also tested on desktop (browser)
- [ ] Printed large enough and with enough white space around it

---

## 🔍 Done? How to check

Scan the printed version (not the digital one) with at least two different phones. Check: does the app or browser open, do you land on the right challenge, and can you start playing straight away? Test with an account from the target group too, not just with your manager account.

---

## 🔎 Still to verify

| # | What | How to check | Who |
|---|---|---|---|
| 1 | What does a player see when they scan the QR code of a challenge that is still locked by "play in order"? | Switch play in order on and scan the QR code of challenge 2 with an account that hasn't finished challenge 1 | 4Growth |

---

*Basis: LearnStrike platform, as of April 2026 · the place in the UI and the way the PNG download works were verified by 4Growth on 30-08-2026 on macOS and Windows. Related cards: TK-05 (tags), TK-06 (campaign), TK-07 (challenge), TK-18 (Direct Play & public micro game).*
