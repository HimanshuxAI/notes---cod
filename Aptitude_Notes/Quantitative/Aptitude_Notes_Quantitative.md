# QUANTITATIVE APTITUDE — COMPREHENSIVE NOTES

**Topics Covered:** Number System | Time and Work | Pipe and Cistern | Time Speed & Distance | Trains, Boats & Streams  
**School:** School of Corporate Innovation and Leadership  
**Category:** Quantitative Aptitude  

---

# PART 1 — NUMBER SYSTEM

## 1.1 Types of Numbers

| Category | Definition | Examples |
|----------|-----------|----------|
| **Real Numbers** | All numbers on number line (-∞ to +∞) | All rational + irrational |
| **Rational Numbers** | Can be written as p/q, q ≠ 0 | 0.5, 1/3, -2, 0.75 |
| **Irrational Numbers** | Cannot be written as p/q | π, √2, √3, non-repeating non-terminating decimals |
| **Terminating Decimals** | End after finite digits | 0.5, 0.2, 1.5 (Rational) |
| **Non-terminating Repeating** | Repeat a pattern | 0.333... = 1/3 (Rational) |
| **Non-terminating Non-repeating** | No pattern | π, √2 (Irrational) |
| **Prime Numbers** | Exactly 2 factors (1 and itself) | 2, 3, 5, 7, 11... |
| **Composite Numbers** | More than 2 factors | 4, 6, 8, 9, 10... |
| **Neither Prime nor Composite** | Only 1 factor | 1 |
| **Even Numbers** | Divisible by 2 | 2, 4, 6, 8... |
| **Odd Numbers** | Not divisible by 2 | 1, 3, 5, 7... |
| **Co-prime Numbers** | HCF = 1 | (2,3), (5,7), (8,9) |
| **Perfect Numbers** | Sum of factors (excluding itself) = number | 6 (1+2+3=6), 28 |

**Key:** 2 is the smallest prime number and the only even prime. 1 is neither prime nor composite.

## 1.2 Divisibility Rules

| Divisor | Rule | Example |
|---------|------|---------|
| **2** | Last digit is even (0,2,4,6,8) | 124 ✓ |
| **4** | Last two digits divisible by 4 | 123456 ✓ (56 ÷ 4) |
| **8** | Last three digits divisible by 8 | 123488 ✓ (488 ÷ 8) |
| **3** | Sum of digits divisible by 3 | 246 → 2+4+6=12 ✓ |
| **9** | Sum of digits divisible by 9 | 729 → 7+2+9=18 ✓ |
| **6** | Divisible by both 2 and 3 | 246 ✓ |
| **7** | Double last digit, subtract from rest, repeat | 203 → 20-6=14 ✓ |
| **11** | (Sum odd positions) - (Sum even positions) = 0 or multiple of 11 | 1331 → (1+3)-(1+3)=0 ✓ |
| **90** | Divisible by both 9 and 10 | Ends in 0, digit sum ÷ 9 |

## 1.3 Remainder Theorem

| Concept | Formula/Rule |
|---------|-------------|
| **Remainder** | Leftover after division |
| **Negative Remainder** | If remainder is -r, positive remainder = divisor - r |
| **Product Property** | Rem(A × B × C) = Rem(A) × Rem(B) × Rem(C) |
| **Fermat's Theorem** | If p is prime and a not divisible by p: a^(p-1) ÷ p → remainder 1 |
| **Wilson's Theorem** | If p is prime: (p-1)! ÷ p → remainder (p-1) |
| **Binomial Expansion** | (a+1)^n ÷ a → remainder 1 |

**Example:** Rem(123 × 124 × 125 ÷ 9) = Rem(-3 × -2 × -1) = -6 → 9-6 = 3

## 1.4 HCF & LCM

| Concept | Definition |
|---------|-----------|
| **HCF (GCD)** | Largest number dividing all given numbers |
| **LCM** | Least number divisible by all given numbers |
| **Key Relationship** | Product of two numbers = HCF × LCM |

**HCF & LCM of fractions:**
- HCF of fractions = HCF of numerators / LCM of denominators
- LCM of fractions = LCM of numerators / HCF of denominators

## 1.5 Unit Digit (Cyclicity)

| Unit Digit of Base | Pattern | Cyclicity |
|-------------------|---------|-----------|
| 0, 1, 5, 6 | Same digit repeats | 1 |
| 4 | 4, 6, 4, 6... | 2 (odd→4, even→6) |
| 9 | 9, 1, 9, 1... | 2 (odd→9, even→1) |
| 2, 3, 7, 8 | 4-step cycle | 4 |

**Method:** Divide exponent by cyclicity. Use remainder as new exponent.

**Example:** Unit digit of 7^74 → 74 ÷ 4 = 18 remainder 2 → 7^2 = 49 → unit digit **9**

---

# PART 2 — TIME AND WORK

## 2.1 Core Formula

**Work (W) = Efficiency (E) × Time (T)**

If A can complete work in `a` days and B in `b` days:
- Together: `1 / (1/a + 1/b)` = `ab / (a+b)` days

## 2.2 MDH Formula (Chain Rule)

`M₁ × D₁ × H₁ / W₁ = M₂ × D₂ × H₂ / W₂`

Where M = men, D = days, H = hours, W = work

## 2.3 LCM Approach

Take LCM of individual days as total work (units). Then:
- A's efficiency = LCM / A's days
- B's efficiency = LCM / B's days
- Combined efficiency = sum of individual efficiencies
- Days to complete = LCM / combined efficiency

## 2.4 Question Types

| Type | Description |
|------|-------------|
| Basic together | A and B together, find days |
| Find individual | A+B together, A alone → find B alone |
| Three persons | A, B, C together → combined days |
| Partial work | Some leave before completion |
| Alternate days | A works day 1, B day 2, etc. |
| Efficiency based | A is x% more efficient than B |
| Work & wages | Divide payment by work ratio |
| Chain rule | MDH formula with men/days/hours |
| Negative efficiency | One person destroys work |

## 2.5 Work & Wages Rule

Wages are divided in ratio of work done (or efficiency if same time).

**If A does work in `a` days and B in `b` days, together they get paid in ratio `b : a`** (inverse of time).

## 2.6 Remaining Work

If work is partially done:
- Remaining work = 1 - work done
- Time for remaining = Remaining work / efficiency of remaining worker(s)

---

# PART 3 — PIPE AND CISTERN

## 3.1 Concepts

Pipe and cistern is a subtopic of Time and Work.

| Term | Meaning |
|------|---------|
| **Cistern** | Tank for storing liquid |
| **Inlet Pipe** | Fills the tank (positive work) |
| **Outlet Pipe** | Empties the tank (negative work) |

**Work formula:** Same as Time and Work. Inlet = positive efficiency, Outlet = negative efficiency.

## 3.2 Question Types

| Type | Description |
|------|-------------|
| Direct | One inlet/outlet, simple time |
| Combined | Both inlet pipes together |
| Leakage | Outlet reduces fill rate |
| Variable | Pipes open/close after certain time |
| Cyclic | Pipes open in fixed order repeatedly |
| Alternate | Pipes open on alternate minutes/hours |

## 3.3 Key Formulas

- **Two inlets A & B together:** `ab / (a+b)` hours
- **Inlet A & Outlet B (B empties):** `ab / (b-a)` hours (if b > a)
- **Net efficiency:** Sum of inlet efficiencies - sum of outlet efficiencies

## 3.4 Leakage Problems

If a pump fills in `x` hours but with leak takes `y` hours:
- Leak empties full tank in `xy / (y-x)` hours
- Leak empties half tank in `xy / (2(y-x))` hours

---

# PART 4 — TIME, SPEED & DISTANCE

## 4.1 Core Formulas

| Formula | Expression |
|---------|-----------|
| **Speed** | Distance / Time |
| **Distance** | Speed × Time |
| **Time** | Distance / Speed |
| **Average Speed** | Total Distance / Total Time |

## 4.2 Unit Conversions

| Conversion | Factor |
|------------|--------|
| km/h → m/s | Multiply by 5/18 |
| m/s → km/h | Multiply by 18/5 |
| km/h → m/min | Multiply by 1000/60 = 50/3 |

**Example:** 54 km/h = 54 × 5/18 = 15 m/s

## 4.3 Proportionality

- **Same distance:** Speed ∝ 1/Time (inverse ratio)
  - If speeds are in ratio 3:4, times are in ratio 4:3
- **Same time:** Distance ∝ Speed

## 4.4 Average Speed

| Scenario | Formula |
|----------|---------|
| Equal distances at speeds x & y | `2xy / (x+y)` |
| Equal times at speeds x & y | `(x+y) / 2` |
| Different distances | Total distance / Total time |

## 4.5 Relative Speed

| Scenario | Relative Speed |
|----------|---------------|
| Same direction | S₁ - S₂ |
| Opposite direction | S₁ + S₂ |

## 4.6 Common Scenarios

| Scenario | Formula/Approach |
|----------|-----------------|
| **Usual time (late/early)** | If walking at x/y of usual speed, late by t mins → Usual time = t × y / (y-x) |
| **Stoppages** | Stop time per hour = (1 - effective speed / actual speed) × 60 |
| **Chasing** | Time to catch = Initial distance / Relative speed |
| **Towards each other** | Time to meet = Distance / (S₁ + S₂) |
| **Same direction meet** | Time to meet = Distance / (S₁ - S₂) |
| **Round trip avg speed** | `2xy / (x+y)` |

## 4.7 Distance-Left Problems

If walking at speed S₁ you're late by t₁, and at speed S₂ you're early by t₂:
- Distance = `(S₁ × S₂ × (t₁ + t₂)) / (S₂ - S₁)`

---

# PART 5 — TRAINS, BOATS & STREAMS

## 5.1 Trains

| Scenario | Formula |
|----------|---------|
| Cross pole (negligible width) | Time = Train Length / Train Speed |
| Cross platform/bridge | Time = (Train Length + Platform Length) / Train Speed |
| Cross man (same direction) | Time = Train Length / (Train Speed - Man Speed) |
| Cross man (opposite direction) | Time = Train Length / (Train Speed + Man Speed) |
| Two trains same direction | Time = (L₁ + L₂) / (S₁ - S₂) |
| Two trains opposite direction | Time = (L₁ + L₂) / (S₁ + S₂) |
| Overtaking | Faster train covers (L₁ + L₂) at relative speed |

**Unit conversion:** km/h → m/s: multiply by 5/18

## 5.2 Boats and Streams

| Term | Formula |
|------|---------|
| **B** | Speed of boat in still water |
| **W** | Speed of stream/current |
| **Downstream (D.S)** | B + W (with stream) |
| **Upstream (U.S)** | B - W (against stream) |
| **Speed in still water** | (D.S + U.S) / 2 |
| **Speed of stream** | (D.S - U.S) / 2 |

## 5.3 Boat Problems

| Scenario | Formula |
|----------|---------|
| Time downstream | Distance / (B + W) |
| Time upstream | Distance / (B - W) |
| Round trip total time | D/(B+W) + D/(B-W) |
| "n times longer upstream" | (B+W) / (B-W) = n |
| Average speed (round trip) | `2 × D.S × U.S / (D.S + U.S)` |

## 5.4 Key Relationships

- If boat takes same time downstream `d₁` and upstream `d₂` for different distances:
  - Stream speed = (d₁ - d₂) / (time × 2) or use ratio method
- If downstream speed = D.S and upstream = U.S:
  - B = (D.S + U.S) / 2
  - W = (D.S - U.S) / 2

---

# PART 6 — PRACTICE QUESTIONS & ANSWERS

## Number System

**Q:** The difference of squares of two consecutive odd integers is divisible by?
**A:** 8. Let integers be (2n+1) and (2n+3). Difference = (2n+3)² - (2n+1)² = 8n+8 = 8(n+1). Always divisible by 8.

**Q:** Remainder when 2^202 is divided by 7?
**A:** 2^3 = 8 ≡ 1 (mod 7). 202 ÷ 3 = 67 remainder 1. So 2^202 ≡ 2^1 ≡ 2 (mod 7). Answer: **2**

**Q:** Unit digit of 7^74?
**A:** Cyclicity of 7 is 4. 74 ÷ 4 = 18 rem 2. 7^2 = 49. Answer: **9**

## Time and Work

**Q:** A does work in 24 days, B in 40 days. Together?
**A:** LCM = 120. A's efficiency = 5, B's = 3. Combined = 8. Days = 120/8 = **15 days**

**Q:** A is thrice as good as B, finishes 50 days less. Together?
**A:** If B takes 3x days, A takes x days. 3x - x = 50, x = 25. A = 25, B = 75. Together = (25×75)/(25+75) = 1875/100 = **18.75 days**

## Pipe and Cistern

**Q:** Pipe A fills in 20 min, B in 30 min. Together?
**A:** LCM = 60. A = 3 units/min, B = 2 units/min. Combined = 5 units/min. Time = 60/5 = **12 minutes**

**Q:** Inlet fills in 5 hr, outlet empties in 6 hr. Together?
**A:** Net = 1/5 - 1/6 = 1/30. Time = **30 hours**

## Time Speed Distance

**Q:** 54 km/h in m/s?
**A:** 54 × 5/18 = **15 m/s**

**Q:** Bus speed 54 km/h without stops, 45 km/h with stops. Stop time per hour?
**A:** (54-45)/54 × 60 = 9/54 × 60 = **10 minutes**

## Trains

**Q:** Train 180m at 72 km/h crosses pole?
**A:** 72 km/h = 20 m/s. Time = 180/20 = **9 seconds**

## Boats and Streams

**Q:** Downstream 20 km/h, upstream 12 km/h. Boat in still water?
**A:** (20+12)/2 = **16 km/h**

**Q:** Downstream 18 km/h, B:W ratio 5:1. Stream speed?
**A:** 6 parts = 18, 1 part = 3. Answer: **3 km/h**
