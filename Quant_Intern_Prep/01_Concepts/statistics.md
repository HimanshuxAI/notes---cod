# 📊 Statistics for Quant Interviews

Quant interviews test statistical intuition more than formal proofs. Focus on distributions, the CLT, and reading data quickly.

---

## 1. Descriptive Statistics

| Measure | Formula | Note |
|---------|---------|------|
| Mean | Σxᵢ/n | sensitive to outliers |
| Median | middle value (sorted) | robust to outliers |
| Variance | Σ(xᵢ−x̄)²/(n−1) | sample uses n−1 |
| Std dev | √variance | same units as data |
| Skewness | E[(X−μ)³]/σ³ | >0 right-skewed, <0 left |
| Kurtosis | E[(X−μ)⁴]/σ⁴ | >3 heavy-tailed |

**IQR** = Q3 − Q1. Outliers often defined as < Q1−1.5·IQR or > Q3+1.5·IQR.

---

## 2. Probability Distributions (deep dive)

### Binomial(n, p)
- n independent Bernoulli trials, probability p of success.
- Use when: fixed number of trials, constant p, binary outcome.
- Mean np, Var np(1−p).

### Poisson(λ)
- Count of rare events in fixed interval, average rate λ.
- Mean λ, Var λ. Approximates Binomial when n large, p small, λ = np.

### Normal(μ, σ²)
- Bell curve. Sum of many independent variables → Normal (CLT).
- Standard Normal Z = (X−μ)/σ.
- Empirical rule: ~68% within 1σ, ~95% within 2σ, ~99.7% within 3σ.

### Exponential(λ)
- Time between Poisson events. Memoryless.
- Mean 1/λ, Var 1/λ².

### Uniform(a, b)
- All values equally likely. Mean (a+b)/2, Var (b−a)²/12.

---

## 3. Central Limit Theorem (CLT)

> The sample mean of n i.i.d. variables (finite mean μ, variance σ²) approaches Normal(μ, σ²/n) as n → ∞.

**Interview use:** approximate distribution of sums/averages, compute probabilities of sample means, justify Normal models for P&L over many trades.

Rule of thumb: n ≥ 30 often "good enough," but heavier tails need more.

---

## 4. Hypothesis Testing Basics

| Concept | Meaning |
|---------|---------|
| Null H₀ | "no effect / status quo" |
| Alternative H₁ | what you're testing for |
| p-value | P(observed data or more extreme \| H₀ true) |
| Significance α | threshold (usually 0.05); reject H₀ if p < α |
| Type I error | false positive (reject true H₀) |
| Type II error | false negative (fail to reject false H₀) |
| Power | 1 − P(Type II) |

**Confidence interval:** x̄ ± z·(σ/√n) for 95% CI (z ≈ 1.96).

**Interview trap:** p-value is NOT P(H₀ is true). It's P(data \| H₀).

---

## 5. Correlation vs Causation

- **Correlation** measures linear association (−1 to 1).
- Zero correlation ≠ independence (except for jointly Normal variables).
- **Simpson's paradox:** a trend appears in groups but reverses when combined. Always check for confounding variables.

---

## 6. Quick Statistical Intuition Checks

- If data is right-skewed: Mean > Median > Mode.
- Adding a constant shifts mean/median but not variance/std dev.
- Multiplying by c scales mean by c, variance by c².
- Standard error of the mean = σ/√n — shrinks as sample grows.
- For Normal data, ~95% of observations lie within μ ± 2σ.

---

*Next: [`linear_algebra.md`](./linear_algebra.md)*