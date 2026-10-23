# 📅 Day 1 — Friday, Oct 23, 2026

**Goal:** Master conditional probability & Bayes' Theorem, and solve Puzzles 1–3 cold.  
**Time budget:** 2–3 hours total (can be split into two 90-min blocks).  
**Location:** `Quant_Intern_Prep/` — this is your only repo for quant prep.

---

## 🕒 Time-Blocked Schedule (pick one)

| Block | Time | Task |
|-------|------|------|
| A | 60 min | Conditional Probability & Bayes (notes below + 4 drills) |
| B | 15 min | Mental math warmup (2-digit × 2-digit) |
| C | 60 min | Puzzles 1, 2, 3 — write out full solutions in your own words |
| D | 15 min | End-of-day checklist + log in tracker |

> If you only have 90 minutes: do Block A (45 min) + Block C (45 min), skip mental math today.

---

## 1️⃣ Conditional Probability & Bayes' Theorem

### What it is
`P(A|B)` = probability of event A **given** that event B has already happened.

```
P(A|B) = P(A ∩ B) / P(B)
```

Think of it as shrinking the sample space to only outcomes where B is true, then asking what fraction of those also have A.

### Bayes' Theorem (the quant interview workhorse)
```
P(A|B) = P(B|A)·P(A) / P(B)
       = P(B|A)·P(A) / [P(B|A)·P(A) + P(B|¬A)·P(¬A)]
```

### Classic setup: Medical test (learn this template)
- Disease prevalence: 1% → P(D) = 0.01
- Test sensitivity: 99% → P(Pos|D) = 0.99
- False positive rate: 5% → P(Pos|¬D) = 0.05
- **Question:** You test positive. P(D|Pos)?

```
P(D|Pos) = 0.99 × 0.01 / [0.99×0.01 + 0.05×0.99]
         = 0.0099 / (0.0099 + 0.0495)
         = 0.0099 / 0.0594
         ≈ 0.1667 → 16.7%
```

**Lesson:** Even a 99% accurate test gives only ~17% chance of disease when prevalence is 1%. Base rates matter.

### Tree diagram method (use in interviews)
1. Draw first-level branches: D / ¬D with probabilities.
2. From each, draw second-level branches: Pos / Neg with conditional probabilities.
3. Multiply along paths to get joint probabilities.
4. For P(D|Pos): (path D∩Pos) / (all paths ending in Pos).

---

## 2️⃣ Four 5-Minute Drills (do these before puzzles)

**Drill 1:** A box has 3 red, 2 blue balls. Draw two without replacement. P(both red)?  
**Drill 2:** P(A) = 0.4, P(B) = 0.5, P(A∩B) = 0.2. P(A|B)? P(B|A)?  
**Drill 3:** Coin is fair (P(H)=0.5) or biased (P(H)=0.8), prior 50/50. You flip once, get heads. P(fair|H)?  
**Drill 4:** Two dice rolled. P(sum = 8 | first die is 5)?

<details>
<summary>Answers (don't peek until you try)</summary>

1. (3/5)·(2/4) = 3/10 = 0.3
2. P(A|B) = 0.2/0.5 = 0.4; P(B|A) = 0.2/0.4 = 0.5
3. P(fair|H) = (0.5×0.5) / (0.5×0.5 + 0.8×0.5) = 0.25/0.65 = 5/13 ≈ 0.385
4. P(sum=8 | first=5) = P(second=3) = 1/6
</details>

---

## 3️⃣ Puzzle 1 — Two Children (Boy/Girl Paradox)

**Problem:** A family has two children. You are told at least one is a boy. What is the probability both are boys?

### Step-by-step solution

**Step 1 — List the sample space (equally likely):**
- BB (older boy, younger boy)
- BG (older boy, younger girl)
- GB (older girl, younger boy)
- GG (older girl, younger girl)

Each has probability 1/4.

**Step 2 — Apply the condition "at least one boy":**
Eliminate GG. Remaining: {BB, BG, GB}. Each still equally likely (conditional prob renormalizes, but here all were 1/4 so they remain equal among the 3).

**Step 3 — Count favorable:**
Both boys = {BB}. That's 1 out of 3.

**Answer: 1/3.**

### The trap
Most people say 1/2 ("the other child is equally likely boy or girl"). That's wrong because "at least one is a boy" is different from "the older child is a boy."

**Variant:** If you're told "the older child is a boy," sample space becomes {BB, BG} → answer is 1/2. Information changes the sample space.

---

## 4️⃣ Puzzle 2 — Monty Hall (3 Doors)

**Problem:** You pick Door 1. Host (who knows what's behind doors) opens Door 3, revealing a goat. He offers: switch to Door 2 or stay with Door 1? Should you switch?

### Step-by-step solution

**Initial probabilities (before host opens anything):**
- P(car behind Door 1) = 1/3
- P(car behind Door 2) = 1/3
- P(car behind Door 3) = 1/3

**Host's action:** He opens a door with a goat, never your door, never the car.

**Case analysis:**
| Where is car? | You picked | Host opens | If you STAY | If you SWITCH |
|---------------|-----------|------------|-------------|---------------|
| Door 1 (1/3) | Door 1 | Door 2 or 3 | WIN | LOSE |
| Door 2 (1/3) | Door 1 | Door 3 | LOSE | WIN |
| Door 3 (1/3) | Door 1 | Door 2 | LOSE | WIN |

**Result:**
- Stay wins 1/3 of the time.
- Switch wins 2/3 of the time.

**Answer: Yes, switch.** You double your chances from 1/3 to 2/3.

### Intuition
Your first pick was right only 1/3 of the time. The host concentrates the remaining 2/3 probability onto the single unopened door he didn't open. Switching wins whenever your initial pick was wrong (which is 2/3 of the time).

**100-door version:** You pick 1 of 100. Host opens 98 goats. Switch → 99/100 win. Same logic.

---

## 5️⃣ Puzzle 3 — Ants on a Plank

**Problem:** 100 ants are on a 1-meter plank. Each ant walks 1 cm/s, either left or right (chosen randomly). When two ants collide, they instantly reverse directions. How long until all ants fall off the plank?

### Step-by-step solution

**Key insight:** Ants are identical. When two collide and reverse, it's indistinguishable from them passing through each other and keeping their original directions.

So ignore collisions entirely. Pretend every ant just walks straight in its initial direction until it falls off.

**Worst case:** An ant starts at one end and has to walk the full 1 meter = 100 cm at 1 cm/s → 100 seconds.

No ant can take longer than that, because even with collisions, the "identity" of the ant falling off doesn't matter — some ant falls off at most every moment, and the last one is gone by the time a straight-walking ant would cross the plank.

**Answer: 100 seconds (1 minute 40 seconds).**

---

## 6️⃣ Mental Math Warmup (5 min)

Do these aloud, timed:

1. 37 × 48  
2. 29 × 31  
3. 15², 25², 35² (two-digit squares ending in 5: first digit × (first digit + 1), append 25 → e.g., 35²: 3×4=12, append 25 = 1225)
4. 17% of 240  
5. 1/13 as decimal (≈ 0.0769)

<details>
<summary>Answers</summary>
1. 1776  
2. 899  
3. 225, 625, 1225  
4. 40.8  
5. 0.0769 (repeating 076923)
</details>

---

## 7️⃣ End-of-Day Checklist

Before you close up today, confirm:

- [ ] I can state Bayes' Theorem from memory.
- [ ] I can solve the medical-test problem (1% prevalence, 99% sens, 5% FPR) without looking.
- [ ] I can explain Puzzle 1 (Two Children) out loud, including why the answer is 1/3 not 1/2.
- [ ] I can explain Puzzle 2 (Monty Hall) out loud, including the 100-door intuition.
- [ ] I can explain Puzzle 3 (Ants) out loud, including the "pass through each other" insight.
- [ ] I logged today in `06_Tracker/weekly_review.md` under Week 1.

---

## 8️⃣ What's Next (Tomorrow, Sat Oct 24)

- Random variables & expectation (`01_Concepts/statistics.md`)
- Puzzles 4–7 (HH vs HT, Gambler's Ruin, Two Envelopes, Biased→Fair Coin)
- Mental math: 2-digit × 2-digit drill again

---

**Day 1 complete. Push this file and get back to it tomorrow.**

*Updated: Oct 23, 2026*