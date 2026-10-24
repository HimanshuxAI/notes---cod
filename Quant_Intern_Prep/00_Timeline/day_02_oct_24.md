# 📅 Day 2 — Saturday, Oct 24, 2026

**Goal:** Master random variables, expectation, variance, and the common distributions.  
**Time budget:** 2–3 hours.  
**Today is the highest-ROI day of Week 1** — expectation and linearity show up in almost every quant interview.

---

## 🕒 Time-Blocked Schedule

| Block | Time | Task |
|-------|------|------|
| A | 60 min | Random variables, expectation, variance (notes below + 5 drills) |
| B | 10 min | Mental math warmup |
| C | 40 min | Common distributions — memorize mean/variance table + 3 drills |
| D | 20 min | Linearity of expectation with indicator variables (the interview trick) |
| E | 10 min | End-of-day checklist + log in tracker |

> If short on time: do Block A (45 min) + Block D (25 min). Skip Block C details, just skim the table.

---

## 1️⃣ Random Variables

A random variable (RV) assigns a number to each outcome in the sample space.

| Type | Example |
|------|---------|
| **Discrete** | Coin flips (0 or 1), die roll (1–6), number of heads in 10 flips |
| **Continuous** | Height, stock price, time until next bus |

### PMF vs PDF
- **Discrete:** PMF `P(X = x)` — probability X equals exactly x. Sums to 1.
- **Continuous:** PDF `f(x)` — probability is area under curve. `P(a ≤ X ≤ b) = ∫ₐᵇ f(x)dx`. `P(X = exactly x) = 0`.

### CDF
`F(x) = P(X ≤ x)` — works for both discrete and continuous. Always non-decreasing, 0 → 1.

---

## 2️⃣ Expectation (Expected Value)

```
E[X] = Σ x·P(X=x)        (discrete)
E[X] = ∫ x·f(x) dx       (continuous)
```

**Intuition:** Long-run average value if you repeat the experiment many times.

### Example: fair die
```
E[X] = (1+2+3+4+5+6)/6 = 21/6 = 3.5
```
Note: 3.5 is not a possible outcome. Expectation doesn't have to be achievable.

### Example: Bernoulli(p) — one coin flip, X = 1 if heads
```
E[X] = 1·p + 0·(1-p) = p
```

---

## 3️⃣ Linearity of Expectation — THE Interview Trick

```
E[X + Y] = E[X] + E[Y]
```
**ALWAYS true**, even if X and Y are dependent (not independent).

This is the #1 trick in quant interviews. It lets you compute expected values without knowing joint distributions.

### Indicator Variables
Define `I = 1` if event happens, `0` otherwise. Then `E[I] = P(event happens)`.

**Classic example:** Expected number of fixed points in a random permutation of n items.
- Let `Iᵢ = 1` if item i ends up in position i, else 0.
- `P(item i in position i) = 1/n`, so `E[Iᵢ] = 1/n`.
- Total fixed points `X = I₁ + ... + Iₙ`.
- `E[X] = Σ E[Iᵢ] = n · (1/n) = 1`.

**Answer: 1.** No matter how large n is, expected fixed points = 1.

---

## 4️⃣ Variance & Standard Deviation

```
Var(X) = E[X²] − (E[X])²
SD(X) = √Var(X) = σ
```

### Key properties
| Property | Formula |
|----------|---------|
| Var(aX + b) | a²·Var(X) |
| Var(X + Y) | Var(X) + Var(Y) + 2·Cov(X,Y) |
| If X, Y independent | Var(X+Y) = Var(X) + Var(Y) |
| Cov(X,X) | Var(X) |
| Corr(X,Y) | Cov(X,Y)/(σ_X·σ_Y), range [−1, 1] |

### Example: Bernoulli(p)
```
E[X] = p
E[X²] = 1²·p + 0²·(1-p) = p
Var(X) = p − p² = p(1−p)
```

---

## 5️⃣ Common Distributions — Memorize Mean & Variance

| Distribution | PMF/PDF | Mean | Variance | When it appears |
|-------------|---------|------|----------|-----------------|
| **Bernoulli(p)** | P(X=1)=p | p | p(1−p) | single coin flip |
| **Binomial(n,p)** | C(n,k)·pᵏ(1−p)ⁿ⁻ᵏ | np | np(1−p) | n independent coin flips |
| **Geometric(p)** | (1−p)ᵏ⁻¹·p | 1/p | (1−p)/p² | flips until first heads |
| **Poisson(λ)** | e⁻ᵟ·λᵏ/k! | λ | λ | rare events over time |
| **Uniform(a,b)** | 1/(b−a) | (a+b)/2 | (b−a)²/12 | random number in range |
| **Exponential(λ)** | λe⁻ˡˣ | 1/λ | 1/λ² | time between events |
| **Normal(μ,σ²)** | bell curve | μ | σ² | sums of many variables |

**Memoryless property:** Geometric and Exponential — `P(X > s+t | X > s) = P(X > t)`.

---

## 6️⃣ Five Drills (do before moving on)

**Drill 1:** X ~ Bernoulli(0.3). E[X]? Var(X)?  
**Drill 2:** Roll a fair die. E[X]? E[X²]? Var(X)?  
**Drill 3:** X ~ Binomial(10, 0.5). E[X]? Var(X)?  
**Drill 4:** Expected number of fixed points in random permutation of 5 items?  
**Drill 5:** Two independent RVs: Var(X)=4, Var(Y)=9. Var(X+Y)? Var(X−Y)?

<details>
<summary>Answers</summary>

1. E[X]=0.3, Var(X)=0.3×0.7=0.21  
2. E[X]=3.5, E[X²]=(1+4+9+16+25+36)/6=91/6≈15.17, Var=15.17−12.25=2.92 (35/12)  
3. E[X]=5, Var(X)=10×0.5×0.5=2.5  
4. Always 1 (linearity of expectation, n×(1/n))  
5. Var(X+Y)=13, Var(X−Y)=13 (independence kills covariance)
</details>

---

## 7️⃣ Mental Math Warmup (10 min)

Aloud, timed:

1. 29 × 31  
2. 45² (ends in 5: 4×5=20, append 25 → 2025)  
3. 12% of 350  
4. 1/7 as decimal (0.142857 repeating)  
5. 2¹⁰, 2²⁰

<details>
<summary>Answers</summary>
1. 899  
2. 2025  
3. 42  
4. 0.142857...  
5. 1024, ~1,048,576
</details>

---

## 8️⃣ End-of-Day Checklist

- [ ] I can define expectation and compute it for a die roll.
- [ ] I can state linearity of expectation and explain why it works even for dependent variables.
- [ ] I can set up an indicator variable and use it to find an expected count.
- [ ] I can recall mean & variance for Bernoulli, Binomial, Geometric, Poisson from memory.
- [ ] I know the memoryless property (Geometric & Exponential).
- [ ] I logged today in `06_Tracker/weekly_review.md` (Week 1, Fri Oct 24 row).

---

## 9️⃣ What's Next (Sunday Oct 25 — Weekly Review + Catch-up)

- Review everything from Days 1–2.
- Re-do any drill you got wrong.
- Puzzles 4–7 start Monday (HH vs HT, Gambler's Ruin, Two Envelopes, Biased→Fair Coin).
- Fill out the weekly review template honestly.

---

**Day 2 complete. Commit and push, then rest.**

*Updated: Oct 24, 2026*