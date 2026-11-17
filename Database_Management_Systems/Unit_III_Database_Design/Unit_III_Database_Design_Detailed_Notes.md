# Database Management Systems Unit III: Database Design

## Course and Source Metadata

| Field | Details |
|---|---|
| Course | Database Management Systems |
| Unit | Unit III: Database Design |
| Institution | MIT School of Computing |
| Department | Department of Computer Science and Engineering |
| Programme | PLD 1, Second Year Engineering |
| Class | S.Y. |
| Academic year and semester | AY 2026–2027, Semester I |
| Course code | `23CSE2022` |
| Source presentation | `Unit_III_Database_Design.pptx`, 51 slides |
| Guide scope | Functional dependencies, inference, redundancy and anomalies, keys, 1NF through 5NF, BCNF, lossless decomposition, and dependency preservation |

## Table of Contents

### Part 1

1. [Unit Overview and Syllabus Map](#1-unit-overview-and-syllabus-map)
2. [Functional Dependencies](#2-functional-dependencies)
3. [Armstrong Axioms and Inference Rules](#3-armstrong-axioms-and-inference-rules)
4. [Data Redundancy and Update Anomalies](#4-data-redundancy-and-update-anomalies)
5. [Keys and Attribute Classification](#5-keys-and-attribute-classification)
6. [First Normal Form (1NF)](#6-first-normal-form-1nf)
7. [Second Normal Form (2NF)](#7-second-normal-form-2nf)
8. [Worked Normalization Examples and Common Traps](#8-worked-normalization-examples-and-common-traps)

### Part 2

1. Third Normal Form (3NF)
2. Boyce-Codd Normal Form (BCNF)
3. Fourth Normal Form (4NF) and multivalued dependencies
4. Fifth Normal Form (5NF) and join dependencies
5. Lossless join decomposition
6. Dependency preservation
7. Integrated design review and exam practice

## 1. Unit Overview and Syllabus Map

### 1.1 Purpose of Unit III

Database design decides how facts about an organisation should be represented in relations. A good design stores each fact in a suitable place, connects relations through keys, and preserves the rules that connect attributes.

The unit follows a direct sequence:

1. Describe how one group of attributes determines another with functional dependencies.
2. Use Armstrong's axioms to find dependencies that follow from known rules.
3. Identify redundancy and the insert, update, and delete problems it causes.
4. Classify candidate keys, superkeys, prime attributes, and non-prime attributes.
5. Normalize relations through 1NF and 2NF in Part 1, then through the higher forms in Part 2.
6. Check that any decomposition is lossless and preserves the dependencies that enforce business rules.

### 1.2 Syllabus map

| Syllabus topic | Main concepts | Source slides | Part |
|---|---|---:|---:|
| Functional dependencies | Determinant, dependent, trivial, nontrivial, transitive, attribute closure | 4–13 | 1 |
| Purpose of normalization | Redundancy and data anomalies | 14–21 | 1 |
| Single-valued normalization | 1NF, 2NF, 3NF, and BCNF | 22–37 | 1 and 2 |
| Decomposition | Lossless joins and dependency preservation | 43–47 | 2 |
| Multivalued normalization | Multivalued dependencies and 4NF | 6–7, 38–42 | 2 |
| Join dependencies | Fifth normal form | 48–50 | 2 |
| Normal-form summary | Conditions for each normal form | 51 | 1 and 2 |

### 1.3 Relation design workflow

Use the following procedure when analysing a relation:

1. **State the business rule.** Record what each attribute means and which facts determine other facts.
2. **List candidate keys.** Find the smallest attribute sets that identify each row under every valid instance of the relation.
3. **Write the functional dependencies.** Express each rule as `X → Y` and separate it from a rule inferred from another dependency.
4. **Compute closures.** Use Armstrong's axioms to find all attributes determined by each key and determinant.
5. **Test the normal forms.** Look for partial and transitive dependencies of non-prime attributes.
6. **Decompose carefully.** Remove the detected violation, then verify that the result is in the required normal form.
7. **Verify the decomposition.** Check lossless join and dependency preservation before accepting the new design.

### 1.4 Core notation

| Notation | Meaning | Example |
|---|---|---|
| `R(A, B, C)` | Relation schema with attributes `A`, `B`, and `C` | `STUDENT(StudentID, Name, Age)` |
| `X` | A set of attributes used as a determinant | `{StudentID}` |
| `Y` | A set of attributes determined by `X` | `{Name, Age}` |
| `X → Y` | `X` functionally determines `Y` | `StudentID → Name` |
| `F` | A set of functional dependencies | `F = {StudentID → Name}` |
| `F⁺` | The closure of dependency set `F`, containing every FD implied by `F` | `F⁺` is a set of dependencies |
| `X⁺` | The attribute closure of attribute set `X` under `F` | `{StudentID}⁺ = {StudentID, Name, Age}` |
| `K⁺` | The attribute closure of candidate key `K` | For a key, `K⁺` contains every attribute of `R` |
| `PK` | Primary key, the candidate key selected for the relation | `PK(StudentID)` |
| `FK` | Foreign key, an attribute or attribute set that references a candidate key in another relation or the same relation | `Course_ID FK → COURSE` |

An attribute name such as `StudentID` and an attribute set such as `{StudentID, Name}` are different objects. Write braces whenever the set matters.

### 1.5 Precision notes for the supplied material

The slides provide the course examples and the intended syllabus. Some wording needs correction:

- A functional dependency expresses a rule that must hold for every valid instance, not merely a pattern visible in one table.
- A multivalued dependency has its own symbol and meaning. It should not be confused with a functional dependency.
- The slides call union and decomposition “properties.” They are inference rules derivable from Armstrong's three axioms.
- 1NF requires atomic cell values and a well-formed relation. It does not require every column to contain different values.
- The full 2NF test uses every candidate key, not only the primary key.
- Normalization reduces redundancy and anomaly risk. No normal form by itself guarantees that every application rule is enforced.

## 2. Functional Dependencies

### 2.1 Formal definition

Let `R` be a relation schema, and let `X` and `Y` be sets of attributes of `R`. The functional dependency

\[
X \rightarrow Y
\]

holds in `R` when, for every valid relation instance `r` of `R`, the following condition is true:

\[
t_1[X] = t_2[X] \Rightarrow t_1[Y] = t_2[Y]
\]

for any two tuples `t₁` and `t₂` in `r`.

In plain language, one value of `X` fixes one value of `Y`. If two rows agree on `X`, they must agree on `Y`.

`X` is the **determinant**. `Y` is the **dependent**. The arrow is read as “`X` determines `Y`.”

### 2.2 Determinants and dependents

Consider the course's `Students` relation:

| StudentID | StudentName | StudentAge |
|---:|---|---:|
| 101 | Rahul | 23 |
| 102 | Ankit | 22 |
| 103 | Aditya | 22 |
| 104 | Sahil | 24 |
| 105 | Ankit | 23 |

The table illustrates these dependencies:

\[
StudentID \rightarrow StudentName
\]

\[
StudentID \rightarrow StudentAge
\]

A `StudentID` fixes the student's name and age. The relation can therefore record `Ankit` more than once when the students have different IDs.

The reverse dependency does not hold:

\[
StudentName \nrightarrow StudentID
\]

Two students may share the name `Ankit`, and they have different IDs. `StudentAge` also does not determine a student because several students are 22 years old.

### 2.3 FD rules concern all valid data

An FD is a semantic constraint. A current table can satisfy an FD by chance, yet violate the rule that the business is supposed to enforce.

For example, the sample `Students` table contains two students named `Ankit`. This disproves `StudentName → StudentID` for the shown data. If a table contains one student named `Ankit` today, that alone does not prove `StudentName → StudentID`. The rule must hold for every valid future state.

This distinction separates an FD from a data observation:

- **FD:** `StudentID → StudentName` is a declared rule.
- **Observation:** The current table happens to show that each displayed ID has one displayed name.

### 2.4 Trivial, nontrivial, and fully nontrivial dependencies

#### Trivial dependency

`X → Y` is **trivial** when `Y ⊆ X`.

Examples:

- `StudentID → StudentID`
- `{StudentID, StudentName} → StudentName`
- `{StudentID, StudentName} → {StudentID, StudentName}`

A trivial dependency says that an attribute set determines attributes already present on its left side. It carries no new information about a row.

#### Nontrivial dependency

`X → Y` is **nontrivial** when `Y ⊄ X`.

Examples from the slides:

- `roll_no → name`
- `{roll_no, name} → age`
- `Id → Name`
- `Name → DOB`

At least one dependent attribute lies outside the determinant.

#### Fully nontrivial dependency

`X → Y` is **fully nontrivial** when `X ∩ Y = ∅`.

For example, `StudentID → StudentName` is fully nontrivial because the two attribute sets do not overlap. This label matters when checking normal forms because trivial dependencies never create a normalization violation.

### 2.5 Transitive dependency

A dependency `X → Z` is **transitive through `Y`** when the design also has:

\[
X \rightarrow Y
\]

\[
Y \rightarrow Z
\]

The course's enrolment example gives:

\[
enrol\_no \rightarrow dept
\]

\[
dept \rightarrow building\_no
\]

Therefore:

\[
enrol\_no \rightarrow building\_no
\]

The enrolment number determines the building indirectly through the department. The relation `ENROLMENT(enrol_no, name, dept, building_no)` contains a transitive dependency of `building_no` on `enrol_no`.

### 2.6 Multivalued dependency is a separate concept

The source groups multivalued dependencies under “types of functional dependency.” The distinction matters for normalization:

- `X → Y` means that one value of `X` fixes one value of `Y`.
- `X ↠ Y` is a multivalued dependency. In `R(X, Y, Z)`, it requires `Y` to be independent of `Z` for each fixed `X`. If tuples `(x, y1, z1)` and `(x, y2, z2)` exist, the relation must also contain the complementary tuples `(x, y1, z2)` and `(x, y2, z1)`.

For the slide's bike example:

| bike_model | color | accessory |
|---|---|---|
| tu1001 | Black | Helmet |
| tu1001 | Black | Gloves |
| tu1001 | Red | Helmet |
| tu1001 | Red | Gloves |

The notation `bike_model ↠ color` and `bike_model ↠ accessory` records the independent collections. The four tuples include both required recombinations. Merely observing several `Y` values for one `X`, without the complementary-tuple requirement, does not prove an MVD. The full MVD definition and 4NF appear in Part 2.

### 2.7 Attribute closure

For a dependency set `F` and an attribute set `X`, the **closure** `X⁺` is the set of all attributes that `F` determines from `X`:

\[
X^{+} = \{A \mid X \rightarrow A \text{ can be derived from } F\}
\]

A practical closure algorithm is:

1. Put `X` into `X⁺`.
2. Find every dependency `A → B` in `F` with `A ⊆ X⁺`.
3. Add every attribute in `B` to `X⁺`.
4. Repeat until no new attribute can be added.

For the student dependencies:

\[
F = \{StudentID \rightarrow StudentName,\ StudentID \rightarrow StudentAge\}
\]

we get:

\[
\{StudentID\}^{+} = \{StudentID, StudentName, StudentAge\}
\]

If `StudentName → City` were added, then:

\[
\{StudentID\}^{+} = \{StudentID, StudentName, StudentAge, City\}
\]

A candidate key is a minimal set whose closure contains every attribute of the relation.

### 2.8 Why functional dependencies matter

FDs support four core design tasks:

1. **Key discovery.** A candidate key identifies rows and must determine every attribute.
2. **Normal-form testing.** Partial and transitive dependencies reveal common design defects.
3. **Decomposition guidance.** FDs suggest sensible component relations, but every decomposition still needs separate lossless-join and dependency-preservation checks.
4. **Constraint enforcement.** A key-enforced FD can use a primary-key or unique constraint. A non-key local FD generally needs an assertion, check constraint, or trigger.

### 2.9 Quick check

For each statement, decide whether it is an FD, a key statement, or only an observation:

1. `StudentID → StudentName`.
2. Every displayed `StudentID` currently has one name.
3. `{StudentID, StudentName}` is a superkey of the student relation.
4. `StudentName → StudentAge`.

Answers:

1. It is an FD because the course rule says a student ID identifies a student.
2. It is an observation about the displayed rows.
3. It is a key statement because the set determines every attribute of the relation and contains extra attributes.
4. The displayed instance violates `StudentName → StudentAge`: `Ankit` appears with ages 22 and 23. The supplied business rules do not establish this FD.

## 3. Armstrong Axioms and Inference Rules

### 3.1 Purpose

A database designer rarely needs to record every dependency implied by the business rules. From a small set `F` of known dependencies, Armstrong's axioms derive all dependencies that follow from `F`.

An inference rule has this form:

\[
\text{premises} \vdash \text{conclusion}
\]

The symbol `⊢` means “entails” or “can be inferred.” The premises must be true dependencies in the relation's intended semantics.

### 3.2 Reflexivity

**Rule:** If `Y ⊆ X`, then `X → Y`.

**Formal statement:**

\[
Y \subseteq X \Rightarrow X \rightarrow Y
\]

**Plain language:** A set always determines the attributes already contained in that set.

**Course examples:**

- `sid → sid`
- `{sid, phone} → phone`
- `ABC → AB`
- `ABC → A`
- `{roll_no, name} → name`

Reflexivity applies to every relation. A trivial dependency cannot reveal a normalization defect.

### 3.3 Augmentation

**Rule:** If `X → Y`, then `XZ → YZ` for any attribute set `Z`.

**Formal statement:**

\[
X \rightarrow Y \Rightarrow XZ \rightarrow YZ
\]

**Plain language:** Adding the same new attributes to both sides preserves a dependency.

**Course example:** Given `sid → sname`, add `phone` to both sides:

\[
\{sid, phone\} \rightarrow \{sname, phone\}
\]

If `sid → {sname, age}`, augmentation with `phone` gives:

\[
\{sid, phone\} \rightarrow \{sname, age, phone\}
\]

Augmentation preserves the original dependency. It does not claim that the enlarged determinant has the same attribute closure as the original determinant.

### 3.4 Transitivity

**Rule:** If `X → Y` and `Y → Z`, then `X → Z`.

**Formal statement:**

\[
X \rightarrow Y \land Y \rightarrow Z \Rightarrow X \rightarrow Z
\]

**Plain language:** If `X` fixes `Y`, and `Y` fixes `Z`, then `X` fixes `Z`.

**Course example:**

\[
sid \rightarrow sname
\]

\[
sname \rightarrow city
\]

Therefore:

\[
sid \rightarrow city
\]

**Enrolment example:**

\[
enrol\_no \rightarrow dept
\]

\[
dept \rightarrow building\_no
\]

Therefore:

\[
enrol\_no \rightarrow building\_no
\]

The same reasoning supports a transitive-dependency test in normalization.

### 3.5 Derived inference rules

The slides also list union and decomposition. They follow from the three Armstrong axioms and are often easier to apply.

#### Union

If `X → Y` and `X → Z`, then `X → YZ`.

\[
X \rightarrow Y \land X \rightarrow Z \Rightarrow X \rightarrow YZ
\]

**Example:** Given `StudentID → StudentName` and `StudentID → StudentAge`:

\[
StudentID \rightarrow \{StudentName, StudentAge\}
\]

#### Decomposition

If `X → YZ`, then `X → Y` and `X → Z`.

\[
X \rightarrow YZ \Rightarrow X \rightarrow Y \land X \rightarrow Z
\]

**Example:** Given `StudentID → {StudentName, StudentAge}`:

\[
StudentID \rightarrow StudentName
\]

\[
StudentID \rightarrow StudentAge
\]

#### Pseudotransitivity

If `X → Y` and `WY → Z`, then `WX → Z`.

\[
X \rightarrow Y \land WY \rightarrow Z \Rightarrow WX \rightarrow Z
\]

#### Contraction

If `X → Y` and `XY → Z`, then `X → Z`.

\[
X \rightarrow Y \land XY \rightarrow Z \Rightarrow X \rightarrow Z
\]

### 3.6 Worked derivation

Given:

\[
F = \{sid \rightarrow sname,\ sname \rightarrow city,\ sid \rightarrow age\}
\]

Derive the following:

1. `sid → {sname, age}`
2. `{sid, phone} → {sname, age}`
3. `sid → city`
4. `sid → sname` from `sid → {sname, city}`

**Solution:**

1. Apply union to `sid → sname` and `sid → age`:

   \[
   sid \rightarrow \{sname, age\}
   \]

2. Apply augmentation with `phone` to the result of step 1:

   \[
   \{sid, phone\} \rightarrow \{sname, age, phone\}
   \]

   Then apply decomposition to remove `phone` from the right-hand side:

   \[
   \{sid, phone\} \rightarrow \{sname, age\}
   \]

3. Apply transitivity to `sid → sname` and `sname → city`:

   \[
   sid \rightarrow city
   \]

4. Use union with `sid → sname` and `sid → city`, then apply decomposition:

   \[
   sid \rightarrow \{sname, city\}
   \]

   Therefore:

   \[
   sid \rightarrow sname
   \]

### 3.7 Why the axioms matter

Armstrong's axioms have two central properties:

- **Soundness:** Every derived dependency follows from the premises under the relational model.
- **Completeness:** Every dependency that follows from `F` can be derived using these axioms.

A student can often use closure computation instead of writing a full proof. The axioms explain why each closure step is valid.

### 3.8 Do not infer a rule from limited evidence

The inference rules act on known dependencies. They cannot create a business rule that was never supplied.

Given only the displayed student rows, a student may observe that `StudentID` and `StudentName` occur together. That observation does not prove that one determines the other for all valid data. The course's business rule supplies `StudentID → StudentName`; the axioms then derive further dependencies from that rule.

## 4. Data Redundancy and Update Anomalies

### 4.1 Redundancy

**Formal idea:** A relation contains redundancy when the same fact can be represented in more than one place, so that the copies must be kept consistent.

**Plain language:** The same college rank is repeated in every student row. Changing the rank means changing several rows, and changing only some rows creates conflicting answers.

The course's unnormalized student relation is:

| Student_ID | Name | Contact | College | Course | Rank |
|---:|---|---|---|---|---:|
| 100 | Michael | 7300934851 | GEU | B.Tech | 1 |
| 101 | David | 7900734858 | GEU | B.Tech | 1 |
| 102 | James | 7300936759 | GEU | B.Tech | 1 |
| 103 | William | 7300901556 | GEU | B.Tech | 1 |

The values `GEU`, `B.Tech`, and rank `1` repeat. Each row mixes three kinds of facts:

- Student facts: `Student_ID`, `Name`, and `Contact`
- College facts: `College` and `Rank`
- Course fact: `Course`

### 4.2 Data anomalies

An **anomaly** is an insert, update, or delete operation that causes unnecessary difficulty, loss of information, or inconsistency because the relation mixes facts in the wrong way.

| Anomaly | Operation in the course table | Problem | Required design response |
|---|---|---|---|
| Insertion | Add a new college before it has a student | No student row exists in which to store the college facts | Store college facts in `COLLEGE` |
| Insertion | Add a student whose course has not been decided | A single relation forces course information into the student row | Store the student independently and record the course assignment later, if the rules allow it |
| Update | Change GEU's rank | The rank must be changed in every GEU row; a missed row creates conflicting ranks | Store each college's rank once in `COLLEGE` |
| Delete | Delete the only student associated with GEU | GEU's name and rank disappear with that row | Delete the student row without deleting `COLLEGE` facts |

The slide's insertion example describes a student whose course is undecided. Whether that student may be stored is a business rule. If the system requires a course during admission, a foreign-key or validation rule should reject the incomplete assignment. If the system permits a student before course selection, the storage design should allow that state. The mixed relation obscures both cases.

### 4.3 Insertion anomaly

An **insertion anomaly** occurs when a valid fact cannot be inserted without supplying an unrelated fact or repeating information.

In the course table, suppose a new college receives its first student. Before the student is inserted, the database has nowhere to record the new college and its rank. The database forces the college to wait for a student.

A second form appears when the course is unknown. The row couples the student fact with a course fact, so the designer must choose one of two poor options:

- store a null or placeholder course value in a column whose business rule expects a decided course, or
- delay a valid student record until the course is known.

Separating the relations removes the storage coupling.

### 4.4 Update anomaly

An **update anomaly** occurs when one fact is stored in several rows, so every copy must be updated together.

If GEU's rank changes from `1` to `2`, the course table has four rank cells to update. A partial update leaves the database with more than one rank for GEU. Queries can then return conflicting results.

The update cost grows with the number of student rows. A single-row design gives one place to change.

### 4.5 Deletion anomaly

A **deletion anomaly** occurs when deleting one intended fact also removes an unrelated fact that has no other row.

If William is the only student shown for GEU, deleting his row also removes GEU and rank `1`. The college still exists, but the database can no longer identify its rank.

This problem depends on row counts in the current instance. The design defect remains because the relation has no independent home for the college fact.

### 4.6 Other effects of redundancy

The slides list several consequences:

- **Inconsistency:** Different copies can report different values.
- **Extra storage:** Repeated facts consume space.
- **Maintenance effort:** Scripts or applications must update every copy.
- **Security exposure:** More copies create more locations to protect.
- **User confusion:** Users may not know which copy is authoritative.

Some duplicated values can be necessary and harmless. A foreign-key value such as `GEU` repeated in student rows is a reference, not a repeated college description and rank. Normalization removes repeated descriptive facts while retaining references between them.

### 4.7 Decomposition of the course relation

#### Step 1: Identify the separate facts

- `STUDENT`: student identity, name, and contact
- `COLLEGE`: college identity, name, and rank
- `COURSE`: course identity and course name

#### Step 2: Create the relations

```text
STUDENT(Student_ID PK, Name, Contact, College FK -> COLLEGE.College, Course FK -> COURSE.Course)
COLLEGE(College PK, Rank)
COURSE(Course PK)
```

`College` and `Course` are natural keys in this model, so no surrogate-ID mapping is needed. `STUDENT.College` and `STUDENT.Course` may be nullable only when the admission and registration rules permit an undecided value.

#### Step 3: Allocate the rows

`COLLEGE`:

| College | Rank |
|---|---:|
| GEU | 1 |

`COURSE`:

| Course |
|---|
| B.Tech |

`STUDENT`:

| Student_ID | Name | Contact | College | Course |
|---:|---|---|---|---|
| 100 | Michael | 7300934851 | GEU | B.Tech |
| 101 | David | 7900734858 | GEU | B.Tech |
| 102 | James | 7300936759 | GEU | B.Tech |
| 103 | William | 7300901556 | GEU | B.Tech |

#### Step 4: Verify the result

Assume the original dependencies include:

\[
F = \{Student\_ID \rightarrow Name,\ Student\_ID \rightarrow Contact,\ Student\_ID \rightarrow College,\ Student\_ID \rightarrow Course,\ College \rightarrow Rank\}
\]

The projected dependencies are preserved locally:

- `STUDENT`: `Student_ID → Name, Contact, College, Course`
- `COLLEGE`: `College → Rank`
- `COURSE`: the key `Course` determines its single descriptive attribute

The decomposition is lossless because each foreign-key value in `STUDENT` references the unique key of one `COLLEGE` or `COURSE` row. Joining `STUDENT` to both referenced relations recreates each original row without adding a college/course pairing that was absent from `STUDENT`.

The result also removes the original anomalies:

- GEU's rank now appears once.
- `B.Tech` appears once as a course fact.
- Each student row keeps references to the college and course facts.
- Deleting the last student does not delete GEU's rank.
- A college can be inserted without a student.
- A student's course assignment can follow the system's registration rules.

### 4.8 Purpose of normalization

**Formal purpose:** FD-based normalization through 3NF and BCNF decomposes a relation according to its functional dependencies. 4NF and 5NF extend the analysis to multivalued and join dependencies so that each fact is stored in an appropriate relation.

**Plain purpose:** Normalization removes repeated facts and reduces the chance of update, insert, and delete anomalies.

Normalization is a design method rather than a guarantee of correctness. A relation can satisfy a normal-form rule while still missing a business constraint, and it can contain redundancy for performance reasons. Designers evaluate the dependencies, required operations, and acceptable trade-offs.

## 5. Keys and Attribute Classification

### 5.1 Superkey

A **superkey** of relation `R` is an attribute set `K` that determines every attribute of `R`:

\[
K \rightarrow R
\]

Equivalently:

\[
K^{+} = R
\]

A superkey identifies every row uniquely under the relation's business rules. It may contain extra attributes.

Example for `TEACHER_ASSIGNMENT(TEACHER_ID, SUBJECT, TEACHER_AGE)`:

- `{TEACHER_ID, SUBJECT}` is a superkey.
- `{TEACHER_ID, SUBJECT, TEACHER_AGE}` is a superkey.
- `{TEACHER_ID}` alone is not a superkey because teacher 25 teaches two subjects.

A superkey can contain one attribute. The slide wording “a set of over one key” is too narrow.

### 5.2 Candidate key

A **candidate key** is a minimal superkey.

It has two required properties:

1. **Uniqueness:** The key determines every attribute and therefore identifies each row.
2. **Minimality:** Removing any attribute from the key destroys the uniqueness property.

For the teacher assignment relation, assume these business rules:

1. A teacher has one age, so `TEACHER_ID → TEACHER_AGE`.
2. A teacher can teach more than one subject, so `TEACHER_ID` alone is not a superkey.
3. The same subject can be assigned to different teachers, so `SUBJECT` alone is not a superkey.
4. Each teacher-subject pair occurs at most once, so `{TEACHER_ID, SUBJECT}` uniquely identifies an assignment.

Then:

\[
\{TEACHER\_ID, SUBJECT\} \rightarrow \{TEACHER\_ID, SUBJECT, TEACHER\_AGE\}
\]

Neither attribute can be removed under these rules:

- `{TEACHER_ID}` cannot distinguish teacher's two subject assignments.
- `{SUBJECT}` cannot distinguish different teachers.

Therefore, `{TEACHER_ID, SUBJECT}` is the candidate key. The slide's sentence that a teacher can teach more than one subject alone does not prove the claim; the other three premises are required.

#### Reconciling the slide 26 candidate-key example

Slide 26 highlights `id` and `roll_no` together as a “candidate key.” The displayed rows give different values for both columns. If the business rules guarantee that `id` is unique and that `roll_no` is also unique, then `{id}` and `{roll_no}` are candidate keys, while `{id, roll_no}` is only a non-minimal superkey. If uniqueness of either singleton is not guaranteed, the sample proves neither key. The composite set cannot be called a candidate key until the designer states which rules make it unique and minimal.

### 5.3 Primary key and alternate key

A relation has one selected **primary key**, chosen from its candidate keys. The remaining candidate keys are **alternate keys**.

For example, if another candidate key existed for the teacher relation, the designer could select `{TEACHER_ID, SUBJECT}` as the primary key and treat the other as an alternate key.

Every candidate key is a superkey, but not every superkey is a candidate key. The primary key is not a subset of every superkey; it is one member of the family of superkeys.

### 5.4 Prime and non-prime attributes

- A **prime attribute** belongs to at least one candidate key.
- A **non-prime attribute** belongs to no candidate key.

The terms **key attribute** and **non-key attribute** are often used for prime and non-prime attributes.

For `TEACHER_ASSIGNMENT`:

| Attribute | Classification | Reason |
|---|---|---|
| `TEACHER_ID` | Prime | Appears in candidate key `{TEACHER_ID, SUBJECT}` |
| `SUBJECT` | Prime | Appears in candidate key `{TEACHER_ID, SUBJECT}` |
| `TEACHER_AGE` | Non-prime | Appears in no candidate key |

The phrase “non-key attribute” should not be interpreted as “an attribute absent from the selected primary key.” If a relation has several candidate keys, an attribute can be absent from the primary key yet remain prime.

### 5.5 Composite key

A **composite key** contains two or more attributes.

The course's teacher relation needs a composite key because a teacher can teach more than one subject:

\[
PK(TEACHER\_ID, SUBJECT)
\]

A composite key is valid in 1NF. The 1NF restriction concerns atomic cell values, not the number of attributes in a key.

### 5.6 Foreign key

A **foreign key** is an attribute set in one relation that references a candidate key in another relation or in the same relation. It represents a relationship between tuples.

In the decomposed student design:

```text
STUDENT.Student_ID       PK
STUDENT.College          FK -> COLLEGE.College
STUDENT.Course           FK -> COURSE.Course
```

Referential integrity requires each non-null `College` value to match an existing college key. A `Course` foreign key may be nullable only when the admission and registration rules permit an undecided course. Foreign keys also support join-based queries.

### 5.7 The course's zip-code example

The slides give this employee relation:

| EMP_ID | EMP_NAME | EMP_ZIP | EMP_STATE | EMP_CITY |
|---:|---|---|---|---|
| 222 | Harry | 201010 | UP | Noida |
| 333 | Stephan | 02228 | US | Boston |
| 444 | Lan | 60007 | US | Chicago |
| 555 | Katharine | 06389 | UK | Norwich |
| 666 | John | 462007 | MP | Bhopal |

The course identifies `{EMP_ID}` as the candidate key. Examples of superkeys include:

- `{EMP_ID}`
- `{EMP_ID, EMP_NAME}`
- `{EMP_ID, EMP_NAME, EMP_ZIP}`
- `{EMP_ID, EMP_ZIP, EMP_CITY}`

Here `EMP_ID` is prime. `EMP_NAME`, `EMP_ZIP`, `EMP_STATE`, and `EMP_CITY` are non-prime.

The stated dependencies include:

\[
EMP\_ID \rightarrow EMP\_NAME
\]

\[
EMP\_ID \rightarrow EMP\_ZIP
\]

\[
EMP\_ZIP \rightarrow EMP\_STATE
\]

\[
EMP\_ZIP \rightarrow EMP\_CITY
\]

Thus `EMP_STATE` and `EMP_CITY` depend transitively on `EMP_ID` through `EMP_ZIP`. Part 2 decomposes this relation for 3NF.

Store `EMP_ZIP` as character data when the domain includes values such as `02228` and `06389`. A numeric type could discard a leading zero and merge distinct codes.

### 5.8 Key discovery procedure

For each relation:

1. Write the business rules as FDs.
2. Compute the closure of each plausible key.
3. Keep sets whose closure contains every attribute.
4. Remove any set that contains a smaller set with the same property.
5. List the remaining sets as candidate keys.
6. Choose one primary key and identify the others as alternate keys.
7. Mark every attribute in any candidate key as prime.

Uniqueness in one displayed table is evidence for investigation. It does not establish a key unless the business rules guarantee that the uniqueness will hold in every valid instance.

## 6. First Normal Form (1NF)

### 6.1 Formal definition

A relation `R` is in **First Normal Form (1NF)** when each attribute value in each tuple is atomic with respect to the relation's domains, and the relation has no repeating groups.

**Plain language:** One cell holds one value from one domain. A cell cannot contain a list, an array, or another table.

### 6.2 What atomicity means

An atomic value is one value from a declared domain that the relational model treats as indivisible. Lists, sets, arrays, nested relations, and repeating groups are non-atomic for this purpose.

Examples:

- A phone number can be one value in a phone-number domain.
- A student's name can remain one value in a name domain; a composite conceptual name may be represented by separate atomic columns when the schema manages its parts separately.
- A course cell such as `c++, ET` is non-atomic because it stores a repeating group of course values.
- A ZIP code such as `02228` can remain one character value, with its leading zero preserved.

Application requirements help the designer choose domains, but changing future application operations does not change whether a declared schema satisfies 1NF.

### 6.3 The course's 1NF student example

The course table contains repeating groups in the `course` cell:

| rollno | name | course | age |
|---:|---|---|---:|
| 1 | Rahul | c++, ET | 22 |
| 2 | Harsh | java | 18 |
| 3 | Sahil | c++, ET | 23 |
| 4 | Adam | c | 22 |
| 5 | Lisa | java | 24 |
| 6 | James | c++, ET | 19 |

This relation violates 1NF because `course` contains a repeating group. The value `c++, ET` contains two course values.

### 6.4 1NF transformation

Move each course value into its own row:

| rollno | name | course | age |
|---:|---|---|---:|
| 1 | Rahul | c++ | 22 |
| 1 | Rahul | ET | 22 |
| 2 | Harsh | java | 18 |
| 3 | Sahil | c++ | 23 |
| 3 | Sahil | ET | 23 |
| 4 | Adam | c | 22 |
| 5 | Lisa | java | 24 |
| 6 | James | c++ | 19 |
| 6 | James | ET | 19 |

The relation now has:

- One course value per cell.
- No repeating course group in a row.
- A composite key `{rollno, course}` that identifies each row.

The slide states that 1NF also makes “every column have unique values.” That statement is incorrect. In this valid 1NF relation:

- `name` repeats because Rahul has two courses.
- `age` repeats because two students are 22.
- `course` repeats because different students take it.

1NF concerns the structure of each value. It does not require unique values in each column.

### 6.5 Optional decomposition after reaching 1NF

If a student can have several course rows, the designer can separate student facts from enrolment facts:

```text
STUDENT(rollno PK, name, age)
ENROLLMENT(rollno FK -> STUDENT.rollno, course, PK(rollno, course))
```

`ENROLLMENT` has the composite primary key `{rollno, course}`. `rollno` is a foreign key that participates in that composite key; it is not a standalone primary key.

This further decomposition reduces repeated student details. `STUDENT` has a singleton key. `ENROLLMENT` has a composite key but no non-prime attributes, so it cannot contain a partial dependency of a non-prime attribute.

### 6.6 Composite attributes and atomic columns

The source says that 1NF disallows composite attributes. The relational implementation needs a precise interpretation:

- A composite **value** such as `c++, ET` violates atomicity because it contains a repeating group.
- A composite **key** is valid in 1NF.
- A conceptual composite attribute can be represented as separate atomic columns when the application manages those parts separately.

The rule targets repeating groups inside one cell. It does not ban multi-column keys.

### 6.7 Null values and missing information

A null value represents a missing or inapplicable value under the schema's null policy. It does not by itself violate 1NF.

If the business permits a student before course selection, model the pending state with a nullable `Course` foreign key outside any confirmed enrolment key, or use a separate `APPLICATION` relation with a surrogate key and nullable `Course`. A confirmed `ENROLLMENT(rollno, course)` relation has a composite primary key, so neither member may be NULL. A cell containing `c++, ET` remains a repeating group regardless of whether either course is currently known.

### 6.8 1NF test

A relation is in 1NF when all of the following hold:

1. Each cell contains one value from its declared domain.
2. No cell contains a list, set, array, or nested table.
3. No repeating group appears within a row.
4. The relation has a key that identifies rows.
5. Each attribute has a coherent domain and consistent meaning across rows.

## 7. Second Normal Form (2NF)

### 7.1 Formal definition

A relation `R` is in **Second Normal Form (2NF)** when:

1. `R` is in 1NF, and
2. every non-prime attribute is fully functionally dependent on every candidate key of `R`.

**Plain language:** No non-prime attribute depends on only part of a composite candidate key.

The slides use “primary key” in the definition. The full test uses **every candidate key**, because a violation involving an alternate candidate key is still a 2NF violation.

### 7.2 Partial and full functional dependency

Let `K` be a candidate key and `A` a non-prime attribute.

- `A` **partially depends** on `K` when some proper subset `K' ⊂ K` determines `A`:

  \[
  K' \rightarrow A,\quad K' \subset K
  \]

- `A` **fully depends** on `K` when `K → A` and no proper subset of `K` determines `A`.

Partial dependency requires a composite candidate key. A relation whose candidate keys are all singleton cannot have a partial dependency of this form.

### 7.3 FD test for 2NF

A relation in 1NF is in 2NF exactly when no non-prime attribute is determined by a proper subset of any candidate key. Equivalently, for every nontrivial FD `X → A` with non-prime `A`, `X` must not be a proper subset of any candidate key.

Do not use the 3NF condition “`X` is a superkey” here. A 2NF relation may still contain a transitive dependency. For example, in `R(A, B, C)` with `F = {C → A, C → B, A → B}`, `{C}` is the candidate key and the relation is in 2NF, even though the determinant `A` in `A → B` is not a superkey.

For the teacher assignment relation:

\[
TEACHER\_ID \rightarrow TEACHER\_AGE
\]

`TEACHER_AGE` is non-prime, and `{TEACHER_ID}` is a proper subset of the candidate key `{TEACHER_ID, SUBJECT}`. The dependency violates 2NF.

### 7.4 Course example: teacher and subject assignments

The source gives:

| TEACHER_ID | SUBJECT | TEACHER_AGE |
|---:|---|---:|
| 25 | Chemistry | 30 |
| 25 | Biology | 30 |
| 47 | English | 35 |
| 83 | Math | 38 |
| 83 | Computer | 38 |

Assume that a teacher has one age, the same subject can be assigned to different teachers, and each teacher-subject pair occurs at most once. Together with the slide's rule that a teacher can teach more than one subject, these premises give:

\[
\{TEACHER\_ID, SUBJECT\} \rightarrow \{TEACHER\_ID, SUBJECT, TEACHER\_AGE\}
\]

The candidate key is `{TEACHER_ID, SUBJECT}`. Without the uniqueness and repetition assumptions, the slide's sentence by itself does not establish a candidate key.

The dependency:

\[
TEACHER\_ID \rightarrow TEACHER\_AGE
\]

creates a partial dependency because `{TEACHER_ID}` is a proper subset of the candidate key. `TEACHER_AGE` is a non-prime attribute. The original relation is in 1NF but not in 2NF.

### 7.5 Decomposition procedure

1. **Confirm 1NF.** Each cell contains one value.
2. **Find every candidate key.** Here, `K = {TEACHER_ID, SUBJECT}`.
3. **Find partial dependencies.** `TEACHER_ID → TEACHER_AGE` depends on a proper subset of `K`.
4. **Create a relation for the determinant and dependent.** Put `TEACHER_ID` and `TEACHER_AGE` in `TEACHER_DETAIL`.
5. **Create a relation for the remaining assignment fact.** Put `TEACHER_ID` and `SUBJECT` in `TEACHER_SUBJECT`.
6. **Assign keys and foreign keys.** Use `TEACHER_ID` as the key of `TEACHER_DETAIL`; use `{TEACHER_ID, SUBJECT}` in `TEACHER_SUBJECT`; link the subject rows to the teacher detail.
7. **Verify the result.** Both relations are in 2NF, the join is lossless, and the dependency is preserved.

### 7.6 Resulting relations

`TEACHER_DETAIL`:

| TEACHER_ID | TEACHER_AGE |
|---:|---:|
| 25 | 30 |
| 47 | 35 |
| 83 | 38 |

`TEACHER_SUBJECT`:

| TEACHER_ID | SUBJECT |
|---:|---|
| 25 | Chemistry |
| 25 | Biology |
| 47 | English |
| 83 | Math |
| 83 | Computer |

Schema:

```text
TEACHER_DETAIL(TEACHER_ID PK, TEACHER_AGE)
TEACHER_SUBJECT(TEACHER_ID FK -> TEACHER_DETAIL.TEACHER_ID, SUBJECT, PK(TEACHER_ID, SUBJECT))
```

Teacher 25 now has one age value in `TEACHER_DETAIL` and two subject assignments in `TEACHER_SUBJECT`.

### 7.7 Verify the decomposition

#### Lossless join

The common attributes are `{TEACHER_ID}`. In `TEACHER_DETAIL`, `{TEACHER_ID}` is a key. Therefore, the common attribute set determines all attributes of `TEACHER_DETAIL`, which establishes a lossless decomposition for this binary split.

Joining the two relations on `TEACHER_ID` recreates every original teacher-subject-age row without adding or losing assignments.

#### Dependency preservation

Dependency preservation means that the union of the projected dependencies entails every original dependency:

\[
(F_1 \cup F_2)^+ \vDash F
\]

Here, `TEACHER_DETAIL` enforces `TEACHER_ID → TEACHER_AGE`, and the key of `TEACHER_SUBJECT` enforces `TEACHER_ID → SUBJECT`. Augmentation gives `{TEACHER_ID, SUBJECT} → {TEACHER_AGE, SUBJECT}`; decomposition then gives `{TEACHER_ID, SUBJECT} → TEACHER_AGE`. Thus the original partial dependency follows from local constraints, so the decomposition is dependency preserving.

### 7.8 Two common 2NF errors

- **Testing only the selected primary key.** A relation with two candidate keys must satisfy the full-dependency condition for both.
- **Calling every dependency on a composite key partial.** A dependency is partial only when a proper subset of the key determines the dependent and that dependent is non-prime.

## 8. Worked Normalization Examples and Common Traps

### 8.1 Worked Exercise 1: Classify dependencies and compute a closure

**Relation:**

```text
STUDENT(StudentID, StudentName, StudentAge)
```

**Dependencies:**

\[
F = \{StudentID \rightarrow StudentName,\ StudentID \rightarrow StudentAge\}
\]

**Tasks:**

1. Classify `{StudentID, StudentName} → StudentName`.
2. Classify `StudentID → StudentName`.
3. Compute `{StudentID}⁺`.
4. Find a candidate key.
5. Decide whether `StudentName → StudentAge` holds for the course's displayed data.

**Solution:**

1. The dependency is **trivial** because `StudentName ⊆ {StudentID, StudentName}`.
2. `StudentID → StudentName` is **nontrivial** because `StudentName` is outside the determinant. It is also fully nontrivial because the attribute sets have no common attribute.
3. Start with `{StudentID}`. Both dependencies in `F` apply, so add `StudentName` and `StudentAge`:

   \[
   \{StudentID\}^{+} = \{StudentID, StudentName, StudentAge\}
   \]

4. `{StudentID}` is a superkey because its closure contains every attribute. It is also minimal, so it is the candidate key.
5. The displayed students named `Ankit` have ages 22 and 23. Thus `StudentName → StudentAge` fails for the sample relation.

### 8.2 Worked Exercise 2: Apply Armstrong's axioms

**Given:**

\[
F = \{enrol\_no \rightarrow name,\ enrol\_no \rightarrow dept,\ dept \rightarrow building\_no\}
\]

**Tasks:**

1. Derive `enrol_no → {name, dept}`.
2. Derive `enrol_no → building_no`.
3. Derive `enrol_no → {name, dept, building_no}`.
4. Apply decomposition to the third result, then decide whether `dept → building_no` and `dept → name` follow from the given facts.

**Solution:**

1. Apply **union** to `enrol_no → name` and `enrol_no → dept`:

   \[
   enrol\_no \rightarrow \{name, dept\}
   \]

2. Apply **transitivity** to `enrol_no → dept` and `dept → building_no`:

   \[
   enrol\_no \rightarrow building\_no
   \]

3. Apply **union** to the results of steps 1 and 2:

   \[
   enrol\_no \rightarrow \{name, dept, building\_no\}
   \]

4. Apply **decomposition** to step 3:

   \[
   enrol\_no \rightarrow dept
   \]

   \[
   enrol\_no \rightarrow name
   \]

   \[
   enrol\_no \rightarrow building\_no
   \]

   `dept → building_no` is one of the original premises. `dept → name` does not follow. There is no premise that lets `dept` determine `name`.

### 8.3 Worked Exercise 3: Diagnose and remove redundancy

**Relation:**

| Student_ID | Name | Contact | College | Course | Rank |
|---:|---|---|---|---|---:|
| 100 | Michael | 7300934851 | GEU | B.Tech | 1 |
| 101 | David | 7900734858 | GEU | B.Tech | 1 |
| 102 | James | 7300936759 | GEU | B.Tech | 1 |

**Tasks:**

1. Identify the repeated facts.
2. Describe one insert anomaly, one update anomaly, and one delete anomaly.
3. Propose a decomposition.
4. Explain why the new foreign-key values do not count as harmful redundancy.

**Solution:**

1. `GEU`, `B.Tech`, and rank `1` are repeated facts about a college or course.
2. **Insert:** a new college cannot be recorded until a student refers to it. **Update:** a rank change requires three row updates. **Delete:** deleting James, the last shown GEU student, also removes the stored college rank.
3. A suitable decomposition is:

   ```text
   STUDENT(Student_ID PK, Name, Contact, College FK -> COLLEGE.College, Course FK -> COURSE.Course)
   COLLEGE(College PK, Rank)
   COURSE(Course PK)
   ```

4. A student row can repeat the foreign-key value `GEU`. This is a reference to one stored college fact. The description `GEU` and its rank exist only in `COLLEGE`, so there is no repeated descriptive fact to synchronize. The decomposition is lossless because each foreign key references a unique parent key, and it preserves `Student_ID → Name, Contact, College, Course` and `College → Rank` through the projected dependencies.

### 8.4 Worked Exercise 4: Classify keys and attributes

Use these two course relations:

```text
TEACHER_ASSIGNMENT(TEACHER_ID, SUBJECT, TEACHER_AGE)
```

```text
EMPLOYEE_DETAIL(EMP_ID, EMP_NAME, EMP_ZIP, EMP_STATE, EMP_CITY)
```

**Tasks:**

1. Find a candidate key for `TEACHER_ASSIGNMENT` and identify its prime and non-prime attributes.
2. Give two superkeys for `TEACHER_ASSIGNMENT`.
3. Find a candidate key for `EMPLOYEE_DETAIL` and classify its attributes.
4. Identify one transitive dependency in `EMPLOYEE_DETAIL`.

**Solution:**

1. The candidate key is `{TEACHER_ID, SUBJECT}`. `TEACHER_ID` and `SUBJECT` are prime. `TEACHER_AGE` is non-prime.
2. Examples are `{TEACHER_ID, SUBJECT}` and `{TEACHER_ID, SUBJECT, TEACHER_AGE}`.
3. The candidate key is `{EMP_ID}`. `EMP_ID` is prime. The other four attributes are non-prime.
4. `EMP_ZIP → EMP_STATE` and `EMP_ID → EMP_ZIP` imply the transitive dependency:

   \[
   EMP\_ID \rightarrow EMP\_STATE
   \]

   through `EMP_ZIP`.

### 8.5 Worked Exercise 5: Convert a relation to 1NF

**Unnormalized relation:**

| rollno | name | course | age |
|---:|---|---|---:|
| 1 | Rahul | c++, ET | 22 |
| 2 | Harsh | java | 18 |
| 3 | Sahil | c++, ET | 23 |
| 4 | Adam | c | 22 |
| 5 | Lisa | java | 24 |
| 6 | James | c++, ET | 19 |

**Tasks:**

1. State the 1NF violation.
2. Convert the relation to 1NF.
3. Identify the key.
4. Decide whether repeated names, ages, or courses violate 1NF.
5. Give an optional two-relation design.

**Solution:**

1. The `course` cells for roll numbers 1, 3, and 6 contain repeating groups.
2. Create one row per course:

   | rollno | name | course | age |
   |---:|---|---|---:|
   | 1 | Rahul | c++ | 22 |
   | 1 | Rahul | ET | 22 |
   | 2 | Harsh | java | 18 |
   | 3 | Sahil | c++ | 23 |
   | 3 | Sahil | ET | 23 |
   | 4 | Adam | c | 22 |
   | 5 | Lisa | java | 24 |
   | 6 | James | c++ | 19 |
   | 6 | James | ET | 19 |

3. The key is `{rollno, course}` under the stated enrolment rules.
4. Repeated values across rows are valid in 1NF. The rule applies to the values inside each cell.
5. A further design is:

   ```text
   STUDENT(rollno PK, name, age)
   ENROLLMENT(rollno FK -> STUDENT.rollno, course, PK(rollno, course))
   ```

### 8.6 Worked Exercise 6: Test and repair 2NF

**Relation:**

| TEACHER_ID | SUBJECT | TEACHER_AGE |
|---:|---|---:|
| 25 | Chemistry | 30 |
| 25 | Biology | 30 |
| 47 | English | 35 |
| 83 | Math | 38 |
| 83 | Computer | 38 |

**Dependencies:**

\[
F = \{TEACHER\_ID \rightarrow TEACHER\_AGE,\ TEACHER\_ID \rightarrow SUBJECT,\ \{TEACHER\_ID, SUBJECT\} \rightarrow TEACHER\_AGE\}
\]

Assume that each teacher-subject pair occurs at most once and that a subject may be assigned to different teachers.

**Tasks:**

1. Find the candidate key.
2. Identify the partial dependency.
3. Decompose the relation into 2NF.
4. Show that the decomposition is lossless.
5. Show that the original functional dependency is preserved.

**Solution:**

1. `{TEACHER_ID, SUBJECT}` is the candidate key.
2. `TEACHER_AGE` is non-prime, and `{TEACHER_ID} → TEACHER_AGE` depends on a proper subset of the candidate key.
3. Decompose the relation:

   ```text
   TEACHER_DETAIL(TEACHER_ID PK, TEACHER_AGE)
   TEACHER_SUBJECT(TEACHER_ID FK -> TEACHER_DETAIL.TEACHER_ID, SUBJECT, PK(TEACHER_ID, SUBJECT))
   ```

4. The shared attribute set is `{TEACHER_ID}`. It is the primary key of `TEACHER_DETAIL`, so it determines every attribute in that component. The binary decomposition is therefore lossless.
5. `TEACHER_ID → TEACHER_AGE` is enforced in `TEACHER_DETAIL`, and `TEACHER_ID → SUBJECT` follows from the key of `TEACHER_SUBJECT`. Augmentation and decomposition derive `{TEACHER_ID, SUBJECT} → TEACHER_AGE`, so `(F₁ ∪ F₂)⁺ ⊨ F`. The decomposition is dependency preserving.

### 8.7 Common traps

1. **Treating a sample pattern as a universal rule.** A dependency must hold for every valid instance, including future data.
2. **Reversing the arrow.** `X → Y` means that `X` determines `Y`. It does not mean that `Y` determines `X`.
3. **Confusing names with identifiers.** Two students can be named `Ankit`, so a name does not identify one student.
4. **Calling every dependency trivial.** A dependency is trivial only when the right-hand attribute set is contained in the left-hand set.
5. **Treating union and decomposition as extra Armstrong axioms.** Both are derived from reflexivity, augmentation, and transitivity.
6. **Calling every superkey a candidate key.** A candidate key must also be minimal.
7. **Confusing prime and non-prime with primary and other attributes.** An attribute in any candidate key is prime.
8. **Requiring unique column values for 1NF.** 1NF requires atomic cell values and a proper relation structure.
9. **Rejecting composite keys in 1NF.** Composite keys are valid. 2NF examines whether non-prime attributes depend on only part of such a key.
10. **Ignoring alternate candidate keys in the 2NF test.** Test full functional dependence against every candidate key.
11. **Using a multivalued dependency when a functional dependency is meant.** The symbol `↠` represents independent multivalues; `→` represents a single determined value.
12. **Treating repeated foreign keys as repeated facts.** A repeated key reference can be normal. The concern is repeated descriptive data that can conflict.
13. **Preserving ZIP codes as integers.** Leading zeros can disappear or merge distinct codes.
14. **Assuming decomposition is always safe.** Check both lossless join and dependency preservation.
15. **Stopping after 2NF.** Transitive dependencies can remain in a 2NF relation, as the employee zip-code example shows.

### 8.8 Part 1 Revision Checklist

Use this checklist for revision and exam preparation.

#### Functional dependencies

- [ ] I can state the formal definition of `X → Y`.
- [ ] I can explain determinant and dependent in plain language.
- [ ] I can distinguish trivial, nontrivial, and fully nontrivial dependencies.
- [ ] I can identify a transitive dependency from two stated FDs.
- [ ] I can distinguish `→` from `↠`.
- [ ] I can compute an attribute closure with repeated application of `F`.

#### Armstrong axioms

- [ ] I can state reflexivity, augmentation, and transitivity.
- [ ] I can apply union and decomposition.
- [ ] I can show a multi-step derivation from course examples.
- [ ] I know that Armstrong's axioms are sound and complete for FDs.
- [ ] I do not infer a business rule from one sample table.

#### Redundancy and anomalies

- [ ] I can describe insert, update, and delete anomalies.
- [ ] I can use the course's GEU, B.Tech, and rank example.
- [ ] I can explain why repeated foreign-key references differ from repeated descriptive facts.
- [ ] I can split student, college, and course facts into separate relations.

#### Keys

- [ ] I can distinguish superkey, candidate key, primary key, and alternate key.
- [ ] I can test minimality of a candidate key.
- [ ] I can classify prime and non-prime attributes.
- [ ] I can recognise composite and foreign keys.
- [ ] I can classify the teacher/subject and employee/zip-code examples.

#### 1NF

- [ ] I can define atomicity in terms of the chosen domains.
- [ ] I can convert a repeating-group course cell into rows.
- [ ] I can explain why duplicate values across rows do not violate 1NF.
- [ ] I can explain why a composite key remains valid in 1NF.

#### 2NF

- [ ] I can state the 2NF definition using all candidate keys.
- [ ] I can identify a partial dependency.
- [ ] I can decompose the teacher/subject relation step by step.
- [ ] I can verify the teacher decomposition for lossless join and dependency preservation.

---

## 9. Third Normal Form (3NF)

### 9.1 Formal definition

Let:

- `R(A1, A2, ..., An)` be a relation schema.
- `F` be a set of functional dependencies that holds on `R`.
- A **prime attribute** belong to at least one candidate key of `R`.
- A **non-prime attribute** belong to no candidate key of `R`.
- A **superkey** be a set of attributes that functionally determines every attribute in `R`.

Because 3NF requires 2NF, recall the precise 2NF condition. `R` is in 2NF when it is in 1NF and, for every non-prime attribute `A` and every candidate key `K`, full dependence holds:

\[
K \rightarrow A
\quad\Rightarrow\quad
\not\exists K' \subsetneq K \text{ such that } K' \rightarrow A
\]

Thus every non-prime attribute must be fully dependent on every candidate key, not only on the selected primary key.

A relation `R` is in **Third Normal Form (3NF)** if, for every nontrivial functional dependency

\[
X \rightarrow Y
\]

that holds on `R`, at least one of the following conditions holds:

1. `X` is a superkey of `R`; or
2. every attribute in `Y` is prime.

Equivalently:

\[
R \text{ is in 3NF}
\iff
\forall X \rightarrow Y \in F^+,\;
Y \not\subseteq X \Rightarrow
\bigl(X^+ = R \bigr) \lor \bigl(Y \subseteq \operatorname{Prime}(R)\bigr)
\]

The condition is applied to each dependency as a set. If `Y` contains both prime and non-prime attributes, condition 2 does not hold.

### 9.2 What 3NF removes

A relation in 1NF can still contain:

- a partial dependency of a non-prime attribute on part of a candidate key, which violates 2NF; or
- a transitive dependency of a non-prime attribute through another non-prime attribute, which violates 3NF.

The usual transitive pattern is:

\[
K \rightarrow A,\qquad A \rightarrow B
\]

where:

- `K` is a candidate key;
- `A` and `B` are non-prime attributes; and
- therefore `K \rightarrow B` by transitivity.

The value of `B` is stored repeatedly for every row associated with the same `A`. Updating one copy can leave the relation inconsistent.

### 9.3 Stepwise 3NF decomposition

Use the following procedure for a relation `R` with dependency set `F`:

1. Find the candidate keys of `R`.
2. Identify the prime and non-prime attributes.
3. Compute a minimal cover `F'` of `F`.
4. Find a nontrivial dependency `X \rightarrow A` in `F'` such that:
   - `X` is not a superkey of `R`; and
   - `A` is non-prime.
5. Split `R` into:

   \[
   R_1 = X \cup \{A\}, \qquad R_2 = R - \{A\}
   \]

6. Verify the binary lossless-join condition:

   \[
   (R_1 \cap R_2) \rightarrow R_1
   \quad\text{or}\quad
   (R_1 \cap R_2) \rightarrow R_2
   \]

   Here, `R1 ∩ R2 = X`, and `X \rightarrow A` gives `X \rightarrow R1`. The decomposition is therefore lossless.
7. Compute the projected dependencies `F1` and `F2` for `R1` and `R2`.
8. Apply the same test to each resulting relation until every relation satisfies 3NF.
9. Check dependency preservation:

   \[
   (F_1 \cup F_2 \cup \cdots \cup F_n)^+ = F^+
   \]

A recursive decomposition of this form guarantees the lossless-join property at each step. It does not automatically preserve every original dependency. A **3NF synthesis algorithm** that adds a relation for a candidate key when needed is the standard method for obtaining a dependency-preserving 3NF design.

### 9.4 Worked decomposition: employee and postal details

Consider the source relation:

```text
EMPLOYEE_DETAIL(
    emp_id, emp_name, emp_zip, emp_state, emp_city
)
```

Assume the dependencies:

```text
emp_id  -> emp_name
emp_id  -> emp_zip
emp_zip -> emp_state
emp_zip -> emp_city
```

#### Step 1: Find candidate keys

\[
emp\_id \rightarrow emp\_name, emp\_zip, emp\_state, emp\_city
\]

Thus:

- candidate key: `{emp_id}`;
- prime attribute: `emp_id`;
- non-prime attributes: `emp_name`, `emp_zip`, `emp_state`, `emp_city`.

#### Step 2: Find the 3NF violation

\[
emp\_zip \rightarrow emp\_state,\ emp\_city
\]

The determinant `emp_zip` is not a superkey, and the right-hand attributes are non-prime. The original relation is not in 3NF.

#### Step 3: Decompose

Create:

```text
EMPLOYEE_ZIP(emp_zip, emp_state, emp_city)
EMPLOYEE(emp_id, emp_name, emp_zip)
```

#### Step 4: Verify lossless join

\[
R_1 \cap R_2 = \{emp\_zip\}
\]

The projected dependency set of `R1` contains:

\[
emp\_zip \rightarrow emp\_state,\ emp\_city
\]

Therefore:

\[
(R_1 \cap R_2) \rightarrow R_1
\]

The binary decomposition is lossless.

#### Step 5: Verify dependency preservation

The projected dependencies are:

```text
F1 = { emp_zip -> emp_state, emp_city }
F2 = { emp_id -> emp_name, emp_zip }
```

Their union derives every original dependency:

- `emp_id -> emp_name`;
- `emp_id -> emp_zip`;
- `emp_id -> emp_state` by transitivity through `emp_zip`;
- `emp_id -> emp_city` by transitivity through `emp_zip`.

Hence:

\[
(F_1 \cup F_2)^+ = F^+
\]

The decomposition preserves dependencies.

#### Step 6: Verify 3NF

- In `EMPLOYEE_ZIP`, `emp_zip` is the candidate key.
- In `EMPLOYEE`, `emp_id` is the candidate key.
- Every nontrivial projected dependency has a candidate key as its determinant.

Both relations are in 3NF. They are also in BCNF because each has a single-attribute candidate key.

### 9.5 3NF and transitive dependencies: the precise distinction

The source description, "no transitive dependency exists," is too broad. A relation may contain a transitive dependency whose right-hand attribute is prime and still satisfy 3NF.

For example, let:

```text
R(student_id, subject, professor)
F = {
    {student_id, subject} -> professor,
    professor -> subject
}
```

Here:

- `{student_id, subject}` is a candidate key;
- `{student_id, professor}` is also a candidate key because `professor -> subject`;
- `subject` is prime because it occurs in a candidate key.

The dependency:

\[
professor \rightarrow subject
\]

does not violate 3NF because `subject` is prime. It does violate BCNF because `professor` is not a superkey. This example is developed in Section 10.

### 9.6 A 3NF test checklist

For each relation, ask:

1. Is the relation in 2NF?
2. What are all candidate keys?
3. Which attributes are prime?
4. For every nontrivial `X -> Y`:
   - Is `X` a superkey? If yes, the dependency satisfies 3NF.
   - If no, is every attribute of `Y` prime? If yes, the dependency satisfies 3NF.
   - If no, decompose the relation.

### 9.7 Common traps

- **Using only the chosen primary key:** 3NF is defined using every candidate key, not only the primary key selected for implementation.
- **Testing `Y` as a whole instead of attribute by attribute:** The standard condition requires every right-hand-side attribute to be prime.
- **Saying that 3NF forbids every transitive dependency:** 3NF permits a transitive dependency when its right-hand attributes are prime.
- **Treating a superkey as the same thing as a candidate key:** Every candidate key is a superkey, but a superkey may contain redundant attributes.
- **Assuming that decomposition always preserves dependencies:** Lossless join and dependency preservation are separate properties.

### 9.8 3NF in brief

| Aspect | 3NF rule |
|---|---|
| Prerequisite | The relation is in 2NF and therefore also in 1NF |
| Dependency tested | Every nontrivial functional dependency `X -> Y` |
| Condition 1 | `X` is a superkey |
| Condition 2 | Every attribute in `Y` is prime |
| Main purpose | Remove non-prime transitive dependencies while retaining key information |
| Relationship to BCNF | Every BCNF relation is in 3NF, but not every 3NF relation is in BCNF |

## 10. Boyce-Codd Normal Form (BCNF)

### 10.1 Formal definition

A relation `R` is in **Boyce-Codd Normal Form (BCNF)** if and only if, for every nontrivial functional dependency

\[
X \rightarrow Y
\]

that holds on `R`, `X` is a superkey of `R`.

In closure notation:

\[
R \text{ is in BCNF}
\iff
\forall X \rightarrow Y \in F^+,\;
Y \not\subseteq X \Rightarrow X^+ = R
\]

Equivalently, every determinant in every nontrivial functional dependency determines all attributes of the relation.

BCNF is sometimes called 3.5NF because it is stronger than 3NF. It is not an intermediate form between two numbered forms that contain it. The label only reflects its stricter condition.

### 10.2 Why BCNF is stricter than 3NF

Suppose a relation has a nontrivial dependency:

\[
X \rightarrow Y
\]

3NF permits this dependency when:

- `X` is a superkey; or
- every attribute in `Y` is prime.

BCNF permits it only when `X` is a superkey. Thus, a dependency whose right-hand side consists of prime attributes can satisfy 3NF while violating BCNF.

Because every BCNF dependency satisfies the first 3NF condition:

\[
\boxed{\text{BCNF} \Rightarrow \text{3NF}}
\]

The reverse implication does not hold.

### 10.3 Stepwise BCNF decomposition

1. Find a nontrivial functional dependency `X -> Y` in `R` for which `X` is not a superkey.
2. Select one right-hand-side attribute `A` in `Y - X`. If `Y` is already a singleton, set `A = Y`.
3. Split `R` into:

   \[
   R_1 = X \cup \{A\},\qquad R_2 = R - \{A\}
   \]

4. Verify lossless join:

   \[
   (R_1 \cap R_2) \rightarrow R_1
   \]

   Since `A` is not in `X`, `R1 ∩ R2 = X`. The dependency `X -> A` gives `X -> R1`, so the decomposition is lossless.
5. Compute the projected dependencies `F1` and `F2`.
6. Apply the same procedure to each component until all components satisfy BCNF.
7. Check dependency preservation:

   \[
   (F_1 \cup F_2 \cup \cdots \cup F_n)^+ = F^+
   \]

A BCNF decomposition is always lossless when produced by this algorithm. It may fail to preserve dependencies.

### 10.4 Worked example: student subject and professor

Consider the source relation:

```text
SUBJECT_ASSIGNMENT(stuid, subject, professor)
```

Assume:

```text
{stuid, subject} -> professor
professor          -> subject
```

The first dependency records the professor assigned to a student's subject. The second records the rule that one professor teaches only one subject, although a subject may have several professors.

#### Step 1: Find candidate keys

\[
\{stuid, subject\} \rightarrow professor
\]

so `{stuid, subject}` is a candidate key.

Also:

\[
\{stuid, professor\} \rightarrow subject
\]

because `professor -> subject`. Therefore `{stuid, professor}` is another candidate key.

Hence:

- prime attributes: `stuid`, `subject`, `professor`;
- the source choice of `{stuid, subject}` as the primary key does not change the normal-form test.

#### Step 2: Test 3NF

For `professor -> subject`:

- `professor` is not a superkey;
- `subject` is prime.

The dependency satisfies 3NF condition 2. The relation is therefore in 3NF.

#### Step 3: Test BCNF

For `professor -> subject`, the determinant `professor` is not a superkey. The relation violates BCNF.

#### Step 4: Decompose

Using the BCNF algorithm:

```text
PROFESSOR_SUBJECT(professor, subject)
ENROLLMENT(stuid, professor)
```

#### Step 5: Verify lossless join

\[
R_1 \cap R_2 = \{professor\}
\]

The projected dependency set of `R1` contains:

\[
professor \rightarrow subject
\]

Therefore:

\[
(R_1 \cap R_2) \rightarrow R_1
\]

The decomposition is lossless.

#### Step 6: Verify dependency preservation

The original dependency:

\[
\{stuid, subject\} \rightarrow professor
\]

uses attributes from both decomposed relations. The local projected dependencies do not derive it:

```text
F1 = { professor -> subject }
F2 = { stuid, professor -> stuid, professor }  {trivial key dependencies}
```

Thus:

\[
(F_1 \cup F_2)^+ \not\supseteq
\{stuid, subject\} \rightarrow professor
\]

The decomposition is lossless but not dependency preserving. If the system must enforce that functional dependency without joining the two tables, an additional constraint or a suitable identifier-based design is required.

The source slides use a `prof_id` variant:

```text
ENROLLMENT(stuid, prof_id)
PROFESSOR_ASSIGNMENT(prof_id, subject, professor)
```

This variant can be implemented when `prof_id` uniquely identifies the professor assignment. The join attribute is `prof_id`, and `prof_id -> subject, professor` proves losslessness for that schema pair. The designer must still test the original dependencies separately; the presence of `prof_id` alone does not prove dependency preservation.

### 10.5 Worked example with lossless join and dependency preservation

Consider:

```text
EMPLOYEE_DEPARTMENT(emp_id, emp_name, dept_id, dept_name)
```

with:

```text
emp_id -> emp_name, dept_id
dept_id -> dept_name
```

Decompose into:

```text
EMPLOYEE(emp_id, emp_name, dept_id)
DEPARTMENT(dept_id, dept_name)
```

#### Lossless join

\[
R_1 \cap R_2 = \{dept\_id\}
\]

Since:

\[
dept\_id \rightarrow dept\_name
\]

we have:

\[
(R_1 \cap R_2) \rightarrow R_2
\]

The decomposition is lossless.

#### Dependency preservation

The projected dependencies are:

```text
F1 = { emp_id -> emp_name, dept_id }
F2 = { dept_id -> dept_name }
```

Their union is exactly the original dependency set, so the decomposition preserves dependencies.

#### Normal form

- `emp_id` is the candidate key of `EMPLOYEE`.
- `dept_id` is the candidate key of `DEPARTMENT`.
- Every nontrivial determinant is a candidate key.

Both relations are in BCNF.

### 10.6 BCNF decomposition algorithm: verification summary

For a selected violating dependency `X -> Y`, choose `A` in `Y - X`:

| Check | Calculation | Result |
|---|---|---|
| Decomposition | `R1 = X ∪ {A}`, `R2 = R - {A}` | Covers all attributes |
| Intersection | `R1 ∩ R2 = X` | Gives the join determinant |
| Lossless join | `X -> R1` because `X -> A` | Lossless |
| Dependency preservation | Compare `(F1 ∪ F2)+` with `F+` | Independent check |
| Termination | Repeat on each component | Each step decreases the relation |

The dependency-preservation test cannot be skipped. The proof of losslessness uses only the selected dependency and says nothing about all dependencies in `F`.

### 10.7 3NF compared with BCNF

| Test point | 3NF | BCNF |
|---|---|---|
| Dependency class | Nontrivial functional dependencies | Nontrivial functional dependencies |
| Accepted determinant | Superkey | Superkey only |
| Alternative accepted case | Right-hand side contains only prime attributes | None |
| Handles prime-attribute transitive dependencies | No | Yes |
| Dependency-preserving decomposition available | Yes, through 3NF synthesis | Not guaranteed by the standard algorithm |
| Relationship | Weaker | Stronger |

### 10.8 Common traps

- **Requiring the right-hand side to be a superkey:** BCNF constrains the determinant `X`, not the dependent attributes `Y`.
- **Accepting a determinant that is only part of a superkey:** `X` must itself determine every attribute of `R`.
- **Ignoring alternative candidate keys:** A determinant can be a superkey through a candidate key other than the designated primary key.
- **Claiming BCNF guarantees dependency preservation:** The standard BCNF decomposition guarantees lossless join, not dependency preservation.
- **Adding an identifier without checking its meaning:** A surrogate key can support a schema design, but it does not remove the original dependency constraints.

### 10.9 BCNF in brief

| Aspect | BCNF rule |
|---|---|
| Prerequisite | The relation is in 3NF |
| Dependency tested | Every nontrivial functional dependency `X -> Y` |
| Required condition | `X` is a superkey of the relation |
| Main purpose | Remove every determinant anomaly, including those involving prime attributes |
| Decomposition property | Lossless join is guaranteed by the standard algorithm |
| Dependency preservation | Must be checked separately |

## 11. Multivalued Dependencies and Fourth Normal Form (4NF)

### 11.1 Formal definition of a multivalued dependency

Let `R` be a relation schema, and let `X` and `Y` be subsets of the attributes of `R`. The multivalued dependency

\[
X \twoheadrightarrow Y
\]

means that `X` independently determines a set of values for `Y`, apart from their pairing with the remaining attributes.

Let:

\[
Z = R - (X \cup Y)
\]

For any two tuples `t1` and `t2` in a legal instance `r` such that:

\[
t_1[X] = t_2[X]
\]

the relation must contain tuples `t3` and `t4` satisfying:

\[
\begin{aligned}
t_3[X] &= t_4[X] = t_1[X] = t_2[X] \\
t_3[Y] &= t_1[Y] \\
t_4[Y] &= t_2[Y] \\
t_3[Z] &= t_2[Z] \\
t_4[Z] &= t_1[Z]
\end{aligned}
\]

In other words, whenever two rows agree on `X`, the values of `Y` must be independent of the values in `Z`. The two rows can be recombined without losing a legal combination.

The symbol `↠` is read as "X multivalued-determines Y."

### 11.2 Trivial and nontrivial MVDs

An MVD `X ↠ Y` is **trivial** if either:

\[
Y \subseteq X
\]

or:

\[
X \cup Y = R
\]

An MVD is **nontrivial** when:

\[
Y \not\subseteq X
\quad\text{and}\quad
X \cup Y \neq R
\]

Only nontrivial MVDs constrain the design of a relation.

### 11.3 Important MVD rules

| Rule | Statement | Meaning |
|---|---|---|
| FD implication | If `X -> Y`, then `X ↠ Y` | Every functional dependency is also a multivalued dependency |
| Complementation | If `X ↠ Y`, then `X ↠ R - (X ∪ Y)` | The independent groups on both sides of the arrow are interchangeable |
| Replication | If `X ↠ Y`, copies of tuples with the same `X` can be made with the same `Y` | The `X` and `Y` values may repeat together |
| Triviality | `X ↠ Y` is trivial if `Y ⊆ X` or `X ∪ Y = R` | The dependency states nothing restrictive |

### 11.4 Formal definition of 4NF

A relation `R` is in **Fourth Normal Form (4NF)** if and only if, for every nontrivial multivalued dependency

\[
X \twoheadrightarrow Y
\]

that holds on `R`, `X` is a superkey of `R`.

In closure notation:

\[
R \text{ is in 4NF}
\iff
\forall X \twoheadrightarrow Y \in F^+,\;
Y \not\subseteq X \land X \cup Y \neq R
\Rightarrow X^+ = R
\]

The definition concerns **nontrivial** MVDs. Trivial MVDs are allowed in every relation.

Since every FD implies an MVD, a nontrivial FD with a non-superkey determinant also creates a 4NF violation. Therefore:

\[
\boxed{\text{4NF} \Rightarrow \text{BCNF} \Rightarrow \text{3NF}}
\]

### 11.5 Stepwise 4NF decomposition

1. Find a nontrivial MVD `X ↠ Y` in `R` for which `X` is not a superkey.
2. Use the non-overlapping right-hand part `A = Y - X`. The nontrivial condition ensures that `A` is nonempty.
3. Decompose `R` into:

   \[
   R_1 = X \cup A,\qquad R_2 = R - A
   \]

4. Verify lossless join with the MVD test:

   \[
   (R_1 \cap R_2) \twoheadrightarrow (R_1 - R_2)
   \]

   Since `R1 ∩ R2 = X` and `R1 - R2 = A`, the MVD `X ↠ A`, derived from `X ↠ Y`, proves losslessness.
5. Compute the projected functional and multivalued dependencies for each component.
6. Repeat until every component is in 4NF.
7. Check dependency preservation.

The standard 4NF decomposition guarantees a lossless join. It does not guarantee dependency preservation for multivalued dependencies. The lossless-join test and the dependency-preservation test remain separate.

### 11.6 Worked example: student courses and hobbies

Consider the source relation:

```text
STUDENT(stu_id, course, hobby)
```

Legal data:

| stu_id | course | hobby |
|---:|---|---|
| 21 | Computer | Dancing |
| 21 | Computer | Singing |
| 21 | Math | Dancing |
| 21 | Math | Singing |

The following MVDs hold:

\[
stu\_id \twoheadrightarrow course
\]

\[
stu\_id \twoheadrightarrow hobby
\]

The two attribute groups are independent. The cross-product of two courses and two hobbies creates four rows.

#### Step 1: Find candidate keys

There is no nontrivial functional dependency if the same course and hobby can belong to different students and a student can have several courses and hobbies. The candidate key is:

\[
\{stu\_id, course, hobby\}
\]

#### Step 2: Test 4NF

For `stu_id ↠ course`:

- the MVD is nontrivial;
- `stu_id` is not a superkey.

The relation is not in 4NF. It is in BCNF because it has no nontrivial FD with a non-superkey determinant.

#### Step 3: Decompose

Using `stu_id ↠ course`:

```text
STUDENT_COURSE(stu_id, course)
STUDENT_HOBBY(stu_id, hobby)
```

#### Step 4: Verify lossless join

\[
R_1 \cap R_2 = \{stu\_id\}
\]

and:

\[
(R_1 \cap R_2) \twoheadrightarrow (R_1 - R_2)
\]

becomes:

\[
stu\_id \twoheadrightarrow course
\]

The decomposition is lossless.

#### Step 5: Verify dependency preservation

For functional dependencies, preservation is vacuous because the original relation has no nontrivial FD. No non-key FD needs enforcement in either child relation.

For multivalued dependencies, the nontrivial constraint is not retained as a nontrivial local MVD. A database that must validate independently inserted rows should retain the original MVD as a schema-level constraint. Thus, the decomposition is lossless with respect to the MVD but should not be described as automatically dependency preserving for all MVD constraints.

#### Step 6: Verify 4NF

- `STUDENT_COURSE` has candidate key `{stu_id, course}` and no nontrivial MVD whose determinant is not a superkey.
- `STUDENT_HOBBY` has candidate key `{stu_id, hobby}` and no nontrivial MVD whose determinant is not a superkey.

Both relations are in 4NF.

### 11.7 Interpreting the source's bike and colour example

The source uses a relation with attributes such as:

```text
BIKE_MODEL(bike_model, manuf_year, color)
```

It describes `MANUF_YEAR` and `COLOR` as independent multivalued groups associated with `BIKE_MODEL`. A correct test must first determine the semantics:

- If `bike_model -> manuf_year`, the second group is functionally dependent, not an independent MVD group.
- If each model has one row, `bike_model` may be a superkey and the MVD creates no 4NF violation.
- If one model has several years and several colors, the independence of those groups must be stated as an MVD and tested against the complete candidate keys.

Multiple values in a column do not by themselves prove an MVD. The tuple-swap property is the formal test.

### 11.8 4NF compared with BCNF

| Test point | BCNF | 4NF |
|---|---|---|
| Dependency class | Nontrivial functional dependencies | Nontrivial multivalued dependencies |
| Required determinant | A superkey | A superkey |
| Handles independent groups | No | Yes |
| Relationship | A 4NF relation is in BCNF | A BCNF relation may still violate 4NF |
| Decomposition property | Standard algorithm is lossless | Standard algorithm is lossless |
| Dependency preservation | Not guaranteed | Not guaranteed for MVDs |

### 11.9 Common traps

- **Defining an MVD as "one value of A maps to many values of B":** Repetition alone does not establish independence or a tuple-swap property.
- **Ignoring trivial MVDs:** A 4NF relation may contain many trivial MVDs.
- **Testing `Y` instead of `X`:** The determinant `X` must be a superkey.
- **Claiming that multiple values imply a violation of 4NF:** A superkey may determine multiple values through an FD or a permitted MVD.
- **Assuming the 4NF algorithm preserves MVDs:** Losslessness does not imply dependency preservation.

### 11.10 4NF in brief

| Aspect | 4NF rule |
|---|---|
| Prerequisite | The relation is in BCNF and has no nontrivial MVD with a non-superkey determinant |
| Dependency tested | Every nontrivial multivalued dependency `X ↠ Y` |
| Required condition | `X` is a superkey of the relation |
| Main purpose | Remove redundancy caused by independent multivalued groups |
| Decomposition property | Lossless join is guaranteed by the standard algorithm |
| Dependency preservation | Must be checked separately |

## 12. Relational Decomposition: Lossless Join and Dependency Preservation

### 12.1 Decomposition: formal definition

A decomposition of a relation schema `R` is a collection of relation schemas:

\[
D = \{R_1, R_2, \ldots, R_n\}
\]

such that:

\[
\bigcup_{i=1}^{n} R_i = R
\]

For an instance `r` of `R`, the projected instances are:

\[
r_i = \pi_{R_i}(r)
\]

A good decomposition must satisfy two independent properties:

1. **Lossless join:** joining the decomposed relations recreates `r` without adding or losing facts.
2. **Dependency preservation:** constraints from `F` can be checked using the decomposed schemas without joining all of them.

Neither property implies the other.

### 12.2 Lossless join: formal definition

A decomposition `D = {R1, R2, ..., Rn}` is **lossless** or **non-additive** with respect to `F` if, for every legal instance `r` of `R` that satisfies `F`:

\[
r =
\pi_{R_1}(r)
\bowtie
\pi_{R_2}(r)
\bowtie \cdots \bowtie
\pi_{R_n}(r)
\]

The equality has two parts:

- no original tuple is missing after the join;
- no tuple that was absent from `r` appears after the join.

A tuple absent from `r` but present after the join is a **spurious tuple**.

### 12.3 Binary lossless-join test

For a binary decomposition:

\[
R \rightarrow \{R_1, R_2\}
\]

the standard lossless-join test is:

\[
(R_1 \cap R_2) \rightarrow R_1
\quad\text{or}\quad
(R_1 \cap R_2) \rightarrow R_2
\]

where the dependency must hold in `F+`.

Interpretation:

- If the common attributes determine all attributes of `R1`, each row of `R1` matches at most one row of `R2` for that key.
- If the common attributes determine all attributes of `R2`, each row of `R2` matches at most one row of `R1` for that key.

The test uses the intersection as the join determinant.

For MVDs, the corresponding binary test is:

\[
(R_1 \cap R_2) \twoheadrightarrow (R_1 - R_2)
\]

or, by symmetry:

\[
(R_1 \cap R_2) \twoheadrightarrow (R_2 - R_1)
\]

### 12.4 Multiway lossless join

For three or more component relations, use either:

- the **chase test**, which applies dependency rules to a tableau; or
- a sequence of binary decompositions in which every step is lossless.

If:

\[
R \rightarrow R_1, R_2
\]

is lossless and:

\[
R_1 \rightarrow R_{1a}, R_{1b}
\]

is lossless, then:

\[
R \rightarrow R_{1a}, R_{1b}, R_2
\]

is lossless. A similar argument applies to any finite sequence of lossless binary splits.

### 12.5 Dependency preservation: formal definition

Let the projection of `F` onto `Ri` be:

\[
F_i =
\{X \rightarrow Y \in F^+ \mid X \cup Y \subseteq R_i\}
\]

The decomposition is **dependency preserving** if:

\[
(F_1 \cup F_2 \cup \cdots \cup F_n)^+ = F^+
\]

This means that every dependency implied by the original relation can also be derived from the union of the local projected dependencies.

The source phrase "at least one decomposed table must satisfy every dependency" is too restrictive. Different dependencies may be checked in different component relations, and their combination may derive a dependency that spans several relations.

### 12.6 Stepwise decomposition procedure

1. Record the schema `R`, dependency set `F`, and business rules.
2. Find candidate keys, superkeys, prime attributes, and non-prime attributes.
3. Identify the anomaly and the dependency that causes it.
4. Choose a split that covers all attributes.
5. Apply the binary lossless-join test, or the MVD test when appropriate.
6. Compute the projected dependency set for each component.
7. Test dependency preservation:

   \[
   (\bigcup_i F_i)^+ \stackrel{?}{=} F^+
   \]

8. Recompute candidate keys in each component.
9. Repeat until each component meets the target normal form.
10. If dependency preservation fails, decide whether to add a constraint, retain a larger relation, or use a different decomposition.

### 12.7 Worked example 1: source decomposition with `A -> BC`

Consider:

```text
R(A, B, C, D)
F = { A -> BC }
```

Decompose into:

```text
R1(A, B, C)
R2(A, D)
```

#### Lossless join

\[
R_1 \cap R_2 = \{A\}
\]

Because:

\[
A \rightarrow B,\ C
\]

we have:

\[
(R_1 \cap R_2) \rightarrow R_1
\]

The decomposition is lossless.

#### Dependency preservation

The projected dependencies are:

```text
F1 = { A -> B, C }
F2 = { A -> A }  {trivial}
```

Thus:

\[
(F_1 \cup F_2)^+ = F^+
\]

The decomposition preserves dependencies.

### 12.8 Worked example 2: employee and department tables

The source relation is:

```text
EMPLOYEE_DEPARTMENT(
    emp_id, emp_name, emp_age, emp_city, dept_id, dept_name
)
```

with:

```text
emp_id -> emp_name, emp_age, emp_city, dept_id
dept_id -> dept_name
```

The source slides use:

```text
EMPLOYEE(emp_id, emp_name, emp_age, emp_city)
EMPLOYEE_DEPARTMENT_ASSIGNMENT(dept_id, emp_id, dept_name)
```

The second relation is an assignment relation because it contains `emp_id`. Calling it only `DEPARTMENT` can confuse the entity represented by the table.

#### Lossless join

\[
R_1 \cap R_2 = \{emp\_id\}
\]

Since:

\[
emp\_id \rightarrow emp\_name,\ emp\_age,\ emp\_city
\]

we have:

\[
(R_1 \cap R_2) \rightarrow R_1
\]

The decomposition is lossless. Joining on `emp_id` recreates every employee row with its department.

#### Dependency preservation

The local dependencies are:

```text
F1 = { emp_id -> emp_name, emp_age, emp_city }
F2 = { emp_id -> dept_id, dept_id -> dept_name }
```

Their union derives the original dependency set, so the decomposition preserves dependencies.

#### Normal form

- `emp_id` is a candidate key of `EMPLOYEE`.
- `emp_id` is a candidate key of `EMPLOYEE_DEPARTMENT_ASSIGNMENT` when an employee has one department.
- `dept_id` is not a superkey of the assignment relation when a department has several employees.

The dependency `dept_id -> dept_name` therefore has a non-superkey determinant and a non-prime right-hand side. The source split is lossless and dependency preserving, but the assignment relation is not in 3NF or BCNF.

Split the assignment relation once more:

```text
DEPARTMENT(dept_id, dept_name)
EMPLOYEE_DEPARTMENT_ASSIGNMENT(dept_id, emp_id)
```

The intersection is `dept_id`, and `dept_id -> dept_name` proves this additional split lossless. The projected dependencies still derive the original set. `dept_id` is the candidate key of `DEPARTMENT`, and `emp_id` is the candidate key of the assignment relation, where `dept_id` is a foreign key. All three relations are in BCNF.

### 12.9 Lossless join does not guarantee dependency preservation

Consider:

```text
R(A, B, C, D)
F = { {A,B} -> C, C -> D, D -> {A,B} }
```

Decompose into:

```text
R1(C, D)
R2(D, A, B)
```

#### Lossless join

\[
R_1 \cap R_2 = \{D\}
\]

Because `D -> A, B`:

\[
(R_1 \cap R_2) \rightarrow R_2
\]

The decomposition is lossless.

#### Dependency preservation

The local dependencies are:

```text
F1 = { C -> D }
F2 = { D -> A, B }
```

They do not derive `{A,B} -> C`. Therefore:

\[
(F_1 \cup F_2)^+ \not\supseteq
\{A,B\} \rightarrow C
\]

The decomposition is lossless but not dependency preserving.

### 12.10 Dependency preservation does not guarantee lossless join

Consider:

```text
R(A, B, C, D)
F = { A -> B, C -> D }
```

Decompose into:

```text
R1(A, B)
R2(C, D)
```

Both original FDs are local, so the decomposition preserves dependencies. However:

\[
R_1 \cap R_2 = \varnothing
\]

Neither empty set determines `R1` or `R2`, so the decomposition is not lossless.

For example, the legal original relation:

```text
(a1, b1, c1, d1)
(a2, b2, c2, d2)
```

projects to:

```text
R1 = {(a1, b1), (a2, b2)}
R2 = {(c1, d1), (c2, d2)}
```

Their join contains four tuples, including combinations absent from the original relation. The extra tuples are spurious.

### 12.11 Property comparison

| Property | Question answered | Test | Main failure prevented |
|---|---|---|---|
| Lossless join | Does the join recreate the original relation? | Join equality, binary determinant test, or chase | Lost facts and spurious tuples |
| Dependency preservation | Can the original constraints be checked locally? | `(F1 ∪ ... ∪ Fn)+ = F+` | Repeated cross-table constraint checks |
| Normalization | Does each relation meet a target normal form? | Prime attributes and dependency determinants | Redundancy and update anomalies |

### 12.12 Decomposition algorithms at a glance

| Starting point | Typical target | Lossless join | Dependency preservation |
|---|---|---|---|
| 1NF relation | 2NF | Can be guaranteed | Can be guaranteed in many cases, but check |
| 1NF relation | 3NF by synthesis | Guaranteed when the algorithm adds a key relation | Guaranteed by the standard synthesis algorithm |
| 1NF relation | BCNF by recursive splitting | Guaranteed | Not guaranteed |
| BCNF relation | 4NF by MVD splitting | Guaranteed | Not guaranteed for MVDs |
| 4NF relation | 5NF by JD splitting | Guaranteed by the JD | Not guaranteed for all dependencies |

### 12.13 Common traps

- **Using lossless join and dependency preservation as synonyms:** They test different properties.
- **Joining on a common attribute without proving uniqueness:** A shared attribute alone does not prevent many-to-many matches.
- **Requiring all dependencies to reside in one table:** The union of local dependencies may derive a crossing dependency.
- **Using only `F`, not `F+`, in a preservation test:** Dependencies implied by `F` also need preservation.
- **Assuming a natural join always restores the relation:** A lossy decomposition can produce extra tuples.
- **Confusing loss of tuples with loss of facts:** A join may retain all original rows and still add false combinations.

### 12.14 Lossless join and dependency preservation in brief

| Aspect | Lossless join | Dependency preservation |
|---|---|---|
| Goal | Reconstruct the original relation exactly | Enforce original constraints efficiently |
| Core equality | `r = ⋈ πRi(r)` | `(∪Fi)+ = F+` |
| Binary FD test | `(R1 ∩ R2) -> R1` or `-> R2` | Compare projected closures |
| Result of failure | Spurious or missing tuples | Cross-table checks or incomplete constraint enforcement |
| Implies the other property | No | No |

## 13. Join Dependencies and Fifth Normal Form (5NF/PJNF)

### 13.1 Formal definition of a join dependency

Let `R` be a relation schema and let:

\[
X_1, X_2, \ldots, X_n \subseteq R
\]

The join dependency:

\[
\bowtie[X_1, X_2, \ldots, X_n]
\]

holds on `R` if, for every legal instance `r` of `R`:

\[
r =
\pi_{X_1}(r)
\bowtie
\pi_{X_2}(r)
\bowtie \cdots \bowtie
\pi_{X_n}(r)
\]

Thus, the projections on the listed attribute sets reconstruct the original relation exactly.

A join dependency is **trivial** if one listed set contains all attributes of `R`, because the dependency then imposes no restriction.

A join dependency is **nontrivial** when no listed set is all of `R` and no proper subset of the listed projections can reconstruct `R`. A redundant projection does not add a constraint.

### 13.2 Candidate-key implication

A join dependency `⋈[X1, ..., Xn]` is **implied by the candidate keys** when every `Xi` is a superkey of `R`.

In that case, each projection uses a key and the join cannot create an additional row beyond the rows represented by those keys. Such a join dependency is required by the key structure and does not require further decomposition.

### 13.3 Formal definition of 5NF

A relation `R` is in **Fifth Normal Form (5NF)** if and only if every nontrivial join dependency that holds on `R` is implied by its candidate keys.

Equivalently:

\[
R \text{ is in 5NF}
\iff
\text{every nontrivial JD satisfied by } R
\text{ has a superkey as each projection}
\]

5NF is also called **Project-Join Normal Form (PJNF)** because a 5NF relation can be reconstructed by the project-join operation without a redundant, non-key-implied join dependency.

A binary JD corresponds to an MVD and is already tested by 4NF. The additional 5NF test targets nonbinary JDs that remain after the BCNF and 4NF tests.

Because 4NF eliminates violations based on MVDs and every MVD is a special case of a join dependency:

\[
\boxed{\text{5NF} \Rightarrow \text{4NF} \Rightarrow \text{BCNF} \Rightarrow \text{3NF}}
\]

### 13.4 Correcting the source definition

The source statement "5NF means no join dependency" is too broad. A 5NF relation may contain:

- trivial join dependencies;
- join dependencies implied by candidate keys.

The source statement "all tables should be broken into as many tables as possible" is also incorrect. Normalization removes dependencies that cause redundancy; it does not require an arbitrary maximum number of tables.

The source requirement that the join be lossless describes the result of a valid 5NF decomposition. It does not replace the formal 5NF condition.

### 13.5 Stepwise 5NF decomposition

1. Identify a join dependency:

   \[
   \bowtie[X_1, X_2, \ldots, X_n]
   \]

2. Check that it is nontrivial.
3. Check whether it is implied by candidate keys. If every `Xi` is a superkey, it does not cause a 5NF violation.
4. If at least one `Xi` is not a superkey, the relation is not in 5NF.
5. Decompose `R` into:

   \[
   R_i(X_i), \qquad i = 1, \ldots, n
   \]

6. Verify lossless join:

   \[
   r = \bowtie_{i=1}^{n} \pi_{X_i}(r)
   \]

   This equality is guaranteed by the join dependency.
7. Compute projected functional and join dependencies for each `Ri`.
8. Recursively decompose any component that still violates 5NF.
9. Check dependency preservation separately.

The standard 5NF decomposition is lossless by the definition of the selected JD. It does not guarantee that every original FD or JD can be checked solely within the component schemas.

### 13.6 Worked example: lecturer, semester, and subject

Use the source relation:

```text
TEACHING(lecturer, semester, subject)
```

Example rows:

| lecturer | semester | subject |
|---|---:|---|
| John | 1 | Computer |
| John | 1 | Math |
| John | 2 | Computer |

The relation records a three-way fact: a lecturer teaches a subject in a semester. It also contains these pairwise facts:

- lecturer and semester;
- semester and subject;
- lecturer and subject.

The business rule states that these three pairwise relations jointly determine the valid teaching assignments. Therefore:

\[
\bowtie
[LS,\ SC,\ LC]
\]

is a join dependency, where:

- `LS = {lecturer, semester}`;
- `SC = {semester, subject}`;
- `LC = {lecturer, subject}`.

#### Candidate key and 5NF test

Assume that:

- a lecturer may teach several subjects;
- a subject may be taught in several semesters;
- a lecturer may teach in several semesters; and
- several lecturers may teach the same subject.

Assume also that no nontrivial MVD holds, so the relation satisfies 4NF before the 5NF test. Then `{lecturer, semester, subject}` is the candidate key. None of `LS`, `SC`, or `LC` is a superkey.

The JD is nontrivial because no listed projection contains all attributes. It is not implied by the candidate key because at least one projection is not a superkey. The relation is therefore not in 5NF.

#### Decomposition

Create:

```text
LECTURER_SEMESTER(lecturer, semester)
SEMESTER_SUBJECT(semester, subject)
LECTURER_SUBJECT(lecturer, subject)
```

#### Lossless join

By the selected JD:

\[
r =
\pi_{LS}(r)
\bowtie
\pi_{SC}(r)
\bowtie
\pi_{LC}(r)
\]

The decomposition is lossless.

#### Dependency preservation

Under the stated assumptions, there are no nontrivial FDs, so FD dependency preservation is vacuous. The three-way JD is the rule used to reconstruct `TEACHING`; it is not a local FD that can be checked in one child relation.

If the three child tables can receive independent updates, retain the JD as a catalog constraint or enforce it in the application. A 5NF decomposition should not be called dependency preserving merely because its join is lossless.

#### Result

Each binary component has only trivial or key-implied join dependencies. The three component relations are in 5NF.

### 13.7 5NF compared with 4NF

| Test point | 4NF | 5NF/PJNF |
|---|---|---|
| Dependency class | Nontrivial MVDs | Nontrivial join dependencies |
| Required determinant or projection | Every MVD determinant is a superkey | Every projection in a key-implied JD is a superkey |
| Handles two independent groups | Yes | Yes |
| Handles cyclic or three-way reconstruction rules | No | Yes |
| Relationship | A 5NF relation is in 4NF | A 4NF relation may violate 5NF |
| Permitted dependencies | Trivial MVDs and key-implied MVDs | Trivial JDs and candidate-key-implied JDs |

### 13.8 5NF and 6NF

| Form | Requirement |
|---|---|
| 5NF/PJNF | Every nontrivial JD is implied by candidate keys |
| 6NF | No nontrivial JD holds at all |

5NF permits key-implied JDs. 6NF removes even those by decomposing into elementary facts.

### 13.9 Common traps

- **Equating 5NF with the absence of every JD:** Trivial and key-implied JDs may remain.
- **Ignoring candidate keys:** 5NF is defined relative to all candidate keys of the relation.
- **Treating a three-way table as automatically 5NF:** A cyclic three-way fact can violate 5NF even without a nontrivial FD or MVD.
- **Confusing losslessness with dependency preservation:** A JD-based split reconstructs the relation, but local constraint checking still needs analysis.
- **Assuming 5NF is common in practice:** Most transactional schemas stop at 3NF or BCNF because 5NF violations require unusual three-way business rules.
- **Using a binary split by default:** A JD may require three or more projected relations.

### 13.10 5NF in brief

| Aspect | 5NF/PJNF rule |
|---|---|
| Prerequisite | The relation is in 4NF |
| Dependency tested | Every nontrivial join dependency |
| Required condition | The JD is implied by candidate keys; equivalently, every listed projection is a superkey |
| Main purpose | Remove redundancy caused by non-key-implied project-join rules |
| Decomposition property | Lossless join follows from the selected JD |
| Dependency preservation | Must be checked separately |

## 14. Exam Questions with Model Answers

### 14.1 Examination pattern

The set contains 15 questions:

- four questions worth 2 marks;
- six questions worth 5 marks;
- five questions worth 10 marks.

Each model answer includes the definition, reasoning, decomposition, or verification requested in the question.

### 14.2 Two-mark questions

#### Question 1 (2 marks): State the standard condition for 3NF

**Model answer:**

For every nontrivial functional dependency `X -> Y` that holds on relation `R`, at least one of the following must hold:

1. `X` is a superkey of `R`; or
2. every attribute in `Y` is prime.

A prime attribute belongs to at least one candidate key. The relation must also be in 2NF.

#### Question 2 (2 marks): Differentiate 3NF from BCNF

**Model answer:**

3NF allows a nontrivial FD `X -> Y` when `X` is a superkey **or** every attribute in `Y` is prime. BCNF allows it only when `X` is a superkey.

Therefore every BCNF relation is in 3NF, but a 3NF relation may violate BCNF when a non-superkey determinant determines only prime attributes.

#### Question 3 (2 marks): State the condition for 4NF

**Model answer:**

A relation is in 4NF if every nontrivial multivalued dependency `X ↠ Y` has `X` as a superkey. Trivial MVDs are allowed. Since every FD implies an MVD, every 4NF relation is in BCNF.

#### Question 4 (2 marks): Distinguish lossless join from dependency preservation

**Model answer:**

- **Lossless join** means `r = ⋈ πRi(r)` for every legal instance `r`. The join produces neither lost facts nor spurious tuples.
- **Dependency preservation** means `(F1 ∪ ... ∪ Fn)+ = F+`. The original constraints can be derived from the projected dependencies of the component relations.

The two properties are independent: either may hold without the other.

### 14.3 Five-mark questions: Questions 5 to 8

#### Question 5 (5 marks): Normalize the teacher relation to 2NF and verify the decomposition

Consider:

```text
TEACHER(teacher_id, subject, teacher_age)
F = {
    teacher_id -> teacher_age,
    {teacher_id, subject} -> teacher_age
}
```

**Model answer:**

**Candidate key:** `{teacher_id, subject}`. It determines `teacher_age`, and no proper subset determines `teacher_age`.

**Violation:** `teacher_age` is a non-prime attribute and `teacher_id -> teacher_age` is a partial dependency on a proper subset of the candidate key. The relation is not in 2NF.

**Decomposition:**

```text
TEACHER_DETAIL(teacher_id, teacher_age)
TEACHER_SUBJECT(teacher_id, subject)
```

**Lossless join:**

\[
R_1 \cap R_2 = \{teacher\_id\}
\]

Since `teacher_id -> teacher_age`:

\[
(R_1 \cap R_2) \rightarrow R_1
\]

The decomposition is lossless.

**Dependency preservation:**

```text
F1 = { teacher_id -> teacher_age }
F2 = { {teacher_id, subject} -> teacher_id, subject }  {trivial}
```

From `teacher_id -> teacher_age`, the union derives `{teacher_id, subject} -> teacher_age`. Thus `(F1 ∪ F2)+ = F+`.

Both relations have single-attribute candidate keys and satisfy 2NF.

#### Question 6 (5 marks): Decompose the employee relation into 3NF

Consider:

```text
EMPLOYEE_DETAIL(emp_id, emp_name, emp_zip, emp_state, emp_city)
F = {
    emp_id -> emp_name, emp_zip,
    emp_zip -> emp_state, emp_city
}
```

**Model answer:**

`emp_id` is the candidate key. `emp_zip` is non-prime, and `emp_zip -> emp_state, emp_city` has a non-superkey determinant with non-prime right-hand attributes. The relation violates 3NF.

Decompose into:

```text
EMPLOYEE_ZIP(emp_zip, emp_state, emp_city)
EMPLOYEE(emp_id, emp_name, emp_zip)
```

**Lossless join:** The intersection is `emp_zip`. Since `emp_zip -> emp_state, emp_city`, we have `(R1 ∩ R2) -> R1`.

**Dependency preservation:**

```text
F1 = { emp_zip -> emp_state, emp_city }
F2 = { emp_id -> emp_name, emp_zip }
```

Their union derives every original FD, including the transitive dependencies from `emp_id` to `emp_state` and `emp_city`.

**Normal form:** `emp_zip` is the candidate key of `EMPLOYEE_ZIP`, and `emp_id` is the candidate key of `EMPLOYEE`. Every nontrivial determinant is a superkey, so both relations are in 3NF and BCNF.

#### Question 7 (5 marks): Test and decompose the subject relation for BCNF

Consider:

```text
SUBJECT_ASSIGNMENT(stuid, subject, professor)
F = {
    {stuid, subject} -> professor,
    professor -> subject
}
```

**Model answer:**

`{stuid, subject}` is a candidate key. Also, `{stuid, professor}` is a candidate key because `professor -> subject`. Therefore `subject` is prime.

The relation satisfies 3NF:

- `{stuid, subject} -> professor` has a candidate-key determinant;
- `professor -> subject` has a prime right-hand side.

It violates BCNF because `professor` is not a superkey.

Decompose into:

```text
PROFESSOR_SUBJECT(professor, subject)
ENROLLMENT(stuid, professor)
```

**Lossless join:** The intersection is `professor`, and `professor -> subject` gives `(R1 ∩ R2) -> R1`.

**Dependency preservation:** The original FD `{stuid, subject} -> professor` spans both relations and is not derived from the local projected FDs. The split is lossless but not dependency preserving.

#### Question 8 (5 marks): Apply MVDs and 4NF to the student relation

Consider:

```text
STUDENT(stu_id, course, hobby)
```

Assume the independent groups `course` and `hobby` produce:

\[
stu\_id \twoheadrightarrow course,
\qquad
stu\_id \twoheadrightarrow hobby
\]

**Model answer:**

The relation has candidate key `{stu_id, course, hobby}` and no nontrivial FD. `stu_id` is not a superkey, and the MVDs are nontrivial because neither right-hand attribute is in `stu_id` and `stu_id ∪ course` or `stu_id ∪ hobby` is less than the full schema.

The relation is in BCNF but not in 4NF.

Decompose into:

```text
STUDENT_COURSE(stu_id, course)
STUDENT_HOBBY(stu_id, hobby)
```

**Lossless join:** `R1 ∩ R2 = stu_id`, and `stu_id ↠ course` gives `(R1 ∩ R2) ↠ (R1 - R2)`.

**Dependency preservation:** FD preservation is vacuous because there is no nontrivial FD. The nontrivial MVD is not a local nontrivial MVD after the split, so the schema should retain the MVD constraint if independent updates must be validated.

Both child relations have two-attribute candidate keys and are in 4NF.

### 14.4 Five-mark questions: Questions 9 and 10

#### Question 9 (5 marks): Explain the two binary decomposition tests

For a decomposition `R -> R1, R2`, state the lossless-join test, the dependency-preservation test, and apply both to `R(A,B,C,D)` with `F = {A -> BC}` and decomposition `R1(A,B,C)`, `R2(A,D)`.

**Model answer:**

**Lossless join:**

\[
(R_1 \cap R_2) \rightarrow R_1
\quad\text{or}\quad
(R_1 \cap R_2) \rightarrow R_2
\]

For the given decomposition, `R1 ∩ R2 = {A}` and `A -> B, C`. Hence `(R1 ∩ R2) -> R1`, so the split is lossless.

**Dependency preservation:**

Let `Fi` be the projection of `F+` onto `Ri`. The split preserves dependencies if:

\[
(F_1 \cup F_2)^+ = F^+
\]

Here:

```text
F1 = { A -> B, C }
F2 = { A -> A }  {trivial}
```

The union therefore derives the original FD and the split preserves dependencies.

The first test protects the data during reconstruction. The second protects constraint enforcement after decomposition.

#### Question 10 (5 marks): Compare 2NF, 3NF, BCNF, 4NF, and 5NF

**Model answer:**

| Form | Formal condition | Main issue addressed |
|---|---|---|
| 2NF | The relation is in 1NF, and every non-prime attribute is fully dependent on every candidate key | Partial dependencies on candidate keys |
| 3NF | For every nontrivial FD `X -> Y`, `X` is a superkey or every attribute in `Y` is prime | Transitive dependencies of non-prime attributes |
| BCNF | For every nontrivial FD `X -> Y`, `X` is a superkey | All FD determinant anomalies, including prime right-hand sides |
| 4NF | For every nontrivial MVD `X ↠ Y`, `X` is a superkey | Independent multivalued groups |
| 5NF/PJNF | Every nontrivial JD is implied by candidate keys; equivalently, every projection in it is a superkey | Non-key-implied project-join rules |

The implication chain is:

\[
5NF \Rightarrow 4NF \Rightarrow BCNF \Rightarrow 3NF \Rightarrow 2NF \Rightarrow 1NF
\]

2NF is stated in terms of non-prime attributes and all candidate keys. 3NF and BCNF use FDs, 4NF uses MVDs, and 5NF uses JDs.

### 14.5 Ten-mark questions: Questions 11 to 15

#### Question 11 (10 marks): Normalize a four-entity relation and verify every step

Consider:

```text
R(emp_id, dept_id, dept_name, project_id, project_name, hours)
F = {
    emp_id -> dept_id,
    dept_id -> dept_name,
    project_id -> project_name,
    {emp_id, project_id} -> hours
}
```

**Model answer:**

#### Step 1: Candidate keys

`{emp_id, project_id}` determines `dept_id` through `emp_id`, `dept_name` through `dept_id`, `project_name` through `project_id`, and `hours` directly. No proper subset determines `hours`, so `{emp_id, project_id}` is the candidate key.

#### Step 2: Identify violating dependencies

- `emp_id -> dept_id`: `emp_id` is not a superkey of `R`.
- `dept_id -> dept_name`: `dept_id` is not a superkey.
- `project_id -> project_name`: `project_id` is not a superkey.

These violations prevent BCNF. The transitive path `emp_id -> dept_id -> dept_name` also violates 3NF.

#### Step 3: Lossless split for department

Create:

```text
DEPARTMENT(dept_id, dept_name)
R1(emp_id, dept_id, project_id, project_name, hours)
```

The intersection is `dept_id`, and `dept_id -> dept_name` gives `(intersection) -> DEPARTMENT`. The split is lossless.

#### Step 4: Lossless split for project

Create:

```text
PROJECT(project_id, project_name)
R2(emp_id, dept_id, project_id, hours)
```

The intersection is `project_id`, and `project_id -> project_name` proves this split lossless.

#### Step 5: Lossless split for employee

From `R2`, create:

```text
EMPLOYEE(emp_id, dept_id)
ASSIGNMENT(emp_id, project_id, hours)
```

The intersection is `emp_id`, and `emp_id -> dept_id` proves this split lossless.

#### Step 6: Dependency preservation

The projected dependencies are:

```text
F_DEPARTMENT = { dept_id -> dept_name }
F_PROJECT   = { project_id -> project_name }
F_EMPLOYEE  = { emp_id -> dept_id }
F_ASSIGN    = { {emp_id, project_id} -> hours }
```

Their union is the original `F`, so the decomposition preserves dependencies.

#### Step 7: Normal form

- `dept_id` is the key of `DEPARTMENT`.
- `project_id` is the key of `PROJECT`.
- `emp_id` is the key of `EMPLOYEE`.
- `{emp_id, project_id}` is the key of `ASSIGNMENT`.

Every nontrivial determinant is a superkey. All four relations are in BCNF, and therefore also in 3NF, 2NF, and 1NF.

#### Question 12 (10 marks): Define an MVD formally, define 4NF, and prove the relation between 4NF and BCNF

**Model answer:**

**MVD definition:** Let `Z = R - (X ∪ Y)`. The MVD `X ↠ Y` holds if, for any `t1` and `t2` with `t1[X] = t2[X]`, the relation contains `t3` and `t4` such that:

\[
\begin{aligned}
t_3[X] &= t_4[X] = t_1[X] = t_2[X] \\
t_3[Y] &= t_1[Y],\quad t_4[Y] = t_2[Y] \\
t_3[Z] &= t_2[Z],\quad t_4[Z] = t_1[Z]
\end{aligned}
\]

This tuple-swap property captures independence between `Y` and `Z` for a fixed `X`.

An MVD is nontrivial if `Y` is not a subset of `X` and `X ∪ Y` does not equal `R`.

**4NF definition:** `R` is in 4NF if every nontrivial MVD `X ↠ Y` has a superkey determinant `X`.

**Proof that 4NF implies BCNF:** Assume a nontrivial FD `X -> Y` exists and `X` is not a superkey. Every FD implies the MVD `X ↠ Y`.

- If `Y ⊆ X`, the FD would be trivial, contrary to the assumption.
- If `X ∪ Y = R`, then `X -> Y` would make `X` a superkey, also contrary to the assumption.

Thus `X ↠ Y` is a nontrivial MVD with a non-superkey determinant. This violates 4NF. Therefore no such FD can exist in a 4NF relation, and every 4NF relation is in BCNF.

**Example:** `STUDENT(stu_id, course, hobby)` has `stu_id ↠ course` and `stu_id ↠ hobby`. Decomposing it into `STUDENT_COURSE` and `STUDENT_HOBBY` is lossless because the common determinant `stu_id` multivalued-determines `course`.

#### Question 13 (10 marks): Demonstrate that lossless join does not imply dependency preservation

Consider:

```text
R(A, B, C, D)
F = { {A,B} -> C, C -> D, D -> {A,B} }
R1(C, D)
R2(D, A, B)
```

**Model answer:**

**Candidate keys and normal form:**

- `{A,B}` is a candidate key because it determines `C`, then `D`, and then all attributes.
- `C` is a candidate key because `C -> D` and `D -> A, B`.
- `D` is a candidate key because `D -> A, B` and `{A,B} -> C`.

Both `R1` and `R2` are in BCNF.

**Lossless join:**

\[
R_1 \cap R_2 = \{D\}
\]

Since `D -> A, B`:

\[
(R_1 \cap R_2) \rightarrow R_2
\]

The decomposition is lossless.

**Dependency preservation:**

The local projected dependencies are:

```text
F1 = { C -> D }
F2 = { D -> A, B }
```

They cannot derive `{A,B} -> C`. Therefore:

\[
(F_1 \cup F_2)^+ \not\supseteq
\{A,B\} \rightarrow C
\]

The decomposition is not dependency preserving.

**Conclusion:** Losslessness proves that a join reconstructs the relation. It does not prove that each original constraint has a local check. The designer may add a constraint, retain a larger relation, or use a different decomposition if the crossing FD must be checked efficiently.

#### Question 14 (10 marks): Define 5NF and decompose a three-way teaching relation

Consider:

```text
TEACHING(lecturer, semester, subject)
```

Assume the pairwise facts `LS`, `SC`, and `LC` satisfy the join dependency:

\[
\bowtie[LS, SC, LC]
\]

The full tuple is the candidate key, the JD is not implied by that key, and no nontrivial MVD holds.

**Model answer:**

**Definition:** `R` is in 5NF/PJNF if every nontrivial join dependency holding on `R` is implied by its candidate keys. A JD is implied by the candidate keys when every listed projection is a superkey.

**Prerequisite and violation:** The absence of a nontrivial MVD means that `TEACHING` satisfies 4NF. Its JD is nontrivial because no projection contains all attributes. It is not key-implied because `LS`, `SC`, and `LC` are not superkeys. Hence `TEACHING` is not in 5NF.

**Decomposition:**

```text
LECTURER_SEMESTER(lecturer, semester)
SEMESTER_SUBJECT(semester, subject)
LECTURER_SUBJECT(lecturer, subject)
```

**Lossless join:**

\[
r =
\pi_{LS}(r)
\bowtie
\pi_{SC}(r)
\bowtie
\pi_{LC}(r)
\]

The equality follows directly from the selected JD, so the decomposition is lossless.

**Dependency preservation:** If no nontrivial FD holds, FD preservation is vacuous. The JD remains a three-way semantic constraint and should remain in the dependency catalog if updates occur in separate component tables. Lossless join alone does not prove complete dependency preservation.

**Result:** Each binary component has only trivial or key-implied JDs and is in 5NF. The source statement "5NF means no join dependency" is incorrect because trivial and key-implied JDs may remain.

#### Question 15 (10 marks): Analyze a relation with two candidate keys

Consider:

```text
R(A, B, C, D, E)
F = {
    {A,B} -> {C,D,E},
    {C,D} -> {A,B,E}
}
```

**Model answer:**

**Candidate keys:** `{A,B}` and `{C,D}` are candidate keys. Under the stated dependencies, no proper subset of either pair determines `E`.

**Prime attributes:** `A`, `B`, `C`, and `D` are prime because each occurs in a candidate key. `E` is non-prime.

**2NF:** For each candidate key, no proper subset determines the non-prime attribute `E`. Thus `E` is fully dependent on every candidate key. Partial dependencies involving prime attributes do not violate 2NF. The relation is in 2NF.

**3NF:** The displayed nontrivial FDs have candidate-key determinants. Every other nontrivial dependency follows from them or is trivial. Thus the relation is in 3NF.

**BCNF:** Every determinant in every nontrivial FD is either `{A,B}` or `{C,D}`, both superkeys. The relation is in BCNF.

**4NF:** Assume there are no nontrivial MVDs except those implied by the FDs. Since every FD determinant in this relation is a superkey, the relation is in 4NF.

**5NF:** Assume that, after binary JDs are handled by the 4NF test, no nontrivial three-way or higher-order JD remains. The relation is then in 5NF.

**Conclusion:** The relation needs no normalization under these assumptions. A further decomposition would be required only if an additional nontrivial MVD or a non-key-implied three-way or higher-order JD represents a real business rule.

## 15. MCQs, Practice Exercises, Cheat Sheet, and Rapid-Revision Checklist

### 15.1 Multiple-choice questions

#### MCQ 1

Which condition defines 3NF for every nontrivial FD `X -> Y`?

A. `X` is a candidate key.
B. `X` is a superkey or every attribute in `Y` is prime.
C. Every attribute in `Y` is non-prime.
D. `X` contains a candidate key.

**Answer: B.** 3NF accepts a superkey determinant or a right-hand side made entirely of prime attributes.

#### MCQ 2

A relation has candidate keys `{A,B}` and `{C,D}`. Its non-prime attribute `E` is determined by `AB` and `CD`, but neither `A`, `B`, `C`, nor `D` alone determines `E`. What is the 2NF result?

A. Not in 2NF because there are two candidate keys.
B. Not in 2NF because `E` is non-prime.
C. In 2NF because `E` is fully dependent on every candidate key.
D. In BCNF without further testing.

**Answer: C.** 2NF tests full dependence of each non-prime attribute on every candidate key.

#### MCQ 3

Which statement is the formal BCNF condition?

A. Every right-hand-side attribute is a superkey.
B. Every determinant is a candidate key only.
C. Every determinant of a nontrivial FD is a superkey.
D. The relation has only one candidate key.

**Answer: C.** BCNF constrains the determinant `X`; it need not be minimal if a larger superkey also determines all attributes.

#### MCQ 4

Which dependency can occur in a relation that is in 3NF but not in BCNF?

A. `X -> Y`, where `X` is a superkey and `Y` is non-prime.
B. `X -> Y`, where `X` is not a superkey and every attribute in `Y` is prime.
C. `X -> Y`, where `X` is a proper subset of a candidate key and `Y` is non-prime.
D. `X -> Y`, where `X` is not a superkey and `Y` contains a non-prime attribute.

**Answer: B.** The prime right-hand side satisfies 3NF, but the non-superkey determinant violates BCNF.

#### MCQ 5

What does `X ↠ Y` mean?

A. `X` determines one value of `Y`.
B. `Y` determines `X`.
C. For a fixed `X`, `Y` is independent of the remaining attributes under the tuple-swap rule.
D. `X` and `Y` are always the same attribute set.

**Answer: C.** An MVD describes independent groups of values associated with a common determinant.

#### MCQ 6

When does a relation satisfy 4NF?

A. It has no MVDs at all.
B. Every nontrivial MVD has a superkey determinant.
C. Every MVD determinant is a candidate key.
D. It has no transitive dependencies.

**Answer: B.** 4NF permits trivial MVDs and MVDs whose determinants are superkeys.

#### MCQ 7

Which condition guarantees that the binary decomposition `R -> R1, R2` is lossless with respect to `F`?

A. `R1` and `R2` share at least one attribute.
B. `R1 ∪ R2 = R`.
C. `(R1 ∩ R2) -> R1` or `(R1 ∩ R2) -> R2`.
D. Every FD in `F` appears in one projection.

**Answer: C.** The intersection must determine one complete component to prevent unmatched or many-to-many joins.

#### MCQ 8

Which equality defines dependency preservation?

A. `F1 = F2`.
B. `(F1 ∪ F2 ∪ ... ∪ Fn)+ = F+`.
C. `R = R1 ∪ R2`.
D. `r1 ∩ r2 = r`.

**Answer: B.** The union of projected dependencies must derive every original dependency.

#### MCQ 9

Which MVD is trivial?

A. `X ↠ Y` where `Y ⊆ X`.
B. `X ↠ Y` where `X` is not a superkey.
C. `X ↠ Y` where `X ∪ Y = R`.
D. Both A and C are trivial.

**Answer: D.** Triviality holds when `Y ⊆ X` or `X ∪ Y = R`.

#### MCQ 10

Which join dependency is trivial?

A. One listed projection contains every attribute of `R`.
B. Every listed projection contains a candidate key.
C. The JD has three projections.
D. The join of two projections is non-additive.

**Answer: A.** A full-attribute projection reconstructs `R` without imposing any additional rule.

#### MCQ 11

Which statement correctly defines 5NF?

A. The relation has no join dependency.
B. Every nontrivial JD is implied by candidate keys.
C. Every determinant is a candidate key.
D. Every relation is decomposed into the maximum number of tables.

**Answer: B.** Trivial and candidate-key-implied JDs may remain in 5NF.

#### MCQ 12

Which implication chain is correct?

A. `3NF => BCNF => 4NF => 5NF`
B. `5NF => 4NF => BCNF => 3NF`
C. `BCNF => 5NF => 4NF => 2NF`
D. `4NF => 5NF => BCNF => 1NF`

**Answer: B.** Each stronger form satisfies the weaker forms that precede it.

#### MCQ 13

The source says, "5NF means no join dependency." What is the correction?

A. A 5NF relation may contain only trivial JDs.
B. A 5NF relation may contain trivial and candidate-key-implied JDs, but no other nontrivial JD.
C. 5NF is identical to BCNF.
D. 5NF requires every projection in every JD to be non-prime.

**Answer: B.** The 5NF test permits dependencies that follow from candidate-key structure.

#### MCQ 14

Can a decomposition preserve dependencies but still be lossy?

A. No. Dependency preservation always implies a lossless join.
B. Yes. For example, `R1(A,B)` and `R2(C,D)` preserve `A -> B` and `C -> D` but have an empty intersection.
C. Only if the decomposition has three relations.
D. Only when the original relation is in 1NF.

**Answer: B.** The two properties test different conditions and are independent.

### 15.2 Practice exercises

#### Exercise 1: Teacher relation

For:

```text
R(teacher_id, subject, teacher_age)
F = {
    teacher_id -> teacher_age,
    {teacher_id, subject} -> teacher_age
}
```

1. Find the candidate key and prime attributes.
2. Decide whether `R` is in 2NF.
3. Decompose `R` into 2NF relations.
4. Verify lossless join and dependency preservation.

**Worked solution:**

1. `{teacher_id, subject}` is the candidate key. `teacher_id` and `subject` are prime; `teacher_age` is non-prime.
2. `teacher_id -> teacher_age` is a partial dependency of a non-prime attribute on a proper subset of the candidate key. `R` is not in 2NF.
3. Use:

   ```text
   TEACHER_DETAIL(teacher_id, teacher_age)
   TEACHER_SUBJECT(teacher_id, subject)
   ```

4. The intersection is `teacher_id`. Since `teacher_id -> teacher_age`, we have `(R1 ∩ R2) -> R1`, so the split is lossless. The local FD `teacher_id -> teacher_age` plus the trivial key dependencies in `R2` derives `{teacher_id, subject} -> teacher_age`, so dependencies are preserved. Both relations are in 2NF and BCNF.

#### Exercise 2: Employee postal details

For:

```text
R(emp_id, emp_name, emp_zip, emp_state, emp_city)
F = {
    emp_id -> emp_name, emp_zip,
    emp_zip -> emp_state, emp_city
}
```

perform a 3NF decomposition and verify both properties.

**Worked solution:**

The candidate key is `{emp_id}`. The dependency `emp_zip -> emp_state, emp_city` has a non-superkey determinant and non-prime right-hand attributes, so the relation violates 3NF.

Use:

```text
EMPLOYEE_ZIP(emp_zip, emp_state, emp_city)
EMPLOYEE(emp_id, emp_name, emp_zip)
```

The intersection is `emp_zip`, and `emp_zip -> emp_state, emp_city` proves losslessness. The projected FDs are:

```text
F1 = { emp_zip -> emp_state, emp_city }
F2 = { emp_id -> emp_name, emp_zip }
```

Their union derives the original set, so dependencies are preserved. The candidate keys of the two relations are `emp_zip` and `emp_id`, respectively, so both are in BCNF.

#### Exercise 3: Professor assignment

For:

```text
R(stuid, subject, professor)
F = {
    {stuid, subject} -> professor,
    professor -> subject
}
```

determine the candidate keys, test 3NF and BCNF, and give a lossless decomposition.

**Worked solution:**

The candidate keys are `{stuid, subject}` and `{stuid, professor}`. Thus `stuid`, `subject`, and `professor` are prime.

The relation is in 3NF because `professor -> subject` has a prime right-hand side. It is not in BCNF because `professor` is not a superkey.

Use:

```text
PROFESSOR_SUBJECT(professor, subject)
ENROLLMENT(stuid, professor)
```

The intersection is `professor`, and `professor -> subject` proves losslessness. The FD `{stuid, subject} -> professor` spans both relations and is not locally derivable, so this split is not dependency preserving. If a stable `prof_id` identifies each professor, a separate identifier-based design can be evaluated with the same two tests.

#### Exercise 4: Student courses and hobbies

For:

```text
R(stu_id, course, hobby)
```

assume:

\[
stu\_id \twoheadrightarrow course,
\qquad
stu\_id \twoheadrightarrow hobby
\]

with no nontrivial FD.

1. Test 4NF.
2. Decompose the relation.
3. Verify lossless join.
4. State the dependency-preservation result.

**Worked solution:**

The candidate key is `{stu_id, course, hobby}`. The determinant `stu_id` is not a superkey, and both MVDs are nontrivial. The relation is in BCNF but not in 4NF.

Use:

```text
STUDENT_COURSE(stu_id, course)
STUDENT_HOBBY(stu_id, hobby)
```

The intersection is `stu_id`. Since `stu_id ↠ course`, the MVD lossless-join test `(R1 ∩ R2) ↠ (R1 - R2)` holds.

FD preservation is vacuous because there is no nontrivial FD. The original nontrivial MVD should remain declared if the two tables receive independent updates. Both components are in 4NF.

#### Exercise 5: Decomposition into BCNF

Consider:

```text
R(A, B, C)
F = { A -> B, B -> C, A -> C }
```

1. Find the candidate key and identify the BCNF violation.
2. Decompose `R`.
3. Verify lossless join and dependency preservation.

**Worked solution:**

`A` is the candidate key because `A -> B` and `B -> C`. The dependency `B -> C` has a non-superkey determinant and non-prime right-hand side, so `R` is in neither 3NF nor BCNF.

Use:

```text
R1(A, B)
R2(B, C)
```

The intersection is `B`, and `B -> C` gives:

\[
(R_1 \cap R_2) \rightarrow R_2
\]

The decomposition is lossless.

The local dependencies are `A -> B` in `R1` and `B -> C` in `R2`. Their union derives `A -> C` by transitivity, so `(F1 ∪ F2)+ = F+`. Dependencies are preserved. The keys are `A` and `B`, so both components are in BCNF.

#### Exercise 6: Two candidate keys

Consider:

```text
R(A, B, C, D, E)
F = {
    {A,B} -> {C,D,E},
    {C,D} -> {A,B,E}
}
```

Determine prime attributes, test 2NF through 5NF under the assumption that no additional MVD or nonbinary JD exists, and state whether decomposition is required.

**Worked solution:**

The candidate keys are `{A,B}` and `{C,D}`. Therefore `A`, `B`, `C`, and `D` are prime, while `E` is non-prime.

- **2NF:** `E` is fully dependent on both candidate keys because no proper subset of either pair determines `E`.
- **3NF:** Every nontrivial FD has a candidate-key determinant.
- **BCNF:** Every determinant is a superkey.
- **4NF:** With no additional MVDs, every nontrivial MVD is FD-implied and has a superkey determinant.
- **5NF:** With no non-key-implied three-way or higher-order JD after the binary-JD test, the relation satisfies the 5NF condition.

No decomposition is required under these assumptions. A new business rule that creates a nontrivial MVD or a non-key-implied nonbinary JD would change the result.

#### Exercise 7: A three-way teaching rule

Consider:

```text
TEACHING(lecturer, semester, subject)
```

Assume the pairwise projections `LS`, `SC`, and `LC` satisfy a nontrivial JD, while the full tuple is the only candidate key.

1. Determine the normal form of the original relation.
2. Decompose it.
3. Prove the decomposition is lossless.
4. State what must happen to the JD constraint.

**Worked solution:**

The JD `⋈[LS, SC, LC]` is nontrivial. Its projections are not superkeys, so the JD is not implied by the candidate key. The relation is not in 5NF.

Create:

```text
LECTURER_SEMESTER(lecturer, semester)
SEMESTER_SUBJECT(semester, subject)
LECTURER_SUBJECT(lecturer, subject)
```

The decomposition is lossless because:

\[
r = \pi_{LS}(r) \bowtie \pi_{SC}(r) \bowtie \pi_{LC}(r)
\]

holds for every legal instance by the selected JD. The relation is also free of a stated nontrivial MVD and therefore satisfies 4NF before the 5NF split.

The JD remains a three-way semantic constraint. Retain it in the dependency catalog or enforce it in the application when component rows change independently. Lossless reconstruction alone does not prove local dependency preservation.

### 15.3 Consolidated common-trap table

| Trap | Correct rule |
|---|---|
| Testing 2NF with only the primary key | Test every candidate key and every non-prime attribute |
| Treating 2NF as full dependence of every attribute | Only non-prime attributes need full dependence for the 2NF test |
| Calling every determinant in 3NF a superkey | 3NF also permits a right-hand side made entirely of prime attributes |
| Saying 3NF forbids every transitive dependency | It forbids the relevant transitive dependency of non-prime attributes; prime-attribute cases may remain |
| Applying BCNF to the right-hand side | Apply BCNF to the determinant |
| Accepting a determinant that is only part of a superkey | The determinant must itself determine every attribute |
| Treating multiple values as proof of an MVD | Use the formal tuple-swap property and business semantics |
| Saying 4NF permits no MVD | 4NF permits trivial MVDs and MVDs with superkey determinants |
| Assuming a shared join column proves losslessness | Prove that the intersection determines one complete component, or use the chase test |
| Requiring every dependency in one relation | The union of projected dependencies must derive `F+` |
| Saying 5NF contains no JD | 5NF permits trivial and candidate-key-implied JDs |
| Maximizing the number of tables | Decompose only to remove dependency-caused redundancy while preserving required facts |

### 15.4 Notation and formula cheat sheet

#### Symbols

| Symbol | Meaning |
|---|---|
| `R(A1, ..., An)` | Relation schema with attributes `A1` through `An` |
| `F` | Given set of dependencies |
| `F+` | Closure of `F`, containing every dependency it implies |
| `X -> Y` | Functional dependency: `X` determines `Y` |
| `X ↠ Y` | Multivalued dependency: `X` multivalued-determines `Y` |
| `⋈[X1, ..., Xn]` | Join dependency over the listed attribute sets |
| `X+` | Attribute closure of `X` under `F` |
| `K` | Candidate key |
| `SK` | Superkey |
| `A` | Non-prime attribute in a 2NF or 3NF test |
| `πRi(F)` | Projection of dependencies onto schema `Ri` |
| `πRi(r)` | Projection of instance `r` onto schema `Ri` |
| `r` | Legal instance of `R` |
| `r_i` | Projected instance of component relation `Ri` |
| `Z` | Remaining attributes: `R - (X ∪ Y)` |

#### Normal-form formulas

| Form | Formula |
|---|---|
| 2NF | `R` is in 1NF, and for every candidate key `K` and non-prime `A`, `K -> A` implies no proper subset `K' ⊂ K` has `K' -> A` |
| 3NF | For every nontrivial `X -> Y`, `X+ = R` or `Y ⊆ Prime(R)` |
| BCNF | For every nontrivial `X -> Y`, `X+ = R` |
| 4NF | For every nontrivial `X ↠ Y`, `X+ = R` |
| 5NF | Every nontrivial JD is candidate-key-implied; equivalently, every projection in it is a superkey |

#### Decomposition formulas

| Purpose | Formula |
|---|---|
| Binary FD lossless-join test | `(R1 ∩ R2) -> R1` or `(R1 ∩ R2) -> R2` |
| Binary MVD lossless-join test | `(R1 ∩ R2) ↠ (R1 - R2)` or `(R1 ∩ R2) ↠ (R2 - R1)` |
| Dependency preservation | `(F1 ∪ F2 ∪ ... ∪ Fn)+ = F+` |
| BCNF split from `X -> Y` | Choose `A` in `Y - X`; use `R1 = X ∪ {A}`, `R2 = R - {A}` |
| 4NF split from `X ↠ Y` | Let `A = Y - X`; use `R1 = X ∪ A`, `R2 = R - A` |
| 5NF split from `⋈[X1, ..., Xn]` | Create `Ri(Xi)` for each listed set |
| Multiway lossless reconstruction | `r = ⋈ πRi(r)` for every legal `r` |

#### Key and attribute tests

| Question | Test |
|---|---|
| Is `X` a superkey? | Compute `X+`; it must equal `R` |
| Is `K` a candidate key? | `K+ = R`, and no proper subset of `K` has closure `R` |
| Is `A` prime? | `A` occurs in at least one candidate key |
| Is an MVD trivial? | `Y ⊆ X` or `X ∪ Y = R` |
| Is a JD trivial? | One projection contains all attributes of `R` |

### 15.5 Normal-form comparison at a glance

| Form | Dependency used | Strict test | Redundancy target |
|---|---|---|---|
| 1NF | Attribute values | Every cell is atomic | Repeating groups and non-atomic values |
| 2NF | FDs | Full dependence of non-prime attributes on every candidate key | Partial dependencies |
| 3NF | FDs | Superkey determinant or prime right-hand side | Non-prime transitive dependencies |
| BCNF | FDs | Every determinant is a superkey | All FD determinant anomalies |
| 4NF | MVDs | Every nontrivial MVD determinant is a superkey | Independent multivalued groups |
| 5NF/PJNF | JDs | Every nontrivial JD is candidate-key-implied | Non-key-implied project-join rules |

### 15.6 Rapid-revision checklist

Before declaring a design normalized, check each item:

- [ ] Every relation is in 1NF.
- [ ] Every candidate key has been found, not only the primary key.
- [ ] Prime and non-prime attributes have been listed.
- [ ] Every non-prime attribute is fully dependent on every candidate key for 2NF.
- [ ] Every nontrivial FD has been checked against the 3NF condition.
- [ ] Every nontrivial FD determinant has been checked against BCNF.
- [ ] Independent multivalued groups and their MVDs have been identified.
- [ ] Every nontrivial MVD determinant has been checked against 4NF.
- [ ] Three-way and cyclic business rules have been checked for non-key-implied JDs.
- [ ] Each decomposition has a lossless-join proof.
- [ ] Each decomposition has a dependency-preservation calculation.
- [ ] Candidate keys have been recomputed in every component relation.
- [ ] Foreign keys connect the decomposed relations without changing their meaning.
- [ ] The final schema still represents the stated business rules.

### 15.7 One-minute answer framework

For a normal-form question, use this order:

1. **State the formal rule.**
2. **List candidate keys and prime attributes.**
3. **Identify the violating dependency.**
4. **Give the decomposition.**
5. **Verify lossless join.**
6. **Verify dependency preservation.**
7. **Confirm the resulting normal form.**
