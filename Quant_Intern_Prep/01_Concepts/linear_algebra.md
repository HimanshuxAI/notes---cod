# 🧮 Linear Algebra for Quant Interviews

You don't need proofs. You need to recognize matrices, compute by hand for 2×2/3×3, and understand eigenvalues intuitively.

---

## 1. Matrix Operations

### Addition / scalar multiplication
Element-wise. A + B requires same dimensions.

### Matrix multiplication (A·B)
- (i,j)-th entry = row i of A ⋅ column j of B (dot product).
- Requires: A is m×n, B is n×p → result is m×p.
- **Not commutative:** AB ≠ BA in general.

### Transpose (Aᵀ)
- Swap rows and columns. (Aᵀ)ᵀ = A. (AB)ᵀ = BᵀAᵀ.

### Identity (I)
- 1s on diagonal, 0s elsewhere. AI = IA = A.

### Inverse (A⁻¹)
- Exists only if A is square and non-singular (det ≠ 0).
- AA⁻¹ = A⁻¹A = I. For 2×2: [[a,b],[c,d]]⁻¹ = (1/det)·[[d,−b],[−c,a]].

### Determinant (det)
- 2×2: ad − bc.
- 3×3: cofactor expansion or rule of Sarrus.
- det(AB) = det(A)·det(B). det(Aᵀ) = det(A).

---

## 2. Vectors

### Dot product
u·v = Σ uᵢvᵢ = |u||v|cos(θ). Orthogonal ⟺ dot product = 0.

### Cross product (3D)
u × v = vector perpendicular to both. |u × v| = |u||v|sin(θ).

### Norm
||v|| = √(Σvᵢ²) — Euclidean (L2) norm. L1 = Σ|vᵢ|.

---

## 3. Eigenvalues & Eigenvectors

```
A·v = λ·v
```
- λ = eigenvalue, v = eigenvector (nonzero).
- Find λ: solve det(A − λI) = 0 (characteristic equation).
- **Trace** = sum of diagonal = sum of eigenvalues.
- **Det** = product of eigenvalues.
- Symmetric matrices → real eigenvalues, orthogonal eigenvectors.

**Interview use:** PCA intuition, covariance matrix decomposition, stability of systems.

---

## 4. Special Matrices

| Type | Property | Use |
|------|----------|-----|
| Symmetric | A = Aᵀ | covariance matrices |
| Diagonal | nonzero only on diagonal | easy powers/inverses |
| Orthogonal | AᵀA = I | rotations, preserve length |
| Positive definite | xᵀAx > 0 ∀x≠0 | convex optimization, valid covariance |
| Idempotent | A² = A | projection matrices |

---

## 5. Linear Systems

Solve Ax = b:
- Gaussian elimination (row reduction).
- If A invertible: x = A⁻¹b.
- Rank = number of linearly independent rows/columns.
- Full rank square → unique solution.

---

## 6. Quick Drills (do by hand, no calculator)

1. Multiply two 2×2 matrices; compute transpose.
2. Find determinant and inverse of [[2,1],[5,3]].
3. Find eigenvalues of [[3,1],[1,3]].
4. Check if vectors [1,2,3] and [2,−1,0] are orthogonal.
5. Given covariance matrix [[4,2],[2,3]], is it positive definite?

---

*Next: [`calculus.md`](./calculus.md)*