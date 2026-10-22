# 🐍 Python for Quant Interviews

Quant interviews increasingly use live coding (Python or C++). You must write clean, bug-free code fast — ideally with no IDE autocomplete crutch.

---

## 1. Python Essentials to Know Cold

| Topic | What to practice |
|-------|------------------|
| **List/dict/set comprehensions** | `[x for x in nums if x%2==0]`, `{k:v for k,v in items}` |
| **Slicing** | `arr[::-1]`, `arr[1:5]`, `arr[::2]` |
| **`enumerate`, `zip`, `sorted`** | `sorted(items, key=lambda x: x[1])` |
| **`collections`** | `Counter`, `deque`, `defaultdict`, `namedtuple` |
| **`itertools`** | `combinations`, `permutations`, `product`, `accumulate` |
| **`heapq`** | `heappush`, `heappop`, `nlargest`, `nsmallest` |
| **`bisect`** | `bisect_left`, `bisect_right` on sorted lists |
| **`functools.lru_cache`** | memoize recursive functions |
| **`datetime` / `timedelta`** | date arithmetic, parsing |

---

## 2. NumPy (vectorized math — what quants actually use)

```python
import numpy as np

arr = np.array([1, 2, 3])
arr * 2          # element-wise
np.dot(a, b)     # inner product
np.cov(X, Y)     # covariance matrix
np.linalg.eig(M) # eigenvalues/eigenvectors
np.random.normal(size=(1000,))
np.percentile(arr, 95)
```

**Know:** broadcasting rules, `axis` argument, boolean masking (`arr[arr > 0]`), `np.where`.

---

## 3. Common Interview Patterns (implement from scratch)

### A. Black-Scholes call price (no lookup!)
```python
import math
from statistics import NormalDist

def black_scholes_call(S, K, T, r, sigma):
    d1 = (math.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)
    nd = NormalDist()
    return S*nd.cdf(d1) - K*math.exp(-r*T)*nd.cdf(d2)
```
**Do this from memory.** Interviewers love it.

### B. Monte Carlo option pricing
Simulate GBM paths, average payoff, discount. Know how to vectorize with NumPy.

### C. Shuffling a deck (Fisher–Yates)
```python
import random
def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i)
        deck[i], deck[j] = deck[j], deck[i]
```

### D. Expected value via simulation
Roll dice / flip coins N times, estimate expectation, compare to analytic.

---

## 4. LeetCode-Style Problems That Show Up

- Easy: Two Sum, Valid Palindrome, FizzBuzz, Fibonacci (iterative + recursive), Reverse Integer.
- Medium: Merge Intervals, Top K Frequent Elements, Longest Substring Without Repeating Characters, Trapping Rain Water.
- Quant-flavored: generate random number from a biased source, shuffle, sample without replacement, running median.

**Target:** 1 easy + 1 medium per day during Phase 2.

---

## 5. Mental Math (non-negotiable for trader interviews)

Practice daily (5–10 min):
- 2-digit × 2-digit multiplication (e.g., 37 × 48).
- Squares up to 30², cubes up to 15².
- Percentages: 15%, 25%, 33⅓% of any number fast.
- Fractions → decimals: 1/7 = 0.142857, 1/13 = 0.076923, etc.
- Estimation: 7.3 × 8.9 ≈ 7 × 9 = 63, then adjust.

**Resource:** `calculation.com` / `arithmetic.zetamac.com` for timed drills.

---

## 6. 5-Minute Pre-Interview Warmup

1. Write Fisher–Yates shuffle from memory.
2. Write Black-Scholes call from memory (no imports except math).
3. Compute 37 × 48, 14², 17% of 240, 1/13 as decimal — aloud, timed.
4. Explain `defaultdict` vs `dict.setdefault`.

---

*Next: [`cpp_quant.md`](./cpp_quant.md) — skip unless your target shops use C++ (most HFTs do)*