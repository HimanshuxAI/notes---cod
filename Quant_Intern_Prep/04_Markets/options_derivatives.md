# 📈 Options & Derivatives for Quant Interviews

Trader intern interviews test options intuition. You don't need to derive Black-Scholes, but you must speak the language.

---

## 1. Option Basics

| Term | Meaning |
|------|---------|
| Call option | Right to BUY underlying at strike K |
| Put option | Right to SELL underlying at strike K |
| European | exercisable only at expiry |
| American | exercisable any time before expiry |
| Strike (K) | agreed buy/sell price |
| Spot (S) | current market price |
| Premium | price of the option |
| Maturity (T) | time to expiry |

### Moneyness
- **ITM (in the money):** call S > K / put S < K → intrinsic value > 0
- **ATM (at the money):** S ≈ K
- **OTM (out of the money):** call S < K / put S > K → intrinsic value = 0

### Payoff at expiry
- Call: max(S − K, 0)
- Put: max(K − S, 0)

---

## 2. Put–Call Parity (European, non-dividend)

```
C + K·e^(−rT) = P + S
```

- C = call price, P = put price
- Know how to rearrange: synthetic positions (e.g., long call + short put = long forward).
- **Interview use:** arbitrage bounds, pricing a put given a call.

---

## 3. The Greeks (intuition + formulas for Black-Scholes)

| Greek | Measures | Formula (BS call) | Intuition |
|-------|----------|-------------------|-----------|
| **Delta** Δ | ∂V/∂S | N(d₁) | price sensitivity to spot; hedge ratio |
| **Gamma** Γ | ∂²V/∂S² | N'(d₁)/(Sσ√T) | convexity; delta changes fastest ATM |
| **Theta** Θ | ∂V/∂t | ... | time decay (usually negative for longs) |
| **Vega** ν | ∂V/∂σ | S√T·N'(d₁) | volatility sensitivity |
| **Rho** ρ | ∂V/∂r | ... | interest-rate sensitivity |

**Key relationships:**
- Put delta = Call delta − 1
- Long gamma = long convexity (profits from big moves either way)
- ATM options have highest gamma and vega

---

## 4. Black-Scholes Inputs & Outputs

Inputs: S, K, T, r, σ (volatility), dividend yield q (optional).

Outputs: price, delta, gamma, vega, theta, rho.

**Volatility smile/skew:** OTM puts often have higher implied vol than OTM calls (crash fear). Know what skew means directionally.

---

## 5. Binomial Tree (conceptual)

- Discrete-time model: at each step price goes up by factor u or down by factor d.
- Risk-neutral probability: p = (e^(rΔt) − d) / (u − d).
- Work backward from expiry to today.
- Converges to Black-Scholes as steps → ∞.

---

## 6. Common Interview Questions

1. **"You think a stock will go up a lot or down a lot — you don't know which. What trade?"** → Long straddle (long call + long put, same K, same T) = long gamma/vega.
2. **"Stock at \$100, call strike \$105 costs \$4. What's your max profit/loss?"** → Long call: max loss = premium (\$4), max profit = unlimited (if S → ∞). Break-even = \$109.
3. **"Put-call parity: C = \$5, S = \$100, K = \$100, r = 5%, T = 1 yr. Find P."** → P = C + Ke^(−rT) − S = 5 + 95.12 − 100 = \$0.12.
4. **"Why is an American option worth ≥ European?"** → Early exercise flexibility adds value.
5. **"What happens to option price as volatility → 0?"** → Payoff becomes deterministic: call → max(S·e^(rT) − K·e^(−rT)... actually → max(S − K·e^(−rT), 0) discounted, roughly intrinsic value at present).

---

## 7. Quick Mental Math for Trading

- Option price ≈ intrinsic + time value. ATM options have max time value.
- If volatility doubles, option price does NOT double (roughly √T scaling for short-dated, vega-linear for small changes).
- Rule of thumb: 1% move in spot ≈ delta × 1% change in option price.

---

*Next: [`../05_Mock_Interviews/quant_interview_questions.md`](../05_Mock_Interviews/quant_interview_questions.md)*