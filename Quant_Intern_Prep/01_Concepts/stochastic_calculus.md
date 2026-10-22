# ⚡ Stochastic Calculus — Optional Intro

**Only needed if targeting quant *research* internships.** Trader roles usually skip this. Skim unless the job description mentions Brownian motion, Itô, or Black-Scholes derivation.

---

## 1. Brownian Motion (Wiener Process) Wₜ

Properties:
- W₀ = 0.
- Independent increments: Wₜ − Wₛ independent of history up to s (t > s).
- Normal increments: Wₜ − Wₛ ~ Normal(0, t−s).
- Continuous paths, nowhere differentiable.

---

## 2. Itô Process

```
dXₜ = μ(Xₜ,t)dt + σ(Xₜ,t)dWₜ
```
- drift term: μdt
- diffusion term: σdWₜ

---

## 3. Itô's Lemma (the chain rule for stochastic processes)

If Xₜ is an Itô process and f(t,x) is twice-differentiable:

```
df(t,Xₜ) = [∂f/∂t + μ·∂f/∂x + (1/2)σ²·∂²f/∂x²]dt + σ·∂f/∂x·dWₜ
```

**Key insight:** the (dWₜ)² = dt term creates the second-order correction. This is why option gamma matters.

---

## 4. Geometric Brownian Motion (GBM)

Stock price model:
```
dSₜ = μSₜdt + σSₜdWₜ
```
Solution:
```
Sₜ = S₀·exp((μ − σ²/2)t + σWₜ)
```
- log(Sₜ/S₀) ~ Normal((μ − σ²/2)t, σ²t).

---

## 5. Black-Scholes PDE (conceptual)

For option price V(S,t):
```
∂V/∂t + (1/2)σ²S²·∂²V/∂S² + rS·∂V/∂S − rV = 0
```
Boundary condition: V(S,T) = payoff at expiry.

---

## 6. What to Remember for Interviews

| Concept | One-line takeaway |
|---------|-------------------|
| Brownian motion | random walk with normal increments, continuous |
| Itô's lemma | chain rule + (dW)² = dt correction |
| GBM | stock price model; log-returns are Normal |
| Black-Scholes | PDE for option pricing; inputs: S, K, T, r, σ |

**Honest advice:** If you're short on time (you are — it's October), prioritize probability puzzles + coding over this. Most quant *trading* intern interviews don't ask Itô's lemma.

---

*Next: [`02_Coding/python_quant.md`](./../02_Coding/python_quant.md)*