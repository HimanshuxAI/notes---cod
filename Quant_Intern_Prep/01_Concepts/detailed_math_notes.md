# 📐 Detailed Math Notes for Quant Interviews

**Purpose:** Deep-dive reference for the math behind quant trading/research interviews.  
**Priority:** Probability & Expectation > Distributions > Linear Algebra > Calculus.  
**Style:** Derivations included, interview traps highlighted, worked examples throughout.

---

## PART 1 — PROBABILITY (The #1 Interview Topic)

Quant interviews are won or lost on probability. You must be able to set up the sample space, condition correctly, and compute expectations under pressure.

---

### 1.1 Axioms & Definitions

**Sample space Ω:** Set of all possible outcomes.
**Event E:** A subset of Ω.
**Probability function P:** Maps events to [0,1] satisfying:
1. P(Ω) = 1
2. P(E) ≥ 0 for all E
3. Countable additivity: if E₁, E₂, ... are disjoint, P(∪Eᵢ) = ΣP(Eᵢ)

**Complement:** P(Eᶜ) = 1 − P(E)  
**Union:** P(A ∪ B) = P(A) + P(B) − P(A ∩ B)  
**Inclusion-Exclusion (3 events):**
P(A ∪ B ∪ C) = P(A) + P(B) + P(C) − P(A∩B) − P(A∩C) − P(B∩C) + P(A∩B∩C)

---

### 1.2 Conditional Probability

**Definition:**
```
P(A|B) = P(A ∩ B) / P(B),   provided P(B) > 0
```

**Interpretation:** Restrict the sample space to only outcomes where B occurred. Within that reduced space, what fraction also has A?

**Multiplication Rule (Chain Rule):**
```
P(A ∩ B) = P(A|B)·P(B) = P(B|A)·P(A)
P(A ∩ B ∩ C) = P(A)·P(B|A)·P(C|A∩B)
```

**Example — Drawing without replacement:**
Urn: 3 red, 2 blue. Draw 2 cards without replacement. P(both red)?

Method 1 (multiplication rule):
- P(1st red) = 3/5
- P(2nd red | 1st red) = 2/4 = 1/2
- P(both red) = (3/5)·(1/2) = 3/10

Method 2 (combinations):
- C(3,2) / C(5,2) = 3 / 10 ✓

---

### 1.3 Bayes' Theorem (The Workhorse)

**Derivation:**
```
P(A|B) = P(A∩B)/P(B)
P(B|A) = P(A∩B)/P(A)  →  P(A∩B) = P(B|A)·P(A)
Therefore: P(A|B) = P(B|A)·P(A) / P(B)
```

**Extended form (law of total probability in denominator):**
```
P(A|B) = P(B|A)·P(A) / [P(B|A)·P(A) + P(B|Aᶜ)·P(Aᶜ)]
```

**Tree diagram method (use this in interviews — it prevents errors):**
1. First-level branches: A vs Aᶜ with prior probabilities.
2. Second-level branches from each: B vs Bᶜ with conditional probabilities.
3. Multiply along paths to get joint probabilities.
4. P(A|B) = (joint prob of A∩B path) / (sum of all joint probs ending at B).

**Example — Medical Test (memorize this template):**
- Disease prevalence P(D) = 0.01
- Sensitivity P(Pos|D) = 0.99
- False positive rate P(Pos|¬D) = 0.05
- **Q:** Test positive. P(D|Pos)?

```
P(D|Pos) = 0.99 × 0.01 / [0.99×0.01 + 0.05×0.99]
         = 0.0099 / [0.0099 + 0.0495]
         = 0.0099 / 0.0594
         ≈ 0.1667 → 16.7%
```

**Trap:** Most people intuitively say ~99%. Wrong. Base rate (prevalence) dominates when the condition is rare.

---

### 1.4 Independence

**Definition:** A and B are independent iff P(A∩B) = P(A)·P(B).

**Consequences:**
- P(A|B) = P(A) (if P(B) > 0) — knowing B tells you nothing about A.
- P(A∩B∩C) = P(A)P(B)P(C) for mutually independent events.

**Trap — Pairwise ≠ Mutual Independence:**
Three events can be pairwise independent but not mutually independent.
Example: Flip two fair coins. 
- A = first coin heads
- B = second coin heads  
- C = coins match (both same)
P(A)=P(B)=P(C)=0.5. Pairwise: P(A∩B)=0.25=P(A)P(B) ✓, etc. But P(A∩B∩C)=P(HH)=0.25, while P(A)P(B)P(C)=0.125. Not mutually independent.

---

### 1.5 Total Probability

If B₁, B₂, ..., Bₙ form a partition of Ω (disjoint, cover everything):
```
P(A) = Σ P(A|Bᵢ)·P(Bᵢ)
```
Use this when you can break a problem into mutually exclusive cases.

**Example:** Two factories produce widgets. Factory 1: 60% of output, 2% defective. Factory 2: 40% of output, 5% defective. P(random widget defective)?
```
P(Def) = 0.02×0.60 + 0.05×0.40 = 0.012 + 0.020 = 0.032 → 3.2%
```

---

## PART 2 — RANDOM VARIABLES, EXPECTATION, VARIANCE

This is the single most-tested topic. Master it cold.

---

### 2.1 Random Variables

**Discrete RV:** Takes countable values. Described by PMF: p(x) = P(X=x), with Σp(x) = 1.
**Continuous RV:** Takes uncountable values. Described by PDF: f(x), with ∫f(x)dx = 1, and P(a≤X≤b) = ∫ₐᵇ f(x)dx.

**CDF:** F(x) = P(X ≤ x). Always: 0 ≤ F ≤ 1, non-decreasing, F(−∞)=0, F(∞)=1.
- For discrete: F(x) = Σ_{t≤x} p(t) (step function)
- For continuous: F(x) = ∫₋∞ˣ f(t)dt, and f(x) = F'(x)

---

### 2.2 Expectation (Expected Value)

**Definition:**
```
E[X] = Σ x·p(x)     (discrete)
E[X] = ∫ x·f(x)dx   (continuous)
```

**Intuition:** Long-run average over many repetitions. The "center of mass" of the distribution.

**Example — Fair die:**
```
E[X] = (1+2+3+4+5+6)/6 = 21/6 = 3.5
```
Note: 3.5 is not a possible outcome. Expectation need not be achievable.

**Example — Bernoulli(p):** X = 1 with prob p, 0 with prob 1−p.
```
E[X] = 1·p + 0·(1−p) = p
```

---

### 2.3 Linearity of Expectation — THE Interview Trick

```
E[X + Y] = E[X] + E[Y]          ALWAYS true
E[aX + bY + c] = a·E[X] + b·E[Y] + c
```

**Crucial:** X and Y do NOT need to be independent. This is what makes it powerful.

**Indicator Variables:**
For any event E, define I_E = 1 if E happens, 0 otherwise.
```
E[I_E] = 1·P(E) + 0·P(Eᶜ) = P(E)
```

**Classic Example — Fixed points in random permutation:**
n items randomly permuted. X = number of items in their original position.
- Let Iᵢ = 1 if item i stays in position i, else 0.
- P(item i in position i) = 1/n → E[Iᵢ] = 1/n.
- X = I₁ + I₂ + ... + Iₙ.
- E[X] = Σ E[Iᵢ] = n × (1/n) = **1**.

Answer: Expected fixed points = 1, regardless of n.

**Another Example — Expected number of heads in n coin flips (not necessarily fair):**
- Iⱼ = 1 if flip j is heads, with P(H) = pⱼ.
- E[#heads] = Σ pⱼ. If all fair: np.

---

### 2.4 Variance & Standard Deviation

**Definition:**
```
Var(X) = E[(X − E[X])²] = E[X²] − (E[X])²
SD(X) = σ = √Var(X)
```

**Properties:**
| Property | Formula |
|----------|---------|
| Var(aX + b) | a²·Var(X) |
| Var(X + Y) | Var(X) + Var(Y) + 2·Cov(X,Y) |
| If X ⟂ Y (independent) | Var(X+Y) = Var(X) + Var(Y) |
| Cov(X,X) | Var(X) |
| Corr(X,Y) | Cov(X,Y) / (σ_X·σ_Y), range [−1,1] |

**Example — Bernoulli(p):**
```
E[X] = p
E[X²] = 1²·p + 0²·(1−p) = p
Var(X) = p − p² = p(1−p)
```

**Example — Fair die:**
```
E[X] = 3.5
E[X²] = (1+4+9+16+25+36)/6 = 91/6 ≈ 15.167
Var(X) = 91/6 − (7/2)² = 91/6 − 49/4 = (182 − 147)/12 = 35/12 ≈ 2.917
```

---

### 2.5 Conditional Expectation

**Definition:** E[X|Y=y] = expected value of X given Y=y.

**Tower Property (Law of Total Expectation):**
```
E[X] = E[E[X|Y]]
```
Meaning: average the conditional expectations over the distribution of Y.

**Example:** Roll a die. X = outcome. Y = "even or odd."
- E[X|Y=even] = (2+4+6)/3 = 4
- E[X|Y=odd] = (1+3+5)/3 = 3
- E[X] = 4×P(even) + 3×P(odd) = 4×0.5 + 3×0.5 = 3.5 ✓

**Use in interviews:** Break complex expectations into cases using conditional expectation.

---

## PART 3 — COMMON DISTRIBUTIONS (MEMORIZE MEAN & VARIANCE)

| Dist. | Notation | PMF/PDF | Mean | Variance | Use Case |
|-------|----------|---------|------|----------|----------|
| Bernoulli | X~Bern(p) | P(X=1)=p | p | p(1−p) | Single yes/no trial |
| Binomial | X~Bin(n,p) | C(n,k)pᵏ(1−p)ⁿ⁻ᵏ | np | np(1−p) | n independent yes/no trials |
| Geometric | X~Geom(p) | (1−p)ᵏ⁻¹·p | 1/p | (1−p)/p² | Trials until first success |
| Poisson | X~Poi(λ) | e⁻ᵟλᵏ/k! | λ | λ | Rare events over fixed interval |
| Uniform | X~Unif(a,b) | 1/(b−a) | (a+b)/2 | (b−a)²/12 | Random number in range |
| Exponential | X~Exp(λ) | λe⁻ˡˣ | 1/λ | 1/λ² | Time between events |
| Normal | X~N(μ,σ²) | bell curve | μ | σ² | Sums of many variables |

**Memoryless Property:** Geometric and Exponential only.
```
P(X > s+t | X > s) = P(X > t)
```
This means the process "forgets" how long you've already waited.

**Poisson approximation to Binomial:** If n large, p small, λ=np moderate → Bin(n,p) ≈ Poi(λ).

**Normal approximation to Binomial:** If n large → Bin(n,p) ≈ N(np, np(1−p)).

---

## PART 4 — LINEAR ALGEBRA

You need 2×2 and 3×3 fluency, not proofs.

---

### 4.1 Matrix Operations

**Multiplication (A·B):** (i,j) entry = row i of A dotted with column j of B.
- A is m×n, B is n×p → AB is m×p.
- **NOT commutative:** AB ≠ BA generally.

**Transpose (Aᵀ):** Swap rows/columns. (AB)ᵀ = BᵀAᵀ.

**Identity (I):** 1s on diagonal. AI = IA = A.

**Inverse (A⁻¹):** Exists iff A square and det(A) ≠ 0. AA⁻¹ = I.
- 2×2 formula: [[a,b],[c,d]]⁻¹ = (1/(ad−bc)) · [[d,−b],[−c,a]]

**Determinant:**
- 2×2 [[a,b],[c,d]]: det = ad − bc
- 3×3: cofactor expansion or Sarrus' rule
- det(AB) = det(A)det(B); det(Aᵀ) = det(A)

---

### 4.2 Vectors

**Dot product:** u·v = Σuᵢvᵢ = |u||v|cos(θ). Orthogonal ⟺ u·v = 0.
**Cross product (3D):** u × v, perpendicular to both, |u×v| = |u||v|sin(θ).
**Norm:** ||v|| = √(Σvᵢ²) (Euclidean/L2).

---

### 4.3 Eigenvalues & Eigenvectors

```
A·v = λ·v
```
λ = eigenvalue, v = eigenvector (nonzero).

**Find λ:** Solve det(A − λI) = 0 (characteristic equation).

**Key facts:**
- Trace(A) = sum of diagonal = sum of eigenvalues
- Det(A) = product of eigenvalues
- Symmetric matrices → real eigenvalues, orthogonal eigenvectors
- Positive definite: xᵀAx > 0 for all x ≠ 0 (all eigenvalues > 0)

**Example — Eigenvalues of [[3,1],[1,3]]:**
```
det([[3−λ, 1],[1, 3−λ]]) = (3−λ)² − 1 = 0
(3−λ)² = 1 → 3−λ = ±1 → λ = 2 or λ = 4
```
Eigenvalues: 2, 4. Trace = 6 = 2+4 ✓. Det = 8 = 2×4 ✓.

---

### 4.4 Special Matrices

| Type | Property | Use |
|------|----------|-----|
| Symmetric | A = Aᵀ | Covariance matrices |
| Diagonal | Nonzero only on diagonal | Easy powers/inverses |
| Orthogonal | AᵀA = I | Rotations, preserve length |
| Positive Definite | xᵀAx > 0 ∀x≠0 | Valid covariance, convex opt |
| Idempotent | A² = A | Projection matrices |

---

## PART 5 — CALCULUS

Focus on derivatives, integrals, optimization.

---

### 5.1 Derivatives (Know Cold)

| Function | Derivative |
|----------|------------|
| xⁿ | n·xⁿ⁻¹ |
| eˣ | eˣ |
| ln x | 1/x |
| sin x | cos x |
| cos x | −sin x |
| f·g | f'g + fg' (product) |
| f/g | (f'g − fg')/g² (quotient) |
| f(g(x)) | f'(g(x))·g'(x) (chain) |

**Second derivative:** f'' tells concavity. f'(x)=0 + f''(x)>0 → local min; f''<0 → local max.

---

### 5.2 Integrals

**Fundamental Theorem:** ∫ₐᵇ f(x)dx = F(b) − F(a) where F' = f.

**Integration by parts:** ∫u dv = uv − ∫v du.

**Example:** ∫₀¹ x·eˣ dx
- u = x, dv = eˣdx → du = dx, v = eˣ
- = [x·eˣ]₀¹ − ∫₀¹ eˣdx = e − (e − 1) = **1**

---

### 5.3 Taylor Series (Small-x Approximations)

```
eˣ ≈ 1 + x + x²/2 + x³/6
ln(1+x) ≈ x − x²/2 + x³/3
sin x ≈ x − x³/6
cos x ≈ 1 − x²/2
(1+x)ⁿ ≈ 1 + nx
```

**Interview use:** First-order Taylor ≈ linear approximation. Option delta = first derivative of price w.r.t. spot.

---

### 5.4 Optimization (Lagrange Multipliers — know setup)

Maximize f(x,y) subject to g(x,y) = c:
```
∇f = λ·∇g,   g(x,y) = c
```
Solve the system. Used in portfolio optimization (maximize return subject to risk constraint).

---

### 5.5 L'Hôpital's Rule

If lim f/g is 0/0 or ∞/∞:
```
lim f/g = lim f'/g'
```
Repeat if still indeterminate.

**Example:** limₓ→₀ (sin x)/x = limₓ→₀ (cos x)/1 = 1.

---

## PART 6 — WORKED INTERVIEW EXAMPLES

---

### Example 1 — Expected Value with States

**Problem:** Flip a fair coin. Expected flips to get two heads in a row (HH)?

**Solution:** Set up state equations.
- E = expected flips from start
- E_H = expected additional flips given last flip was H

From start:
```
E = 1 + 0.5·E + 0.5·E_H      (flip T: back to start; flip H: state H)
```

From state H:
```
E_H = 1 + 0.5·0 + 0.5·E_H    (flip H: done; flip T: back to start)
    = 1 + 0.5·E_H
    → 0.5·E_H = 1 → E_H = 2
```

Substitute:
```
E = 1 + 0.5E + 0.5(2) = 1 + 0.5E + 1 = 2 + 0.5E
→ 0.5E = 2 → E = 4
```

Wait — that's wrong. Let me redo carefully.

From start:
- Flip H (prob 0.5): now in state H, used 1 flip
- Flip T (prob 0.5): back to start, used 1 flip
```
E = 1 + 0.5·E_H + 0.5·E
```

From state H (last flip was H):
- Flip H (prob 0.5): done! total additional = 1
- Flip T (prob 0.5): back to start, used 1 flip
```
E_H = 1 + 0.5·0 + 0.5·E = 1 + 0.5E
```

Substitute E_H into first:
```
E = 1 + 0.5(1 + 0.5E) + 0.5E
E = 1 + 0.5 + 0.25E + 0.5E
E = 1.5 + 0.75E
0.25E = 1.5
E = 6
```

**Answer: 6 flips.** (Compare: HT = 4 flips.)

---

### Example 2 — Gambler's Ruin

**Problem:** You start with \$i, opponent with \$N−i. Each round you win \$1 with prob p, lose with q=1−p. P(you reach N before 0)?

**Solution:** Let Pᵢ = probability of reaching N starting from i.
Boundary: P₀ = 0, P_N = 1.
Recurrence: Pᵢ = p·Pᵢ₊₁ + q·Pᵢ₋₁.

If p = q = 0.5: **Pᵢ = i/N** (linear).
If p ≠ 0.5: **Pᵢ = (1 − (q/p)ⁱ) / (1 − (q/p)ᴺ)**

**Intuition:** If p > 0.5 (favorable), probability rises faster than linear.

---

### Example 3 — Put-Call Parity

**European options, no dividends:**
```
C + K·e^(−rT) = P + S
```
Where C=call, P=put, S=spot, K=strike, r=risk-free rate, T=time to expiry.

**Use:** Given any 5 of {C, P, S, K, r, T}, solve for the 6th.

**Example:** C = 5, S = 100, K = 100, r = 5%, T = 1. Find P.
```
P = C + K·e^(−rT) − S = 5 + 100·e^(−0.05) − 100
e^(−0.05) ≈ 0.9512
P = 5 + 95.12 − 100 = 0.12
```

---

## PART 7 — COMMON INTERVIEW TRAPS & HOW TO AVOID THEM

| Trap | Correct Approach |
|------|------------------|
| Confusing P(A\|B) with P(B\|A) | Write Bayes explicitly; use tree diagram |
| Assuming independence when not stated | Check: does knowing A change P(B)? |
| Forgetting base rates | Always include prior P(A) in Bayes |
| Using E[X²] = (E[X])² | Wrong! Var(X) = E[X²] − (E[X])² ≠ 0 generally |
| Linearity only for independent variables | **False** — linearity always holds |
| Normal approximation for small n | Need n ≥ ~30, more if skewed |
| p-value = P(null true) | **False** — p-value = P(data \| null) |

---

## PART 8 — 7-DAY MEMORY DRILL PLAN

| Day | Focus |
|-----|-------|
| Day 1 | Bayes + conditional probability (tree diagrams) |
| Day 2 | Expectation + linearity + indicator variables |
| Day 3 | Variance + common distributions (memorize table) |
| Day 4 | Linear algebra (2×2 ops, eigenvalues) |
| Day 5 | Calculus (derivatives, Taylor, optimization setup) |
| Day 6 | Mixed probability puzzles (timed) |
| Day 7 | Full review + weak spots |

**Recite cold each morning:** Bayes formula, linearity property, Bernoulli/Binomial/Geometric/Poisson mean & variance, fixed-points result = 1.

---

*File location: Quant_Intern_Prep/01_Concepts/detailed_math_notes.md*  
*Updated: Oct 25, 2026*