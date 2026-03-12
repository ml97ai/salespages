# THE PRECISION TRADER SYSTEM — SALES PAGE MASTER DOCUMENT
## The Only Document You Need to Build This Page

---

# TABLE OF CONTENTS

1. [Global Design System](#1-global-design-system)
2. [Page Architecture Overview](#2-page-architecture-overview)
3. [Section-by-Section Build Guide](#3-section-by-section-build-guide)
4. [Sticky/Fixed Elements](#4-stickyfixed-elements)
5. [Mobile Adaptations](#5-mobile-adaptations)
6. [Technical Notes for GHL](#6-technical-notes-for-ghl)

---

# 1. GLOBAL DESIGN SYSTEM

## Color Palette

| Role | Color | Hex | Usage |
|------|-------|-----|-------|
| **Background (primary)** | Deep charcoal/near-black | `#0D0D0D` | Main page background. Dark = premium feel, matches trading terminal aesthetic, reduces eye strain for traders who stare at charts. |
| **Background (sections)** | Slightly lighter charcoal | `#1A1A1A` | Alternating section backgrounds to create visual separation without hard lines. |
| **Background (cards/boxes)** | Dark grey | `#242424` | Testimonial cards, feature boxes, value stack table. Subtle lift from background. |
| **Text (primary)** | Off-white | `#F0F0F0` | All body copy. Pure white (#FFF) is too harsh on dark backgrounds — off-white is easier to read. |
| **Text (secondary)** | Muted grey | `#A0A0A0` | Subtext, captions, fine print, micro-copy. |
| **Text (headings)** | White | `#FFFFFF` | Section headings only. Creates hierarchy contrast against off-white body. |
| **Accent (primary)** | Electric green | `#00D26A` | CTA buttons, price highlights, checkmarks, "included" badges. Green = money, profit, go. |
| **Accent (secondary)** | Gold/amber | `#FFB800` | Stars in testimonials, achievement badges, highlight spans for key phrases in copy. |
| **Accent (danger/urgency)** | Soft red | `#FF4444` | Crossed-out prices, "limited spots" indicators, warning callouts. |
| **Border/divider** | Subtle grey | `#333333` | Card borders, horizontal rules, section dividers. Barely visible — felt more than seen. |

## Typography

| Role | Font | Size (Desktop) | Size (Mobile) | Weight | Line Height |
|------|------|----------------|---------------|--------|-------------|
| **Hero headline** | System sans-serif (Inter, SF Pro, or Helvetica Neue) | 48px | 32px | 800 (Extra Bold) | 1.1 |
| **Section headings (H2)** | Same | 36px | 26px | 700 (Bold) | 1.2 |
| **Sub-headings (H3)** | Same | 24px | 20px | 600 (Semi-bold) | 1.3 |
| **Body copy** | Same | 18px | 16px | 400 (Regular) | 1.7 |
| **Small/micro-copy** | Same | 14px | 13px | 400 | 1.5 |
| **CTA button text** | Same | 20px | 18px | 700 | 1.0 |
| **Testimonial quotes** | Same, italic | 17px | 15px | 400 italic | 1.6 |

**Why system sans-serif:** Loads instantly (no font download), clean, modern, universally readable. Trading audience values speed and clarity over design flair.

## Spacing System

| Element | Desktop | Mobile |
|---------|---------|--------|
| **Section padding (top/bottom)** | 80px | 48px |
| **Between paragraphs** | 24px | 20px |
| **Between sections** | 0px (background color change creates separation) | 0px |
| **Max content width** | 720px (centered) | 100% with 20px side padding |
| **Image/video max width** | 800px | 100% |

**Why 720px max width:** Optimal reading line length (65-75 characters per line). Wider = harder to read. This is a text-heavy page — readability is everything. Alen's 4-line text block rule is easier to achieve at this width.

## Button Style

```
Background: #00D26A (electric green)
Text: #FFFFFF (white)
Font weight: 700
Font size: 20px
Padding: 18px 48px
Border radius: 8px
Box shadow: 0 4px 15px rgba(0, 210, 106, 0.3)
Hover: Background brightens to #00E878, shadow expands
Full width on mobile
```

## Card/Box Style (for testimonials, feature cards, value stack)

```
Background: #242424
Border: 1px solid #333333
Border radius: 12px
Padding: 24px
Box shadow: none (flat design, dark mode)
```

## Iconography

Use simple line icons (Lucide, Phosphor, or Heroicons set). White or green color. 24px size. Used for:
- Checkmarks next to included items (green)
- Feature indicators in product section
- Shield icon for guarantee
- Clock icon for time references
- Chart icon for trading references

---

# 2. PAGE ARCHITECTURE OVERVIEW

The page follows Alen's TSL (Text Sales Letter) 3-Stage Model:

```
STAGE 1: PROBLEM AGREEMENT (20% of page)
├── Section 1: Hero (Above the Fold)
├── Section 2: The Pain (Emotional Gut-Punch)
└── Section 3: The Real Problem (Diagnosis)

STAGE 2: SOLUTION AGREEMENT (40% of page)
├── Section 4: The POV Shift
├── Section 5: The Mechanism (Discovery Story)
├── Section 6: Social Proof Break #1
└── Section 7: The "What If" Bridge

STAGE 3: PRODUCT AGREEMENT (40% of page)
├── Section 8: Product Reveal + Component Breakdown
├── Section 9: Social Proof Break #2
├── Section 10: Who This Is For / Not For
├── Section 11: About Joey (Authority for Cold Traffic)
├── Section 12: Value Stack + Price Reveal
├── Section 13: Guarantee
├── Section 14: Objection Handling
├── Section 15: FAQ
├── Section 16: The Final Close
└── Section 17: Footer / Legal
```

**Emotional oscillation map:**
```
Section 1:  ■■■■□□□□□□  Neutral/Curious (hook)
Section 2:  ■■■■■■■■■□  LOW — deep pain state
Section 3:  ■■■■■■■□□□  LOW — diagnosis (but lighter, intellectual)
Section 4:  □□□■■■■■■■  HIGH — revelation/realization
Section 5:  ■■■■■□□□□□  MID — story, relatable
Section 6:  □□□□■■■■■■  HIGH — proof, validation
Section 7:  □□□□□■■■■■  HIGH — possibility, desire
Section 8:  □□□■■■■■□□  MID-HIGH — excitement
Section 9:  □□□□■■■■■■  HIGH — more proof
Section 10: ■■■■■□□□□□  MID — qualifier (creates identity)
Section 11: □□□■■■■■□□  MID — trust building
Section 12: □□□□□■■■■■  HIGH — value revelation
Section 13: □□□□■■■■■■  HIGH — safety, risk removal
Section 14: ■■■■■■□□□□  MID-LOW — concerns addressed calmly
Section 15: ■■■□□□□□□□  LOW — factual
Section 16: □□□□□■■■■■  PEAK HIGH — future vision + consequence
```

---

# 3. SECTION-BY-SECTION BUILD GUIDE

---

## ═══════════════════════════════════════════
## SECTION 1: HERO (Above the Fold)
## ═══════════════════════════════════════════

**Background:** `#0D0D0D`
**Content width:** 720px centered
**Padding top:** 40px (desktop), 24px (mobile)

### Layout (Desktop):

```
┌─────────────────────────────────────────────┐
│           [LOGO: 90MTRADER - small]         │  ← 32px height, centered, white version
│                                             │
│                                             │  ← 40px gap
│                                             │
│     You Already Know How To Trade.          │  ← H1, white, 48px, centered
│     Here's Why You Still Can't              │
│              Get Paid.                      │
│                                             │
│                                             │  ← 16px gap
│                                             │
│  The system that shows you exactly what     │  ← Subheadline, #A0A0A0, 20px
│  to risk based on YOUR trading data — so    │     centered, max-width 600px
│  you stop guessing and start getting        │
│  payouts month after month.                 │
│                                             │
│                                             │  ← 32px gap
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │                                     │    │  ← VSL embed, 16:9 ratio
│  │          [VIDEO PLAYER]             │    │     max-width 800px
│  │                                     │    │     Thumbnail: Joey at desk with
│  │     Thumbnail: Joey looking at      │    │     charts behind him. Text overlay
│  │     camera, charts behind him.      │    │     on thumbnail: "Watch This Before
│  │     Text overlay on thumbnail:      │    │     Your Next Trade"
│  │     "Watch This Before Your         │    │     Play button centered.
│  │      Next Trade"                    │    │     Border radius: 12px
│  │                                     │    │     Subtle border: 1px solid #333
│  └─────────────────────────────────────┘    │
│                                             │
│                                             │  ← 24px gap
│                                             │
│    [ 🟢 GET THE PRECISION TRADER SYSTEM ]   │  ← CTA button, full green style
│             $697 — Instant Access           │  ← Text ON the button (two lines)
│                                             │
│       Or 3 payments of $249                 │  ← Below button, #A0A0A0, 14px
│                                             │
│  ✓ Instant access  ✓ 30-day guarantee      │  ← Below that, #A0A0A0, 13px
│       ✓ One payment, lifetime access        │     Checkmarks in green (#00D26A)
│                                             │
│                                             │  ← 24px gap
│                                             │
│  "Excellent" rated by 1,275+ traders        │  ← Social proof micro-bar
│  ★★★★★                                     │     Stars in gold (#FFB800)
│                                             │     Text in #A0A0A0, 14px, centered
└─────────────────────────────────────────────┘
```

### Why this headline works (Alen's principles applied):

- **Realization-based hook:** "You already know how to trade" is the realization — it validates them. Then "here's why you still can't get paid" creates the absence of knowledge that Alen says IS attention.
- **Binding statement:** They cannot disagree with the first line. Every person on this page has been trying to trade. Agreeing with line 1 pulls them into line 2.
- **Contrast mechanism:** The contrast between "know how to trade" and "can't get paid" creates cognitive tension. Alen: "contrast is the mechanism of awareness, and awareness is the mechanism of attention."
- **No abstraction:** Every word is concrete. No jargon. No vague promises. Alen: "The #1 thing that kills conversions is abstraction."

### COPY NOTES:
- The headline does NOT mention rPilot, software, course, or any product name. Alen: "The less you talk about the product, the better it sells."
- The subheadline adds specificity ("YOUR trading data") and outcomes ("stop guessing, start getting payouts").
- The CTA appears immediately for high-intent viewers who watched the VSL and are ready to buy. Don't make them scroll.

---

## ═══════════════════════════════════════════
## SECTION 2: THE PAIN (Emotional Gut-Punch)
## ═══════════════════════════════════════════

**Background:** `#1A1A1A` (subtle shift from hero)
**Content width:** 720px centered
**Emotional state:** LOW — this is the deepest pain section. Short choppy cadence.

### Layout:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ── Section divider: thin line, #333 ──     │
│                                             │
│  [Text content below, left-aligned]         │
│                                             │
└─────────────────────────────────────────────┘
```

**No heading for this section.** It flows directly from the hero. Starting with a heading would give people a "copywriting fast pass" (Alen's term) — they'd skip ahead. We want them to READ every word.

### COPY:

---

You've seen the payouts. You've seen the funded accounts. You've seen people making $10K, $15K, $20K a month from trading.

And you know it's real because you've watched them do it.

So you learned a strategy. You studied the setups. You took notes. You practised.

And you had winning days. Days where everything clicked. Days where you thought: *this is it. I've actually got this.*

Then you gave it all back.

Maybe you passed an eval and blew the funded account two weeks later. Maybe you had a great month followed by a month that wiped it all out. Maybe you keep getting close — *so close* — but you can never hold onto it.

And here's the thing that eats at you:

**You know the strategy works.** You've seen it work for other people. You can spot the setups. You can take good trades. Something is still wrong — and you can't figure out what it is.

So you watch more videos. You try a different time frame. You switch strategies. You look for the secret that's going to make it click.

Six months go by. You're in the exact same place.

Still inconsistent. Still frustrated. Still watching other people post payouts while you're stuck passing the same eval for the third time.

That question keeps coming back.

*When is this going to work for me?*

---

### VISUAL ELEMENT — EMOTIONAL BREAK:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Card style: #242424 background
│  │  "I would like to stop learning       │  │     Border-left: 3px solid #FFB800
│  │   another strategy each week and      │  │     Italic text, 17px
│  │   learn to be consistent. I pass      │  │     Padding: 24px
│  │   most prop firms but never get       │  │     No attribution (anonymous =
│  │   to the payout point due to          │  │     more relatable, they see
│  │   blow outs."                         │  │     themselves in it)
│  │                                       │  │
│  │               — 90-Minute Trader      │  │  ← Attribution: just "90-Minute
│  │                  student              │  │     Trader student", #A0A0A0
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

### More copy after the quote:

---

Maybe you relate to that. Maybe you've said something similar yourself.

Here's what nobody's telling you:

**The problem isn't your strategy. The problem isn't your discipline. And the problem isn't you.**

The problem is that you're trading blind.

---

### WHY THIS SECTION WORKS:

- **Alen's "agree to problem" stage:** Every line is something they've experienced. They're nodding along. Each agreement builds momentum toward the diagnosis.
- **Copy cadence:** Short. Punchy. Fragments. This is HIGH EMOTION copy — Alen says short chop cadence = high emotional state.
- **The customer quote** is a binding statement from someone like them. It's not Joey telling them they have a problem — it's a peer. Alen: "When sociology puts them in problem state = more powerful than when you do it."
- **"Trading blind"** is the key phrase. It's the mechanism of the problem, planted here and carried through the entire page. Simple. Concrete. No abstraction.
- **No heading** means they can't skip this section. They have to read through it.

---

## ═══════════════════════════════════════════
## SECTION 3: THE REAL PROBLEM (Diagnosis)
## ═══════════════════════════════════════════

**Background:** `#0D0D0D` (back to primary)
**Emotional state:** Still LOW but shifting toward intellectual — we're diagnosing, not just feeling.

### COPY:

---

### What "Trading Blind" Actually Means

Here's a quick test.

Answer these honestly:

---

### VISUAL ELEMENT — Interactive-feeling checklist:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Card: #1A1A1A background
│  │  □  Do you know your real win rate?   │  │     Each line is a row
│  │     Not what you think it is — your   │  │     □ = empty checkbox icon
│  │     actual tracked win rate from      │  │        (grey, #666)
│  │     your last 30+ trades.            │  │     Body text: #F0F0F0, 17px
│  │                                       │  │     Clarifying text: #A0A0A0, 15px
│  │  □  Do you know exactly how much     │  │     16px gap between each item
│  │     to risk per trade — calculated    │  │
│  │     from YOUR numbers, not someone    │  │
│  │     else's?                          │  │
│  │                                       │  │
│  │  □  Do you know which times of day   │  │
│  │     you actually trade best?         │  │
│  │                                       │  │
│  │  □  Do you know what triggers you    │  │
│  │     to break your rules?             │  │
│  │                                       │  │
│  │  □  Do you know — mathematically —   │  │
│  │     how many days it should take     │  │
│  │     you to pass your next eval?      │  │
│  │                                       │  │
│  │  □  Do you know if you're actually   │  │
│  │     improving... or just getting     │  │
│  │     lucky?                           │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

### Copy continues:

---

If you checked zero... you're not alone. Most traders can't answer a single one of these.

And that's the problem. Not the strategy. Not the psychology. Not the discipline.

**You're making decisions without data.**

Every trade you take without knowing your numbers is a coin flip dressed up as a trade. You might win. You might lose. But you have no way to know *why* — which means you have no way to improve.

This is how traders stay stuck for months. Years. Some forever.

They learn strategy after strategy. They switch from model to model. They think the answer is out there somewhere — a better setup, a different time frame, the right indicator.

But the answer was never out there. It's in here — in their own performance data. Data they've never tracked, never analysed, and never used.

**That's what trading blind means. And that's what keeps you from getting paid.**

---

### VISUAL ELEMENT — The Two Traders comparison:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌──────────────────┐ ┌──────────────────┐  │
│  │   TRADER A       │ │   TRADER B       │  │  ← Two cards side by side
│  │   (Trading Blind)│ │   (Trading w/    │  │     (stack on mobile)
│  │                  │ │    Precision)     │  │
│  │                  │ │                  │  │  Card A: #242424 bg
│  │  ✗ Guesses risk  │ │  ✓ Calculates    │  │  with red-tinted left
│  │    every trade   │ │    risk from     │  │  border (#FF4444)
│  │                  │ │    real data     │  │
│  │  ✗ Doesn't know  │ │                  │  │  Card B: #242424 bg
│  │    win rate      │ │  ✓ Knows exact   │  │  with green-tinted left
│  │                  │ │    win rate      │  │  border (#00D26A)
│  │  ✗ Repeats same  │ │                  │  │
│  │    mistakes      │ │  ✓ Spots         │  │  ✗ = #FF4444
│  │                  │ │    patterns,     │  │  ✓ = #00D26A
│  │  ✗ Passes evals, │ │    fixes them   │  │
│  │    blows funded  │ │                  │  │  Text: 15px
│  │                  │ │  ✓ Passes AND    │  │
│  │  ✗ Hopes it      │ │    gets payouts  │  │
│  │    works out     │ │                  │  │
│  │                  │ │  ✓ Knows exactly │  │
│  │  Result:         │ │    what to do    │  │
│  │  INCONSISTENT    │ │                  │  │  Result text: 14px, bold
│  │                  │ │  Result:         │  │  Card A result: #FF4444
│  │                  │ │  CONSISTENTLY    │  │  Card B result: #00D26A
│  │                  │ │  PROFITABLE      │  │
│  └──────────────────┘ └──────────────────┘  │
│                                             │
│  The difference isn't talent.               │  ← Below cards, centered
│  It's data.                                 │     Bold, white, 20px
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 4: THE POV SHIFT (Revelation)
## ═══════════════════════════════════════════

**Background:** `#1A1A1A`
**Emotional state:** Shifting from LOW to HIGH. This is the turning point. The realization.

**Alen's key principle:** "EVERY single sales letter HAS TO CHANGE THE POINT OF VIEW OR IT WILL NOT CONVERT. The degree it converts = the degree you can change points of view."

**The POV shift we're making:** FROM "I need a better strategy / more knowledge / more discipline" → TO "I need to know MY numbers and trade based on MY data."

### COPY:

---

### Here's What Took Me 8 Years and $30,000 To Figure Out

Every trading course on the planet teaches you **what** to trade.

Setups. Patterns. Entries. Exits. Models.

That's the 20%.

None of them teach you the other **80%.**

The 80% is knowing what to risk. Knowing your real numbers. Knowing when you trade best and what triggers you to blow up. Knowing — mathematically — whether your approach actually works for YOU.

Not for the guru who taught it to you. For **you.**

Here's what I mean.

My win rate is around 55%. My average R is about 2.0. I risk $150-250 per trade and I trade best between 9:30 and 11:00 AM.

Those are **my** numbers.

Your win rate might be 42%. Your average R might be 1.4. You might trade best in the afternoon. You might blow up every Monday morning.

**If you're using my risk settings with your numbers, you will blow accounts.** Not because the strategy doesn't work — because the math doesn't match.

This is the thing nobody talks about. Two traders. Same strategy. Same setups. Completely different results.

The one who wins? Knows their numbers.
The one who loses? Is guessing.

---

### VISUAL ELEMENT — The Numbers Comparison:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Card: #242424 background
│  │         Joey's Numbers                │  │     Center-aligned
│  │                                       │  │
│  │    Win Rate: 55%                      │  │     Numbers in large font (28px)
│  │    Average R: 2.0                     │  │     in gold (#FFB800)
│  │    Risk/Trade: $150-250               │  │
│  │    Best Time: 9:30-11:00 AM           │  │     Labels in #A0A0A0, 14px
│  │    Monthly: $17K-23K                  │  │
│  │                                       │  │
│  │         ≠                             │  │  ← Large "≠" symbol, #FF4444, 36px
│  │                                       │  │
│  │         Your Numbers                  │  │
│  │                                       │  │
│  │    Win Rate: ???                       │  │     "???" in #FF4444
│  │    Average R: ???                      │  │     Everything else same style
│  │    Risk/Trade: ???                     │  │
│  │    Best Time: ???                      │  │
│  │    Monthly: ???                        │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  If you don't know your numbers,            │  ← Below card
│  you don't have an edge.                    │     Bold, white, 18px, centered
│  You have a hope.                           │     "hope" in gold italic
│                                             │
└─────────────────────────────────────────────┘
```

### Copy continues:

---

And here's the painful part.

Every coach, every guru, every YouTube video will tell you: **journal your trades.** Track your performance. Analyse your data.

They're completely right.

But here's what that actually looks like:

You open a spreadsheet. You type in your entry and exit. You write some notes. Maybe you do it for a week. Maybe two.

Then life gets in the way. It's boring. It's tedious. You never go back and actually analyse any of it. The data just... sits there.

And even the traders who DO journal — they're writing stuff down but never extracting anything useful. They're logging for the sake of logging. They never spot the patterns. They never calculate their edge.

**It's like recording every rep at the gym but never checking if you're actually getting stronger.**

So even when you're doing what you're told, you're still guessing. You're still trading blind.

---

### VISUAL ELEMENT — Customer quote:

```
┌─────────────────────────────────────────────┐
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Same quote card style as before
│  │  "I have a butt load of knowledge,    │  │     Gold left border
│  │   just seems like too much knowledge  │  │     Italic, 17px
│  │   and now I don't feel comfortable    │  │
│  │   applying said knowledge."           │  │
│  │                                       │  │
│  │               — 90-Minute Trader      │  │
│  │                  student              │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 5: THE MECHANISM (Joey's Discovery Story)
## ═══════════════════════════════════════════

**Background:** `#0D0D0D`
**Emotional state:** MID — storytelling mode. Longer sentences. Alen's "discovery story" section.

**Alen's framework:** "Where they WERE → WHERE THEY ARE → WHAT THEY DO → AND THAT'S NOT GETTING THEM THE OUTCOME." Then: the discovery of the mechanism that caused the CHANGE.

### COPY:

---

### How I Went From Losing $30,000 To Making $20K+ Per Month

I've been trading for over eight years.

And for the first five of those years, I was you. I knew trading could change my life. I could see the potential — work 90 minutes, make $500, $1,000, even $2K a day. No boss. No employees. Just a laptop.

But here's what nobody tells you about trading: **knowing the potential and reaching it are two completely different things.**

I lost over $30,000 of my own money. Blown accounts. Bad trades. Emotional spirals. I blew at least 30 evaluation accounts. I once lost 20 evaluation accounts in a single day from one bad trade.

When I discovered prop firms, I thought everything would change. Get funded, trade someone else's capital, keep the profits. Simple.

Except it wasn't. I'd pass the evaluation. I'd get funded. I'd get excited. And I'd blow the account two weeks later.

Over and over and over.

I was so frustrated because I knew the strategy worked. I could spot the setups. I was taking good trades. **Something was still wrong.**

Then I did something different.

I stopped looking for a better strategy. I stopped switching time frames. I stopped watching more videos.

Instead, I started writing down every single trade. Not just logging them — *paying attention to the results.*

How often was I winning? How much was I actually making when I won? How much was I losing when I lost? What times of day was I trading best? Which assets were losing me money? When was I emotional versus disciplined?

After about 30 trades, I looked at the numbers. And I saw things I'd never noticed.

I was risking different amounts on every trade. My profit targets were all over the place. Certain assets were consistently losing me money. Certain times of day were destroying my results.

**I wasn't trading to my strengths because I didn't know what my strengths were.**

So I fixed it. I started trading at the right times, with the right assets, using the right risk amount, with the right targets — all based on my actual data. Not what some guru told me. My real numbers.

And here's what happened:

The guesswork disappeared. I wasn't confused anymore. I wasn't second-guessing every trade. I wasn't emotional. I knew exactly what I was supposed to do.

I got funded again. I traded carefully with my plan.

First payout: $3K.
Then $4K.
Then $8K.
Then $12K.

Then consistently $20-25K every single month. Managing over $3.8 million in funded capital.

**Not because I learned a secret strategy. Because I started trading based on my real numbers.**

---

### VISUAL ELEMENT — Joey's Results Timeline:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Card: #242424 background
│  │  [PLACEHOLDER: Joey's Equity Curve    │  │     This should be a real
│  │   or Payout Screenshots]              │  │     screenshot of Joey's
│  │                                       │  │     funded account equity
│  │   If possible: a real screenshot      │  │     curve or payout history.
│  │   from one of Joey's funded           │  │
│  │   accounts showing the equity         │  │     If no screenshot available:
│  │   curve climbing. Or a screenshot     │  │     use a clean graphic showing
│  │   of a payout notification.           │  │     the timeline:
│  │                                       │  │     Lost $30K → 30 blown evals
│  │   This is THE most important          │  │     → First payout $3K → $4K
│  │   visual on the entire page.          │  │     → $8K → $12K → $20-25K/mo
│  │   Real proof > any designed           │  │
│  │   graphic.                            │  │     Style: horizontal timeline
│  │                                       │  │     with dots and labels.
│  │   Border-radius: 8px                  │  │     Red dots for losses,
│  │   Max-width: 600px, centered          │  │     green dots for payouts.
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│   $3.8M+ in funded capital managed          │  ← Below image
│   $20-25K consistent monthly payouts        │     Three stat lines, centered
│   48-55% win rate · 1.8-2.0 R:R            │     Green text, 16px, bold
│                                             │
└─────────────────────────────────────────────┘
```

### Copy continues:

---

That experience taught me the most important lesson in trading:

**Your edge isn't your strategy. Your edge is knowing your numbers.**

But I also learned something else. Figuring out your numbers manually — with spreadsheets and notes and hours of analysis — is brutal. Most traders just won't do it. Not because they're lazy. Because it's genuinely exhausting.

So I built something that does it for them. Automatically.

---

## ═══════════════════════════════════════════
## SECTION 6: SOCIAL PROOF BREAK #1
## ═══════════════════════════════════════════

**Background:** `#1A1A1A`
**Emotional state:** HIGH — validation, relief, excitement.

### Layout:

```
┌─────────────────────────────────────────────┐
│                                             │
│  What Traders Are Saying                    │  ← H3, white, 24px, centered
│                                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐    │  ← 3 cards in a row (desktop)
│  │          │ │          │ │          │    │     Stack vertically on mobile
│  │ "Got my  │ │ "3x100k  │ │ "Best    │    │     Card style: #242424 bg
│  │ first    │ │ passed,  │ │ trading  │    │     12px border-radius
│  │ payout   │ │ more in  │ │ week I've│    │     Gold star row on top
│  │ today,   │ │ the      │ │ had in a │    │     ★★★★★ (#FFB800)
│  │ the 90   │ │ pipeline"│ │ very long│    │
│  │ minutes  │ │          │ │ time...  │    │
│  │ Strategy │ │ — Ade    │ │ so much  │    │
│  │ made     │ │          │ │ less     │    │
│  │ such a   │ │          │ │ anxiety" │    │
│  │ big      │ │          │ │          │    │
│  │ differ-  │ │          │ │ — richH  │    │
│  │ ence"    │ │          │ │          │    │
│  │          │ │          │ │          │    │
│  │ —Littylit│ │          │ │          │    │
│  └──────────┘ └──────────┘ └──────────┘    │
│                                             │
│  ┌──────────────────────────────────────┐   │
│  │  "Joey's 90 Minute system is one     │   │  ← Wider card below the 3
│  │   that is simple and yet highly      │   │     This is a longer testimonial
│  │   effective. Before, I was studying  │   │     Same style but full width
│  │   several systems which were complex │   │
│  │   and did not give consistent        │   │
│  │   results... I now know when to best │   │
│  │   enter the market." — JoshLie       │   │
│  └──────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

**Selection criteria for testimonials:** Choose ones that address different objections:
- Littylit = "it actually leads to payouts" (result proof)
- Ade = "you can scale with this" (aspiration)
- richH = "reduced anxiety in 4 days" (speed + emotional benefit)
- JoshLie = "simple, effective, replaces complexity" (ease)

---

## ═══════════════════════════════════════════
## SECTION 7: THE "WHAT IF" BRIDGE
## ═══════════════════════════════════════════

**Background:** `#0D0D0D`
**Emotional state:** HIGH — this is the desire-building section. Alen: "What if" opens the solution without pushing it.

### COPY:

---

### What If You Didn't Have To Figure This Out Alone?

What if there was a system that tracked everything automatically?

A system that logged your trades in seconds. That calculated your win rate, your R, your patterns — without you touching a spreadsheet.

A system that told you:

**"Based on your last 30 trades, here's your real win rate. Here's how much you should be risking. Here's when you trade best. Here's what's costing you money. And here's exactly how many days until you pass your next eval."**

Not generic advice from a YouTube video. Not "what works for me." What works for **you** — based on your actual trading data.

What if after 20 trades, it started spotting patterns you can't see yourself? Like the fact that you lose 3x more on Mondays. Or that your win rate drops to 31% after a 2-loss day. Or that you trade best on NQ between 9:30 and 10:15 AM.

What if it warned you *before* you made a mistake — not after?

What if you could open your dashboard every morning, see your exact plan, and trade with the kind of clarity you've been chasing for months?

**What if the guesswork just... disappeared?**

That's what I built.

---

### WHY THIS SECTION WORKS:
- Alen: "You NEVER want to be the one who pushes the solution." The "What if" framing makes THEM imagine the solution. Their brain constructs the desire.
- **Sequential permission structure** (Alen): "What if it tracked → What if it told you → What if it spotted → What if it warned → What if the guesswork disappeared." Each "what if" gives permission for the next, building desire momentum.
- The AI insights examples are SPECIFIC and CONCRETE — no abstraction. "You lose 3x more on Mondays" is visceral. They can picture it.

---

## ═══════════════════════════════════════════
## SECTION 8: PRODUCT REVEAL + COMPONENTS
## ═══════════════════════════════════════════

**Background:** `#1A1A1A`
**Emotional state:** MID-HIGH — excitement, tangibility.

**Alen's principle:** "Feature → Benefit → Outcome → Feeling." Never stop at the feature. Always go to the feeling.

### COPY:

---

### The Precision Trader System

**Everything you need to go from guessing to knowing.**

Three components. One system. Working together.

---

### VISUAL ELEMENT — Component 1 Header:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │  🎓                                   │  │  ← Icon: graduation cap, 32px
│  │                                       │  │     Card: #242424 bg
│  │  COMPONENT 1                          │  │     "COMPONENT 1" in #A0A0A0,
│  │                                       │  │     12px, uppercase, letter-spacing
│  │  The Precision Trader                 │  │     Title: white, 28px, bold
│  │  Certification                        │  │
│  │                                       │  │
│  │  6 modules that teach you the 80%     │  │  ← Subtitle: #F0F0F0, 17px
│  │  every other course ignores.          │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

### COPY (Component 1):

---

This isn't another strategy course. You already know how to trade.

This is the **execution system** — the part that turns a strategy into consistent income.

**Module 1: How to Trade with Precision (Instead of Hope)**
What separates funded traders from everyone else. Why most traders lose even with a good strategy. The foundation that makes everything else work.
→ *You'll stop guessing and start trading with a clear plan every single day.*

**Module 2: Know Exactly What to Risk (On Every Single Trade)**
The formula that prevents blown accounts. Why risking the same amount every day is actually a mistake. How to calculate your risk based on YOUR account and YOUR goals.
→ *You'll never wonder "how much should I risk?" again. You'll know.*

**Module 3: The Consistency Formula**
Why boring 1.5R wins make you richer than chasing 5R home runs. The math behind $10K months from small, repeatable trades. How to stop the boom-bust cycle for good.
→ *You'll stop chasing big wins and start stacking consistent ones — the ones that compound.*

**Module 4: The Pass Formula**
How to pass prop firm evals in 10-20 days instead of months. The exact calculation that makes passing predictable, not hopeful.
→ *You'll know exactly when you'll pass — down to the day. Not "hopefully." Mathematically.*

**Module 5: The Payout System**
The difference between passing once and getting paid every month. How to trade funded accounts without blowing them. Buffer management. Risk adjustments. The system for repeatable payouts.
→ *Passing is step one. This is how you actually get money in your account, month after month.*

**Module 6: Joey's Complete Trading Models**
Every model I trade daily — including one I've never taught on YouTube, in any course, anywhere. This is the model behind my $15-25K months. Entries, stops, targets, management. Everything.
→ *You'll trade the exact same way I trade every day in our Discord community.*

*Total: 4-5 hours of focused training. No fluff. No filler. Complete it in a weekend.*

---

### VISUAL ELEMENT — Component 2 Header + Software Screenshots:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │  💻                                   │  │  ← Same card style
│  │                                       │  │
│  │  COMPONENT 2                          │  │
│  │                                       │  │
│  │  rPilot — Your AI Trading             │  │
│  │  System                               │  │
│  │                                       │  │
│  │  The engine that makes everything     │  │
│  │  work automatically.                  │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

### COPY (Component 2):

---

rPilot isn't a journal. It isn't a spreadsheet with a nice skin.

It's a complete system that **learns YOUR trading** and tells you exactly what to do.

---

### VISUAL ELEMENT — Feature blocks with screenshots:

For each feature below, the layout should be:

```
┌─────────────────────────────────────────────┐
│                                             │
│  Feature Name                               │  ← H3, white, 22px
│                                             │
│  [Copy block — 3-4 lines max]               │  ← Body text, left-aligned
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │  [PLACEHOLDER: Screenshot of this     │  │  ← Screenshot of the actual
│  │   feature in rPilot]                  │  │     rPilot interface showing
│  │                                       │  │     this specific feature.
│  │   Border-radius: 12px                 │  │
│  │   Border: 1px solid #333              │  │     If no screenshot available:
│  │   Max-width: 600px                    │  │     use a mockup or annotated
│  │   Centered                            │  │     wireframe. Real screenshots
│  │   Subtle glow: box-shadow with        │  │     are 10x better than mockups.
│  │   green tint on hover                 │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  → Outcome statement in green italic        │  ← #00D26A, italic, 16px
│                                             │
└─────────────────────────────────────────────┘
```

**Repeat this layout for each feature:**

---

**Log Any Trade in 30 Seconds**

No spreadsheets. No 20-minute journal sessions. Open rPilot, fill in the quick form — entry, exit, notes — and you're done. The system handles everything else.

[PLACEHOLDER: Screenshot of rPilot trade entry form — show the simple input fields]

→ *If you can type into your phone, you can use this.*

---

**Your Numbers. Calculated Automatically.**

Win rate. Average R. Profit factor. Equity curve. Timing patterns. Emotional triggers. Updated in real-time as you trade. You never touch a calculator.

[PLACEHOLDER: Screenshot of rPilot dashboard showing equity curve, win rate, and key metrics]

→ *Open your dashboard and know exactly where you stand — every single day.*

---

**Risk Shield — Know Exactly What To Risk**

Type in your account size and your limits. Risk Shield calculates exactly how much to risk per trade — based on YOUR actual performance. Not a generic formula. YOUR data.

It'll tell you how many consecutive losses you can take before hitting your drawdown. It'll warn you if you're risking too much. It's like having a risk manager sitting next to you.

[PLACEHOLDER: Screenshot of Risk Shield tool showing account input and calculated risk output]

→ *"Risk $200 per trade." That's it. No more guessing. No more blown accounts.*

---

**Pass Planner — Know Exactly When You'll Pass**

Input your numbers. The Pass Planner tells you how many trading days it'll take to pass your eval. Not a hope. A mathematical calculation based on your tracked win rate and R.

You can model different scenarios — "what if I increase my win rate by 5%?" — and see exactly what moves the needle.

[PLACEHOLDER: Screenshot of Pass Planner with projected days-to-pass and scenario modelling]

→ *You'll know the date you'll pass your eval. Not "hopefully." Down to the day.*

---

**Payout Planner — Map Your Path to Every Payout**

Once you're funded, it shows you exactly how to get to each payout. Buffer management. Risk adjustments. Breach distance. All calculated automatically.

[PLACEHOLDER: Screenshot of Payout Planner showing payout trajectory]

→ *Turn one pass into consistent, repeatable income.*

---

**Pilot — Your AI Trading Coach**

This is the part that changes everything.

After 20+ logged trades, rPilot's AI starts learning your patterns. It reads your trade notes, your journal, your psychology — everything you feed it.

And it tells you things you can't see yourself:

*"You lose 3x more money on Mondays after stressful weekends."*
*"Your win rate drops to 31% after a 2-loss day — stop trading."*
*"You perform best between 9:30 and 10:15 AM on NQ."*
*"When you journal before trading, your average R increases by 0.4."*

It catches revenge trading before you do it. It spots the patterns that cost you money. It knows more about your trading than you do — and the more you use it, the smarter it gets.

A human trading coach charges $5,000-$10,000 a year. They're not available at 5 AM when you're about to make a bad trade. They don't have access to every data point from every trade you've ever taken.

Pilot does. It's included. Available 24/7. Forever.

[PLACEHOLDER: Screenshot of Pilot AI coach conversation — showing a personalized insight based on the trader's data. Ideally a real conversation, not a mockup.]

→ *Like having a coach who knows you better than you know yourself — without the $10K price tag.*

---

**Community & Accountability**

Trading pods where you team up with 3-5 other traders. A community feed where real people share real results. An achievement system that makes consistency feel like a game.

You don't have to trade alone anymore.

[PLACEHOLDER: Screenshot of rPilot community feed or trading pod interface]

→ *Surround yourself with traders who are on the same path. Accountability changes everything.*

---

### VISUAL ELEMENT — Component 3 (simple, no screenshot needed):

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │  🤝                                   │  │
│  │                                       │  │
│  │  COMPONENT 3                          │  │
│  │                                       │  │
│  │  Lifetime Access.                     │  │
│  │  No Subscriptions. Ever.              │  │
│  │                                       │  │
│  │  ✓ All future software updates        │  │  ← Green checkmarks
│  │  ✓ All future course additions        │  │     16px body text
│  │  ✓ Email support                      │  │     Inside the card
│  │  ✓ Discord community access           │  │
│  │  ✓ Joey's ongoing content             │  │
│  │                                       │  │
│  │  One payment. Everything. Forever.    │  │  ← Bold, white, 18px
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

### CTA BREAK:

```
┌─────────────────────────────────────────────┐
│                                             │  ← #0D0D0D background
│  ── thin divider line ──                    │
│                                             │
│  [ 🟢 GET THE PRECISION TRADER SYSTEM ]     │  ← Same CTA button style
│           $697 — Instant Access             │
│                                             │
│         Or 3 payments of $249               │
│                                             │
│  ✓ Instant access · ✓ 30-day guarantee     │
│       ✓ Lifetime access, no fees            │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 9: SOCIAL PROOF BREAK #2
## ═══════════════════════════════════════════

**Background:** `#1A1A1A`
**Same layout as Section 6 but different testimonials.**

Choose 3-4 testimonials focused on:
- **Transformation:** "Before I was X, now I'm Y"
- **Software-specific:** Someone praising rPilot's insights or tools
- **Emotional:** "I finally feel in control / I have clarity / less anxiety"
- **Speed:** "Passed in X days" or "First payout in X weeks"

**Best options from the data:**

1. Maaz Khan: *"I have joined the course few days. Watched all videos and got the confidence which was needed... I never thought it would be this much valuable for such a price."*

2. richH: *"Best trading week I've had in a very long time. Not meaning the $$, though I did well there. It's only been 4 days but I already have so much less anxiety when trading."*

3. SafePlay: *"Joey's 90 Minute system is one that is simple and yet highly effective. I finally understood how to use prop firms to scale up safely while following a clear, rule-based intraday plan."*

4. Cdub: *"Thank you this strategy works. I'm planning on implementing it every day to pass this combine. Course is great, you explain it so well, easy to understand."*

### VISUAL ELEMENT — Longer testimonial card:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │  ★★★★★                               │  │  ← Gold stars, 16px
│  │                                       │  │
│  │  "I have joined the course few days.  │  │  ← Italic, #F0F0F0, 17px
│  │   Watched all videos and got the      │  │
│  │   confidence which was needed... I    │  │
│  │   never thought it would be this      │  │
│  │   much valuable for such a price."    │  │
│  │                                       │  │
│  │   Maaz Khan                           │  │  ← Bold, white, 15px
│  │   ★★★★★ Verified Buyer               │  │  ← #A0A0A0, 13px
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 10: WHO THIS IS FOR / NOT FOR
## ═══════════════════════════════════════════

**Background:** `#0D0D0D`
**Emotional state:** MID — this is a qualifier. It creates identity. Alen's identity close: "If they say NO, they're not rejecting the product, they're rejecting THEMSELVES."

### COPY:

---

### This Is For You If:

✓ You already have a trading strategy but you're not getting consistent results
✓ You've passed evals but keep blowing funded accounts or can't get to the payout
✓ You know you should be tracking your trades but you're not doing it (or doing it poorly)
✓ You're tired of guessing your risk and want a calculated, data-driven approach
✓ You're willing to log your trades for 30 seconds a day and let the system do the rest
✓ You want to trade 90 minutes a day, not 8 hours glued to charts

### This Is NOT For You If:

✗ You're looking for a "get rich quick" scheme — this requires actual trading
✗ You don't want to log your trades — the system needs your data to work
✗ You're not willing to follow a structured approach
✗ You want someone to trade for you — this is a tool that makes YOU a better trader

---

### VISUAL LAYOUT:

```
┌─────────────────────────────────────────────┐
│                                             │
│  This Is For You If:                        │  ← H3, white, 24px
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Card: #242424 bg
│  │  ✓  [line item]                       │  │     Green border-left
│  │  ✓  [line item]                       │  │     ✓ in #00D26A, 18px
│  │  ✓  [line item]                       │  │     Text: #F0F0F0, 17px
│  │  ✓  [line item]                       │  │     12px gap between items
│  │  ✓  [line item]                       │  │
│  │  ✓  [line item]                       │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│                 24px gap                     │
│                                             │
│  This Is NOT For You If:                    │  ← H3, white, 24px
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Card: #242424 bg
│  │  ✗  [line item]                       │  │     Red border-left (#FF4444)
│  │  ✗  [line item]                       │  │     ✗ in #FF4444
│  │  ✗  [line item]                       │  │     Text: #A0A0A0, 16px
│  │  ✗  [line item]                       │  │     (slightly muted — less
│  │                                       │  │      emphasis than the "for" list)
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 11: ABOUT JOEY (Authority Builder)
## ═══════════════════════════════════════════

**Background:** `#1A1A1A`
**Purpose:** Cold traffic from YouTube knows Joey's face but may not know his full story. This section builds authority. Warm traffic skips it naturally (they already know him). Keep it short.

### Layout:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌─────────────┐                            │
│  │             │  Meet Joey                 │  ← Photo on left, text on right
│  │  [PHOTO:    │                            │     (stack on mobile: photo on
│  │   Joey,     │  8+ years trading.         │      top, text below)
│  │   headshot  │  $3.8M+ in funded          │
│  │   or        │  capital.                  │     Photo: 200x200px, circular
│  │   candid    │  $20-25K/month             │     border-radius: 50%
│  │   at desk]  │  consistently.             │     border: 3px solid #333
│  │             │                            │
│  │  200x200px  │  Founder of 90MTRADER      │     Stats in bold white
│  │  circular   │  and Cryptic Hustle.       │     Bio text: #A0A0A0, 16px
│  │  crop       │  Creator of the            │
│  │             │  90-Minute Method.         │
│  └─────────────┘  Also founder of           │
│                   Viddyoze (separate         │
│                   software business).        │
│                                             │
│  I lost $30,000 and blew 30 evaluation      │  ← Below the photo/bio block
│  accounts before I figured any of this      │     #F0F0F0, 17px
│  out. I'm not here to sell you hype.        │     Left-aligned
│  I'm here because I've been exactly         │
│  where you are, and I built the thing       │
│  I wish I had when I started.               │
│                                             │
└─────────────────────────────────────────────┘
```

**Photo requirements:** Candid, approachable, NOT "guru on a yacht." Joey at his desk, or Joey looking at camera casually. Matches his brand voice: real, transparent, no-BS. If possible, use the same photo style as the YouTube channel so cold traffic recognizes him.

---

## ═══════════════════════════════════════════
## SECTION 12: VALUE STACK + PRICE REVEAL
## ═══════════════════════════════════════════

**Background:** `#0D0D0D`
**Emotional state:** HIGH — this is the "holy shit that's a good deal" moment.

### COPY:

---

### Here's Everything You're Getting Today

---

### VISUAL ELEMENT — Value Stack Table:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │  ← Card: #242424 bg
│  │  What You Get              Value      │  │     Table layout
│  │  ─────────────────────────────────    │  │
│  │                                       │  │     Left column: #F0F0F0, 16px
│  │  ✓ Precision Trader                   │  │     Right column (values):
│  │    Certification            $497      │  │       #A0A0A0, 16px
│  │    (6 modules)                        │  │       with strikethrough style
│  │                                       │  │
│  │  ✓ rPilot Trading                     │  │     ✓ in green (#00D26A)
│  │    Journal (lifetime)     $600/yr     │  │
│  │                                       │  │     Divider lines between rows:
│  │  ✓ Risk Management                    │  │       1px solid #333
│  │    Tools Suite              $297      │  │
│  │    (Risk Shield, Pass                 │  │
│  │     Planner, Payout                   │  │
│  │     Planner, Position                 │  │
│  │     Sizer, Funding                    │  │
│  │     Planner)                          │  │
│  │                                       │  │
│  │  ✓ AI Trading Coach       $5,000+/yr  │  │
│  │    — Pilot (lifetime)                 │  │
│  │                                       │  │
│  │  ✓ Community &                        │  │
│  │    Accountability           $997/yr   │  │
│  │    Pods                               │  │
│  │                                       │  │
│  │  ✓ Performance Tracking               │  │
│  │    & Analytics              $197/yr   │  │
│  │                                       │  │
│  │  ═════════════════════════════════    │  │  ← Thicker divider
│  │                                       │  │
│  │  Total Value:             $7,588+     │  │  ← Bold, white, 20px
│  │                                       │  │     Value in gold (#FFB800)
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

### COPY + PRICE REVEAL:

---

Total value: **$7,588+**

You're not paying that.

You're not paying $2,167 (what we originally planned to charge).

You're not even paying $997.

---

### VISUAL ELEMENT — Price Reveal Block:

```
┌─────────────────────────────────────────────┐
│                                             │  ← Centered block
│         ~~$7,588~~                          │     Crossed out prices in
│         ~~$2,167~~                          │     #FF4444 with strikethrough
│         ~~$997~~                            │     Each on its own line
│                                             │     Progressively smaller
│                                             │     (24px → 22px → 20px)
│                                             │
│         $697                                │  ← HUGE. White. 56px (desktop)
│                                             │     40px mobile. Extra bold.
│  One-time payment. Lifetime access.         │  ← #00D26A, 18px, bold
│                                             │
│         Or 3 payments of $249               │  ← #A0A0A0, 16px
│                                             │
└─────────────────────────────────────────────┘
```

### Copy continues:

---

Think about what you've already spent trying to figure this out.

Challenge fees. $150-300 every time. Blown accounts. Courses that promised results. Time going in circles watching YouTube videos at midnight.

Now think about this:

**One payout from one funded account is $3,000+.**

This system is designed to get you there faster and more consistently. One single payout pays for the entire system four times over. Everything after that is profit.

And you have lifetime access. No monthly fees. No subscriptions. No hidden costs. One payment and it's yours forever.

---

### CTA BLOCK:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │  ← Card: #1A1A1A bg
│  │                                       │  │     (slightly lifted from page bg)
│  │  [ 🟢 GET THE PRECISION TRADER        │  │     Border: 1px solid #333
│  │       SYSTEM — $697 ]                 │  │     Padding: 32px
│  │                                       │  │     Centered
│  │       Or 3 payments of $249           │  │
│  │                                       │  │
│  │  ✓ Precision Trader Certification     │  │  ← Checklist below button
│  │  ✓ rPilot AI Trading System           │  │     Green checks, 14px
│  │  ✓ AI Coach, Risk Tools,              │  │     #A0A0A0 text
│  │    Pass & Payout Planners             │  │
│  │  ✓ Community & Accountability         │  │
│  │  ✓ 30-Day Money-Back Guarantee        │  │
│  │  ✓ Lifetime Access. No Fees. Ever.    │  │
│  │                                       │  │
│  │  🔒 Secure 256-bit encrypted          │  │  ← Lock icon, #A0A0A0, 13px
│  │     checkout                          │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 13: GUARANTEE
## ═══════════════════════════════════════════

**Background:** `#1A1A1A`
**Emotional state:** HIGH — safety, relief.

### Layout:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │  ← Card: #242424 bg
│  │                                       │  │     Border: 1px solid #00D26A
│  │  [ICON: Shield with checkmark]        │  │     (green border = safety)
│  │   48px, centered, #00D26A             │  │
│  │                                       │  │
│  │  The 30-Day Precision Guarantee       │  │  ← H3, white, 24px, centered
│  │                                       │  │
│  │  Use the entire system for 30 days.   │  │  ← Body text, centered
│  │  Watch the training. Log at least     │  │     #F0F0F0, 17px
│  │  20 trades. Let rPilot start          │  │     Max-width: 540px
│  │  learning your patterns.              │  │     Centered within card
│  │                                       │  │
│  │  If you're not trading with more      │  │
│  │  clarity, more confidence, and more   │  │
│  │  consistency — email us and we'll     │  │
│  │  refund every penny.                  │  │
│  │                                       │  │
│  │  No questions asked.                  │  │  ← Bold, white, 18px
│  │                                       │  │
│  │  We can offer this because we've      │  │  ← #A0A0A0, 15px
│  │  seen what happens when traders       │  │
│  │  actually start tracking their        │  │
│  │  numbers. They don't come back for    │  │
│  │  refunds. They come back with         │  │
│  │  payout screenshots.                  │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 14: OBJECTION HANDLING
## ═══════════════════════════════════════════

**Background:** `#0D0D0D`
**Emotional state:** MID-LOW — calm, empathetic, direct. Joey's voice at its most honest.

**Alen's principle:** "A-listers don't let things become objections; they address them as concerns." Each block should feel like Joey talking to them directly. Not defensive. Empathetic then resolving.

### COPY:

---

### You Might Be Thinking...

---

**"I've been burned by courses before."**

I get it. Here's the difference. A course gives you information and leaves you alone. This gives you information AND a system that applies it for you.

The software calculates your risk. The AI analyses your patterns. The tools plan your path. The community keeps you accountable. You're not being left with videos and good intentions. You're being given an ecosystem that does the hard part automatically.

And if it doesn't work — 30-day money-back guarantee. You lose nothing.

---

**"I don't have time for another system."**

Logging a trade: 30 seconds. The entire course: 4-5 hours (one weekend). This replaces your guesswork — it doesn't add to your workload.

If you can find 90 minutes to trade, you can find 30 seconds to log. That's all it takes.

---

**"I'm not a numbers person."**

Good. You don't have to be. The software does everything. You answer three questions — account size, limits, goals — and it tells you: "Risk $200 per trade." That's it.

If you can type into your phone, you can use this. It's genuinely that simple.

---

**"$697 is a lot of money."**

One prop firm payout is $3,000+. If this system helps you pass even one eval you would've otherwise failed, it's paid for itself four times over.

There's a 3-payment option ($249 x 3). And a 30-day guarantee. If it doesn't deliver, you get every penny back.

---

**"My partner thinks I'm wasting money on trading."**

Show them this: it's a risk management system with a money-back guarantee. It's designed to turn trading from gambling into a calculated business. If it doesn't work in 30 days — full refund.

This isn't another "strategy." It's the system that makes the strategy actually work.

---

**"What if it doesn't work for me?"**

The system personalises to YOUR numbers. It doesn't say "do what Joey does." It says "based on YOUR data, here's what YOU should do." That's the whole point.

And again — 30 days. If it doesn't work, you get your money back.

---

### VISUAL LAYOUT for objections:

```
Each objection block:
┌─────────────────────────────────────────────┐
│                                             │
│  "I've been burned by courses before."      │  ← Objection in bold, white, 18px
│                                             │     Quoted format (with quotes)
│  I get it. Here's the difference...         │  ← Response in #F0F0F0, 17px
│  [response copy]                            │     Regular weight
│                                             │
│  ── thin divider #333 ──                    │  ← Between each objection block
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 15: FAQ
## ═══════════════════════════════════════════

**Background:** `#1A1A1A`
**Emotional state:** LOW — factual, clean.

### Layout: Accordion-style (click to expand)

```
┌─────────────────────────────────────────────┐
│                                             │
│  Frequently Asked Questions                 │  ← H3, white, 24px, centered
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │  ▸ What exactly do I get?             │  │  ← Accordion row
│  ├───────────────────────────────────────┤  │     Closed: question only
│  │  ▸ Is this a subscription?            │  │     Open: answer slides down
│  ├───────────────────────────────────────┤  │     Question: white, 16px, bold
│  │  ▸ Do I need the 90-Minute Method?    │  │     Answer: #A0A0A0, 15px
│  ├───────────────────────────────────────┤  │     ▸ icon rotates to ▾ on open
│  │  ▸ How long before I see results?     │  │     Background: #242424
│  ├───────────────────────────────────────┤  │     Border: 1px solid #333
│  │  ▸ Does it work on mobile?            │  │     Border-radius: 8px
│  ├───────────────────────────────────────┤  │
│  │  ▸ What if I need help?               │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

### FAQ Content:

**What exactly do I get when I sign up?**
Instant access to the Precision Trader Certification (6-module video course), lifetime access to rPilot (AI trading journal, risk tools, and coaching system), and community access including accountability pods and the trader feed. Everything is available immediately after purchase.

**Is this a subscription?**
No. One payment, lifetime access. No monthly fees. No hidden charges. All future updates included.

**Do I need to have taken the 90-Minute Method first?**
No. The Precision Trader System works with any trading strategy. That said, it pairs perfectly with the 90-Minute Method — and Module 6 teaches Joey's complete trading models, so you'll have a strategy to use regardless.

**How long before I see results?**
After 20 logged trades, rPilot starts generating personalised insights. After 50 trades, it's fully dialled in to your patterns. Most traders start seeing more clarity within the first 2 weeks of consistent use.

**Does it work on mobile?**
Yes. rPilot works on both desktop and mobile. Log trades from anywhere.

**What if I need help?**
Full email support at support@email.90mtrader.com plus an active Discord community. You're not doing this alone.

**What brokers/prop firms does it work with?**
All of them. rPilot is broker-agnostic — you log trades manually (30 seconds), so there's nothing to integrate. Works with Apex, Topstep, any prop firm, NinjaTrader, TradingView, Tradovate, MetaTrader — everything.

**What's the refund policy?**
Use the system for 30 days. Log at least 20 trades. If you're not trading with more clarity and consistency, email us for a full refund. No questions asked.

---

## ═══════════════════════════════════════════
## SECTION 16: THE FINAL CLOSE
## ═══════════════════════════════════════════

**Background:** `#0D0D0D`
**Emotional state:** PEAK HIGH — this is the most emotionally charged section on the page. Future pacing + consequence of inaction + identity trigger.

**Alen's frameworks applied here:**
- Future pacing (visualization of the outcome)
- Consequence close (what happens if they don't act)
- Identity close ("if you're someone who...")
- Desire stacking (primary desire → secondary → tertiary → feeling)
- Short chop cadence = peak emotional state
- Towards language (solution-focused, proactive, HIGH VALUE customer acquisition)

### COPY:

---

### Imagine This. 30 Days From Now.

You wake up. You open rPilot.

Your equity curve is climbing. Not perfect — there are red days — but the trend is clear. Steady. Consistent. Moving in the right direction.

You can see your win rate: 52%. Average R: 1.8. The Pass Planner says 11 days to your next eval pass. Pilot is telling you that your Tuesdays are your best day and that your NQ trades are outperforming everything else.

There's no more guessing. No more "should I take this trade?" No more spiralling after a loss. You have a plan. You have data. You have clarity.

You take your trades. You log them in 30 seconds. You close the charts.

And you go live your life.

**That's what trading looks like when you know your numbers.**

---

Now imagine 90 days from now.

You've passed two evaluations. You're funded. The Payout Planner is showing you're 8 trading days from your first payout.

Your partner sees the funded account notification. They don't say anything — but you catch the look. The one that says *maybe this is actually going to work.*

Your kid asks about the weekend trip. And this time, you don't check the bank account first.

You just say yes.

---

**That's what this is really about.**

Not software. Not a course. Not another thing to add to your stack.

It's about becoming the trader — and the person — you know you're capable of being. The one who stopped guessing and started knowing. The one who bet on themselves and won.

---

Or you can close this page.

Keep trading the way you've been trading. Keep guessing your risk. Keep blowing accounts. Keep watching other traders post payouts in the Discord while you're stuck passing the same eval.

Keep telling yourself you'll figure it out eventually.

Every day you trade without knowing your numbers is another day you're leaving money on the table. Another eval fee you didn't need to pay. Another month of inconsistency you didn't need to suffer.

**The strategy isn't the problem. You've already got that.**

**The problem is that you're trading blind. And this is the system that fixes it.**

---

### FINAL CTA BLOCK:

```
┌─────────────────────────────────────────────┐
│                                             │
│  ┌───────────────────────────────────────┐  │  ← Card: #1A1A1A bg
│  │                                       │  │     Border: 1px solid #00D26A
│  │                                       │  │     Padding: 40px
│  │  [ 🟢 GET THE PRECISION TRADER        │  │     Max-width: 600px
│  │       SYSTEM — $697 ]                 │  │     Centered on page
│  │                                       │  │
│  │       Or 3 payments of $249           │  │
│  │                                       │  │
│  │  ✓ Precision Trader Certification     │  │
│  │    (6 modules)                        │  │
│  │  ✓ rPilot AI Trading System           │  │
│  │    (lifetime access)                  │  │
│  │  ✓ AI Coach — Pilot                   │  │
│  │  ✓ Risk Shield, Pass Planner,         │  │
│  │    Payout Planner                     │  │
│  │  ✓ Community & Accountability Pods    │  │
│  │  ✓ 30-Day Money-Back Guarantee        │  │
│  │  ✓ No subscriptions. One payment.     │  │
│  │    Forever.                           │  │
│  │                                       │  │
│  │  🔒 Secure 256-bit encrypted          │  │
│  │     checkout                          │  │
│  │                                       │  │
│  │  "Excellent" rated by 1,275+ traders  │  │
│  │  ★★★★★                               │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
│                                             │
│  ┌───────────────────────────────────────┐  │  ← BELOW the CTA card
│  │                                       │  │     Scarcity block
│  │  ⚠ We're manually onboarding the     │  │     Card: #242424 bg
│  │  first 50 members. Once we hit 50,    │  │     Border-left: 3px solid
│  │  enrolment closes for 30 days.        │  │     #FFB800
│  │                                       │  │     Text: #F0F0F0, 15px
│  │  This is real — not a fake countdown  │  │     ⚠ icon: #FFB800
│  │  timer. We want to get onboarding     │  │
│  │  right for the first group.           │  │
│  │                                       │  │
│  └───────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ═══════════════════════════════════════════
## SECTION 17: FOOTER / LEGAL
## ═══════════════════════════════════════════

**Background:** `#0A0A0A` (slightly darker than page bg)
**Text:** `#666666` (very muted)
**Font size:** 12px
**Padding:** 40px top/bottom

### Content:

```
┌─────────────────────────────────────────────┐
│                                             │
│  [90MTRADER LOGO — small, grey version]     │
│                                             │
│  Charts Paradise LLC                        │
│  30 N Gould St Ste R                        │
│  Sheridan, Wyoming 82801                    │
│  support@email.90mtrader.com                │
│                                             │
│  Terms of Service | Privacy Policy |        │
│  Refund Policy                              │
│                                             │
│  ─────────────────────────────────────────  │
│                                             │
│  DISCLAIMER: Trading futures and options    │
│  involves substantial risk of loss and is   │
│  not suitable for every investor. The       │
│  valuation of futures and options may       │
│  fluctuate, and as a result, you may lose   │
│  more than your original investment. Past   │
│  results are not necessarily indicative     │
│  of future results. All content is for      │
│  educational purposes only and does not     │
│  constitute financial advice. Individual    │
│  results will vary. We do not guarantee     │
│  any specific results or earnings.          │
│                                             │
│  © 2026 Charts Paradise LLC.                │
│  All rights reserved.                       │
│                                             │
└─────────────────────────────────────────────┘
```

---

# 4. STICKY/FIXED ELEMENTS

## Sticky CTA Bar (Mobile Only)

```
┌─────────────────────────────────────────────┐
│  [ 🟢 Get The System — $697 ]               │  ← Fixed to bottom of viewport
│                                             │     Background: #1A1A1A
│                                             │     Border-top: 1px solid #333
│                                             │     Padding: 12px 20px
│                                             │     Button: same green style
│                                             │     but smaller (16px font)
│                                             │     z-index: 9999
│                                             │
│  APPEARS: After user scrolls past the       │     Show after scroll past
│  first CTA button (below VSL).              │     Section 1's CTA button.
│  HIDES: When user is in viewport of         │     Hide when any CTA block
│  any existing CTA block (to avoid           │     is visible (to avoid
│  visual duplication).                       │     doubling up).
│                                             │
└─────────────────────────────────────────────┘
```

## No Sticky Bar on Desktop
Desktop users can scroll quickly and the page has enough CTA breaks. A sticky bar on desktop feels aggressive and cheap for a $697 product.

---

# 5. MOBILE ADAPTATIONS

| Element | Desktop | Mobile |
|---------|---------|--------|
| Logo | 32px height | 28px height |
| Hero headline | 48px, 3 lines | 32px, 4-5 lines |
| VSL | 800px max-width | Full width, 16:9 |
| Body text | 18px | 16px |
| Cards (side by side) | 2-3 columns | Stack vertically, full width |
| Two Traders comparison | Side by side | Stack (Trader A on top, B below) |
| Joey Numbers comparison | Side by side panels | Stack vertically |
| CTA buttons | Auto width, centered | Full width |
| Joey photo + bio | Side by side | Photo centered on top, bio below |
| Value stack table | Table format | Simplified list format |
| Section padding | 80px | 48px |
| Testimonial grid | 3 across | 1 column, swipeable carousel (optional) |
| Sticky CTA bar | Hidden | Fixed bottom bar (see above) |
| FAQ accordion | Same | Same (touch-friendly, min 48px tap targets) |

**Mobile page speed targets:**
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Compress all images to WebP
- Lazy-load everything below the fold
- VSL thumbnail loads first, video loads on play

---

# 6. TECHNICAL NOTES FOR GHL

## Page Setup
- **Page type:** Funnel page (not website page) — no navigation, no footer links except legal
- **Custom domain:** Use your 90mtrader.com domain, subdirectory `/precision-trader`
- **SSL:** Ensure HTTPS is active (should be automatic on GHL)
- **Favicon:** Use 90MTRADER logo/icon

## Tracking
- **Facebook Pixel:** Fire on page load (for future retargeting when you run FB ads)
- **Google Analytics / GA4:** Fire on page load
- **Conversion tracking:** Fire on checkout success page (thank you page)
- **UTM parameters:** Build CTA links in emails with UTM tags:
  - `?utm_source=email&utm_medium=launch&utm_campaign=precision-trader&utm_content=email1`
  - This lets you track which email drives the most sales

## VSL Hosting
- **Recommended:** Wistia (best analytics, heatmaps, play rate tracking) or Vimeo Pro (clean, no suggested videos)
- **NOT YouTube** (even unlisted) — YouTube shows suggested videos at end, distracting and can show competitor content
- **Settings:** Autoplay OFF. No controls visible except play/pause and volume. No playback speed. No download. Brand color on player: match your green (#00D26A).

## Checkout Integration
- Link the CTA buttons to your GHL checkout page (`/precision-trader/checkout`)
- Stripe product: Create two price options — $697 one-time and $249 x 3 installment plan
- Checkout page: Simple order form (name, email, payment). No bumps. No upsells. Clean.

## Email Tracking
- Use GHL's built-in link tracking in email sequences
- Tag anyone who clicks through to the sales page: `clicked-precision-trader-page`
- Tag anyone who visits checkout: `visited-precision-trader-checkout`
- This lets you build your abandoned checkout automation

---

# APPENDIX: SCREENSHOT/IMAGE CHECKLIST

Before building the page, gather these visual assets:

| # | Asset | Where It Goes | Priority |
|---|-------|--------------|----------|
| 1 | **Joey headshot/candid photo** (high-res, approachable) | Section 11 (About Joey) | CRITICAL |
| 2 | **VSL video file** (already recorded) | Section 1 (Hero) | CRITICAL |
| 3 | **VSL thumbnail** (Joey at desk or looking at camera, text overlay) | Section 1 (Hero) | CRITICAL |
| 4 | **rPilot dashboard screenshot** (equity curve, key metrics visible) | Section 8 (Product) | HIGH |
| 5 | **rPilot trade entry form screenshot** | Section 8 (Product) | HIGH |
| 6 | **Risk Shield tool screenshot** (showing account input → risk output) | Section 8 (Product) | HIGH |
| 7 | **Pass Planner screenshot** (showing projected days to pass) | Section 8 (Product) | HIGH |
| 8 | **Payout Planner screenshot** | Section 8 (Product) | MEDIUM |
| 9 | **Pilot AI coach conversation screenshot** (real, not mockup) | Section 8 (Product) | HIGH |
| 10 | **Community feed / trading pod screenshot** | Section 8 (Product) | MEDIUM |
| 11 | **Joey payout screenshot or equity curve** (real proof) | Section 5 (Story) | HIGH |
| 12 | **90MTRADER logo** (white version for dark background) | Section 1 + Section 17 | CRITICAL |
| 13 | **90MTRADER logo** (grey version for footer) | Section 17 | LOW |

**If any screenshots aren't available yet:** Use a placeholder card with text "Screenshot coming soon" in #666 text on #1A1A1A background. Better to launch with placeholder + real copy than to delay launch waiting for perfect screenshots. Replace them as you get them.

---

# APPENDIX: COPY PRINCIPLES SCORECARD

Self-audit checklist — every item should be YES before going live:

| Principle (Alen's Framework) | Applied? | Where |
|------------------------------|----------|-------|
| TSL 3-stage model (Problem → Solution → Product) | ✓ | Sections 2-3, 4-7, 8-16 |
| POV change (strategy → numbers) | ✓ | Section 4 |
| AIDVVA (Attention → Interest → Desire → Visualization → Validation → Action) | ✓ | Throughout |
| 70% feeling / 30% thinking ratio | ✓ | Sections 2, 5, 16 are feeling. 3, 4, 8 are thinking. |
| Binding statements | ✓ | Sections 2, 3, 10, 16 |
| Identity close | ✓ | Sections 10, 16 |
| Risk reversal INFUSED (not just stacked at end) | ✓ | "One payout pays 4x" in Section 12, guarantee mentioned in Sections 1, 12, 13, 14 |
| Consequence close | ✓ | Section 16 |
| Future pacing / visualization | ✓ | Section 16 |
| No abstraction — every concept is concrete | ✓ | Specific numbers, specific examples throughout |
| Absolution of responsibility | ✓ | "Not your strategy, not your discipline" (Section 2), "Software does it for you" (Section 8) |
| Emotional oscillation (low → high → low → high) | ✓ | Mapped in Section 2 architecture |
| Copy cadence (short chop for emotion, long for story) | ✓ | Sections 2, 16 = short. Section 5 = longer. |
| Social proof at verification points | ✓ | Sections 6, 9, 1 (micro-bar), 16 (star rating) |
| Customer's own words used | ✓ | Verbatim quotes in Sections 2, 4 |
| Discovery story with mechanism | ✓ | Section 5 |
| "What if" bridge to solution | ✓ | Section 7 |
| Value stack with anchoring | ✓ | Section 12 |
| Desire stacking (primary → secondary → tertiary → feeling) | ✓ | Section 16 close |
| Show then tell (not tell then show) | ✓ | Screenshots follow after feature description |
| Triple stack close ("without / even if / so you can") | ✓ | Embedded in CTA blocks |
| Invisible copy (reads as education, not sales) | ✓ | Sections 3-5 read as diagnosis and story, not pitch |

---

*This document is the single source of truth for building the Precision Trader System sales page.*
*Every section, every element, every visual, every word is specified.*
*Build it section by section in GHL. Follow the order. Trust the structure.*

*Last updated: March 2026*
