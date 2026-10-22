# ❓ Quant Interview Question Bank

Past/reconstructed questions from prop shops and hedge funds (Jane Street, Optiver, Citadel, Hudson River, Jump, etc.). Organized by type.

---

## A. Probability & Brainteasers

1. Two children: at least one boy → P(both boys)?
2. Monty Hall: switch or stay?
3. Expected flips to get HH vs HT.
4. 100 prisoners and a light bulb.
5. Biased coin → fair outcome (von Neumann).
6. Ants on a plank (collisions).
7. Gambler's ruin with p ≠ 0.5.
8. Random points on a circle in a semicircle.
9. Two envelopes paradox.
10. Dice game with reroll option — compute EV.
11. You roll a die, get paid the value. You can reroll once, but pay \$1 each reroll. Optimal strategy & EV?
12. 3 ants on a triangle, each picks a direction randomly. P(no collision)?
13. Expected number of loops when tying 2n rope ends randomly?
14. Stick broken at 2 random points → P(3 pieces form a triangle)?

---

## B. Expected Value / Decision

15. Game: flip until heads, get paid 2ⁿ dollars where n = flip number. Fair price to play? (St. Petersburg paradox — discuss divergence vs practical cap.)
16. Envelope contains \$X or \$2X with equal prob. You see \$100. Switch? (Discuss prior dependence.)
17. You have 100 coins, one is double-headed. Pick one, flip 5 times, all heads. P(it's double-headed)?
18. Urn with 3 red, 3 blue. Draw 2 without replacement. P(same color)?
19. Expected value of max of 2 dice? min? max of n dice?
20. You bid on an item. Value is uniform [0,100]. If you win you pay your bid. Optimal bid? (First-price auction logic.)

---

## C. Mental Math / Estimation

21. 37 × 48 = ?
22. 17% of 240 = ?
23. 1/13 as decimal ≈ ?
24. √2000 ≈ ?
25. 2¹⁰, 2²⁰ = ?
26. 99² = ?
27. 15 × 15, 25 × 25, 35 × 35 (two-digit squares ending in 5).
28. 1024 × 1024 ≈ ?
29. 7.3 × 8.9 estimate then adjust.
30. 100! trailing zeros?

---

## D. Options & Markets

31. Call payoff at expiry? Put payoff?
32. Put-call parity equation.
33. What does delta measure? Gamma? Vega?
34. Long straddle = bet on what?
35. American vs European option — which is worth more and why?
36. If vol → 0, what happens to option price?
37. Stock at 100, call K=105, premium 4. Max profit/loss? Break-even?
38. Risk-neutral pricing intuition (one sentence).
39. What is implied volatility smile/skew?
40. Delta-hedging: what are you hedging? What remains (gamma/theta P&L)?

---

## E. Coding (Python / C++)

41. Implement Fisher–Yates shuffle.
42. Black-Scholes call price from scratch.
43. Two Sum / 3 Sum.
44. Valid parentheses with stack.
45. First unique character in a string.
46. Simulate dice rolls, estimate P(sum = 7).
47. Running median with two heaps.
48. Reservoir sampling (pick 1 random from stream).
49. Generate fair bit from biased coin.
50. Merge two sorted arrays.

---

## F. Fit / Behavioral

51. Why quant trading? Why this firm?
52. Tell me about a time you failed. What did you learn?
53. What's a trading idea you'd research if given \$1M?
54. How do you handle pressure / losing streaks?
55. What's your edge? What are you better at than other candidates?

---

## How to Practice

1. Pick 3 questions/day (1 probability, 1 coding, 1 markets/fit).
2. Set a timer: 10 min for probability, 25 min for coding, 5 min for mental math.
3. Speak your solution out loud (interviews are interactive).
4. After solving, write the "ideal answer" in your own words.
5. Track mistakes in [`answer_templates.md`](./answer_templates.md).

---

*Next: [`answer_templates.md`](./answer_templates.md)*