# 🔷 C++ for Quant Interviews

Many prop shops and HFTs (Jane Street, Hudson River, Optiver, Citadel Securities) use C++. You don't need to be an expert — but you must read and write basic C++ under pressure.

---

## 1. C++ Basics to Know Cold

| Feature | What to know |
|---------|--------------|
| **I/O** | `cin`, `cout`, `endl`, `scanf`/`printf` basics |
| **Pointers & references** | `int* p`, `int& ref`, `nullptr`, address-of `&`, dereference `*` |
| **Dynamic memory** | `new`, `delete` (conceptually; prefer containers in interviews) |
| **Struct / class** | members, constructors, `this` pointer, `const` methods |
| **STL containers** | `vector`, `array`, `string`, `map`, `unordered_map`, `set`, `unordered_set`, `stack`, `queue`, `priority_queue`, `deque` |
| **STL algorithms** | `sort`, `reverse`, `binary_search`, `lower_bound`, `upper_bound`, `max_element`, `accumulate` |
| **Iterators** | `begin()`, `end()`, `rbegin()`, `rend()` |
| **Lambdas** | `[capture](params) -> ret { body }` — for custom comparators |

---

## 2. Must-Know STL Idioms

```cpp
vector<int> v = {3, 1, 4};
sort(v.begin(), v.end());                    // ascending
sort(v.begin(), v.end(), greater<int>());    // descending
auto it = lower_bound(v.begin(), v.end(), x);// first >= x
unordered_map<int, int> freq;               // hash map
priority_queue<int> pq;                     // max-heap by default
priority_queue<int, vector<int>, greater<int>> min_pq;
string s = "hello";
s.substr(1, 3);                             // "ell"
```

---

## 3. Common C++ Interview Tasks

1. **Read input, process, print output** — standard competitive programming style.
2. **Implement a data structure** — stack, queue, linked list (singly/doubly), binary search tree insert/search.
3. **Black-Scholes in C++** — same formula as Python, using `<cmath>` (`exp`, `log`, `sqrt`) and a Normal CDF approximation (or `<boost/math>` if allowed — usually not, so write a rational approximation).
4. **Parse a string** — tokenize by delimiter, convert to int/stod.

---

## 4. C++ Gotchas to Avoid

- Integer division: `5 / 2 = 2`. Cast to `double` when needed.
- Vector index out of bounds — use `.at()` if you want bounds checking.
- `map` vs `unordered_map`: ordered (log n) vs hash (average O(1)).
- Passing by value vs reference: `void f(vector<int> v)` copies; `void f(const vector<int>& v)` doesn't.
- `endl` flushes (slower); use `"\n"` in loops.

---

## 5. If You Only Know One Language

Pick **Python** if you're not already comfortable with C++. Most shops accept either for early-round coding. Only prep C++ if a target shop specifically requires it.

---

*Next: [`dsa_patterns.md`](./dsa_patterns.md)*