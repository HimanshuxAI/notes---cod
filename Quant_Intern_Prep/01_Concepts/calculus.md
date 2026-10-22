# ∫ Calculus for Quant Interviews

Focus on derivatives, integrals, and optimization — the tools behind option pricing and backtests.

---

## 1. Derivatives

| Rule | Formula |
|------|---------|
| Power | d/dx[xⁿ] = n·xⁿ⁻¹ |
| Product | (fg)' = f'g + fg' |
| Quotient | (f/g)' = (f'g − fg')/g² |
| Chain | d/dx[f(g(x))] = f'(g(x))·g'(x) |
| Exponential | d/dx[eˣ] = eˣ; d/dx[aˣ] = aˣ·ln(a) |
| Logarithm | d/dx[ln x] = 1/x |
| Trig | d/dx[sin x] = cos x; d/dx[cos x] = −sin x |

### Higher derivatives
- f'' = second derivative (concavity/acceleration).
- f'(x) = 0 → critical point. f''(x) > 0 → local min; f''(x) < 0 → local max.

---

## 2. Integrals

| Rule | Formula |
|------|---------|
| Power | ∫xⁿdx = xⁿ⁺¹/(n+1) + C |
| Exponential | ∫eˣdx = eˣ + C |
| Log | ∫(1/x)dx = ln|x| + C |
| Trig | ∫sin x dx = −cos x + C |

### Definite integral
∫ₐᵇ f(x)dx = F(b) − F(a), where F' = f (Fundamental Theorem of Calculus).

### Integration by parts
∫u dv = uv − ∫v du

---

## 3. Optimization

### Unconstrained (one variable)
1. f'(x) = 0 → candidates.
2. Check endpoints of domain.
3. f'' sign or compare values → min/max.

### Constrained (Lagrange multipliers — know the setup)
Optimize f(x,y) subject to g(x,y) = c:
```
∇f = λ·∇g,   g(x,y) = c
```
Solve the system. Common in portfolio optimization.

---

## 4. Taylor Series

```
f(x) ≈ f(a) + f'(a)(x−a) + f''(a)(x−a)²/2! + ...
```
- **First-order approx:** f(x) ≈ f(a) + f'(a)(x−a) — used for option delta/gamma intuition.
- eˣ ≈ 1 + x + x²/2 + x³/6
- ln(1+x) ≈ x − x²/2 + x³/3 (for small x)
- sin x ≈ x − x³/6; cos x ≈ 1 − x²/2

---

## 5. L'Hôpital's Rule

If lim f(x)/g(x) is 0/0 or ∞/∞:
```
lim f(x)/g(x) = lim f'(x)/g'(x)
```
Repeat if still indeterminate.

---

## 6. Interview-Relevant Calculus Patterns

- **Derivative of an integral:** d/dx ∫ₐˣ f(t)dt = f(x) (FTC part 1).
- **Maximize expected log utility** → Kelly criterion setup.
- **Option pricing intuition:** derivative of option price w.r.t. spot = delta; second derivative = gamma.
- **Integration for expected value:** E[X] = ∫ x·f(x)dx over the PDF support.

---

## 7. 5-Minute Drill

1. d/dx[x³·e²ˣ] — product + chain.
2. ∫₀¹ x·eˣ dx — integration by parts.
3. Taylor: eˣ up to x³ term; approximate e⁰·¹.
4. Maximize f(x) = x(10−x) on [0,10].
5. limₓ→₀ (sin x)/x via L'Hôpital.

---

*Next: [`stochastic_calculus.md`](./stochastic_calculus.md) — optional intro (only if targeting research roles)*