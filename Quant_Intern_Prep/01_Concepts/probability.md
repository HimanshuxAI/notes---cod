# 🎲 Probability for Quant Interviews

**Core idea:** Quant interviews are largely probability puzzles dressed up as brainteasers. Master the basics, then solve problems fast.

---

## 1. Foundations

### Sample space & events
- **Sample space Ω:** set of all possible outcomes.
- **Event:** a subset of Ω.
- **Probability:** P(A) = (favorable outcomes) / (total outcomes), assuming equally likely.

### Conditional probability
```
P(A|B) = P(A ∩ B) / P(B)
```
"The probability of A given B has occurred."

### Bayes' Theorem
```
P(A|B) = P(B|A)·P(A) / P(B)
        = P(B|A)·P(A) / [P(B|A)·P(A) + P(B|¬A)·P(¬A)]
```
**Classic quant interview use:** medical test false positives, coin bias given observed flips, Monty Hall variants.

### Independence
- A and B independent ⟺ P(A ∩ B) = P(A)·P(B).
- **Careful:** pairwise independence ≠ mutual independence (3+ events).

---

## 2. Random Variables & Expectation

### Expectation (mean)
```
E[X] = Σ x·P(X=x)   (discrete)
E[X] = ∫ x·f(x) dx  (continuous)
```

### Linearity of expectation (the #1 interview trick)
```
E[X + Y] = E[X] + E[Y]   — ALWAYS true, even if X and Y are dependent!
```
Use this to avoid computing joint distributions. Example: expected number of fixed points in a random permutation.

### Variance & standard deviation
```
Var(X) = E[X²] − (E[X])²
Var(aX + b) = a²·Var(X)
Var(X + Y) = Var(X) + Var(Y) + 2·Cov(X,Y)
```
If X, Y independent: Var(X+Y) = Var(X) + Var(Y).

### Covariance & correlation
```
Cov(X,Y) = E[(X−E[X])(Y−E[Y])] = E[XY] − E[X]E[Y]
Corr(X,Y) = Cov(X,Y) / (σ_X · σ_Y),   range [−1, 1]
```

### Conditional expectation
```
E[X] = E[E[X|Y]]   (tower property / law of total expectation)
```

---

## 3. Common Distributions (know PMF/PDF, mean, variance)

| Distribution | PMF/PDF | Mean | Variance | When it appears |
|-------------|---------|------|----------|-----------------|
| **Bernoulli(p)** | P(X=1)=p | p | p(1−p) | single coin flip |
| **Binomial(n,p)** | C(n,k)·pᵏ(1−p)ⁿ⁻ᵏ | np | np(1−p) | n coin flips |
| **Geometric(p)** | (1−p)ᵏ⁻¹·p | 1/p | (1−p)/p² | trials until first success |
| **Poisson(λ)** | e⁻ᵟ·λᵏ/k! | λ | λ | rare events over time |
| **Uniform(a,b)** | 1/(b−a) | (a+b)/2 | (b−a)²/12 | continuous range |
| **Exponential(λ)** | λe⁻ˡˣ | 1/λ | 1/λ² | time between events |
| **Normal(μ,σ²)** | (1/σ√2π)·e^{−(x−μ)²/2σ²} | μ | σ² | sums of many variables |

**Memoryless property:** Geometric and Exponential — P(X > s+t | X > s) = P(X > t).

---

## 4. Classic Interview Problem Patterns

### A. Expected value with states (gambler's ruin / random walks)
Set up equations: E = 1 + Σ pᵢ·Eᵢ. Solve the linear system.

### B. Conditional probability with Bayes
Draw a tree. Label each node with probabilities. Compute numerator and denominator explicitly.

### C. Linearity of expectation with indicator variables
Define Iⱼ = 1 if event j happens, 0 otherwise. E[#events] = Σ E[Iⱼ] = Σ P(event j).

### D. Symmetry arguments
If the setup is symmetric, all positions/players are equally likely. Often avoids messy computation.

---

## 5. Must-Know Puzzles (see `03_Puzzles/puzzles.md`)

1. Two children problem (boy/girl paradox)
2. Monty Hall / 100 doors
3. Ants on a plank / elastic collisions
4. Expected number of coin flips to get HH vs HT
5. Gambler's ruin / random walk absorption
6. Envelope paradox / two envelopes
7. 100 prisoners and a light bulb (advanced)
8. Bayes: biased coin given k heads in n flips

---

## 6. 5-Minute Drill (do before every interview)

1. Compute P(A∪B), P(A∩B), P(A|B) from a word problem — under 60 seconds.
2. Apply Bayes to a false-positive scenario.
3. Use linearity of expectation on an indicator-variable problem.
4. Identify the distribution: Binomial vs Poisson vs Geometric.
5. Compute Var(X+Y) for independent and correlated cases.

---

*Next: [`statistics.md`](./statistics.md)*