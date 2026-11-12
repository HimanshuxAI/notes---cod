# 🐍 Python Crash Course — Complete Detailed Notes

> **Book:** *Python Crash Course, 3rd Edition — A Hands-On, Project-Based Introduction to Programming*
> **Author:** Eric Matthes
> **Publisher:** No Starch Press (December 2022, 552 pages)
> **ISBN-13:** 978-1-7185-0270-3
> **Python version used in book:** Python 3.11 (works on 3.9+)
> **Structure:** Part I — Basics (Ch. 1–11) · Part II — Projects (Ch. 12–20) · Appendices A–E

These notes cover **every chapter, every major concept, every important method, all three projects, the appendices, and the cheat sheets** — with runnable code, gotchas, and the exact things beginners get wrong.

---

## 📑 Table of Contents

**Part I — Basics**
1. [Getting Started](#chapter-1--getting-started)
2. [Variables and Simple Data Types](#chapter-2--variables-and-simple-data-types)
3. [Introducing Lists](#chapter-3--introducing-lists)
4. [Working with Lists](#chapter-4--working-with-lists)
5. [if Statements](#chapter-5--if-statements)
6. [Dictionaries](#chapter-6--dictionaries)
7. [User Input and while Loops](#chapter-7--user-input-and-while-loops)
8. [Functions](#chapter-8--functions)
9. [Classes](#chapter-9--classes)
10. [Files and Exceptions](#chapter-10--files-and-exceptions)
11. [Testing Your Code](#chapter-11--testing-your-code)

**Part II — Projects**
- **Project 1: Alien Invasion** — [Ch. 12](#chapter-12--a-ship-that-fires-bullets) · [Ch. 13](#chapter-13--aliens) · [Ch. 14](#chapter-14--scoring)
- **Project 2: Data Visualization** — [Ch. 15](#chapter-15--generating-data) · [Ch. 16](#chapter-16--downloading-data) · [Ch. 17](#chapter-17--working-with-apis)
- **Project 3: Web Applications** — [Ch. 18](#chapter-18--getting-started-with-django) · [Ch. 19](#chapter-19--user-accounts) · [Ch. 20](#chapter-20--styling-and-deploying-an-app)

**Appendices & Extras**
- [Appendix A — Installation & Troubleshooting](#appendix-a--installation-and-troubleshooting)
- [Appendix B — Text Editors & IDEs](#appendix-b--text-editors-and-ides)
- [Appendix C — Getting Help](#appendix-c--getting-help)
- [Appendix D — Git for Version Control](#appendix-d--using-git-for-version-control)
- [Appendix E — Troubleshooting Deployments](#appendix-e--troubleshooting-deployments)
- [Master Cheat Sheets](#-master-cheat-sheets)
- [Top 40 Beginner Mistakes](#-top-40-beginner-mistakes)
- [30-Day Study Plan](#-30-day-study-plan)

---

## 📖 Book at a Glance

| Part | Chapters | What you learn | Output |
|------|----------|----------------|--------|
| **Part I — Basics** | 1–11 | Python syntax, data structures, OOP, files, testing | Solid language foundation |
| **Project 1 — Alien Invasion** | 12–14 | Pygame, game loops, sprites, collisions, scoring | 2D arcade game |
| **Project 2 — Data Visualization** | 15–17 | Matplotlib, Plotly, CSV, JSON, APIs | Data-driven charts/maps |
| **Project 3 — Web Apps** | 18–20 | Django models, views, templates, auth, deployment | Live web app |
| **Appendices** | A–E | Setup, editors, help, Git, deployment fixes | Working dev environment |

**The book's philosophy:** learn a concept → immediately type code → do exercises → repeat. Every chapter ends with "Try It Yourself" exercises. You are meant to *type everything*, not copy-paste.

---

# PART I — BASICS

---

## Chapter 1 — Getting Started

### 1.1 Setting Up Your Programming Environment

You need two things:

1. **Python** — the interpreter that runs your code.
2. **A text editor / IDE** — where you write code (VS Code is the book's choice).

#### Installing Python

| OS | How |
|----|-----|
| **Windows** | Download from [python.org/downloads](https://python.org/downloads). ✅ Check **"Add python.exe to PATH"** during install. |
| **macOS** | Download the official installer, or `brew install python`. macOS ships an old Python; install a fresh one. |
| **Linux** | Usually preinstalled (`python3`). Use `sudo apt install python3 python3-pip` if needed. |

**Verify installation:**

```bash
python --version      # Windows
python3 --version     # macOS / Linux
```

Expected: `Python 3.11.x` (anything 3.9+ is fine).

> ⚠️ **Windows gotcha:** if `python` opens the Microsoft Store, install Python from python.org and disable the Store aliases in *Settings → Apps → App execution aliases*.

#### Installing VS Code

1. Download from [code.visualstudio.com](https://code.visualstudio.com).
2. Install the **Python extension** (by Microsoft).
3. Open a folder (`File → Open Folder`) — always open the *project folder*, not a single file.
4. Select the interpreter: `Ctrl/Cmd + Shift + P` → **Python: Select Interpreter**.

### 1.2 Running Snippets of Python Code

Two ways to run Python:

**A. Interactive interpreter (REPL)** — good for quick experiments:

```bash
python          # or python3
>>> print("Hello, Python!")
Hello, Python!
>>> 2 + 3
5
>>> exit()      # or Ctrl+D / Ctrl+Z then Enter
```

**B. Running a file** — the normal way:

```bash
python hello_world.py
```

`hello_world.py`:

```python
print("Hello, Python world!")
```

The `.py` extension tells everyone (and the editor) this is a Python file.

### 1.3 Anatomy of a Python Program

```python
# hello_world.py
print("Hello, Python world!")     # print() displays text
```

- `#` starts a **comment** — ignored by Python.
- `print()` is a **function** — it does something.
- `"..."` is a **string** — text data.
- Python reads **top to bottom**, one line at a time.

### 1.4 Common Beginner Problems (Chapter 1's troubleshooting)

| Problem | Cause | Fix |
|---------|-------|-----|
| `python: command not found` | Python not installed / not on PATH | Reinstall with PATH option; use `python3` |
| `SyntaxError: invalid syntax` | Typo, missing quote/parenthesis | Compare with book code exactly |
| `NameError: name 'prnt' is not defined` | Misspelled function name | Fix spelling |
| Nothing happens | Forgot to save the file | `Ctrl/Cmd + S` before running |
| Code runs but wrong output | Ran an old saved version | Check the filename/path in terminal |
| `IndentationError` | Stray space at the start of a line | Remove leading spaces |

**Rule of thumb:** read the *last line* of a traceback first — it names the error type; the line above points to where it happened.

### 1.5 Key Takeaways

- Python is **interpreted**: run the file directly, no compile step.
- `print()` is your first debugging tool.
- Save → run → read errors → fix → repeat.
- Interactive mode is for testing tiny snippets; files are for real programs.

---

## Chapter 2 — Variables and Simple Data Types

### 2.1 What Is a Variable?

A **variable** is a label attached to a value. You assign with `=`.

```python
message = "Hello, Python reader!"
print(message)
```

- `message` → variable name
- `=` → assignment operator (not "equals"!)
- `"Hello..."` → value (a string)

You can **reassign** at any time; the old value is discarded:

```python
message = "Hello"
print(message)     # Hello
message = "Goodbye"
print(message)     # Goodbye
```

### 2.2 Naming Rules & Conventions

**Hard rules (Python enforces):**

- Only letters, digits, and underscores: `user_name`, `score1`.
- Cannot start with a digit: `1score` ❌.
- No spaces: `user name` ❌ → use `user_name`.
- Cannot be a **keyword**: `if`, `for`, `class`, `def`, `True`, `False`, `None`, `import`, etc.
- Case-sensitive: `Age`, `age`, `AGE` are three variables.

**Conventions (humans prefer):**

- `snake_case` for variables and functions: `high_score`, `get_name()`.
- `UPPER_CASE` for constants: `MAX_SPEED = 120`.
- `PascalCase` for classes: `AlienInvasion`, `UserProfile`.
- Short but descriptive: `name` ✅, `n` ⚠️, `this_is_the_name_of_the_user` ❌.

**Avoid confusion:** lowercase `l`, uppercase `O`, uppercase `I` look like `1`/`0`.

### 2.3 Strings

A **string** is text inside quotes. Single or double quotes both work:

```python
name = "ada lovelace"
name = 'ada lovelace'      # same thing
```

Use the other quote type when the text contains one:

```python
quote = "She said, 'Hello.'"
quote = 'He said, "Hi."'
```

Or escape it:

```python
quote = 'She said, \'Hello.\''
```

#### String methods (they return a *new* string; originals don't change)

```python
name = "ada lovelace"
name.title()      # 'Ada Lovelace'  → capitalize each word
name.upper()      # 'ADA LOVELACE'
name.lower()      # 'ada lovelace'
```

> 💡 **Why `.lower()` matters:** comparing user input is case-sensitive unless you normalize:
> ```python
> answer = input("Continue? (Y/N) ")
> if answer.lower() == "y":
>     ...
> ```

#### f-strings (the modern way to combine text + variables)

```python
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
# Hello, Ada Lovelace!
```

Anything inside `{}` is evaluated as Python:

```python
print(f"2 + 2 = {2 + 2}")          # 2 + 2 = 4
print(f"{'hi'.upper()}")            # HI
```

> 3rd edition uses **f-strings** everywhere. The older `.format()` and `%` styles still work but are legacy.

#### Whitespace: `\t`, `\n`, and stripping

```python
print("Python")
print("\tPython")     # tab
print("Languages:\nPython\nC\nJavaScript")   # newlines
```

Trailing/leading whitespace is a classic bug source:

```python
favorite = " python "
favorite.rstrip()     # ' python'   → right side only
favorite.lstrip()     # 'python '   → left side only
favorite.strip()      # 'python'    → both sides
```

These return a **new** string — they do **not** modify the original:

```python
favorite = " python "
favorite.strip()
print(favorite)              # ' python '  ← unchanged!
favorite = favorite.strip()  # must reassign
```

#### Avoiding syntax errors with quotes

```python
message = 'One of Python's strengths is its diverse community.'
# ❌ SyntaxError: the apostrophe closes the string
message = "One of Python's strengths is its diverse community."   # ✅
```

### 2.4 Numbers

#### Integers

```python
2 + 3      # 5
3 - 2      # 1
2 * 3      # 6
3 / 2      # 1.5   ← always float
3 // 2     # 1     ← floor division (integer result)
3 % 2      # 1     ← modulo: remainder
2 ** 3     # 8     ← exponent
(2 + 3) * 4  # 20  ← parentheses control order
```

Operator precedence (high → low): `**` → `* / // %` → `+ -`.

#### Floats

```python
0.1 + 0.1       # 0.2
0.2 + 0.1       # 0.30000000000000004  ← floating-point precision
```

That's normal in every language. For display, round:

```python
round(0.30000000000000004, 2)   # 0.3
```

Or format: `f"{value:.2f}"`.

#### Mixing ints and floats

```python
4 / 2       # 2.0  ← division always gives float
1 + 2.0     # 3.0  ← any float in the expression → float result
```

#### Underscores in big numbers (readability)

```python
universe_age = 14_000_000_000
print(universe_age)     # 14000000000
```

#### Multiple assignment (unpacking)

```python
x, y, z = 0, 0, 0
```

#### Constants

Python has no true constants. By convention:

```python
MAX_CONNECTIONS = 5000    # do not change this
```

#### `str()` — convert numbers to strings

```python
age = 23
message = "Happy " + age + "rd Birthday!"   # ❌ TypeError
message = "Happy " + str(age) + "rd Birthday!"   # ✅
print(f"Happy {age}rd Birthday!")            # ✅ easier
```

### 2.5 Comments

```python
# This is a comment — ignored by Python.
# Use comments to explain *why*, not *what*.

# Say hello to the user.
print("Hello!")
```

Good comments explain intent and non-obvious decisions. Bad comments repeat the code (`# add 1 to x`).

### 2.6 The Zen of Python

```python
import this
```

Prints Tim Peters' 19 aphorisms, including:

> Beautiful is better than ugly.  
> Explicit is better than implicit.  
> Simple is better than complex.  
> Readability counts.  
> Errors should never pass silently.  
> There should be one — and preferably only one — obvious way to do it.

These values shape all Python style.

### 2.7 Chapter 2 Exercises (summary)

- Print a simple message, then change it.
- Print a name in lowercase, uppercase, title case.
- Print a famous quote with quotation marks.
- Strip whitespace and print with/without it.
- Compute `8` in four different ways (`+`, `-`, `*`, `/`).
- Store your favorite number and print a message with it.
- Add a comment describing your favorite number program.

### 2.8 Key Takeaways

- Variables are labels; assignment with `=`.
- Use `snake_case`, be descriptive, avoid keywords.
- Strings: `.title()`, `.upper()`, `.lower()`, `.strip()`, f-strings.
- `//` floor division, `%` modulo, `**` power; `/` always float.
- Floats have precision quirks — round or format for display.
- Strings and numbers don't mix: convert with `str()` / `int()` / `float()`.

---

## Chapter 3 — Introducing Lists

### 3.1 What Is a List?

An **ordered, mutable** collection of items:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
```

- Square brackets `[]`
- Comma-separated items
- Items can be any type (even mixed, though usually uniform)

### 3.2 Accessing Elements — Indexing

```python
print(bicycles[0])      # trek
print(bicycles[0].title())   # Trek
print(bicycles[2])      # redline
print(bicycles[-1])     # specialized  ← last item
print(bicycles[-2])     # redline      ← second-last
```

**Indexes start at 0.** Negative indexes count from the end: `-1` = last, `-2` = second-last.

```python
message = f"My first bicycle was a {bicycles[0].title()}."
```

### 3.3 Changing, Adding, Removing Elements

#### Modify

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
# ['ducati', 'yamaha', 'suzuki']
```

#### Add

```python
motorcycles.append('honda')        # add to END
motorcycles.insert(0, 'bmw')       # insert at index 0
```

#### Remove

```python
del motorcycles[0]                 # remove by INDEX (no return)
popped = motorcycles.pop()         # remove & return LAST
first = motorcycles.pop(0)         # remove & return index 0
motorcycles.remove('yamaha')       # remove by VALUE (first match)
```

- Use `del` when you know the position and don't need the value.
- Use `pop()` when you need the removed value (e.g., a stack/queue).
- Use `remove()` when you know the value, not the position.
- `remove()` only removes the **first** occurrence. Loop to remove all duplicates.

### 3.4 Organizing a List

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

cars.sort()                  # permanent, alphabetical
cars.sort(reverse=True)      # permanent, reverse alphabetical
print(sorted(cars))          # temporary sorted copy
print(sorted(cars, reverse=True))
cars.reverse()               # permanent, reverses current order
len(cars)                    # 4
```

> ⚠️ `.sort()` works **in place** and returns `None` — `cars = cars.sort()` destroys your list!

#### Sorting case-insensitively

```python
cars.sort(key=str.lower)
```

### 3.5 Avoiding Index Errors

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])       # ❌ IndexError: list index out of range
print(motorcycles[-1])      # ✅ safe: always the last item
```

An empty list has no `[-1]` either — guard with `if my_list:` first.

### 3.6 Chapter 3 Exercises (summary)

- Print greetings for each name in a list.
- Build a guest list, then add/replace/remove guests.
- Sort a list of places temporarily and permanently; reverse it.
- Count items with `len()`.
- Intentionally trigger and fix an `IndexError`.

### 3.7 Key Takeaways

- Lists are ordered and changeable.
- Index from `0`; `-1` is the last item.
- `append` / `insert` add; `del` / `pop` / `remove` delete.
- `sort()` is permanent; `sorted()` returns a copy.
- `len()` counts items; `IndexError` means you went past the end.

---

## Chapter 4 — Working with Lists

### 4.1 Looping with `for`

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

Output:

```
alice
david
carolina
```

- `for` line ends with a **colon**.
- The loop body is **indented** (4 spaces).
- `magician` is a temporary variable; name it singular for readability.
- After the loop, unindented code runs once.

```python
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
```

### 4.2 Indentation Errors (the #1 beginner bug)

| Error | Example | Result |
|-------|---------|--------|
| Forgot to indent | `for x in xs:` then `print(x)` at column 0 | `IndentationError` |
| Indented when not needed | `print("done")` indented after loop | `IndentationError` (unexpected indent) |
| Indented too much/little | 2 spaces vs 4 | `IndentationError` |
| Missing colon | `for x in xs` | `SyntaxError` |
| Extra indent inside a block | inconsistent mixing | `IndentationError` |

**Rule:** Python uses indentation to define blocks — 4 spaces per level, never tabs mixed with spaces.

### 4.3 Numerical Lists

#### `range()`

```python
for value in range(1, 5):
    print(value)        # 1 2 3 4  (stops BEFORE 5)

list(range(1, 6))       # [1, 2, 3, 4, 5]
list(range(0, 10, 2))   # [0, 2, 4, 6, 8]  step=2
list(range(5))          # [0, 1, 2, 3, 4]  start defaults to 0
```

#### `list()` converts a range (or any iterable) to a list

```python
squares = [value ** 2 for value in range(1, 11)]
```

#### Simple statistics

```python
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)   # 0
max(digits)   # 9
sum(digits)   # 45
```

#### List comprehensions

One line: expression + `for` + optional `if`.

```python
squares = [value ** 2 for value in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
```

Equivalent long form:

```python
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
```

> Read a comprehension as: **"make [this expression] for each [item] in [collection], if [condition]."**

### 4.4 Slicing a List

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

players[0:3]     # ['charles', 'martina', 'michael']  ← 0,1,2
players[1:4]     # ['martina', 'michael', 'florence']
players[:4]      # first four
players[2:]      # from index 2 to end
players[-3:]     # last three
players[:]       # full copy
players[::2]     # every second item
```

Slices never raise `IndexError` for out-of-range bounds — they just return fewer items.

#### Looping through a slice

```python
for player in players[:3]:
    print(player.title())
```

### 4.5 Copying a List

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]      # ✅ real copy
friend_foods = my_foods         # ❌ both names point to the SAME list
```

Test it:

```python
my_foods.append('cannoli')
print(friend_foods)    # copy: unchanged; alias: also changed
```

Use `list(my_foods)` or `my_foods.copy()` as alternatives.

### 4.6 Tuples (immutable lists)

```python
dimensions = (200, 50)
print(dimensions[0])    # 200
dimensions[0] = 250     # ❌ TypeError: 'tuple' object does not support item assignment
```

A **one-element tuple needs a trailing comma**:

```python
my_t = (3,)     # tuple
my_t = (3)      # just the int 3
```

You can't change items, but you *can* reassign the whole variable:

```python
dimensions = (200, 50)
dimensions = (400, 100)   # ✅ new tuple
```

Tuples are used for data that must not change (coordinates, settings, RGB colors).

### 4.7 Styling Your Code (PEP 8)

- **4 spaces** per indentation level (editors can insert tabs, but Python style = spaces).
- Limit lines to **79 characters** (comments/docstrings often 72).
- Blank lines: 2 between top-level functions/classes; 1 between methods.
- Spaces around operators: `x = 1 + 2`, not `x=1+2` (but no spaces inside `f(a, b)`).
- `snake_case` for variables/functions, `PascalCase` for classes, `UPPER_CASE` for constants.
- Comments: `# ` with a space, complete sentences.
- Avoid extra whitespace inside brackets: `[1, 2]`, not `[ 1, 2 ]`.

PEP 8 = *Python Enhancement Proposal 8* — the official style guide.

### 4.8 Chapter 4 Exercises (summary)

- Loop through a list and print messages.
- Count to 20 with `range()`; make a million-item list and test `min/max/sum`.
- Odd numbers, multiples of 3, cubes — with comprehensions.
- Slice a list (first three, middle three, last three).
- Copy a list and prove the copy is independent.
- Create a tuple, loop over it, then reassign it.

### 4.9 Key Takeaways

- `for item in list:` + indented block.
- `range(start, stop, step)` stops **before** `stop`.
- Comprehensions build lists in one line.
- `list[:]` copies; `list` alone aliases.
- Tuples are immutable; use `(x,)` for one item.
- Follow PEP 8 from day one.

---

## Chapter 5 — if Statements

### 5.1 Conditional Tests

An `if` statement runs code **only when a condition is true**.

```python
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
```

A **conditional test** is an expression that evaluates to `True` or `False`.

#### Comparison operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `==` | equal | `age == 18` |
| `!=` | not equal | `age != 18` |
| `<` | less than | `age < 18` |
| `<=` | less or equal | `age <= 18` |
| `>` | greater than | `age > 18` |
| `>=` | greater or equal | `age >= 18` |

> ⚠️ `=` assigns, `==` compares. Mixing them is a classic bug (and a `SyntaxError` in an `if`).

#### Case sensitivity

```python
car = 'Audi'
car == 'audi'          # False
car.lower() == 'audi'  # True
```

#### Checking inequality

```python
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
```

#### Numerical comparisons

```python
age = 18
age == 18        # True
age != 21        # True
age < 21         # True
age <= 18        # True
```

### 5.2 Boolean Expressions & `and` / `or` / `not`

A **boolean** is `True` or `False` (capitalized!). Always use these, not strings `"true"`.

```python
age = 22
age >= 21 and age <= 35     # True  → both must be True
age < 21 or age > 65        # False → at least one True
not (age == 22)             # False
```

Real example:

```python
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21     # False
(age_0 >= 21) or (age_1 >= 21)  # True
```

### 5.3 Checking Membership: `in` / `not in`

```python
requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_toppings       # True
'pepperoni' in requested_toppings       # False
'pepperoni' not in requested_toppings   # True
```

### 5.4 `if`, `if-else`, `if-elif-else`

```python
# if
if age >= 18:
    print("You can vote.")

# if-else
if age >= 18:
    print("You can vote.")
else:
    print("You are too young to vote.")

# if-elif-else
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
```

- Python checks **top to bottom** and stops at the first `True`.
- `elif` = "else if". You can have any number of `elif` blocks.
- `else` is optional and catches **everything** else — don't use it when you need to be specific.

```python
# Multiple independent ifs (all get checked)
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
```

### 5.5 Omitting `else`

Sometimes you only care about one case:

```python
if user not in banned_users:
    print(f"{user.title()}, you can post a response.")
```

### 5.6 Checking That a List Is Not Empty

```python
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
else:
    print("Are you sure you want a plain pizza?")
```

An empty list is **falsy**; a non-empty list is **truthy**.

### 5.7 Truthiness Cheat Sheet

| Falsy values | Truthy values |
|--------------|---------------|
| `False`, `None` | `True` |
| `0`, `0.0` | any non-zero number |
| `""` (empty string) | any non-empty string |
| `[]`, `()`, `{}`, `set()` | any non-empty collection |

### 5.8 Chapter 5 Exercises (summary)

- Write true/false condition tests and predict results.
- Alien colors: `if-elif-else` chains for points.
- Stages of life (baby → toddler → kid → teenager → adult → elder).
- Favorite fruit membership tests.
- Ordinal numbers using `if-elif-else` and `range(1, 10)`.
- Hello Admin: special greeting for `'admin'`, generic for others; handle empty list.

### 5.9 Key Takeaways

- `if`/`elif`/`else` + colon + indented block.
- `==` compares, `=` assigns.
- Combine tests with `and`, `or`, `not`.
- Use `in` / `not in` for membership.
- Empty collections are falsy — a clean way to test "has items".
- Only one branch of `if-elif-else` ever runs.

---

## Chapter 6 — Dictionaries

### 6.1 What Is a Dictionary?

A collection of **key-value pairs**, wrapped in `{}`:

```python
alien_0 = {'color': 'green', 'points': 5}
```

- Keys are usually strings (must be immutable).
- Values can be anything: numbers, strings, lists, even other dictionaries.
- Dictionaries are **mutable** and (since Python 3.7) keep **insertion order**.

### 6.2 Accessing Values

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])     # green
print(alien_0['points'])    # 5
```

Accessing a missing key raises `KeyError`:

```python
print(alien_0['x_position'])   # ❌ KeyError
```

Safe access with `.get()`:

```python
print(alien_0.get('x_position'))            # None
print(alien_0.get('x_position', 0))         # 0 (default)
```

> Use `.get()` whenever a key might be absent — no crash, no `try/except` needed.

### 6.3 Adding, Modifying, Removing

```python
alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0        # ADD a new key
alien_0['y_position'] = 25
alien_0['color'] = 'yellow'      # MODIFY existing key
alien_0['speed'] = 'medium'

del alien_0['points']            # REMOVE a key-value pair
```

Dictionaries have **no fixed size** — add keys at any time.

### 6.4 A Dictionary of Similar Objects

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
```

Style: trailing comma after the last pair is fine and makes diffs cleaner.

### 6.5 Looping Through a Dictionary

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
```

#### Keys only (default iteration)

```python
for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:      # same as .keys()
    print(name)
```

#### Values only

```python
for language in favorite_languages.values():
    print(language.title())
```

#### Unique values with `set()`

```python
for language in set(favorite_languages.values()):
    print(language.title())
```

A **set** is an unordered collection of unique items: `{1, 2, 3}`.

#### Sorted keys

```python
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
```

### 6.6 Nesting

#### A list of dictionaries

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Build 30 aliens programmatically
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

print(f"Total aliens: {len(aliens)}")
```

Change the first three:

```python
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
```

#### A list inside a dictionary

```python
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
```

#### A dictionary inside a dictionary

```python
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
```

### 6.7 Useful Dictionary Methods

| Method | Purpose |
|--------|---------|
| `d[key]` | Get value; `KeyError` if missing |
| `d.get(key, default)` | Get value or default (`None` if omitted) |
| `d.keys()` | View of keys |
| `d.values()` | View of values |
| `d.items()` | View of `(key, value)` pairs |
| `d.pop(key, default)` | Remove key and return value |
| `d.popitem()` | Remove and return last inserted pair |
| `d.update(other)` | Merge/overwrite with another dict |
| `d.setdefault(key, default)` | Get key, inserting default if missing |
| `d.clear()` | Remove everything |
| `key in d` | Membership test (keys only) |
| `len(d)` | Number of pairs |

### 6.8 Chapter 6 Exercises (summary)

- Store a person's info in a dict and print each field.
- Favorite numbers: a dict of people → numbers.
- Glossary: programming words → meanings; loop and print.
- Rivers: country → river; loop with keys/values.
- Polling: check who has/hasn't taken a poll.
- Pets, favorite places, cities: nested dicts/lists.
- People and pizza: list of dicts / list inside dict.

### 6.9 Key Takeaways

- Dict = `{key: value}`; access by key, not index.
- `.get()` avoids `KeyError`.
- Loop with `.items()`, `.keys()`, `.values()`.
- `set(d.values())` gives unique values.
- Nest freely: lists of dicts, dicts of lists, dicts of dicts.
- Dictionaries are the natural model for real-world records.

---

## Chapter 7 — User Input and while Loops

### 7.1 How `input()` Works

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

- The argument is the **prompt** shown to the user.
- `input()` always returns a **string**.
- Add a space at the end of the prompt for readability.

#### Multi-line prompts

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
```

### 7.2 `int()` to Accept Numerical Input

```python
age = input("How old are you? ")     # '23' (string!)
age = int(age)                        # 23 (int)
if age >= 18:
    print("You can vote!")
```

#### Modulo operator for even/odd

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
```

#### `float()` for decimals

```python
height = float(input("How tall are you, in inches? "))
```

> ⚠️ `int("23.5")` raises `ValueError`. Use `float()` when decimals are possible.

### 7.3 `while` Loops

Runs **as long as** the condition is true:

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

> Forgetting `current_number += 1` creates an **infinite loop** — `Ctrl+C` stops it.

### 7.4 Letting the User Choose When to Quit

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
```

### 7.5 Using a Flag

A **flag** is a boolean variable that signals whether the program should keep running:

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
```

Flags are cleaner than long compound conditions and easier to extend.

### 7.6 `break` and `continue`

#### `break` — exit the loop immediately

```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
```

`while True:` + `break` is a standard pattern for "loop until something happens".

#### `continue` — skip the rest of this iteration

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)      # prints 1, 3, 5, 7, 9
```

> `break` leaves the loop entirely; `continue` jumps back to the condition check.

### 7.7 Avoiding Infinite Loops

```python
x = 1
while x <= 5:
    print(x)
    # x += 1  ← missing! infinite loop
```

Checklist:
- Does the loop variable change inside the loop?
- Is the condition reachable?
- If using `while True`, is there a guaranteed `break`?
- Ctrl+C is your emergency exit.

### 7.8 Using `while` with Lists and Dictionaries

#### Move items between lists

```python
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

#### Remove all instances of a value

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
# ['dog', 'goldfish', 'rabbit']
```

#### Fill a dictionary with user input

```python
responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
```

### 7.9 Chapter 7 Exercises (summary)

- Rental car: ask for a car and print a message.
- Restaurant seating: ask party size; `> 8` → wait, else → table ready.
- Multiples of ten.
- Pizza toppings: `while` loop until `'quit'`; print the final list.
- Movie tickets: price by age; `break` on `'quit'`.
- Three exits: demonstrate `break`, a flag, and a condition.
- Deli: move items from `sandwich_orders` to `finished_sandwiches`; remove `'pastrami'`.
- Dream vacation poll with a dictionary.

### 7.10 Key Takeaways

- `input()` returns a string — convert with `int()` / `float()`.
- `while` loops repeat until the condition is false.
- Use a flag for multi-condition stopping.
- `break` exits, `continue` skips.
- `while` + `pop()` moves items between lists.
- Every loop must make progress toward termination.

---

## Chapter 8 — Functions

### 8.1 Defining a Function

```python
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()
```

- `def` + name + parentheses + colon.
- Body is indented.
- The **docstring** `"""..."""` documents what the function does.
- Define before you call (top-to-bottom execution).

### 8.2 Passing Information to a Function

```python
def greet_user(username):
    """Display a personalized greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('sarah')
```

- `username` = **parameter** (in the definition).
- `'jesse'` = **argument** (the actual value passed in).

### 8.3 Positional vs Keyword Arguments

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')              # positional: order matters
describe_pet(animal_type='hamster', pet_name='harry')   # keyword: order free
describe_pet(pet_name='harry', animal_type='hamster')   # still works
```

> ⚠️ Positional arguments must come **before** keyword arguments in a call.

### 8.4 Default Values

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')                                  # uses 'dog'
describe_pet(pet_name='willie')                         # uses 'dog'
describe_pet('harry', 'hamster')                        # overrides
describe_pet(pet_name='harry', animal_type='hamster')   # overrides
```

> **Rule:** parameters **with** defaults must come **after** parameters without defaults.

### 8.5 Return Values

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)      # Jimi Hendrix
```

- `return` sends a value back and **ends the function**.
- A function without `return` returns `None`.

#### Making an argument optional

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('john', 'hooker', 'lee'))
```

#### Returning a dictionary

```python
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

### 8.6 Using a Function with a `while` Loop

```python
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

### 8.7 Passing a List

```python
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

#### Modifying a list in a function

```python
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

> Lists are passed **by reference** — the function mutates the original.

#### Preventing a function from modifying a list

```python
print_models(unprinted_designs[:], completed_models)
```

`[:]` passes a **copy**; the original survives.

### 8.8 Arbitrary Number of Arguments

#### `*args` — positional variable arguments

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

`toppings` is a **tuple**.

#### `**kwargs` — arbitrary keyword arguments

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)
# {'location': 'princeton', 'field': 'physics',
#  'first_name': 'albert', 'last_name': 'einstein'}
```

`user_info` is a **dictionary**.

#### Mixing argument types

Order in the definition must be:
`normal params → *args → default params → **kwargs` (roughly; defaults before `*args` also work).

### 8.9 Modules

A **module** is a `.py` file full of functions/classes you can import.

**`pizza.py`**

```python
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

**`making_pizzas.py`**

```python
import pizza
pizza.make_pizza(16, 'pepperoni')
```

#### Import styles

```python
import pizza                          # module.function()
from pizza import make_pizza          # function()
from pizza import make_pizza as mp    # mp()
import pizza as p                     # p.make_pizza()
from pizza import *                   # ⚠️ avoid: name collisions
```

> Best practice: import only what you need, or `import module`, to keep names clear.

### 8.10 Styling Functions (PEP 8)

- `snake_case` names.
- Docstring right after `def`.
- 2 blank lines between top-level functions.
- Default values with **no spaces** around `=`: `def f(x=1):`.
- Keyword arguments in calls: spaces around `=` are fine if you like: `f(x=1)`.

### 8.11 Chapter 8 Exercises (summary)

- Message: define and call a display function.
- Favorite book: function with a title parameter.
- T-shirt: `make_shirt(size, message)`; default `size='L'` and message.
- Cities/Country: default country; keyword args.
- Album: optional number of tracks; return a dict.
- User profile: `**kwargs`-style profile builder.
- Cars: `make_car(manufacturer, model, **options)`.
- Printing models / unprinted designs: mutate vs copy with `[:]`.
- Sandwiches: `*args`.
- Import practice: create a module and import it several ways.

### 8.12 Key Takeaways

- `def name(params):` + docstring + body.
- Positional → keyword → defaults; defaults go last.
- `return` sends a value back; no `return` → `None`.
- Lists mutate inside functions unless copied with `[:]`.
- `*args` → tuple, `**kwargs` → dict.
- Modules: `import`, `from ... import ...`, `as`.

---

## Chapter 9 — Classes

### 9.1 Creating and Using a Class

A **class** bundles data (attributes) and behavior (methods). An **object/instance** is one thing built from the class.

```python
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
```

Key ideas:

- `class Dog:` — class name in **PascalCase**.
- `__init__()` — the **initializer**, runs automatically when you create an instance.
- `self` — refers to the instance itself; **always the first parameter** of a method.
- `self.name = name` — attaches an **attribute** to the instance.

### 9.2 Making an Instance

```python
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
```

Output:

```
My dog's name is Willie.
My dog is 6 years old.
```

#### Calling methods

```python
my_dog.sit()
my_dog.roll_over()
```

Output:

```
Willie is now sitting.
Willie rolled over!
```

#### Creating many instances

```python
your_dog = Dog('Lucy', 3)
your_dog.sit()
```

Each instance has its own attributes; the methods are shared.

### 9.3 Working with Classes and Instances

#### The `Car` class

```python
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject any attempt to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
```

Usage:

```python
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23      # direct modification
my_new_car.read_odometer()

my_new_car.update_odometer(23_500)    # through a method
my_new_car.increment_odometer(100)
```

#### Default attribute values

Set defaults in `__init__` (here `odometer_reading = 0`) or as a class-level attribute.

#### Why methods beat direct access

Methods can **validate** changes (e.g., no rolling back the odometer). Direct attribute access skips validation.

### 9.4 Inheritance

One class (child) inherits from another (parent):

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
```

- `class ElectricCar(Car):` — inherits everything from `Car`.
- `super().__init__(...)` — calls the parent's initializer.
- Child can add new attributes/methods.
- Child can **override** a parent method by redefining it.

Usage:

```python
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

#### Composition (a class inside a class)

```python
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
```

Then:

```python
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

This is **composition**: one object owns another.

### 9.5 Importing Classes

Put classes in their own modules:

**`car.py`**

```python
class Car:
    ...
```

**`my_car.py`**

```python
from car import Car
my_new_car = Car('audi', 'a4', 2019)
```

Import styles:

```python
from car import Car
from car import Car, ElectricCar
from car import Car as C
import car
from car import *
```

#### `__init__.py` (packages)

A folder of modules is a **package**. An `__init__.py` file marks it as importable, e.g.:

```
electric_car/
├── __init__.py
├── car.py
└── battery.py
```

### 9.6 The Python Standard Library

Python ships with a huge library. Example — `random`:

```python
from random import randint, choice

randint(1, 6)                         # random int 1–6 inclusive
choice(['rock', 'paper', 'scissors']) # random item
```

Other must-know modules: `math`, `datetime`, `json`, `os`, `pathlib`, `sys`, `collections`, `itertools`, `statistics`, `random`.

### 9.7 Styling Classes

- `PascalCase` for class names.
- Docstring immediately after `class`.
- One blank line between methods; two blank lines around top-level classes.
- `self` always first; don't rename it.
- Keep methods focused; move helpers into their own classes.

### 9.8 Chapter 9 Exercises (summary)

- Restaurant: `Restaurant(name, cuisine)` with `describe_restaurant()` and `open_restaurant()`.
- Three restaurants: create multiple instances.
- Users: `User(first_name, last_name, ...)` with `describe_user()` and `greet_user()`.
- Login attempts: track `login_attempts` and increment/reset.
- Ice cream stand: inherit from `Restaurant`.
- Admin: inherit from `User`, add privileges; then use a `Privileges` class (composition).
- Battery upgrade: `Battery` class with `upgrade_battery()`.
- Imported restaurant / admin: split classes into modules.

### 9.9 Key Takeaways

- A class is a blueprint; an instance is a concrete object.
- `__init__` + `self` initialize attributes.
- Methods define behavior; call them with `instance.method()`.
- Default attribute values go in `__init__`.
- Inheritance: `class Child(Parent)`, `super().__init__(...)`.
- Composition: `self.battery = Battery()`.
- Import classes from modules to keep files manageable.

---

## Chapter 10 — Files and Exceptions

### 10.1 Reading from a File

Assume `pi_digits.txt` contains `3.1415926535 8979323846 2643383279`.

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
```

- `pathlib.Path` is the modern, cross-platform way to handle paths.
- `read_text()` returns the whole file as one string.
- Paths are **relative to the current working directory** (where you run the script), not the script file.

#### Removing trailing blank lines

```python
contents = path.read_text()
contents = contents.rstrip()
print(contents)
```

#### Relative vs absolute paths

- **Relative:** `Path('text_files/filename.txt')` — from the current working directory.
- **Absolute:** `Path('/home/eric/data.txt')` (Linux/macOS) or `Path('C:/Users/...')`.
- Get absolute path: `path.absolute()`.

#### Accessing lines

```python
path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
```

#### Working with a file's contents

```python
path = Path('pi_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

> Don't build huge strings with `+=` in a loop for big files — use `''.join(parts)`.

#### Large files (one million digits)

```python
path = Path('pi_million_digits.txt')
contents = path.read_text()

pi_string = ''
for line in contents.splitlines():
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

#### Checking whether a file exists

```python
path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
```

### 10.2 Writing to a File

```python
from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.")
```

#### Writing multiple lines

```python
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path.write_text(contents)
```

> ⚠️ `write_text()` **overwrites** the entire file. To append, read first and write back, or use `open(path, 'a')`.

#### Using `open()` modes

| Mode | Meaning |
|------|---------|
| `'r'` | read (default) |
| `'w'` | write (truncate/overwrite) |
| `'a'` | append |
| `'x'` | create, fail if exists |
| `'r+'` | read and write |
| `'b'` | binary (combine: `'rb'`, `'wb'`) |

```python
with open('programming.txt', 'a') as f:
    f.write("I love Python.\n")
```

`with` automatically closes the file, even if an error occurs.

### 10.3 Exceptions

An **exception** is Python's way of saying "something went wrong". Unhandled → traceback → program crashes.

#### `ZeroDivisionError`

```python
print(5 / 0)
# ZeroDivisionError: division by zero
```

#### `try-except`

```python
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

The program keeps running.

#### `try-except-else`

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

- `try` — code that might fail.
- `except` — what to do if it fails.
- `else` — runs only if `try` succeeded.

#### `try-except-else-finally`

```python
try:
    ...
except SomeError:
    ...
else:
    ...
finally:
    ...   # always runs (cleanup)
```

#### Handling `FileNotFoundError`

```python
from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)
```

#### Failing silently with `pass`

```python
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    pass        # do nothing — acceptable when the error is expected
```

> `pass` should be rare and deliberate. Don't hide bugs.

#### Deciding which errors to catch

- Catch only errors you can **handle meaningfully**.
- Don't wrap everything in a bare `except:` — it hides typos and real bugs.
- Catch specific exceptions: `FileNotFoundError`, `ZeroDivisionError`, `ValueError`, `KeyError`, `TypeError`.

### 10.4 Storing Data with `json`

**JSON** (JavaScript Object Notation) is a text format for sharing data.

#### `json.dumps()` — Python → JSON string

```python
import json

numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)
```

#### `json.loads()` — JSON string → Python

```python
import json

path = Path('numbers.json')
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)
```

#### `json.dump()` / `json.load()` — file helpers

```python
import json

with open('numbers.json', 'w') as f:
    json.dump(numbers, f)

with open('numbers.json') as f:
    numbers = json.load(f)
```

#### Saving and reading user data

```python
import json

# Save
username = input("What is your name? ")
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)
print(f"We'll remember you when you come back, {username}!")

# Load / greet
path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")
```

#### Refactoring into functions

```python
import json
from pathlib import Path

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()
```

### 10.5 Chapter 10 Exercises (summary)

- Learning Python: read a file and print its contents.
- Guest: write a name to `guest.txt`.
- Guest book: append names until `'quit'`.
- Guest list: read the guest book back.
- Addition: `try/except` around two-number addition.
- Cats and dogs: read two files; handle missing files with `pass`.
- Silent cats and dogs / common words: count words in files.
- Favorite number: save and load with `json`.

### 10.6 Key Takeaways

- `Path.read_text()` reads, `Path.write_text()` writes (overwrites).
- Use `with open(...)` for append mode or big files.
- `try/except/else/finally` controls failure flow.
- Catch **specific** exceptions; use `pass` sparingly.
- JSON is the standard for saving simple Python data.
- Every file operation can fail — plan for it.

---

## Chapter 11 — Testing Your Code

### 11.1 Why Test?

Tests verify that code behaves as expected, catch regressions when you change things, and force you to define what "correct" means.

### 11.2 Testing a Function

**`name_function.py`**

```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()
```

**`test_name_function.py`** (pytest style, 3rd edition)

```python
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

Run:

```bash
pytest
# or
pytest test_name_function.py
```

Output:

```
==================== test session starts ====================
collected 1 item

test_name_function.py .                              [100%]

===================== 1 passed in 0.01s =====================
```

#### A failing test

```python
def test_first_last_name():
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

If the function returns something else, pytest shows the expected vs actual values and the failing line.

#### Adding a middle name

```python
def get_formatted_name(first, middle, last):
    full_name = f"{first} {middle} {last}"
    return full_name.title()
```

Now `test_first_last_name` fails — this is the **point**: tests catch breakage. Fix the function to make the middle name optional:

```python
def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

Add tests for both cases:

```python
def test_first_last_name():
    assert get_formatted_name('janis', 'joplin') == 'Janis Joplin'

def test_first_last_middle_name():
    assert get_formatted_name('wolfgang', 'mozart', 'amadeus') == 'Wolfgang Amadeus Mozart'
```

### 11.3 Testing a Class

**`survey.py`**

```python
class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

**`test_survey.py`** with pytest fixtures

```python
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    return AnonymousSurvey(question)

def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
```

- `@pytest.fixture` — a setup function reused by tests.
- Each test gets a **fresh** survey instance (isolation).
- Test names must start with `test_`.
- Use `assert` for checks.

### 11.4 The Classic `unittest` Approach

The 2nd edition used `unittest`; it's still worth knowing.

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
```

Run:

```bash
python -m unittest test_name_function.py
```

`unittest` assertions: `assertEqual`, `assertNotEqual`, `assertTrue`, `assertFalse`, `assertIn`, `assertNotIn`, `assertRaises`.

### 11.5 Testing Best Practices

- **One behavior per test** — easy to diagnose failures.
- **Descriptive test names** — `test_first_last_name` beats `test1`.
- **Arrange–Act–Assert** — set up, call, check.
- Test **edge cases**: empty input, wrong types, boundaries.
- Tests should be **independent** — no shared mutable state.
- Run tests often; run all tests before committing.
- Don't test the library — test **your** logic.

### 11.6 Chapter 11 Exercises (summary)

- City, Country: `city_country(city, country)` and tests.
- Population: optional population parameter and tests.
- Employee: `Employee(first, last, salary)` with `give_raise()`; test default and custom raises with pytest fixtures.
- (Also practice converting a `unittest` test to pytest.)

### 11.7 Key Takeaways

- `assert` + pytest is the modern minimal testing setup.
- `pytest` auto-discovers `test_*.py` / `*_test.py` and `test_*` functions.
- Fixtures provide reusable setup.
- A failing test after a change is a **feature**, not a problem.
- Test behavior, not implementation details.

---

# PART II — PROJECTS

---

## Project 1 — Alien Invasion (Chapters 12–14)

A 2D arcade game: a ship at the bottom shoots bullets at a fleet of aliens. You control the ship with arrow keys and Space to fire.

**Skills:** Pygame, game loop, event handling, sprites, collision detection, refactoring, game state, JSON persistence.

**Final project structure** (3rd edition style):

```
alien_invasion/
├── alien_invasion.py      # main game loop and AlienInvasion class
├── settings.py            # Settings class
├── ship.py                # Ship class
├── bullet.py              # Bullet class
├── alien.py               # Alien class
├── game_stats.py          # GameStats class
├── scoreboard.py          # Scoreboard class
├── button.py              # Play button
└── images/
    ├── ship.bmp
    └── alien.bmp
```

**Install Pygame:**

```bash
python -m pip install --user pygame
# or inside a venv:
pip install pygame
```

> The 3rd edition eliminated the old `game_functions.py` module. Game logic now lives in methods on the `AlienInvasion` class (`_check_events()`, `_update_screen()`, `_update_bullets()`, etc.) and in the sprite classes.

---

## Chapter 12 — A Ship That Fires Bullets

### 12.1 Starting the Game Project

`alien_invasion.py` (initial version):

```python
import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
```

### 12.2 The `Settings` Class

`settings.py`:

```python
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
```

- Colors are `(R, G, B)` tuples, each 0–255.
- Keeping settings in one class makes tuning easy and avoids magic numbers.

### 12.3 Adding the Ship

`ship.py`:

```python
import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

Key ideas:

- `pygame.image.load()` loads a bitmap.
- `image.get_rect()` gives a rectangle with position/size.
- `screen.blit(image, rect)` draws it.
- Store a **float** `self.x` so fractional speeds work; copy to `rect.x` (ints) for drawing.
- Clamp movement to screen edges.

### 12.4 Refactoring: `_check_events()`

Handling every key in one giant `if` gets messy. Split into helpers:

```python
def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

def _check_keyup_events(self, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
```

> Refactoring = improving structure **without changing behavior**. Do it as you go.

### 12.5 Adding Bullets

`bullet.py`:

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

`Sprite` is Pygame's base class for game objects; `Group` manages collections of sprites efficiently.

### 12.6 Storing Bullets in a Group

In `AlienInvasion.__init__()`:

```python
self.bullets = pygame.sprite.Group()
```

Firing:

```python
def _check_keydown_events(self, event):
    ...
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()

def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    self.bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)
```

Draw them in `_update_screen()`:

```python
for bullet in self.bullets.sprites():
    bullet.draw_bullet()
```

> Iterate over `self.bullets.copy()` when removing, because you can't modify a group while iterating over it directly.

### 12.7 Game Loop Summary

```python
while True:
    self._check_events()      # input
    self.ship.update()        # physics/logic
    self._update_bullets()    # bullets
    self._update_screen()     # render
    self.clock.tick(60)       # 60 FPS cap
```

Order matters: handle input → update state → draw. `clock.tick(60)` keeps the game at 60 frames per second on every machine.

### 12.8 Chapter 12 Exercises (summary)

- **Blue Sky:** change the background color.
- **Raindrops:** create a grid of raindrops falling; recycle them at the top.
- **Better Stars:** random star field.

### 12.9 Key Takeaways

- Pygame needs `pygame.init()`, a display surface, and a game loop.
- The loop does: events → update → draw → tick.
- `Sprite` + `Group` is the standard way to manage many objects.
- Refactor into methods/classes early.
- `pygame.Rect` handles positions and collision geometry.

---

## Chapter 13 — Aliens!

### 13.1 The Alien Class

`alien.py`:

```python
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
```

Add alien settings:

```python
self.alien_speed = 1.0
self.fleet_drop_speed = 10
self.fleet_direction = 1     # 1 = right, -1 = left
```

### 13.2 Creating the Fleet

In `AlienInvasion.__init__()`:

```python
self.aliens = pygame.sprite.Group()
self._create_fleet()
```

Methods:

```python
def _create_fleet(self):
    """Create the fleet of aliens."""
    # Create an alien and keep adding aliens until there's no room left.
    # Spacing between aliens is one alien width and one alien height.
    alien = Alien(self)
    alien_width, alien_height = alien.rect.size

    current_x, current_y = alien_width, alien_height
    while current_y < (self.settings.screen_height - 3 * alien_height):
        while current_x < (self.settings.screen_width - 2 * alien_width):
            self._create_alien(current_x, current_y)
            current_x += 2 * alien_width

        # Finished a row; reset x value, and increment y value.
        current_x = alien_width
        current_y += 2 * alien_height

def _create_alien(self, x_position, y_position):
    """Create an alien and place it in the row."""
    new_alien = Alien(self)
    new_alien.x = x_position
    new_alien.rect.x = x_position
    new_alien.rect.y = y_position
    self.aliens.add(new_alien)
```

Draw in `_update_screen()`:

```python
self.aliens.draw(self.screen)
```

### 13.3 Making the Fleet Move

```python
def _update_aliens(self):
    """Check if the fleet is at an edge, then update positions."""
    self._check_fleet_edges()
    self.aliens.update()

def _check_fleet_edges(self):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in self.aliens.sprites():
        if alien.check_edges():
            self._change_fleet_direction()
            break

def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in self.aliens.sprites():
        alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1
```

Call `self._update_aliens()` in the main loop after updating bullets.

### 13.4 Shooting Aliens

```python
def _update_bullets(self):
    ...
    self._check_bullet_alien_collisions()

def _check_bullet_alien_collisions(self):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True)

    if not self.aliens:
        # Destroy existing bullets and create a new fleet.
        self.bullets.empty()
        self._create_fleet()
```

`groupcollide(group1, group2, kill1, kill2)`:
- `True` for `kill1` removes the bullet on collision.
- `True` for `kill2` removes the alien.
- Returns a dict of collisions.

> For explosive bullets that destroy multiple aliens, set `kill2=True` and modify `kill1` behavior, or keep bullets and clear them manually.

### 13.5 Ship–Alien Collisions and Game Over

```python
def _ship_hit(self):
    """Respond to the ship being hit by an alien."""
    if self.stats.ships_left > 0:
        # Decrement ships_left.
        self.stats.ships_left -= 1

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Pause.
        sleep(0.5)
    else:
        self.stats.game_active = False
```

Add to `_update_aliens()`:

```python
# Look for alien-ship collisions.
if pygame.sprite.spritecollideany(self.ship, self.aliens):
    self._ship_hit()

# Look for aliens hitting the bottom of the screen.
self._check_aliens_bottom()

def _check_aliens_bottom(self):
    """Check if any aliens have reached the bottom of the screen."""
    for alien in self.aliens.sprites():
        if alien.rect.bottom >= self.settings.screen_height:
            # Treat this the same as if the ship got hit.
            self._ship_hit()
            break
```

Game over handling in `run_game()`:

```python
while True:
    self._check_events()
    if self.stats.game_active:
        self.ship.update()
        self._update_bullets()
        self._update_aliens()
    self._update_screen()
    self.clock.tick(60)
```

`Ship.center_ship()`:

```python
def center_ship(self):
    """Center the ship on the screen."""
    self.rect.midbottom = self.screen_rect.midbottom
    self.x = float(self.rect.x)
```

### 13.6 Chapter 13 Exercises (summary)

- **Stars:** create a star field by replacing the alien image.
- **Fleet of 1000 aliens:** experiment with spacing/scroll speed.
- **Random alien placement:** build a fleet with random positions.
- **Alien speed:** make some aliens faster than others.

### 13.7 Key Takeaways

- `Sprite` + `Group` scales from 1 alien to hundreds.
- Fleet movement = move all aliens, flip direction at edges, drop down.
- `groupcollide()` and `spritecollideany()` handle collisions.
- Reset state (bullets, aliens, ship) after a hit.
- A `game_active` flag pauses updates without exiting the loop.

---

## Chapter 14 — Scoring

### 14.1 Adding the Play Button

`button.py`:

```python
import pygame.font

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
```

In `AlienInvasion.__init__()`:

```python
self.play_button = Button(self, "Play")
```

Draw it when the game is inactive:

```python
if not self.stats.game_active:
    self.play_button.draw_button()
```

Handle clicks:

```python
elif event.type == pygame.MOUSEBUTTONDOWN:
    mouse_pos = pygame.mouse.get_pos()
    self._check_play_button(mouse_pos)

def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.stats.game_active:
        # Reset the game settings.
        self.settings.initialize_dynamic_settings()

        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
```

Show the cursor again when the game ends.

### 14.2 The `GameStats` Class

`game_stats.py`:

```python
class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
```

Add `ship_limit = 3` to `Settings`.

### 14.3 The Scoreboard

`scoreboard.py`:

```python
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
```

### 14.4 Updating the Score

In `_check_bullet_alien_collisions()`:

```python
collisions = pygame.sprite.groupcollide(
    self.bullets, self.aliens, True, True)

if collisions:
    for aliens in collisions.values():
        self.stats.score += self.settings.alien_points * len(aliens)
    self.sb.prep_score()
    self.sb.check_high_score()
```

`alien_points` in settings (e.g., `50`).

### 14.5 Leveling Up

```python
def _check_bullet_alien_collisions(self):
    ...
    if not self.aliens:
        # Destroy existing bullets and create a new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()
```

`Settings`:

```python
def initialize_dynamic_settings(self):
    """Initialize settings that change throughout the game."""
    self.ship_speed = 1.5
    self.bullet_speed = 2.0
    self.alien_speed = 1.0

    self.fleet_direction = 1

    self.alien_points = 50

def increase_speed(self):
    """Increase speed settings and alien point values."""
    self.ship_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale

    self.alien_points = int(self.alien_points * self.score_scale)
```

With `self.speedup_scale = 1.1` and `self.score_scale = 1.5`.

Call `initialize_dynamic_settings()` in `Settings.__init__()` so the game starts with valid values.

### 14.6 Persisting the High Score

Store it in `high_score.json`:

```python
def _check_high_score(self):
    if self.stats.score > self.stats.high_score:
        self.stats.high_score = self.stats.score
        self.prep_high_score()
```

Save on quit:

```python
def _check_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            self._save_high_score()
            sys.exit()
        ...
```

Load on start:

```python
from pathlib import Path
import json

self.high_score_path = Path('high_score.json')
if self.high_score_path.exists():
    self.stats.high_score = json.loads(self.high_score_path.read_text())
```

### 14.7 Chapter 14 Exercises (summary)

- **Scoring:** show a "Level" label and extra ships.
- **High score:** persist it to a file (as above).
- **Button:** style the Play button; add a "Quit" button.
- **Difficulty:** add a settings screen/difficulty levels.

### 14.8 Key Takeaways

- Render text with `font.render()` and blit it.
- `GameStats` keeps mutable state (`score`, `ships_left`, `level`).
- Dynamic settings scale difficulty each level.
- `round(score, -1)` rounds to the nearest 10; `f"{n:,}"` adds commas.
- Buttons need hit-testing with `rect.collidepoint(mouse_pos)`.
- Persist high scores with JSON.
- `pygame.mouse.set_visible()` toggles the cursor during play.

---

## Project 2 — Data Visualization (Chapters 15–17)

Turn data into charts, maps, and interactive plots. Tools: **Matplotlib** (static plots) and **Plotly** (interactive browser plots).

```bash
python -m pip install matplotlib plotly
```

---

## Chapter 15 — Generating Data

### 15.1 Plotting a Simple Line Graph

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()
```

- `plt.subplots()` returns a **figure** (`fig`) and an **axes** object (`ax`).
- `ax.plot(data)` draws a line.
- `plt.show()` opens the plot window.

#### Changing labels and line thickness

```python
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
```

#### Providing input values

If you pass only y-values, x defaults to `0, 1, 2, ...`. Pass x explicitly:

```python
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
...
```

#### Using built-in styles

```python
plt.style.use('seaborn-v0_8')
# other options: 'ggplot', 'fivethirtyeight', 'dark_background', 'bmh'
```

> Style names changed across Matplotlib versions; `plt.style.available` lists valid ones.

### 15.2 Scatter Plots

```python
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)
```

- `scatter()` draws points; `s` = marker size.
- `c` = color (name, hex, or RGB tuple).
- `edgecolors='none'` removes marker outlines.

#### A thousand points

```python
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)
ax.axis([0, 1100, 0, 1_100_000])

plt.show()
```

#### Colormaps

```python
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
```

Small y-values → light blue, large → dark blue.

#### Saving plots

```python
plt.savefig('squares_plot.png', bbox_inches='tight')
```

Call `savefig()` **before** `show()`.

### 15.3 Random Walks

A random walk: repeatedly pick a random direction and step.

`random_walk.py`:

```python
from random import choice

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
```

Plotting:

```python
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=15)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
```

Key points:
- Large walks (50,000 points) show diffusion patterns.
- Color by point number to show time progression.
- `figsize=(15, 9)` sets figure dimensions in inches.
- `continue` skips zero-length steps.

### 15.4 Rolling Dice with Plotly

`die.py`:

```python
from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
```

Rolling and tallying:

```python
from die import Die

die = Die()
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
```

#### Visualizing with Plotly

```python
import plotly.express as px

fig = px.bar(
    x=list(poss_results),
    y=frequencies,
    labels={'x': 'Result', 'y': 'Frequency of Result'},
    title='Results of Rolling One D6 1,000 Times',
)
fig.show()
```

> The book uses Plotly's `Bar`/`Layout` graph-objects API in earlier editions. `plotly.express` is the modern, concise wrapper — both produce the same interactive HTML chart.

#### Two dice (D6 + D6)

```python
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

frequencies = [results.count(value) for value in poss_results]

fig = px.bar(
    x=list(poss_results),
    y=frequencies,
    labels={'x': 'Result', 'y': 'Frequency of Result'},
    title='Results of Rolling Two D6 Dice 1,000 Times',
)
fig.show()
```

The triangular distribution appears — sums near 7 are most common.

#### Saving and customizing

```python
fig.write_html('dice_visualization.html')
fig.update_layout(title='Results of Rolling Two D6 1,000 Times',
                  xaxis_title='Result', yaxis_title='Frequency')
```

With more rolls (e.g., 50,000), the shape becomes smooth and bell-like.

### 15.5 Chapter 15 Exercises (summary)

- **Cubes:** plot cubes of numbers 1–5000; use a colormap.
- **Colored cubes:** color points by value.
- **Molecular motion:** simulate particles moving randomly.
- **Three dice:** roll three D6 and plot the distribution.
- **Multiplication:** multiply two dice instead of adding, and plot.
- **Die class:** add a `roll_die()` method with a custom number of sides.

### 15.6 Key Takeaways

- `fig, ax = plt.subplots()` is the modern Matplotlib pattern.
- `plot()` = line, `scatter()` = points; use `c`, `cmap`, `s` for style.
- `savefig()` before `show()`.
- Random walks: random direction + distance, reject zero moves.
- Plotly makes interactive, browser-based charts.
- Frequencies: `results.count(value)` per possible value.

---

## Chapter 16 — Downloading Data

Real datasets come as **CSV**, **JSON**, or from **APIs**. This chapter processes weather CSVs, earthquake JSON, and plots them.

### 16.1 The CSV File Format

CSV = comma-separated values, one record per line.

```
"USW00025333","SITKA AIRPORT, AK US","2021-01-01",0.0,...
```

Read with the built-in `csv` module:

```python
import csv
from pathlib import Path

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)
```

- `csv.reader()` yields rows as lists of strings.
- `next(reader)` grabs the header row.
- `enumerate()` gives index + value.

#### Extracting and reading data

```python
import matplotlib.pyplot as plt
from datetime import datetime

# Extract dates and high temperatures.
dates, highs, lows = [], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

# Plot the high and low temperatures.
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
```

- `datetime.strptime(string, format)` parses dates.
- `%Y-%m-%d` = year-month-day.
- `alpha` controls transparency; `fill_between()` shades the range.

#### Formatting the plot

```python
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=20)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(labelsize=14)
```

`fig.autofmt_xdate()` rotates date labels so they don't overlap.

#### Handling missing data

Real CSVs have blanks or bad values:

```python
for row in reader:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
```

> `continue` skips the bad row; `else` runs only when the `try` succeeds.

#### Comparing two locations (Death Valley vs Sitka)

Open two files, build two sets of lists, plot both with labels and a legend:

```python
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates_sitka, highs_sitka, color='blue', alpha=0.5)
```

Use different colors and `label=` + `ax.legend()`.

### 16.2 The JSON Format

JSON structures: objects `{}` (dicts), arrays `[]` (lists), strings, numbers, booleans, `null`.

Earthquake data (USGS GeoJSON) looks like:

```json
{
  "type": "FeatureCollection",
  "metadata": {"count": 1234},
  "features": [
    {
      "properties": {"mag": 5.2, "place": "..."},
      "geometry": {"coordinates": [-120.5, 35.2, 10.0]}
    }
  ]
}
```

#### Reading JSON

```python
import json
from pathlib import Path

path = Path('eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Explore the structure.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
```

#### Extracting magnitudes and locations

```python
mags, lons, lats, eq_titles = [], [], [], []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(title)

print(mags[:10])
print(lons[:5])
```

Key point: navigate nested dicts/lists one key/index at a time. Print intermediate values when unsure.

#### Plotting earthquakes on a world map with Plotly

```python
import plotly.express as px

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title='Global Earthquakes',
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles,
)
fig.show()
```

- `scatter_geo` draws points on a world map.
- `size` scales marker size by magnitude.
- `hover_name` shows text on hover.
- `projection` selects the map projection.

### 16.3 Other Data Sources

- **CSV**: weather bureaus, government open-data portals, Kaggle.
- **JSON**: APIs, GeoJSON maps, configuration files.
- **APIs** (next chapter): live data, often JSON.

Always check:
- Missing/invalid values.
- Data licenses/attribution.
- Encoding (`utf-8`).
- File size — stream large files instead of `read_text()`.

### 16.4 Chapter 16 Exercises (summary)

- **San Francisco temperatures:** reuse the weather code on a second city.
- **Sitka vs Death Valley:** compare highs/lows on one chart.
- **Chicago:** handle missing data.
- **Earthquake magnitudes:** filter for mag ≥ 5.
- **World fires:** download a fire dataset and map it.
- **Global earthquakes:** plot the last 30 days with size/color by magnitude.

### 16.5 Key Takeaways

- `csv.reader` + `next()` for headers; `enumerate()` for column indexes.
- `datetime.strptime()` parses dates; `autofmt_xdate()` fixes labels.
- `try/except` around data conversion handles missing values.
- `json.loads()` turns JSON text into Python dicts/lists.
- Nested data is navigated key-by-key.
- Plotly `scatter_geo` makes world maps with size/color encodings.

---

## Chapter 17 — Working with APIs

An **API** (Application Programming Interface) lets your program request data from another service over HTTP.

### 17.1 Using an API

```bash
python -m pip install --user requests
```

Basic request:

```python
import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)

print(f"Status code: {r.status_code}")
```

#### Status codes

| Code | Meaning |
|------|---------|
| `200` | OK |
| `301`/`302` | Redirect |
| `400` | Bad request |
| `401` | Unauthorized |
| `403` | Forbidden / rate-limited |
| `404` | Not found |
| `500` | Server error |

#### Inspect the response

```python
response_dict = r.json()
print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
```

#### Extracting information

```python
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
```

#### Monitoring rate limits

```python
print(f"Rate limit: {r.headers.get('X-RateLimit-Limit')}")
print(f"Remaining: {r.headers.get('X-RateLimit-Remaining')}")
```

GitHub's unauthenticated limit is low (≈60 requests/hour); a token raises it.

### 17.2 Visualizing Repositories with Plotly

```python
import plotly.express as px

repo_names = [repo['name'] for repo in repo_dicts]
stars = [repo['stargazers_count'] for repo in repo_dicts]

fig = px.bar(
    x=repo_names,
    y=stars,
    labels={'x': 'Repository', 'y': 'Stars'},
    title='Most-Starred Python Projects on GitHub',
)
fig.show()
```

Add hover data and links:

```python
fig = px.bar(
    x=repo_names, y=stars,
    hover_data=['description', 'html_url'],
)
```

### 17.3 The Hacker News API

```python
import requests

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=lambda x: x['comments'], reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```

Key ideas:
- APIs often require **multiple calls** (one for IDs, one per item).
- `.get('descendants', 0)` handles missing keys.
- `sorted(..., key=lambda x: x['comments'], reverse=True)`.

### 17.4 API Best Practices

- **Read the docs** — endpoints, parameters, response shape, limits.
- **Respect rate limits** — cache, delay, use tokens.
- **Handle errors** — check `status_code` before `.json()`.
- **Use headers** — `Accept`, `Authorization`, `User-Agent`.
- **Don't commit secrets** — store API keys in environment variables.
- **Paginate** — results usually come in pages.
- **Assume fields can be missing** — use `.get()`.

### 17.5 Chapter 17 Exercises (summary)

- **Other languages:** compare top repos by language.
- **Active discussions:** filter Hacker News by comment count.
- **GitHub topics:** query repositories for a topic and chart stars.
- **API explorer:** pick any public API (weather, news, crypto) and build a CLI or chart.

### 17.6 Key Takeaways

- `requests.get()` → check `status_code` → `r.json()`.
- APIs return nested JSON; explore keys before extracting.
- Rate limits and pagination are real constraints.
- Plotly turns API data into interactive charts.
- Multiple API calls are normal for list + detail endpoints.

---

## Project 3 — Web Applications with Django (Chapters 18–20)

Build **Learning Log** — a web app where users register, log in, create topics, and add entries.

**Skills:** Django project/app structure, models, migrations, admin, templates, URLs, views, authentication, Bootstrap, deployment.

**Install Django:**

```bash
python -m pip install --user django
# or in a virtual environment (recommended):
python -m venv ll_env
source ll_env/bin/activate         # macOS / Linux
ll_env\Scripts\activate            # Windows
pip install django
```

---

## Chapter 18 — Getting Started with Django

### 18.1 Creating a Virtual Environment

A **virtual environment** isolates project dependencies.

```bash
mkdir learning_log
cd learning_log
python -m venv ll_env
```

Activate:

| OS | Command |
|----|---------|
| Windows | `ll_env\Scripts\activate` |
| macOS/Linux | `source ll_env/bin/activate` |

Your prompt shows `(ll_env)`. Deactivate with `deactivate`.

> Always create the venv **before** installing Django, and activate it every session.

### 18.2 Creating the Project

```bash
django-admin startproject learning_log .
```

The trailing `.` puts `manage.py` in the current directory instead of nesting another folder.

Result:

```
learning_log/
├── manage.py
├── db.sqlite3
└── learning_log/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

- `manage.py` — command-line utility.
- `settings.py` — configuration.
- `urls.py` — root URL routing.
- `wsgi.py` / `asgi.py` — server entry points.

Run the development server:

```bash
python manage.py runserver
```

Open `http://localhost:8000/` — you should see the Django rocket. Stop with `Ctrl+C`.

> The dev server auto-reloads on file changes; it is **not** for production.

### 18.3 Creating an App

```bash
python manage.py startapp learning_logs
```

Structure:

```
learning_logs/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
├── migrations/
└── __init__.py
```

Register the app in `settings.py`:

```python
INSTALLED_APPS = [
    # My apps
    'learning_logs',

    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### 18.4 Defining Models

Models describe the data; Django creates the database tables.

`learning_logs/models.py`:

```python
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representation of the model."""
        return f"{self.text[:50]}..."
```

Key fields:

| Field | Use |
|-------|-----|
| `CharField(max_length=...)` | Short text (requires max_length) |
| `TextField()` | Long text |
| `DateTimeField(auto_now_add=True)` | Set once on creation |
| `DateTimeField(auto_now=True)` | Update on every save |
| `ForeignKey(Other, on_delete=...)` | Many-to-one relationship |
| `IntegerField`, `BooleanField`, `EmailField`, `URLField`, `ImageField` | Other common types |

`on_delete=models.CASCADE` means deleting a topic deletes its entries.

### 18.5 Migrations

Migrations turn model changes into database changes.

```bash
python manage.py makemigrations learning_logs
python manage.py migrate
```

- `makemigrations` writes a migration file in `migrations/`.
- `migrate` applies pending migrations.
- Re-run both whenever you change `models.py`.

### 18.6 The Django Admin Site

Create an admin user:

```bash
python manage.py createsuperuser
```

Register models in `learning_logs/admin.py`:

```python
from django.contrib import admin
from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)
```

Run the server and visit `http://localhost:8000/admin/`. Log in and add a topic or two.

### 18.7 The Django Shell

```bash
python manage.py shell
```

```python
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>

>>> topics = Topic.objects.all()
>>> for topic in topics:
...     print(topic.id, topic)
...
1 Chess
2 Rock Climbing

>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(...)

>>> t.entry_set.all()
<QuerySet [...]>
```

- `Model.objects.all()` — all records.
- `.get(id=1)` — one record (raises `DoesNotExist` if absent).
- `.filter(...)` — matching records.
- `topic.entry_set` — reverse relation for a `ForeignKey`.

Create records:

```python
>>> t = Topic(text='Chess')
>>> t.save()
>>> t.id
3
```

### 18.8 Making Pages: The Learning Logs Home Page

#### Mapping a URL

`learning_logs/urls.py` (create this file):

```python
"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
```

Include it in the project's `learning_log/urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
]
```

#### Writing a view

`learning_logs/views.py`:

```python
from django.shortcuts import render

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')
```

#### Writing a template

Create `learning_logs/templates/learning_logs/index.html`:

```html
<p>Learning Log</p>

<p>Learning Log helps you keep track of your learning,
for any topic you're curious about.</p>
```

`render(request, template, context)` combines a template with data.

### 18.9 Template Inheritance

`learning_logs/templates/learning_logs/base.html`:

```html
<p>
  <a href="{% url 'learning_logs:index' %}">Learning Log</a>
</p>

{% block content %}{% endblock content %}
```

`index.html`:

```html
{% extends "learning_logs/base.html" %}

{% block content %}
  <p>Learning Log helps you keep track of your learning.</p>
{% endblock content %}
```

- `{% extends %}` must be the **first** template tag.
- `{% block name %}` defines replaceable sections.
- `{% url 'app_name:view_name' %}` builds URLs safely.

### 18.10 Building the Topic Pages

Add URL patterns:

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
```

Views:

```python
from django.shortcuts import render
from .models import Topic

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
```

Templates:

`topics.html`

```html
{% extends "learning_logs/base.html" %}

{% block content %}
  <p>Topics</p>

  <ul>
    {% for topic in topics %}
      <li>
        <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
      </li>
    {% empty %}
      <li>No topics have been added yet.</li>
    {% endfor %}
  </ul>
{% endblock content %}
```

`topic.html`

```html
{% extends "learning_logs/base.html" %}

{% block content %}
  <p>Topic: {{ topic }}</p>

  <p>Entries:</p>
  <ul>
    {% for entry in entries %}
      <li>
        <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
        <p>{{ entry.text|linebreaks }}</p>
      </li>
    {% empty %}
      <li>There are no entries for this topic yet.</li>
    {% endfor %}
  </ul>
{% endblock content %}
```

Template filters: `date:'M d, Y H:i'`, `linebreaks`, `length`, `truncatewords`, `default`.

### 18.11 Chapter 18 Exercises (summary)

- **Blog:** start a blog app with `BlogPost` model and pages.
- **Pizza:** model `Pizza` and `Topping` with a `ForeignKey`.
- **Learning Log additions:** add a description field, ordering, etc.

### 18.12 Key Takeaways

- venv isolates dependencies; activate it every time.
- `startproject` creates the site; `startapp` creates a feature module.
- Models → migrations → database.
- Admin gives a free CRUD UI.
- URLs map paths to views; views render templates with context.
- Template inheritance keeps pages consistent.
- `{% csrf_token %}` is required in every POST form.

---

## Chapter 19 — User Accounts

### 19.1 The `users` App

```bash
python manage.py startapp accounts
```

Add `'accounts'` to `INSTALLED_APPS`.

Add to `learning_log/urls.py`:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('learning_logs.urls')),
]
```

Django's auth URLs provide:

| URL | View |
|-----|------|
| `/accounts/login/` | Login page |
| `/accounts/logout/` | Logout |
| `/accounts/password_change/` | Change password |
| `/accounts/password_reset/` | Reset password |

### 19.2 The Login Page

Create `registration/login.html`:

```html
{% extends "learning_logs/base.html" %}

{% block content %}
  {% if form.errors %}
    <p>Your username and password didn't match. Please try again.</p>
  {% endif %}

  <form action="{% url 'login' %}" method="post">
    {% csrf_token %}
    {{ form.as_div }}
    <button name="submit">Log in</button>
  </form>
{% endblock content %}
```

Settings:

```python
LOGIN_REDIRECT_URL = 'learning_logs:index'
LOGOUT_REDIRECT_URL = 'learning_logs:index'
```

> The `registration/` folder must be inside a `templates/` directory that Django can find. Put it in `learning_logs/templates/registration/login.html` or create a project-level `templates/` folder and add it to `TEMPLATES['DIRS']`.

### 19.3 Logging Out

`base.html`:

```html
<p>
  <a href="{% url 'learning_logs:index' %}">Learning Log</a> -
  <a href="{% url 'learning_logs:topics' %}">Topics</a> -
  {% if user.is_authenticated %}
    Hello, {{ user.username }}.
    <a href="{% url 'logout' %}">Log out</a>
  {% else %}
    <a href="{% url 'login' %}">Log in</a>
  {% endif %}
</p>

{% block content %}{% endblock content %}
```

- `user` is available in every template.
- `user.is_authenticated` is True for logged-in users.
- `{{ user.username }}` shows the name.

### 19.4 Restricting Access with `@login_required`

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Topic

@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
```

Settings:

```python
LOGIN_URL = 'login'
```

Unauthenticated users are redirected to the login page.

### 19.5 Associating Data with Users

Add an owner to `Topic`:

```python
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
```

Migrate:

```bash
python manage.py makemigrations learning_logs
python manage.py migrate
```

> Django will ask for a default value for existing rows. Choose option 1 and enter an id (e.g., `1`), or delete the database for a fresh start.

#### Filter topics by owner

```python
@login_required
def topics(request):
    """Show all topics for the current user."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
```

Import `Http404` from `django.http`.

#### Assign the owner when creating a topic

```python
@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method == 'POST':
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    else:
        form = TopicForm()

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
```

`commit=False` builds the object without saving, so you can add the owner first.

### 19.6 The Registration Page

`accounts/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='register'),
]
```

Include it in the project URLs **before** `django.contrib.auth.urls`:

```python
path('accounts/', include('accounts.urls')),
path('accounts/', include('django.contrib.auth.urls')),
```

`accounts/views.py`:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect to the home page.
            login(request, new_user)
            return redirect('learning_logs:index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)
```

`registration/register.html`:

```html
{% extends "learning_logs/base.html" %}

{% block content %}
  <form action="{% url 'accounts:register' %}" method="post">
    {% csrf_token %}
    {{ form.as_div }}
    <button name="submit">Register</button>
  </form>
{% endblock content %}
```

Add a register link to `base.html`:

```html
<a href="{% url 'accounts:register' %}">Register</a>
```

### 19.7 Forms (ModelForm)

`learning_logs/forms.py`:

```python
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
```

Views for adding entries:

```python
@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    else:
        form = EntryForm()

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)
```

### 19.8 Chapter 19 Exercises (summary)

- **Blog accounts:** restrict blog posts to their authors.
- **Registration flow:** redirect new users to a profile/setup page.
- **Password reset:** configure email backend and test the reset flow.
- **Permissions:** add an "edit entry" page with ownership checks.

### 19.9 Key Takeaways

- `django.contrib.auth` gives login/logout/password management for free.
- `@login_required` protects views; `LOGIN_URL` sets the redirect.
- Add `owner = ForeignKey(User)` to make data per-user.
- Filter querysets by `request.user`; check ownership before showing objects.
- `UserCreationForm` + `login()` handles registration.
- `commit=False` lets you fill extra fields before saving.

---

## Chapter 20 — Styling and Deploying an App

### 20.1 Styling with Bootstrap

```bash
pip install django-bootstrap5
```

Add to `INSTALLED_APPS`:

```python
'django_bootstrap5',
```

`base.html`:

```html
{% load django_bootstrap5 %}

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Learning Log</title>

  {% bootstrap_css %}
  {% bootstrap_javascript %}
</head>
<body>

  <nav class="navbar navbar-expand-md navbar-light bg-light mb-4 border">
    <div class="container-fluid">
      <a class="navbar-brand" href="{% url 'learning_logs:index' %}">
        Learning Log</a>

      <button class="navbar-toggler" type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarCollapse"
              aria-controls="navbarCollapse"
              aria-expanded="false"
              aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarCollapse">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item">
            <a class="nav-link" href="{% url 'learning_logs:topics' %}">
              Topics</a>
          </li>
        </ul>

        <ul class="navbar-nav">
          {% if user.is_authenticated %}
            <li class="nav-item">
              <span class="navbar-text me-2">Hello, {{ user.username }}.</span>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'logout' %}">Log out</a>
            </li>
          {% else %}
            <li class="nav-item">
              <a class="nav-link" href="{% url 'accounts:register' %}">
                Register</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{% url 'login' %}">Log in</a>
            </li>
          {% endif %}
        </ul>
      </div>
    </div>
  </nav>

  <main class="container">
    <div class="pb-2 mb-2 border-bottom">
      {% block page_header %}{% endblock page_header %}
    </div>
    <div>
      {% block content %}{% endblock content %}
    </div>
  </main>

</body>
</html>
```

#### Styling forms with `django-bootstrap5`

```html
{% extends "learning_logs/base.html" %}
{% load django_bootstrap5 %}

{% block page_header %}
  <h1>Add a new topic</h1>
{% endblock page_header %}

{% block content %}
  <form action="{% url 'learning_logs:new_topic' %}" method="post">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="Add topic" %}
  </form>
{% endblock content %}
```

#### Styling the topics list

```html
{% block content %}
  <ul class="list-group">
    {% for topic in topics %}
      <li class="list-group-item">
        <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
      </li>
    {% empty %}
      <li class="list-group-item">No topics have been added yet.</li>
    {% endfor %}
  </ul>
{% endblock content %}
```

### 20.2 Adding a Custom Static File

Create `static/css/custom.css`:

```css
body {
  background-color: #f8f9fa;
}
```

`settings.py`:

```python
STATICFILES_DIRS = [BASE_DIR / "static"]
```

In `base.html` after Bootstrap CSS:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/custom.css' %}">
```

Use `{% load static %}` once near the top, then `{% static 'path' %}`.

### 20.3 Preparing to Deploy

Deployment checklist:

1. **Create a requirements file:**

   ```bash
   pip freeze > requirements.txt
   ```

2. **Use a production database** (PostgreSQL) instead of SQLite.
3. **Hide the secret key** and set `DEBUG = False`.
4. **Set `ALLOWED_HOSTS`** to your domain(s).
5. **Serve static files** properly.
6. **Use a production server** (Gunicorn), not `runserver`.
7. **Version control** everything except secrets/venv/db.
8. **Test locally** with production-ish settings.

`.gitignore`:

```
ll_env/
__pycache__/
*.py[cod]
*.sqlite3
.env
.DS_Store
staticfiles/
```

### 20.4 Deploying with Platform.sh (the book's choice)

> Deployment providers change their UIs; the concepts below matter more than exact clicks. The 3rd edition uses **Platform.sh**. Alternatives: Render, Railway, Fly.io, PythonAnywhere.

#### Install the CLI and log in

```bash
# macOS/Linux
curl -fsS https://platform.sh/cli/installer | php
platform login
```

#### Project configuration files

`.platform.app.yaml`:

```yaml
name: learning-log

type: python:3.11

disk: 1024

web:
  commands:
    start: "gunicorn learning_log.wsgi:application --bind 0.0.0.0:$PORT"

hooks:
  build: |
    pip install -r requirements.txt
    python manage.py collectstatic --noinput

mounts:
  "staticfiles":
    source: local
    source_path: staticfiles
```

`.platform/routes.yaml`:

```yaml
"https://{default}/":
  type: upstream
  upstream: "learning-log:http"
```

`.platform/services.yaml` (PostgreSQL):

```yaml
db:
  type: postgresql:15
  disk: 1024
```

#### Production settings

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-only-change-me')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']   # tighten to your domain in real projects

# Database (example with dj-database-url)
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Security
CSRF_TRUSTED_ORIGINS = ['https://your-app.platform.sh']
```

Install helpers:

```bash
pip install gunicorn dj-database-url psycopg2-binary
pip freeze > requirements.txt
```

#### Push

```bash
git init
git add .
git commit -m "Initial Learning Log project"
platform project:create
platform push
```

Platform.sh builds, migrates, and serves the app. Run migrations via an SSH session if needed:

```bash
platform ssh
python manage.py migrate
python manage.py createsuperuser
```

### 20.5 Deploying on Render / Railway (modern alternative)

**Render:**

1. Push the repo to GitHub.
2. Create a **Web Service**, connect the repo.
3. Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
4. Start command: `gunicorn learning_log.wsgi:application`
5. Add environment variables: `SECRET_KEY`, `DEBUG=False`, `DATABASE_URL`.
6. Add a PostgreSQL instance and link `DATABASE_URL`.

**Railway:** similar — connect GitHub, add a Postgres plugin, set env vars, set the start command.

### 20.6 Common Deployment Errors

| Symptom | Cause | Fix |
|---------|-------|-----|
| `DisallowedHost` | Domain not in `ALLOWED_HOSTS` | Add the domain / `*` temporarily |
| 500 error with debug off | Uncaught exception | Check server logs; enable `DEBUG=True` briefly |
| Static files missing | Not collected / not served | `collectstatic`, configure WhiteNoise or platform static handling |
| `OperationalError: no such table` | Migrations not run | Run `migrate` on the server |
| `Invalid HTTP_HOST` | Missing host header config | Fix `ALLOWED_HOSTS` |
| Secret key leaked | Hard-coded in settings | Move to env var; rotate it |
| `psycopg2` build error | Missing system libs | Use `psycopg2-binary` or install `libpq-dev` |
| Database resets on deploy | SQLite on ephemeral disk | Use managed PostgreSQL |

### 20.7 Chapter 20 Exercises (summary)

- **Styling:** add a custom color theme and style the topic/entry pages.
- **Bootstrap components:** add cards, alerts, or a footer.
- **Deploy:** deploy Learning Log and test registration/login on the live site.
- **Custom domain:** point a domain at your deployment.
- **Security:** set `DEBUG=False`, rotate `SECRET_KEY`, restrict `ALLOWED_HOSTS`.

### 20.8 Key Takeaways

- Bootstrap + `django-bootstrap5` gives a professional UI fast.
- Static files: `STATICFILES_DIRS` for development, `collectstatic` for production.
- Never deploy with `DEBUG=True` or a hard-coded secret key.
- Use PostgreSQL and Gunicorn in production.
- `.gitignore` must exclude `ll_env/`, `db.sqlite3`, `.env`.
- Deployment is mostly configuration and logs — read the error, fix one thing at a time.

---

# APPENDICES

---

## Appendix A — Installation and Troubleshooting

### A.1 Installing Python by OS

#### Windows

1. Go to [python.org/downloads](https://python.org/downloads) and download the latest 3.x installer.
2. Run it and **check "Add python.exe to PATH"**.
3. Choose "Install Now".
4. Verify in a **new** terminal:

   ```bash
   python --version
   py --version
   ```

5. If `python` opens the Microsoft Store: *Settings → Apps → Advanced app settings → App execution aliases* → turn off `python.exe` / `python3.exe`.

#### macOS

```bash
# Official installer from python.org, or Homebrew:
brew install python
python3 --version
```

Use `python3` / `pip3` (macOS reserves `python` for legacy Python 2 on some systems).

#### Linux

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

### A.2 Installing Packages

```bash
python -m pip install --user package_name     # user install
pip install package_name                      # inside a venv
python -m pip install --upgrade package_name
python -m pip list
python -m pip show package_name
python -m pip uninstall package_name
```

Prefer `python -m pip` — it guarantees you're installing into the same Python you run.

### A.3 Virtual Environments

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
pip install -r requirements.txt
deactivate
```

Common issues:

| Problem | Fix |
|---------|-----|
| `No module named venv` (Linux) | `sudo apt install python3-venv` |
| Activation blocked on Windows | `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `pip` installs globally despite venv | Use `python -m pip`; check `which python` |
| Wrong interpreter in VS Code | `Python: Select Interpreter` → pick `.venv` |

### A.4 Common Python Errors and Fixes

| Error | Typical cause | Fix |
|-------|---------------|-----|
| `SyntaxError: invalid syntax` | Missing colon/paren/quote, typo | Read the caret `^` position |
| `IndentationError` | Wrong/mixed indentation | Use 4 spaces consistently |
| `NameError` | Variable/function not defined or misspelled | Define before use; check spelling |
| `TypeError` | Wrong type (e.g., `str + int`) | Convert with `int()`/`str()` |
| `ValueError` | Right type, bad value (`int("abc")`) | Validate input |
| `IndexError` | List index out of range | Check `len()`; use `-1` carefully |
| `KeyError` | Missing dict key | Use `.get()` or check `in` |
| `AttributeError` | Wrong object/method name | Check the type and docs |
| `FileNotFoundError` | Wrong path / cwd | Use `Path(...).absolute()`, check cwd |
| `ModuleNotFoundError` | Package not installed / wrong venv | `pip install`, activate venv |
| `PermissionError` | Writing to a protected path | Write to home/project dir |
| Infinite loop | Loop variable never changes | Add/update the condition variable |

### A.5 Reading a Traceback

```
Traceback (most recent call last):
  File "hello.py", line 3, in <module>
    print(greeting)
          ^^^^^^^^
NameError: name 'greeting' is not defined
```

Read **bottom-up**:
1. Error type + message (`NameError: ...`).
2. The last file/line (`hello.py`, line 3).
3. The code snippet and caret.

---

## Appendix B — Text Editors and IDEs

### B.1 VS Code (book's recommendation)

- Free, cross-platform, huge extension ecosystem.
- Install the **Python** extension (Microsoft) and optionally **Pylance**.
- Features: IntelliSense, debugging, integrated terminal, Git, Jupyter.
- Useful settings: format on save, ruler at 79, `python.analysis.typeCheckingMode`.

Recommended extensions:
- Python, Pylance, Black Formatter, isort, GitLens, Django, Even Better TOML, Markdown All in One.

### B.2 PyCharm

- Full IDE; Community Edition is free.
- Excellent Django support, refactoring, debugger.
- Heavier than VS Code; great for large projects.

### B.3 Other Options

| Editor | Notes |
|--------|-------|
| **Sublime Text** | Fast, lightweight, paid |
| **Vim / Neovim** | Terminal-based, steep learning curve, very powerful |
| **Emacs** | Extensible, terminal/GUI |
| **IDLE** | Ships with Python, minimal but fine for beginners |
| **Jupyter Notebook** | Great for data exploration and teaching |
| **Thonny** | Beginner-friendly, built-in debugger |

### B.4 Editor Tips

- Use **syntax highlighting** — errors become visible.
- Enable **auto-indent** (4 spaces).
- Learn **multi-cursor**, **find/replace**, **go to definition**.
- Set a **ruler at 79 columns**.
- Format with **Black** (`pip install black`, `black file.py`).
- Keep the terminal open beside the editor.

---

## Appendix C — Getting Help

### C.1 Read the Error Carefully

- The last line names the error.
- The line above shows where.
- Search the exact error message in quotes.

### C.2 Use the Official Docs

- Python: [docs.python.org/3](https://docs.python.org/3)
- Django: [docs.djangoproject.com](https://docs.djangoproject.com)
- Pygame: [pygame.org/docs](https://pygame.org/docs)
- Matplotlib: [matplotlib.org](https://matplotlib.org)
- Plotly: [plotly.com/python](https://plotly.com/python)
- Requests: [requests.readthedocs.io](https://requests.readthedocs.io)

### C.3 Search Effectively

- Put exact error text in quotes: `"TypeError: can only concatenate str"`.
- Include the library + version.
- Search Stack Overflow, GitHub Issues, Reddit r/learnpython.
- Prefer answers with recent dates and accepted status.

### C.4 Debugging Techniques

```python
print(f"DEBUG x={x}, type={type(x)}")   # print debugging
```

- **Rubber duck**: explain the code out loud, line by line.
- **Minimal reproduction**: delete code until the bug disappears.
- **Binary search**: comment out half the code.
- **`breakpoint()`** — drops into `pdb`:

  ```python
  breakpoint()
  # n = next line, s = step into, c = continue, p expr = print, q = quit
  ```

- Use the editor's **debugger** with breakpoints and watches.
- Check assumptions: types, lengths, empty values, off-by-one.

### C.5 Asking a Good Question

Include:
1. What you're trying to do.
2. The **full** traceback.
3. The relevant code (minimal).
4. What you expected vs. what happened.
5. What you already tried.
6. Python/library versions and OS.

Never paste 500 lines; isolate the smallest failing example.

### C.6 Communities

- r/learnpython
- Python Discord
- Stack Overflow
- Django Forum
- Pygame Discord
- Local user groups / study buddies

---

## Appendix D — Using Git for Version Control

### D.1 Why Git?

- Track changes over time.
- Undo mistakes.
- Experiment on branches.
- Collaborate and back up to GitHub.

### D.2 First-Time Setup

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

### D.3 Core Workflow

```bash
git init                       # create a repo in the current folder
git status                     # what changed?
git add file.py                # stage one file
git add .                      # stage everything
git commit -m "Add hello.py"   # snapshot
git log --oneline              # history
git diff                       # unstaged changes
git diff --staged              # staged changes
```

### D.4 Undoing Changes

```bash
git restore file.py            # discard unstaged changes
git restore --staged file.py   # unstage
git reset --soft HEAD~1        # undo last commit, keep changes staged
git reset --hard HEAD~1        # ⚠️ undo last commit and DELETE changes
git revert <commit>            # new commit that undoes an old one
```

### D.5 Branches

```bash
git branch                     # list branches
git branch feature             # create
git switch feature             # switch (newer)
git checkout feature           # switch (older)
git switch -c feature          # create + switch
git merge feature              # merge into current branch
git branch -d feature          # delete merged branch
```

### D.6 Remotes (GitHub)

```bash
git remote add origin https://github.com/user/repo.git
git push -u origin main
git pull
git clone https://github.com/user/repo.git
```

### D.7 `.gitignore`

```
__pycache__/
*.py[cod]
.venv/
ll_env/
*.sqlite3
.env
.DS_Store
staticfiles/
```

### D.8 Good Commit Practice

- Commit often, in logical chunks.
- Message: imperative mood, short subject (`Add login page`), details in body.
- Never commit secrets, virtualenvs, databases, or huge binaries.
- Commit before big refactors and before deploying.

---

## Appendix E — Troubleshooting Deployments

### E.1 Where to Look

1. **Build logs** — did dependencies install?
2. **Runtime logs** — tracebacks from the server.
3. **Browser** — status code and generic error page.
4. **Platform dashboard** — health checks, env vars, database status.

### E.2 Frequent Problems

| Problem | Likely cause | Fix |
|---------|--------------|-----|
| Build fails | Missing/incorrect `requirements.txt` | Regenerate with `pip freeze`; pin versions |
| `ModuleNotFoundError` in prod | Dependency not installed | Add to requirements; rebuild |
| 500 error | Unhandled exception | Read logs; reproduce locally |
| Static files 404 | Not collected/served | `collectstatic`; WhiteNoise/platform config |
| Database errors | Wrong `DATABASE_URL`/migrations | Check env var; run `migrate` |
| `DisallowedHost` | `ALLOWED_HOSTS` incomplete | Add domain |
| CSRF errors | Missing trusted origins | Set `CSRF_TRUSTED_ORIGINS` |
| Secret key error | Env var missing | Set `SECRET_KEY` |
| App sleeps/cold starts | Free tier | Upgrade or accept delay |
| Data disappears | Ephemeral filesystem/SQLite | Use managed DB + object storage |

### E.3 Production Settings Template

```python
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']            # fail fast if missing
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
```

### E.4 Deploy Checklist

- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` from environment
- [ ] `ALLOWED_HOSTS` set
- [ ] PostgreSQL configured
- [ ] `migrate` run
- [ ] `collectstatic` run
- [ ] Gunicorn/ASGI server
- [ ] Static files served
- [ ] HTTPS enforced
- [ ] Logs monitored
- [ ] Backups enabled

---

# 📋 MASTER CHEAT SHEETS

## 1. Python Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `+ - * /` | arithmetic | `2 / 3 = 0.666...` |
| `//` | floor division | `7 // 2 = 3` |
| `%` | modulo | `7 % 2 = 1` |
| `**` | exponent | `2 ** 10 = 1024` |
| `== !=` | equality | `3 != 4` → True |
| `< <= > >=` | comparison | `3 <= 3` → True |
| `and or not` | boolean | `True and False` |
| `in`, `not in` | membership | `'a' in 'cat'` |
| `is`, `is not` | identity | `x is None` |
| `=` | assignment | `x = 5` |
| `+= -= *= /=` | augmented assignment | `x += 1` |
| `:=` | walrus (3.8+) | `if (n := len(x)) > 0:` |

---

## 2. Strings

```python
s = "Hello, World"

len(s)                 # 13
s[0]                   # H
s[-1]                  # d
s[0:5]                 # Hello
s[::2]                 # every 2nd char
s.lower() / s.upper()  # case
s.title()              # Hello, World
s.strip()              # trim both ends
s.lstrip() / s.rstrip()
s.split(',')           # ['Hello', ' World']
s.split()              # split on whitespace
'-'.join(['a', 'b'])   # 'a-b'
s.replace('World', 'Python')
s.find('World')        # 7, -1 if missing
s.index('World')       # 7, ValueError if missing
s.startswith('Hello')  # True
s.endswith('World')    # True
s.count('l')           # 3
s.capitalize()         # 'Hello, world'
s.casefold()           # aggressive lowercase (i18n)
s.zfill(5)             # '00042'
s.center(20, '-')      # padding
s.isdigit() / s.isalpha() / s.isalnum() / s.isspace()
ord('A') / chr(65)     # 65 / 'A'
f"{name} is {age}"     # f-string
f"{pi:.2f}"            # 3.14
f"{n:,}"               # 1,000,000
f"{n:>10}" / f"{n:<10}" / f"{n:^10}"
f"{name!r}"            # repr
```

Strings are **immutable** — every method returns a new string.

---

## 3. Lists

```python
xs = [3, 1, 2]

xs[0]              # 3
xs[-1]             # 2
xs[1:3]            # [1, 2]
len(xs)            # 3
xs.append(4)       # add to end
xs.insert(1, 9)    # insert at index
xs.extend([5, 6])  # add many
xs.pop()           # remove & return last
xs.pop(0)          # remove & return first
xs.remove(1)       # remove first matching value
del xs[0]          # delete by index
xs.clear()         # empty
xs.sort()          # in place
xs.sort(reverse=True)
xs.sort(key=str.lower)
sorted(xs)         # new list
xs.reverse()       # in place
xs.index(2)        # position
xs.count(2)        # occurrences
xs.copy()          # shallow copy
xs + [7]           # concatenate
[0] * 3            # [0, 0, 0]
2 in xs            # membership
min(xs), max(xs), sum(xs)
```

---

## 4. List Comprehensions

```python
[x for x in range(5)]                  # [0, 1, 2, 3, 4]
[x ** 2 for x in range(1, 6)]          # squares
[x for x in xs if x % 2 == 0]          # filter
[x if x > 0 else 0 for x in xs]        # conditional expression
[(x, y) for x in a for y in b]         # nested loops
{x: x ** 2 for x in range(3)}          # dict comprehension
{x for x in xs}                        # set comprehension
```

---

## 5. Dictionaries

```python
d = {'a': 1, 'b': 2}

d['a']                  # 1 (KeyError if missing)
d.get('z')              # None
d.get('z', 0)           # 0
d['c'] = 3              # add/update
del d['a']              # remove
d.pop('b')              # remove & return
d.popitem()             # last pair
d.keys() / d.values() / d.items()
list(d)                 # keys
'a' in d                # True
d.update({'c': 4})
d.setdefault('x', 0)
len(d)
d.clear()
```

Loop:

```python
for k, v in d.items():
    print(k, v)
```

---

## 6. Sets

```python
s = {1, 2, 3}

s.add(4)
s.discard(1)            # no error if missing
s.remove(1)             # KeyError if missing
s.union({4, 5})         # |
s.intersection({2, 3})  # &
s.difference({1})       # -
s.symmetric_difference({3, 4})  # ^
{1, 2} <= {1, 2, 3}     # subset
len(s)
```

Sets are unordered and hold unique items — great for deduplication.

---

## 7. Tuples

```python
t = (1, 2, 3)
t[0]               # 1
t[1:]              # (2, 3)
a, b, c = t        # unpacking
single = (3,)      # one-item tuple
t.count(2) / t.index(2)
```

Immutable; hashable (usable as dict keys).

---

## 8. Conditionals

```python
if x > 0:
    ...
elif x == 0:
    ...
else:
    ...

value = "yes" if ok else "no"       # ternary

if 0 <= x <= 10:                    # chained comparison
    ...
```

Falsy: `False`, `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`.

---

## 9. Loops

```python
for item in items:
    ...

for i, item in enumerate(items, start=1):
    ...

for a, b in zip(list1, list2):
    ...

while condition:
    ...

break        # exit loop
continue     # next iteration
else:        # runs if loop completed without break
    ...
```

`range(start, stop, step)` — stop is exclusive.

---

## 10. Functions

```python
def f(a, b=2, *args, **kwargs):
    """Docstring."""
    return a + b

f(1)
f(1, 3)
f(a=1, b=3)
f(1, 2, 3, 4, x=5)     # args=(3,4), kwargs={'x': 5}
```

- Default args: never use a mutable default (`def f(x=[])` bug).
- `*` forces keyword-only args: `def f(a, *, b): ...`.
- `/` forces positional-only: `def f(a, /, b): ...`.

---

## 11. Classes / OOP

```python
class Parent:
    class_attribute = "shared"

    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hi, {self.name}"

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Parent({self.name!r})"

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):              # override
        return f"{super().greet()}, age {self.age}"
```

Dunder methods:

| Method | Purpose |
|--------|---------|
| `__init__` | initialize |
| `__str__` | human-readable string |
| `__repr__` | developer string |
| `__len__` | `len(obj)` |
| `__eq__` | `==` |
| `__lt__` | `<` |
| `__iter__` | iteration |
| `__next__` | next item |
| `__getitem__` | `obj[key]` |
| `__call__` | `obj()` |
| `__enter__/__exit__` | context manager |

---

## 12. Files

```python
from pathlib import Path

p = Path('data.txt')
p.read_text()                     # whole file
p.write_text("hello")             # overwrite
p.exists() / p.is_file() / p.is_dir()
p.name / p.stem / p.suffix / p.parent
p.absolute()

with open('data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())

with open('out.txt', 'w') as f:
    f.write("line\n")

with open('out.txt', 'a') as f:
    f.write("more\n")

with open('data.bin', 'rb') as f:
    data = f.read()
```

| Mode | Meaning |
|------|---------|
| `r` | read |
| `w` | write (truncate) |
| `a` | append |
| `x` | create (fail if exists) |
| `r+` | read/write |
| `b` | binary |

---

## 13. Exceptions

```python
try:
    risky()
except ValueError as e:
    print(e)
except (TypeError, KeyError):
    ...
else:
    print("no error")
finally:
    cleanup()
```

Common exceptions: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `AttributeError`, `NameError`, `FileNotFoundError`, `ZeroDivisionError`, `ImportError`, `PermissionError`, `StopIteration`.

Raise your own:

```python
raise ValueError("invalid input")
```

Custom exception:

```python
class MyError(Exception):
    pass
```

---

## 14. JSON

```python
import json

json.dumps(obj)                 # Python → JSON string
json.loads(text)                # JSON string → Python
json.dump(obj, file)            # write to file
json.load(file)                 # read from file

json.dumps(obj, indent=4)       # pretty print
```

`pathlib` version:

```python
from pathlib import Path
Path('d.json').write_text(json.dumps(obj))
obj = json.loads(Path('d.json').read_text())
```

---

## 15. Built-in Functions

| Function | Purpose |
|----------|---------|
| `print()`, `input()` | I/O |
| `len()`, `type()`, `id()` | introspection |
| `int()`, `float()`, `str()`, `bool()` | conversion |
| `list()`, `tuple()`, `set()`, `dict()` | constructors |
| `range()`, `enumerate()`, `zip()` | iteration helpers |
| `sorted()`, `reversed()` | ordering |
| `min()`, `max()`, `sum()`, `abs()`, `round()` | math |
| `any()`, `all()` | boolean aggregation |
| `map()`, `filter()` | functional transforms |
| `isinstance()`, `issubclass()` | type checks |
| `hasattr()`, `getattr()`, `setattr()` | attribute access |
| `open()` | files |
| `help()`, `dir()` | documentation |
| `breakpoint()` | debugger |

---

## 16. Modules & Packages

```python
import math
from math import sqrt
from math import sqrt as root
import numpy as np
from package.module import Class
from . import sibling          # relative import inside a package
```

Package layout:

```
mypackage/
├── __init__.py
├── module_a.py
└── subpackage/
    ├── __init__.py
    └── module_b.py
```

Run as a script: `if __name__ == '__main__': main()`.

---

## 17. pytest

```bash
pytest                    # discover and run
pytest -v                 # verbose
pytest test_file.py       # one file
pytest -k "name"          # filter by name
pytest -x                 # stop on first failure
pytest --lf               # last failed
pytest -q                 # quiet
```

```python
import pytest

def test_something():
    assert add(1, 2) == 3

@pytest.fixture
def sample():
    return build_sample()

def test_with_fixture(sample):
    assert sample.ready

with pytest.raises(ValueError):
    int("abc")
```

---

## 18. Virtualenv / pip

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip freeze > requirements.txt
pip list
pip show pkg
pip uninstall pkg
deactivate
```

---

## 19. Django Commands

```bash
django-admin startproject mysite .
python manage.py startapp myapp
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py shell
python manage.py collectstatic
python manage.py test
python manage.py check
python manage.py dbshell
```

Handy shell queries:

```python
Model.objects.all()
Model.objects.filter(field=value)
Model.objects.exclude(field=value)
Model.objects.get(pk=1)
Model.objects.order_by('-date')
Model.objects.count()
obj.related_set.all()
```

---

## 20. Matplotlib & Plotly Recipes

```python
# Matplotlib line
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2, color='red', label='Series')
ax.set_title("Title")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
plt.savefig('plot.png', bbox_inches='tight')
plt.show()

# Matplotlib scatter
ax.scatter(x, y, s=20, c=y, cmap=plt.cm.Blues, edgecolors='none')

# Plotly bar
fig = px.bar(x=labels, y=values, labels={'x': 'X', 'y': 'Y'})
fig.show()
fig.write_html('chart.html')

# Plotly world map
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, color=mags,
                     hover_name=titles, projection='natural earth')
fig.show()
```

---

## 21. Pygame Essentials

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((230, 230, 230))
    # update + draw
    pygame.display.flip()
    clock.tick(60)
```

| Concept | API |
|---------|-----|
| Load image | `pygame.image.load('ship.bmp')` |
| Rect | `image.get_rect()` |
| Draw image | `screen.blit(image, rect)` |
| Draw rect | `pygame.draw.rect(screen, color, rect)` |
| Key state | `pygame.key.get_pressed()` |
| Collision | `spritecollideany`, `groupcollide` |
| Groups | `pygame.sprite.Group()` |
| Text | `pygame.font.SysFont(None, 48).render(...)` |
| Mouse | `pygame.mouse.get_pos()` |

---

## 22. Git Quick Reference

```bash
git init
git status
git add .
git commit -m "message"
git log --oneline --graph
git diff
git branch
git switch -c feature
git merge feature
git remote add origin URL
git push -u origin main
git pull
git clone URL
git restore file
git revert COMMIT
```

---

## 23. Terminal / Shell Basics

```bash
pwd                 # current directory
ls / dir            # list files
cd folder           # change directory
cd ..               # up one level
mkdir name          # make directory
touch file.py       # create empty file
cp a b              # copy
mv a b              # move/rename
rm file             # delete (no recycle bin!)
rm -r folder        # delete folder recursively
cat file            # print file
python file.py      # run script
Ctrl+C              # stop a running program
Ctrl+D / exit()     # leave the Python REPL
```

---

# ⚠️ TOP 40 BEGINNER MISTAKES

1. Using `=` instead of `==` in comparisons.
2. Forgetting the colon after `if`, `for`, `while`, `def`, `class`.
3. Mixing tabs and spaces → `IndentationError`.
4. Forgetting to save before running.
5. Missing or mismatched quotes/parentheses.
6. Using a variable before assigning it → `NameError`.
7. Concatenating a string and an int without `str()`.
8. Calling `.sort()` and assigning its result (`x = x.sort()` → `None`).
9. Modifying a list while iterating over it (iterate over a copy).
10. Copying a list with `=` instead of `[:]` / `.copy()`.
11. Indexing past the end of a list.
12. Off-by-one with `range(1, 5)` (stops at 4).
13. Using `remove()` expecting it to delete all matches.
14. Accessing a dict key that doesn't exist (`KeyError`) — use `.get()`.
15. Confusing `keys()`, `values()`, `items()`.
16. Forgetting `input()` returns a string.
17. `int("3.5")` → `ValueError`; use `float()`.
18. Infinite `while` loop with no state change.
19. Using a mutable default argument (`def f(x=[])`).
20. Forgetting `self` in method definitions.
21. Forgetting `super().__init__(...)` in a subclass.
22. Naming a variable the same as a built-in (`list`, `dict`, `str`).
23. Importing a module with the same name as a variable.
24. Circular imports.
25. Running a script from the wrong directory → file not found.
26. Writing files with `'w'` and accidentally erasing them.
27. Not closing files (use `with`).
28. Catching all exceptions with a bare `except:`.
29. Swallowing errors with `except: pass`.
30. Comparing floats with `==` (use `math.isclose`).
31. Mutating a dict while looping over it (loop over `list(d)`).
32. Assuming dicts/sets are ordered (dicts are in 3.7+, sets are not).
33. Shadowing `self` or using it outside a method.
34. Forgetting to call a function (`x = f` vs `x = f()`).
35. Wrong `pathlib` relative path (cwd vs script dir).
36. Using `is` to compare strings/numbers instead of `==`.
37. Editing `sys.path` instead of installing/using packages properly.
38. Committing a venv, database, or `.env` to Git.
39. Deploying with `DEBUG=True` or a hard-coded secret key.
40. Not reading the traceback — guessing instead of diagnosing.

---

# 🗓️ 30-DAY STUDY PLAN

| Day | Focus | Deliverable |
|-----|-------|-------------|
| 1 | Ch. 1–2 | Install Python/VS Code, run `hello.py`, play with strings |
| 2 | Ch. 2 | Exercises: names, quotes, numbers, comments |
| 3 | Ch. 3 | Lists: guest list, sorting, `IndexError` |
| 4 | Ch. 4 | Loops, `range`, slices, tuples, PEP 8 |
| 5 | Ch. 4–5 | Comprehensions + `if/elif/else` exercises |
| 6 | Ch. 5 | Alien colors, stages of life, admin check |
| 7 | Ch. 6 | Dictionaries: glossary, rivers, nesting |
| 8 | Ch. 6 | Nested data exercises (pizza, users) |
| 9 | Ch. 7 | `input()`, `while`, flags, `break`/`continue` |
| 10 | Ch. 7–8 | Deli, vacation poll; define first functions |
| 11 | Ch. 8 | Functions: arguments, returns, `*args`, `**kwargs` |
| 12 | Ch. 8 | Modules + printing-models exercise |
| 13 | Ch. 9 | Classes: `Dog`, `Car`, attributes, methods |
| 14 | Ch. 9 | Inheritance, composition, imports |
| 15 | Ch. 10 | Read/write files, `pathlib` |
| 16 | Ch. 10 | Exceptions + JSON persistence |
| 17 | Ch. 11 | pytest: functions and classes |
| 18 | Ch. 12 | Pygame setup, ship that moves |
| 19 | Ch. 12 | Bullets and refactoring |
| 20 | Ch. 13 | Alien fleet, collisions |
| 21 | Ch. 14 | Scoring, levels, play button |
| 22 | Ch. 15 | Matplotlib line/scatter plots |
| 23 | Ch. 15 | Random walks + Plotly dice |
| 24 | Ch. 16 | CSV weather data + missing values |
| 25 | Ch. 16 | JSON earthquakes + world map |
| 26 | Ch. 17 | APIs with `requests`, GitHub data |
| 27 | Ch. 17 | Hacker News + chart |
| 28 | Ch. 18 | Django project, models, migrations, admin |
| 29 | Ch. 19 | Auth, registration, per-user data |
| 30 | Ch. 20 | Bootstrap styling + deploy |

**Daily rhythm (90–120 min):** 15 min review → 30 min read/type examples → 30 min exercises → 15 min notes/flashcards → 15 min stretch goal.

**Rules that make it stick:**
- Type every example by hand — no copy-paste.
- Do the "Try It Yourself" exercises before moving on.
- Break the code on purpose and read the errors.
- Build a tiny project after every 3 chapters.
- Push everything to Git daily.

---

# 🧠 THE BIG PICTURE — WHAT THE BOOK TEACHES

| Skill | Where | Real-world use |
|-------|-------|----------------|
| Syntax & data types | Ch. 1–2 | Every Python program |
| Collections | Ch. 3–6 | Data wrangling, configs, records |
| Control flow | Ch. 5, 7 | Business logic |
| Functions & modules | Ch. 8 | Reusable, testable code |
| OOP | Ch. 9 | Modeling real systems |
| Files & errors | Ch. 10 | Persistence, robustness |
| Testing | Ch. 11 | Confidence to change code |
| Game dev | Ch. 12–14 | Real-time loops, state, collisions |
| Data viz | Ch. 15–17 | Analysis, reporting, dashboards |
| Web dev | Ch. 18–20 | Full-stack CRUD + auth + deploy |
| Git & tooling | Appendices | Professional workflow |

**The single biggest lesson:** programming is learned by **building**, not by reading. The book's three projects exist to force you to integrate everything — and to teach you how to debug when the pieces don't fit.

---

*Notes compiled from Python Crash Course, 3rd Edition by Eric Matthes (No Starch Press). Code examples are educational reproductions of the book's approach; always check the current library documentation for version-specific details.*
