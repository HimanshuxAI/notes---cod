# 🧩 Quant Interview Puzzles

**Strategy:** Don't memorize answers. Learn to structure your thinking: state assumptions, draw a diagram/tree, work small cases, look for symmetry, then generalize.

---

## Puzzle 1 — Two Children (Boy/Girl Paradox)
> "A family has two children. At least one is a boy. What's the probability both are boys?"

**Trap:** It's not 1/2. Sample space: BB, BG, GB, GG. Given at least one boy → {BB, BG, GB}. P(both boys) = 1/3.

**Variant:** "The older child is a boy" → {BB, BG} → P = 1/2. Information changes the sample space.

---

## Puzzle 2 — Monty Hall (3 doors)
> You pick door 1. Host opens door 3 (goat). Switch to door 2?

**Answer:** Yes. P(win by switching) = 2/3. Your initial pick was right 1/3 of the time; host concentrates the 2/3 on the other door.

**100-door version:** You pick 1. Host opens 98 goats. Switch → 99/100 win.

---

## Puzzle 3 — Ants on a Plank
> 100 ants on a 1-meter plank, each walks 1 cm/s left or right. When two collide they reverse. How long until all fall off?

**Answer:** 100 seconds. Collisions = ants pass through each other (identical ants). Max time = plank length / speed.

---

## Puzzle 4 — Coin Flips: HH vs HT
> Flip a fair coin. Expected flips to see HH? To see HT?

**Answer:** HH = 6, HT = 4.
- HT: geometric-like, E = 4.
- HH: use states. Let E = expected from start, E_H = expected after last flip was H.
  - E = 1 + 0.5·E + 0.5·E_H
  - E_H = 1 + 0.5·0 + 0.5·E_H → E_H = 2
  - E = 1 + 0.5E + 1 → E = 6.

**Pattern:** Set up state equations: E = 1 + Σ pᵢ·Eᵢ.

---

## Puzzle 5 — Gambler's Ruin
> You start with \$i, opponent with \$N−i. Each round win \$1 with prob p, lose with q=1−p. Probability you reach N before 0?

- If p = 0.5: P = i/N.
- If p ≠ 0.5: P = (1 − (q/p)ⁱ) / (1 − (q/p)ᴺ).

---

## Puzzle 6 — 100 Prisoners and a Light Bulb (advanced)
> 100 prisoners, one light bulb (initially off), one prisoner taken daily to a room, can toggle bulb, can declare "all have visited." If correct, all freed; if wrong, all executed. Strategy?

**Answer:** Designate a counter. Others turn bulb on once (first time they find it off). Counter turns it off and counts. When counter reaches 99, declare. Expected ~10,000 days but works with certainty.

---

## Puzzle 7 — Two Envelopes
> Two envelopes, one has 2× the other. You pick one, see \$X. Switch?

**Answer:** It's a paradox — naive EV says switch (1.25X), but that double-counts. Without a distribution on envelope amounts, there's no well-defined answer. State assumptions clearly.

---

## Puzzle 8 — Biased Coin to Fair Coin
> You have a coin with unknown bias p. Generate a fair 50/50 outcome.

**Answer (von Neumann):** Flip twice.
- HT → output H
- TH → output T
- HH or TT → discard, repeat.
P(HT) = P(TH) = p(1−p), so conditional on a decision it's 50/50.

---

## Puzzle 9 — Expected Value of a Dice Game
> Roll a die. You get the value in dollars. Can reroll once if you pay \$1. Should you?

Reroll if current value < E[reroll] − cost = 3.5 − 1 = 2.5. So reroll on 1 or 2. EV = (3+4+5+6)/6 + (1/6)·(3.5−1) ... compute exactly: keep ≥3, reroll ≤2.
EV = (4+5+6)/6 × ... let's compute properly:
- Roll 1,2 (prob 2/6): reroll, net EV = 3.5 − 1 = 2.5
- Roll 3,4,5,6 (prob 4/6): keep, avg = 4.5
- Total = (2/6)(2.5) + (4/6)(4.5) = 5/6 + 3 = 3.833. Without reroll option EV = 3.5. So yes, reroll option adds ~$0.33.

---

## Puzzle 10 — Random Points on a Circle
> 3 random points on a circle. Probability they lie in some semicircle?

**Answer:** 3/4. Fix one point; the other two must fall within a semicircle starting from it. Standard geometric probability result: n points → n/2ⁿ⁻¹ for n=3 gives 3/4.

---

## 📋 Solving Template (use in interviews)

```
1. Restate the problem. Clarify assumptions (fair coin? independent? with replacement?).
2. Draw it: tree, table, state diagram, or small example (n=2, n=3).
3. Work small cases by hand. Look for a pattern.
4. State your approach: symmetry? linearity of expectation? state equations? Bayes?
5. Compute. Sanity-check the answer (does it fall in [0,1]? limiting cases?).
6. Communicate clearly — narrate as you go.
```

---

## Practice Tracker

| # | Puzzle | Solved? | Time (min) | Notes |
|---|--------|---------|------------|-------|
| 1 | Two Children | ☐ | | |
| 2 | Monty Hall | ☐ | | |
| 3 | Ants on Plank | ☐ | | |
| 4 | HH vs HT | ☐ | | |
| 5 | Gambler's Ruin | ☐ | | |
| 6 | 100 Prisoners | ☐ | | |
| 7 | Two Envelopes | ☐ | | |
| 8 | Biased → Fair Coin | ☐ | | |
| 9 | Dice Reroll EV | ☐ | | |
| 10 | Circle Semicircle | ☐ | | |

Target: 50+ puzzles by end of Phase 2 (Dec 2). Add your own as you find them.

---

*Resources:* Heard on the Street (Falcone), A Practical Guide to Quant Finance Interviews (Xinfeng Zhou), quantguide.io