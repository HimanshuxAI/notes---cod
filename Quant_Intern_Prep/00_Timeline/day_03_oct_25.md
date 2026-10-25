# 📅 Day 3 — Sunday, Oct 25, 2026

**Goal:** Weekly review + catch-up. Consolidate Days 1–2, fix weak spots, and set up Week 2.  
**Time budget:** 1.5–2 hours.  
**Rule:** If you didn't finish something from Fri/Sat, do it FIRST today before anything new.

---

## 🕒 Time-Blocked Schedule

| Block | Time | Task |
|-------|------|------|
| A | 30 min | Re-do every drill you got wrong (Days 1–2) |
| B | 20 min | Re-explain Puzzles 1–3 out loud (no notes) |
| C | 30 min | Fill out Weekly Review (template below) — be brutally honest |
| D | 20 min | Memorize checklist: Bayes, linearity, distribution table |
| E | 10 min | Preview Week 2 (Monday = Puzzles 4–7) |
| F | 10 min | Commit & push |

---

## 1️⃣ Block A — Drill Redo (30 min)

Go back to `day_01_oct_23.md` (4 drills) and `day_02_oct_24.md` (5 drills). Re-do **every** one you got wrong or hesitated on. Write the answer fresh, don't just read the solution.

| Drill | Day | Redone? | Correct? | Notes |
|-------|-----|---------|----------|-------|
| Conditional prob (balls) | 1 | ☐ | ☐ | |
| P(A\|B), P(B\|A) | 1 | ☐ | ☐ | |
| Fair vs biased coin | 1 | ☐ | ☐ | |
| Dice conditional | 1 | ☐ | ☐ | |
| Bernoulli E/Var | 2 | ☐ | ☐ | |
| Die E[X], E[X²], Var | 2 | ☐ | ☐ | |
| Binomial(10, 0.5) | 2 | ☐ | ☐ | |
| Fixed points (permutation) | 2 | ☐ | ☐ | |
| Var(X+Y), Var(X−Y) | 2 | ☐ | ☐ | |

**If any are still wrong:** re-read the concept section, then re-do. Do not move on until all 9 are correct.

---

## 2️⃣ Block B — Puzzle Re-Explain Out Loud (20 min)

Stand up and explain each puzzle to an empty room (or record yourself on your phone). No notes allowed.

| Puzzle | Can explain cold? | Key insight to state |
|--------|-------------------|----------------------|
| 1. Two Children | ☐ | Sample space {BB,BG,GB}, eliminate GG → 1/3 |
| 2. Monty Hall | ☐ | Switch wins 2/3; host concentrates probability |
| 3. Ants on Plank | ☐ | Identical ants → pass through each other → 100s |

**If you stumble on any:** re-read that puzzle's solution in `03_Puzzles/puzzles.md`, then re-explain out loud again.

---

## 3️⃣ Block C — Weekly Review (30 min)

Fill this out honestly. This goes in `06_Tracker/weekly_review.md`.

```
Week: 1 | Dates: Oct 22–28, 2026

What I completed:
- [ ] Concept: Conditional probability + Bayes (Day 1)
- [ ] Concept: Random variables, expectation, variance (Day 2)
- [ ] Coding: none yet (starts Week 2)
- [ ] Puzzles: 3/10 solved (Puzzles 1–3)
- [ ] Applications: none yet (starts Week 9)

What I got wrong (and why):
_ [be specific — e.g., "mixed up P(A|B) vs P(B|A) on drill 2"]

Next week's focus (Oct 26–Nov 1):
- [ ] Puzzles 4–7 (HH vs HT, Gambler's Ruin, Two Envelopes, Biased→Fair Coin)
- [ ] More Bayes drills
- [ ] Start Python (Black-Scholes from scratch)

Hours logged this week: __
```

---

## 4️⃣ Block D — Memorization Checklist (20 min)

Recite from memory, no peeking:

1. **Bayes' Theorem:** `P(A|B) = P(B|A)·P(A) / P(B)` ✓
2. **Medical test template:** prevalence 1%, sens 99%, FPR 5% → P(D|Pos) ≈ 16.7% ✓
3. **Linearity of expectation:** `E[X+Y] = E[X] + E[Y]` — ALWAYS true ✓
4. **Indicator variable trick:** `E[I] = P(event)` ✓
5. **Fixed points result:** expected fixed points in random permutation = **1** ✓
6. **Distribution means/variances:**
   - Bernoulli(p): mean p, var p(1−p) ✓
   - Binomial(n,p): mean np, var np(1−p) ✓
   - Geometric(p): mean 1/p, var (1−p)/p² ✓
   - Poisson(λ): mean λ, var λ ✓
7. **Memoryless property:** Geometric and Exponential only ✓

**If you can't recite all 7 cold:** spend another 10 minutes on the weak ones.

---

## 5️⃣ Block E — Week 2 Preview (10 min)

Monday Oct 26 starts with **Puzzles 4–7** plus more Bayes/conditional probability drills. Quick preview:

| Puzzle | Concept | Page |
|--------|---------|------|
| 4. HH vs HT | State equations / expected waiting time | `03_Puzzles/puzzles.md` |
| 5. Gambler's Ruin | Absorption probability | `03_Puzzles/puzzles.md` |
| 6. Two Envelopes | EV paradox / prior dependence | `03_Puzzles/puzzles.md` |
| 7. Biased→Fair Coin | von Neumann trick | `03_Puzzles/puzzles.md` |

Also: `01_Concepts/probability.md` has more drill problems if you want extra practice.

---

## 6️⃣ Block F — Commit & Push (10 min)

```
git add Quant_Intern_Prep/
git commit -m "Day 3 weekly review (Sun Oct 25, 2026)"
git push origin main
```

---

## ✅ End-of-Day Checklist (today)

- [ ] All 9 drills re-done correctly
- [ ] Puzzles 1–3 explained out loud without notes
- [ ] Weekly review filled in `06_Tracker/weekly_review.md`
- [ ] Memorization checklist recited cold (all 7 items)
- [ ] Committed and pushed to GitHub

---

**Week 1 is halfway done. You've built the probability foundation — now lock it in. Monday we start Puzzles 4–7.**

*Updated: Oct 25, 2026*