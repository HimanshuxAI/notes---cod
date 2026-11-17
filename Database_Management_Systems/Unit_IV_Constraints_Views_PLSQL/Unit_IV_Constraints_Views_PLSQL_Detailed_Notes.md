# Database Management Systems Unit IV Study Guide

**Part 1: Constraints and Views**

| Metadata | Detail |
|---|---|
| Course | Database Management System |
| Course code and class | 23CSE2022, S.Y. |
| Institution | MIT Art Design and Technology University, MIT School of Computing, Pune |
| Unit | IV: Constraints, Views and PL/SQL |
| Academic session | AY 2026-2027, Semester I |
| Unit allocation | 09 hours |
| Source basis | `UNIT IV.pptx` (58 slides), checked against the supplied slide text and image-slide OCR |
| Scope of this part | Integrity constraints, referential actions, deferred checking, and views |
| SQL convention | Portable SQL unless a block is labeled for PostgreSQL, MySQL, or Oracle |

### Table of Contents

#### Part 1: Constraints and Views

1. Unit Overview and Syllabus Map
2. Constraints and Their Importance
3. Entity, Referential, Domain, and User-Defined Integrity
4. Constraint Types and SQL Syntax
5. Referential Actions and Deferred Constraint Checking
6. Views: Virtual Relations and Definitions
7. View Dependencies, Expansion, and Materialized Views
8. View Updates, Security, and Views vs Tables
9. Worked Constraint and View Exercises, Common Traps, Revision Checklist

#### Part 2: SQL Functions and PL/SQL Programming

Part 2 covers the remaining Unit IV material: data-definition statements, aggregate functions, `NULL` values, nested subqueries, PL/SQL blocks, stored procedures, functions, triggers, and cursors. It also includes integrated PL/SQL exercises and a revision checklist.

---

## 1. Unit Overview and Syllabus Map

### 1.1 Formal overview

Unit IV divides database design rules into two layers:

1. **Declarative integrity rules** constrain the values and relationships that the DBMS permits.
2. **Programmatic database logic** extends SQL with reusable procedural units, exception handling, row-by-row processing, and event-driven actions.

Part 1 covers the first layer and the database objects that control how users observe stored data. Part 2 covers SQL query features and PL/SQL programming.

### 1.2 Plain-language overview

A constraint tells the database which data it must accept. A view gives a user a controlled question over one or more stored tables without storing a second copy of the result. Together, they separate business rules and access boundaries from the physical base tables.

### 1.3 Source-to-study-guide map

| Source slides | Topic | Treatment in this guide |
|---|---|---|
| 2 | Unit IV syllabus and nine-hour allocation | Section 1 |
| 3-5 | Constraint purpose, major types, integrity categories | Sections 2-4 |
| 6-9 | Entity, domain, and referential integrity | Section 3 |
| 10-11 | Cascading actions and deferred checking | Section 5 |
| 12-20 | View definitions, dependencies, expansion, materialized views | Sections 6-7 |
| 21-24 | View updates, security, table comparison, query use | Section 8 |
| 25-41 | Aggregate functions, window functions, `NULL`, nested subqueries | Part 2 |
| 42-49 | PL/SQL blocks, procedures, and functions | Part 2 |
| 50-58 | Triggers and cursors | Part 2 |

### 1.4 Learning outcomes

After Part 1, you should be able to:

- distinguish entity, referential, domain, and user-defined integrity;
- write table-level and column-level constraints;
- choose and explain `CASCADE`, `SET NULL`, `SET DEFAULT`, `RESTRICT`, and `NO ACTION`;
- explain when a foreign-key check can be deferred;
- define a view, trace its dependencies, and expand a view over another view;
- distinguish an ordinary view from a materialized view;
- determine whether a simple view is updatable under common DBMS rules;
- use views to restrict exposed columns and rows; and
- avoid claims that constraints or ordinary views automatically guarantee faster queries.

---

## 2. Constraints and Their Importance

### 2.1 Definition

**Formal definition.** A constraint is a declarative rule attached to a table, column, or relationship and enforced by the DBMS when relevant data is inserted, updated, or deleted.

**Plain-language definition.** A constraint is a boundary on what the database will accept. The application cannot bypass it with a normal `INSERT`, `UPDATE`, or `DELETE` statement.

### 2.2 Why constraints matter

| Benefit | Formal effect | Practical effect |
|---|---|---|
| Data validity | Rejects a row that violates a declared rule | Prevents impossible values such as a negative salary |
| Entity identity | Assigns a unique, non-null key to each row | Lets applications refer to one exact record |
| Relationship validity | Keeps foreign-key values linked to valid parent rows | Prevents orphaned child records |
| Consistency | Applies the same rule to every application that writes through the DBMS | Avoids one client enforcing a rule that another client omits |
| Error detection | Reports a constraint violation when a write breaks a rule | Turns a silent data defect into a rejected transaction |
| Change control | Stores rules in database metadata | Centralizes business-rule maintenance |

### 2.3 Constraint enforcement in a write

A constraint does not inspect every table after every command. The DBMS evaluates it only when the affected row or relationship could break the rule.

**Portable SQL example:**

```sql
CREATE TABLE account (
    account_id INTEGER PRIMARY KEY,
    balance DECIMAL(12, 2) NOT NULL,
    CONSTRAINT ck_account_minimum_balance CHECK (balance > 10000.00)
);

-- Rejected: the balance violates ck_account_minimum_balance.
INSERT INTO account (account_id, balance)
VALUES (1, 5000.00);

-- Accepted: the balance satisfies the CHECK constraint.
INSERT INTO account (account_id, balance)
VALUES (2, 15000.00);
```

### 2.4 Constraints and performance

The slide source groups “performance” with constraint benefits. The precise statement is narrower:

- A `PRIMARY KEY` or `UNIQUE` constraint often has an associated index because the DBMS needs an efficient way to detect duplicate keys.
- A `FOREIGN KEY` can require checks or index support on referenced columns.
- Constraints add validation work to writes.
- Constraints do **not** guarantee faster retrieval, better query plans, or lower storage cost.

The safe design rule is to declare required keys and rules first, then inspect the DBMS's actual indexes and execution plans separately.

---

## 3. Entity, Referential, Domain, and User-Defined Integrity

### 3.1 The four integrity categories

| Integrity category | Formal meaning | Plain-language meaning | Typical SQL mechanism |
|---|---|---|---|
| Entity integrity | A row has a unique, non-null identifier | Every record has one dependable identity | `PRIMARY KEY` |
| Referential integrity | A non-null foreign-key value identifies a row in the referenced relation | A child cannot point to a parent that does not exist | `FOREIGN KEY` |
| Domain integrity | An attribute's value belongs to its declared type and allowed set | Each column accepts only sensible values | data type, `NOT NULL`, `CHECK`, `DEFAULT` |
| User-defined integrity | A business rule extends the built-in relational rules | The organization has its own rules, such as “senior staff earn at least 50,000” | named `CHECK`; sometimes a domain or trigger |

The categories overlap in practice. A primary key is also a domain rule because its values must be non-null and unique. A foreign key is a relationship rule as well as a domain restriction on the child columns.

### 3.2 Entity integrity

**Formal explanation.** A primary key identifies each row in a relation. No two rows may have the same complete key, and no component of a primary key may be `NULL`.

**Plain-language explanation.** A primary key works like a dependable row number. It lets another table refer to one row without ambiguity.

**Portable SQL example:**

```sql
CREATE TABLE department (
    dept_id INTEGER,
    dept_name VARCHAR(50) NOT NULL,
    CONSTRAINT pk_department PRIMARY KEY (dept_id),
    CONSTRAINT uq_department_name UNIQUE (dept_name)
);
```

The `UNIQUE` constraint on `dept_name` does not make that column a primary key. It creates a separate candidate key that may be referenced by a foreign key.

### 3.3 Referential integrity

**Formal explanation.** A foreign key is a set of child columns whose non-null values must match a candidate key in the referenced parent relation. The referenced columns must have a `PRIMARY KEY` or `UNIQUE` constraint.

**Plain-language explanation.** If an instructor belongs to a department, the department must exist. The database prevents an orphaned instructor row.

**Portable SQL example:**

```sql
CREATE TABLE instructor (
    instructor_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dept_id INTEGER NOT NULL,
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0,
    CONSTRAINT fk_instructor_department
        FOREIGN KEY (dept_id)
        REFERENCES department (dept_id)
);

INSERT INTO department (dept_id, dept_name)
VALUES (10, 'Biology');

-- Rejected: no department has dept_id = 99.
INSERT INTO instructor (instructor_id, name, dept_id)
VALUES (30765, 'Green', 99);
```

A foreign-key column may be nullable unless the schema adds `NOT NULL`. Under common SQL `MATCH SIMPLE` semantics, a `NULL` foreign-key value does not require a matching parent row.

### 3.4 Domain integrity

**Formal explanation.** A domain defines the permitted values of an attribute through a data type, nullability, permitted set, range, format, or default value.

**Plain-language explanation.** A domain rule defines what one column may contain.

**Portable SQL example:**

```sql
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    age SMALLINT,
    employment_status VARCHAR(20) NOT NULL DEFAULT 'Junior',
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0,
    CONSTRAINT ck_employee_age CHECK (age BETWEEN 18 AND 65),
    CONSTRAINT ck_employee_status
        CHECK (employment_status IN ('Junior', 'Senior', 'Manager'))
);
```

Important details:

- `CHECK` rejects a row when its predicate evaluates to false.
- Under common SQL semantics, a predicate that evaluates to unknown because of `NULL` does not reject the row. Use `NOT NULL` or write `age IS NULL OR age BETWEEN 18 AND 65` when the business rule requires a non-null value.
- `DEFAULT` supplies a value when the column is omitted. It does not repair every later invalid value.
- The source's `ENUM` example is MySQL-specific. The portable `VARCHAR` plus `CHECK` form above expresses the same permitted set.

**MySQL-specific example from the source pattern:**

```sql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE NOT NULL,
    status ENUM('Pending', 'Shipped', 'Delivered') DEFAULT 'Pending'
);
```

### 3.5 User-defined integrity

**Formal explanation.** User-defined integrity captures organization-specific rules that are not supplied by entity or referential integrity alone.

**Plain-language explanation.** The institution decides that a Senior employee must earn at least 50,000. That rule belongs in the schema if every writer must obey it.

**Portable SQL example:**

```sql
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    employment_status VARCHAR(20) NOT NULL DEFAULT 'Junior',
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0,
    CONSTRAINT ck_senior_minimum_salary
        CHECK (employment_status <> 'Senior' OR salary >= 50000)
);
```

The named constraint gives the rule a stable identity in database metadata and produces a more useful error message than an unnamed condition.

Some systems support a standard-style domain object:

```sql
CREATE DOMAIN employee_age AS SMALLINT
CHECK (VALUE BETWEEN 18 AND 65);
```

`CREATE DOMAIN` support varies by DBMS. A named `CHECK` constraint is the portable classroom choice.

## 4. Constraint Types and SQL Syntax

### 4.1 Where constraints appear

A constraint can be declared at the column level or at the table level.

- **Column-level constraint** applies to one column, such as `age SMALLINT NOT NULL`.
- **Table-level constraint** applies to one column or a group of columns, such as a composite `PRIMARY KEY` or `FOREIGN KEY`.
- A **named constraint** gives the rule a stable label in metadata. Named table-level constraints are preferable for relationships and business rules.

### 4.2 Constraint reference table

| Constraint | Core rule | Example syntax | Key detail |
|---|---|---|---|
| `NOT NULL` | The column cannot contain `NULL` | `name VARCHAR(100) NOT NULL` | A primary-key column is non-null by definition |
| `PRIMARY KEY` | The complete key is unique and non-null | `CONSTRAINT pk_employee PRIMARY KEY (employee_id)` | Identifies rows and can support references |
| `UNIQUE` | The key or column has no duplicate non-null value | `CONSTRAINT uq_email UNIQUE (email)` | May allow several `NULL` values unless the DBMS or schema forbids it |
| `CHECK` | A row must satisfy a Boolean expression | `CHECK (age BETWEEN 18 AND 65)` | Common `NULL` semantics allow unknown-valued checks |
| `FOREIGN KEY` | Child values must match a parent candidate key | `FOREIGN KEY (dept_id) REFERENCES department (dept_id)` | The parent key needs `PRIMARY KEY` or `UNIQUE` |
| `DEFAULT` | Supplies a value when the column is omitted | `status VARCHAR(20) DEFAULT 'Pending'` | Not a substitute for `NOT NULL` or `CHECK` |

### 4.3 Column-level syntax

**Portable SQL example:**

```sql
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    age SMALLINT NOT NULL CHECK (age BETWEEN 18 AND 65),
    status VARCHAR(20) NOT NULL DEFAULT 'Junior'
);
```

Read the definition from left to right:

1. `employee_id` is the row identifier.
2. `employee_name` must have a value.
3. `email` must have a value and must not duplicate another non-null email.
4. `age` must have a value from 18 through 65.
5. `status` receives `'Junior'` when the column is omitted, and every stored status must be non-null.

### 4.4 Table-level syntax and composite keys

**Portable SQL example:**

```sql
CREATE TABLE course_offering (
    course_id INTEGER NOT NULL,
    semester VARCHAR(20) NOT NULL,
    year INTEGER NOT NULL,
    instructor_id INTEGER NOT NULL,
    CONSTRAINT pk_course_offering
        PRIMARY KEY (course_id, semester, year),
    CONSTRAINT uq_course_offering_instructor
        UNIQUE (course_id, semester, year, instructor_id),
    CONSTRAINT fk_offering_instructor
        FOREIGN KEY (instructor_id)
        REFERENCES instructor (instructor_id)
);
```

The composite key `(course_id, semester, year)` identifies an offering. Two rows may share a course if they occur in different terms. The same term and course cannot occur twice for the same instructor because of the larger `UNIQUE` constraint.

### 4.5 Constraint behavior checks

| Question | Correct answer |
|---|---|
| Must every table have a `PRIMARY KEY`? | No, but every relation that needs stable row identity normally should have one. |
| Does `UNIQUE` imply `NOT NULL`? | No. Handle `NULL` behavior explicitly if it matters. |
| Can a foreign key reference any column? | No. The target must be a primary key or other unique candidate key. |
| Does `CHECK` guarantee that its expression is true? | Under common SQL semantics, `FALSE` rejects a row while `UNKNOWN` does not. |
| Does `DEFAULT` run after every update? | No. It normally supplies a value only when the column is omitted on insert. |
| Can one row be checked against another row in a basic `CHECK`? | Usually not. Use keys, foreign keys, assertions, or procedural triggers for cross-row rules. |

---

## 5. Referential Actions and Deferred Constraint Checking

### 5.1 When referential actions apply

An `ON DELETE` or `ON UPDATE` action describes what the DBMS does when a **parent row's referenced key** is deleted or changed. The action affects matching child rows.

### 5.2 Action comparison

| Action | On parent `DELETE` | On parent key `UPDATE` | Required schema condition |
|---|---|---|---|
| `CASCADE` | Delete matching child rows | Change matching child foreign-key values to the new parent key | The propagated value must satisfy every other constraint |
| `SET NULL` | Set matching child foreign-key columns to `NULL` | Set matching child foreign-key columns to `NULL` | The affected foreign-key columns must allow `NULL` |
| `SET DEFAULT` | Set matching child foreign-key columns to their defaults | Set matching child foreign-key columns to their defaults | Each affected column needs a default; the resulting value must still satisfy the foreign key |
| `RESTRICT` | Reject the parent operation immediately | Reject the parent operation immediately | This action does not repair child rows |
| `NO ACTION` | Apply no automatic repair | Apply no automatic repair | The violation is rejected according to the constraint's checking time; a deferrable constraint can postpone the check |

DBMS products differ in their default action. MySQL commonly reports the default as `RESTRICT`; PostgreSQL uses `NO ACTION` semantics for an unspecified foreign-key action. State the desired action rather than relying on a default.

### 5.3 `CASCADE`, `SET NULL`, and `SET DEFAULT` examples

**PostgreSQL example:**

```sql
CREATE TABLE course (
    course_id INTEGER PRIMARY KEY,
    course_code VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE enrollment (
    enrollment_id INTEGER PRIMARY KEY,
    course_id INTEGER NOT NULL,
    student_id INTEGER,
    CONSTRAINT fk_enrollment_course
        FOREIGN KEY (course_id)
        REFERENCES course (course_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

Here, deleting a `course` row deletes its `enrollment` rows. Updating `course.course_id` changes the child foreign-key values to the new key.

For `SET NULL`, the child key must be nullable:

```sql
CREATE TABLE enrollment_nullable (
    enrollment_id INTEGER PRIMARY KEY,
    course_id INTEGER,
    CONSTRAINT fk_enrollment_nullable_course
        FOREIGN KEY (course_id)
        REFERENCES course (course_id)
        ON DELETE SET NULL
);
```

For `SET DEFAULT`, define a default on every affected foreign-key column. The default still has to match an existing parent key or the operation fails.

### 5.4 `RESTRICT` versus `NO ACTION`

Both actions reject a parent change that would leave a dangling child reference. Their timing differs:

- `RESTRICT` normally prevents the operation as soon as the constraint would be violated.
- `NO ACTION` follows the constraint's declared timing. If the foreign key is deferrable, the DBMS may postpone the check until commit.
- `NO ACTION` does not mean “do nothing at all.” The DBMS still checks referential integrity.

### 5.5 Why defer a constraint?

A circular relationship can require a temporary state that violates a foreign key during the transaction.

**Example:** `person.father_id` and `person.mother_id` both refer to `person.person_id`. A transaction may need to insert a child before both parents exist.

### 5.6 Deferred foreign-key example

**PostgreSQL example:**

```sql
CREATE TABLE person (
    person_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    father_id INTEGER,
    mother_id INTEGER,
    CONSTRAINT fk_person_father
        FOREIGN KEY (father_id)
        REFERENCES person (person_id)
        DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT fk_person_mother
        FOREIGN KEY (mother_id)
        REFERENCES person (person_id)
        DEFERRABLE INITIALLY IMMEDIATE
);

BEGIN;

SET CONSTRAINTS fk_person_father, fk_person_mother DEFERRED;

INSERT INTO person (person_id, name, father_id, mother_id)
VALUES (1, 'Ava', NULL, NULL);

INSERT INTO person (person_id, name, father_id, mother_id)
VALUES (2, 'Ben', 1, 1);

INSERT INTO person (person_id, name, father_id, mother_id)
VALUES (3, 'Cara', 2, 2);

COMMIT;
```

At `COMMIT`, PostgreSQL checks the deferred foreign keys. The referenced rows now exist, so the transaction succeeds. If `person_id = 1` were still missing at commit, PostgreSQL would reject the transaction.

### 5.7 Deferral rules and limits

- A deferrable constraint has one of three timing modes: `NOT DEFERRABLE`, `DEFERRABLE INITIALLY IMMEDIATE`, or `DEFERRABLE INITIALLY DEFERRED`.
- `SET CONSTRAINTS ... DEFERRED` changes the timing for the current transaction.
- PostgreSQL permits `UNIQUE`, `PRIMARY KEY`, `EXCLUDE`, and foreign-key constraints to be deferred. It checks `NOT NULL` and `CHECK` constraints immediately.
- MySQL and SQL Server do not provide PostgreSQL-style deferrable foreign-key checking.
- Deferral changes only the **check time**. The final committed state must still satisfy the constraint.

## 6. Views: Virtual Relations and Definitions

### 6.1 Definition

**Formal definition.** A view is a named, schema-level query definition. When a user queries a view, the DBMS derives a result relation from the view definition and its base relations.

**Plain-language definition.** A view is a saved question. It stores the query, not a separate copy of the answer.

### 6.2 Creating and using a view

**Portable SQL example:**

```sql
CREATE VIEW faculty AS
SELECT instructor_id, name, dept_id
FROM instructor;

SELECT name
FROM faculty
WHERE dept_id = 10;
```

The view `faculty` exposes instructor identity and department information but not salary. Its result changes when the underlying `instructor` table changes because the DBMS evaluates the definition against current base-table data.

### 6.3 Defining view column names

A view may supply its own column names when the query expression would otherwise produce unclear names.

**Portable SQL example:**

```sql
CREATE VIEW faculty_directory (
    instructor_id,
    instructor_name,
    department_id
)
AS
SELECT instructor_id, name, dept_id
FROM instructor;
```

The column list describes the view's external interface. It does not rename the base-table columns.

### 6.4 Main uses of views

| Use | Example | Benefit |
|---|---|---|
| Column projection | Expose `name` and `dept_id` but hide `salary` | Reduces the data visible to a role |
| Row filtering | Show only instructors in Biology | Restricts the rows visible through that interface |
| Query reuse | Store a recurring join or aggregation | Gives applications one stable object to query |
| Logical data independence | Map an application to a view while the underlying table design changes | Reduces application changes when the mapping is maintained |
| Controlled transformation | Rename columns or calculate a derived value | Presents data in a task-specific form |

### 6.5 Ordinary views do not guarantee faster queries

An ordinary view often contains the same joins, filters, and aggregations as the query that a user could have typed. The view can make code easier to write, but it does not remove that work.

- A query optimizer may inline a view, rewrite it, or use dependency metadata to produce an equivalent plan.
- Predicate pushdown may improve a plan, but the optimizer decides whether it is valid and useful.
- A complex view can be as expensive to query as the expanded query.
- A materialized view is the option that stores a result to avoid recomputing a query on every use, at the cost of storage and refresh work.

### 6.6 What a view is not

An ordinary view is not:

- a snapshot of the base data;
- a second physical copy of the rows;
- an automatic audit log;
- a substitute for table-level security; or
- proof that the query will run faster.

Permissions on a view help only when users cannot bypass it by accessing the base table or another exposed path.

---

## 7. View Dependencies, Expansion, and Materialized Views

### 7.1 Dependency types

The source defines three dependency relationships:

| Relationship | Definition | Example |
|---|---|---|
| Direct dependency | View `v2` appears in the definition of view `v1` | `staff_contact` directly depends on `staff` |
| Indirect dependency | A dependency path connects `v1` to `v2` | `staff_directory` indirectly depends on `staff` through `staff_contact` |
| Recursive dependency | A view depends on itself | A view whose definition selects from that same view |

A dependency graph records which base tables and views contribute to a view's result. The DBMS uses such metadata for expansion, renaming, permission checks, and change analysis.

Most ordinary DBMS products reject a self-referencing view at creation time. A recursive common table expression (`WITH ...`) is the usual SQL mechanism for recursive queries.

### 7.2 Views built on other views

**Portable SQL example:**

```sql
CREATE VIEW physics_fall_2017 AS
SELECT c.course_id,
       s.sec_id,
       c.building,
       s.room_number
FROM course AS c
JOIN section AS s
  ON s.course_id = c.course_id
WHERE c.dept_name = 'Physics'
  AND s.semester = 'Fall'
  AND s.year = 2017;

CREATE VIEW physics_fall_2017_watson AS
SELECT course_id, room_number
FROM physics_fall_2017
WHERE building = 'Watson';
```

`physics_fall_2017_watson` directly depends on `physics_fall_2017`. It also depends indirectly on `course` and `section`.

### 7.3 View expansion

**Formal expansion rule.** To expand an expression, replace each referenced view with that view's defining query. Repeat until the expression contains no view references, provided the dependency graph is not recursive.

**Plain-language expansion rule.** Replace each saved question with the query that defines it.

For the example above, the expanded meaning is:

```sql
SELECT outer_view.course_id,
       outer_view.room_number
FROM (
    SELECT c.course_id,
           s.sec_id,
           c.building,
           s.room_number
    FROM course AS c
    JOIN section AS s
      ON s.course_id = c.course_id
    WHERE c.dept_name = 'Physics'
      AND s.semester = 'Fall'
      AND s.year = 2017
) AS outer_view
WHERE outer_view.building = 'Watson';
```

Expansion explains why the nested view produces the same rows as the original definition. It does not prove that the DBMS will execute the SQL in exactly this textual form. An optimizer may produce a different but equivalent plan, rewrite predicates, or use stored dependency information.

### 7.4 Ordinary view versus materialized view

| Feature | Ordinary view | Materialized view |
|---|---|---|
| Stored content | Query definition | Query definition plus a stored result |
| Freshness | Reflects current base-table data when queried | Can be stale until refreshed |
| Storage cost | Little or no result storage | Uses storage for result rows and indexes |
| Write behavior | May support updates through an updatable view | Usually read-only or subject to DBMS-specific rules |
| Refresh burden | None | On-demand, scheduled, or incremental refresh work |
| Typical use | Access control, reusable SQL, logical mapping | Repeated expensive aggregates or reporting queries |

### 7.5 Materialized-view example

**PostgreSQL example:**

```sql
CREATE MATERIALIZED VIEW department_salary_total AS
SELECT dept_id,
       SUM(salary) AS total_salary
FROM instructor
GROUP BY dept_id
WITH NO DATA;

-- WITH NO DATA leaves the view unscannable until its first refresh.
REFRESH MATERIALIZED VIEW department_salary_total;

SELECT dept_id, total_salary
FROM department_salary_total
ORDER BY dept_id;
```

After a base-table change, the materialized result remains unchanged until a refresh occurs.

```sql
UPDATE instructor
SET salary = salary + 1000
WHERE dept_id = 10;

-- The stored result still has its previous value.
REFRESH MATERIALIZED VIEW department_salary_total;
```

A materialized view trades freshness control and storage for lower recomputation cost on repeated reads. It helps only when the workload and refresh strategy match that trade-off.

## 8. View Updates, Security, and Views vs Tables

### 8.1 How a view update reaches a base table

**Formal explanation.** For an updatable view, the DBMS translates a data-change statement on the view into an equivalent statement on its base relation or relations.

**Plain-language explanation.** A permitted `UPDATE` through a view changes the stored table row that produced the visible view row.

For a simple updatable view:

- `INSERT` creates a base-table row.
- `UPDATE` changes mapped columns in matching base-table rows.
- `DELETE` removes matching base-table rows.

### 8.2 A common automatically updatable pattern

“Simple view” is an informal label. SQL standards and DBMS products define updatability in slightly different ways. A common automatically updatable pattern has these properties:

| Property | Rule for a common simple updatable view |
|---|---|
| Sources | Exactly one base table or another updatable view |
| Selected columns | Direct references to updatable base-table columns |
| Row duplication | No `DISTINCT` |
| Grouping | No `GROUP BY` or `HAVING` |
| Aggregation | No aggregate or window function |
| Set operations | No top-level `UNION`, `INTERSECT`, or `EXCEPT` |
| Row limit | No top-level `LIMIT` or `OFFSET` in PostgreSQL's updatable-view rules |
| Omitted columns | The base column must have a usable default or accept `NULL` |

Some DBMS products also support updates through carefully designed join views, often when the view preserves a unique key and each output row maps to one base row. Those product-specific rules go beyond the basic one-table pattern.

### 8.3 Update example

Using the `instructor` table from Section 3:

```sql
CREATE VIEW faculty AS
SELECT instructor_id, name, dept_id
FROM instructor;

-- Maps to an INSERT into instructor.
-- salary is omitted, so its DEFAULT value of 0 is used.
INSERT INTO faculty (instructor_id, name, dept_id)
VALUES (30765, 'Green', 10);

-- Maps to an UPDATE of instructor.
UPDATE faculty
SET name = 'Martin Green'
WHERE instructor_id = 30765;

-- Maps to a DELETE from instructor.
DELETE FROM faculty
WHERE instructor_id = 30765;
```

The source slides state that an omitted view column “can be set to null.” The precise rule is:

1. If the base column has a default, the DBMS normally uses that default when an insert omits the column.
2. If no default exists, the DBMS may use `NULL` only when the base column permits it.
3. If the base column is `NOT NULL` and has no usable default, the insert fails.

### 8.4 Non-updatable views

**Portable SQL example:**

```sql
CREATE VIEW department_salary_total AS
SELECT dept_id,
       SUM(salary) AS total_salary
FROM instructor
GROUP BY dept_id;
```

A DBMS cannot map one aggregate output row back to a unique set of base rows without additional rules. For that reason, this view is normally read-only. Update the base data directly or create a trigger or procedure that implements a defined business action.

### 8.5 `WITH CHECK OPTION`

A filtered view may allow an `INSERT` or `UPDATE` that creates a base row that the view's predicate excludes. `WITH CHECK OPTION` prevents that result for supported updatable views.

**PostgreSQL example:**

```sql
CREATE VIEW biology_faculty AS
SELECT instructor_id, name, dept_id
FROM instructor
WHERE dept_id = 10
WITH CHECK OPTION;

-- Rejected: the inserted row would not satisfy the view's WHERE clause.
INSERT INTO biology_faculty (instructor_id, name, dept_id)
VALUES (40001, 'Hidden Row', 20);
```

`WITH LOCAL CHECK OPTION` checks the current view's predicate. `WITH CASCADED CHECK OPTION` also checks predicates of underlying views. The option does not make an aggregate or otherwise non-updatable view updatable.

### 8.6 Security benefits of views

A view can serve as a controlled interface between users and base tables.

| Security benefit | How the view helps | Required precaution |
|---|---|---|
| Column exposure control | Projects only approved columns | Revoke direct base-table access |
| Row exposure control | Filters rows by department, role, or other criteria | Test that the predicate cannot be bypassed |
| Least privilege | Grants `SELECT` on a narrow view instead of a broad table | Create and manage the role explicitly |
| Logical masking | Replaces sensitive values with a safe transformation | Review the expression for information leakage |
| Stable application interface | Keeps a controlled query definition in the catalog | Maintain the definition when base schemas change |

**PostgreSQL privilege example, assuming `analyst_role` already exists:**

```sql
CREATE VIEW analyst_faculty AS
SELECT instructor_id, name, dept_id
FROM instructor
WHERE dept_id = 10;

GRANT SELECT ON analyst_faculty TO analyst_role;
REVOKE ALL ON instructor FROM analyst_role;
```

The user can query `analyst_faculty` but cannot query `instructor` directly. The security benefit disappears if the same user retains another path to the base table or a more revealing view.

### 8.7 Limits of view-based security

- A view does not create an audit trail by itself. Use the DBMS's audit facilities to record access.
- Granting `SELECT` on a view grants access to the result exposed by that view, including any sensitive values the query returns.
- The permissions of a view owner can affect what a user can see through the view. Review ownership and any invoked functions.
- A filtered view does not protect a base row from a user who can still update the base table directly.
- Row-level security may provide stronger, centrally enforced controls in DBMS products that support it.

### 8.8 Views versus tables

| Property | Base table | Ordinary view | Materialized view |
|---|---|---|---|
| Main content | Stored rows and schema | Stored query definition | Query definition and stored result |
| Freshness | Current stored state | Derived when queried | Current only after a refresh |
| Column structure | Defined directly by `CREATE TABLE` | Derived from the query, with optional view column names | Derived from the query, with optional view column names |
| `SELECT` | Reads stored rows | Executes the view query | Reads stored result |
| `INSERT`, `UPDATE`, `DELETE` | Supported subject to constraints | Supported only when the DBMS can map the operation | Usually restricted or read-only |
| Storage | Holds table data | Does not hold a second row copy | Holds an additional result copy |
| Dependency | May be referenced by other objects | Depends on base tables and other views | Depends on its defining query's relations |
| Performance | Indexes and plans determine cost | No guaranteed speedup; cost depends on the expanded query | Can speed repeated reads, but refresh and freshness costs apply |
| Security | Permissions expose the whole table subject to granted operations | Can expose a restricted, controlled result | Exposes a stored snapshot, which may be stale |

### 8.9 Corrections to common source claims

| Source wording or implication | Precise correction |
|---|---|
| “Most SQL implementations allow updates only on simple views.” | Updatability depends on the SQL standard's rules and each DBMS's extensions. Some products support additional join-view cases. |
| An omitted column in a view insert “can be set to null.” | A default is used when available; `NULL` is used only if the base column accepts it. |
| Views provide “audit trails.” | Views control access but do not record access unless the DBMS audit facility is enabled. |
| Views “optimize query performance.” | An ordinary view does not guarantee faster execution. The optimizer may rewrite it, but the underlying work remains. A materialized view stores a result and adds refresh costs. |

## 9. Worked Constraint and View Exercises, Common Traps, Revision Checklist

### 9.1 Exercise conventions

The exercises use the `department` and `instructor` tables introduced in Section 3. A useful seed dataset is:

```sql
INSERT INTO department (dept_id, dept_name)
VALUES (10, 'Biology'),
       (20, 'History');

INSERT INTO instructor (instructor_id, name, dept_id, salary)
VALUES (101, 'Asha', 10, 65000),
       (102, 'Bilal', 10, 72000),
       (103, 'Chandra', 20, 61000);
```

Run each exercise in a clean database or reset the affected rows first.

### 9.2 Worked Exercise 1: Build and classify integrity rules

**Task.** Define an `employee` table with entity integrity, domain integrity, a uniqueness rule, and the user-defined rule “a Senior employee earns at least 50,000.”

**Step 1: Select the rules.**

- `employee_id` identifies each employee.
- `email` must exist and must be unique.
- `age` must be present and between 18 and 65.
- `employment_status` must use `Junior`, `Senior`, or `Manager`.
- `salary` cannot be negative.
- A Senior employee must earn at least 50,000.

**Step 2: Write the schema.**

```sql
CREATE TABLE employee (
    employee_id INTEGER PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    age SMALLINT NOT NULL,
    employment_status VARCHAR(20) NOT NULL DEFAULT 'Junior',
    salary DECIMAL(10, 2) NOT NULL DEFAULT 0,
    CONSTRAINT ck_employee_age
        CHECK (age BETWEEN 18 AND 65),
    CONSTRAINT ck_employee_status
        CHECK (employment_status IN ('Junior', 'Senior', 'Manager')),
    CONSTRAINT ck_employee_nonnegative_salary
        CHECK (salary >= 0),
    CONSTRAINT ck_senior_minimum_salary
        CHECK (employment_status <> 'Senior' OR salary >= 50000)
);
```

**Step 3: Test one valid and two invalid rows.**

```sql
-- Accepted.
INSERT INTO employee
    (employee_id, email, age, employment_status, salary)
VALUES
    (1, 'asha@example.edu', 29, 'Senior', 60000);

-- Rejected: age is below 18.
INSERT INTO employee
    (employee_id, email, age, employment_status, salary)
VALUES
    (2, 'too-young@example.edu', 17, 'Junior', 30000);

-- Rejected: a Senior employee earns less than 50,000.
INSERT INTO employee
    (employee_id, email, age, employment_status, salary)
VALUES
    (3, 'low-senior@example.edu', 35, 'Senior', 40000);
```

**Result.** The `PRIMARY KEY` provides entity integrity. The type, nullability, and `CHECK` constraints provide domain integrity. The Senior salary rule is user-defined integrity.

### 9.3 Worked Exercise 2: Choose and test referential actions

**Task.** A course has enrollments. Deleting the course should delete its enrollments, and changing the course key should propagate the new key to the enrollments.

**Step 1: Choose the actions.** Use `ON DELETE CASCADE` and `ON UPDATE CASCADE`.

**Step 2: Create the tables.**

```sql
CREATE TABLE course (
    course_id INTEGER PRIMARY KEY,
    course_code VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE enrollment (
    enrollment_id INTEGER PRIMARY KEY,
    course_id INTEGER NOT NULL,
    student_id INTEGER NOT NULL,
    CONSTRAINT fk_enrollment_course
        FOREIGN KEY (course_id)
        REFERENCES course (course_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

**Step 3: Insert test rows.**

```sql
INSERT INTO course (course_id, course_code)
VALUES (501, 'DBMS');

INSERT INTO enrollment (enrollment_id, course_id, student_id)
VALUES (9001, 501, 41),
       (9002, 501, 42);
```

**Step 4: Update the parent key.**

```sql
UPDATE course
SET course_id = 502
WHERE course_id = 501;

SELECT enrollment_id, course_id
FROM enrollment
ORDER BY enrollment_id;
```

**Expected result:**

```text
enrollment_id | course_id
9001          | 502
9002          | 502
```

**Step 5: Delete the parent.**

```sql
DELETE FROM course
WHERE course_id = 502;

SELECT COUNT(*) AS remaining_enrollments
FROM enrollment;
```

**Expected result:** `remaining_enrollments = 0` because both child rows were cascaded away.

**Design note.** `CASCADE` is appropriate only when child enrollment history should disappear with the course. If the enrollment history must remain, use nullable foreign-key columns with `ON DELETE SET NULL`.

### 9.4 Worked Exercise 3: Defer a self-referencing foreign key

**Task.** Insert a child person before the referenced parent rows exist, while keeping the final transaction state valid.

**Step 1: Define deferrable foreign keys.**

```sql
CREATE TABLE person (
    person_id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    father_id INTEGER,
    mother_id INTEGER,
    CONSTRAINT fk_person_father
        FOREIGN KEY (father_id)
        REFERENCES person (person_id)
        DEFERRABLE INITIALLY IMMEDIATE,
    CONSTRAINT fk_person_mother
        FOREIGN KEY (mother_id)
        REFERENCES person (person_id)
        DEFERRABLE INITIALLY IMMEDIATE
);
```

**Step 2: Start a transaction and defer only the foreign keys.**

```sql
BEGIN;

SET CONSTRAINTS fk_person_father, fk_person_mother DEFERRED;
```

**Step 3: Insert the child first.**

```sql
INSERT INTO person (person_id, name, father_id, mother_id)
VALUES (3, 'Cara', 2, 2);
```

This statement is accepted because the foreign-key checks are deferred. The same insert would fail under immediate checking because `person_id = 2` does not yet exist.

**Step 4: Insert the referenced rows and commit.**

```sql
INSERT INTO person (person_id, name, father_id, mother_id)
VALUES (1, 'Ava', NULL, NULL),
       (2, 'Ben', 1, 1);

COMMIT;
```

**Result.** At commit, all non-null foreign-key values match existing parent rows. Deferral postpones validation; it does not permit an invalid final state.

### 9.5 Worked Exercise 4: Define a filtered view and query it

**Task.** Expose instructor identity and department information while hiding salary. Provide a second view that exposes only Biology instructors.

**Step 1: Define the general view.**

```sql
CREATE VIEW faculty AS
SELECT instructor_id, name, dept_id
FROM instructor;
```

**Step 2: Define the filtered view.**

```sql
CREATE VIEW biology_faculty AS
SELECT instructor_id, name, dept_id
FROM faculty
WHERE dept_id = 10;
```

**Step 3: Query both interfaces.**

```sql
SELECT instructor_id, name, dept_id
FROM faculty
ORDER BY instructor_id;

SELECT instructor_id, name
FROM biology_faculty
ORDER BY instructor_id;
```

**Expected result from `faculty`:** three rows with IDs 101, 102, and 103.

**Expected result from `biology_faculty`:** rows 101 and 102 only.

**Dependency analysis.** `biology_faculty` directly depends on `faculty` and indirectly depends on `instructor`.

### 9.6 Worked Exercise 5: Expand a view over another view

**Task.** Expand `biology_instructor_names` until no view name remains.

**Step 1: Inspect the definitions.**

```sql
CREATE VIEW faculty AS
SELECT instructor_id, name, dept_id
FROM instructor;

CREATE VIEW biology_instructor_names AS
SELECT instructor_id, name
FROM faculty
WHERE dept_id = 10;
```

**Step 2: Replace the inner view reference.**

```sql
SELECT outer_view.instructor_id,
       outer_view.name
FROM (
    SELECT instructor_id, name, dept_id
    FROM instructor
) AS outer_view
WHERE outer_view.dept_id = 10;
```

**Step 3: Check that no view remains.** The only remaining relation is the base table `instructor`, so expansion is complete.

**Result.** The expanded query returns instructor IDs 101 and 102 with their names. The optimizer may execute a different equivalent plan, but the dependency chain remains:

```text
biology_instructor_names -> faculty -> instructor
```

### 9.7 Worked Exercise 6: Test view updatability

**Task.** Decide whether the following views are updatable and test an update.

**Step 1: Examine the simple view.**

```sql
CREATE VIEW instructor_names AS
SELECT instructor_id, name, dept_id
FROM instructor;
```

It uses one table, selects plain columns, and contains no `DISTINCT`, grouping, aggregate, window function, or set operation. It is a common automatically updatable pattern.

**Step 2: Update through it.**

```sql
UPDATE instructor_names
SET name = 'Asha Patel'
WHERE instructor_id = 101;

SELECT name
FROM instructor
WHERE instructor_id = 101;
```

**Expected result:** `Asha Patel`.

**Step 3: Examine the aggregate view.**

```sql
CREATE VIEW department_salary_total AS
SELECT dept_id,
       SUM(salary) AS total_salary
FROM instructor
GROUP BY dept_id;
```

It is not updatable because its rows summarize base rows and do not map one-to-one to base rows.

**Step 4: Test view membership protection.**

```sql
CREATE VIEW biology_instructor_names_checked AS
SELECT instructor_id, name, dept_id
FROM instructor
WHERE dept_id = 10
WITH CHECK OPTION;
```

An insert with `dept_id = 20` is rejected because the resulting row would fall outside the view.

### 9.8 Worked Exercise 7: Refresh a materialized view

**Task.** Store department salary totals, demonstrate staleness, and refresh the stored result.

**Step 1: Create the materialized view without initial data.**

```sql
CREATE MATERIALIZED VIEW department_salary_total AS
SELECT dept_id,
       SUM(salary) AS total_salary
FROM instructor
GROUP BY dept_id
WITH NO DATA;
```

**Step 2: Refresh and query.**

```sql
REFRESH MATERIALIZED VIEW department_salary_total;

SELECT dept_id, total_salary
FROM department_salary_total
ORDER BY dept_id;
```

**Expected result:**

```text
dept_id | total_salary
10       | 137000
20       | 61000
```

**Step 3: Change a base row.**

```sql
UPDATE instructor
SET salary = salary + 1000
WHERE instructor_id = 101;
```

**Step 4: Query before and after refresh.**

```sql
-- Still shows the old total.
SELECT total_salary
FROM department_salary_total
WHERE dept_id = 10;

REFRESH MATERIALIZED VIEW department_salary_total;

-- Shows 138000.
SELECT total_salary
FROM department_salary_total
WHERE dept_id = 10;
```

**Result.** The materialized view saves the query result but does not track every base-table change automatically.

### 9.9 Worked Exercise 8: Enforce access through a view

**Task.** Give the `analyst_role` access to Biology instructor identity and department information, but not salary and not direct access to the base table.

**Step 1: Define the restricted view.**

```sql
CREATE VIEW analyst_faculty AS
SELECT instructor_id, name, dept_id
FROM instructor
WHERE dept_id = 10;
```

**Step 2: Grant view access and remove base-table access.**

```sql
GRANT SELECT ON analyst_faculty TO analyst_role;
REVOKE ALL ON instructor FROM analyst_role;
```

This example assumes that `analyst_role` already exists and that the administrator has the required privileges.

**Step 3: Test the permitted query.**

```sql
SELECT instructor_id, name, dept_id
FROM analyst_faculty
ORDER BY instructor_id;
```

**Expected result:** IDs 101 and 102, with no salary column.

**Step 4: Test the forbidden query.**

```sql
SELECT salary
FROM instructor;
```

**Expected result:** a permission error for the `analyst_role` user. The view alone would not provide this protection if the user retained base-table access.

### 9.10 Common traps

| Trap | Correction |
|---|---|
| Treating `PRIMARY KEY` and `UNIQUE` as identical | A primary key is also non-null and identifies the row. A `UNIQUE` key may permit `NULL` under common DBMS rules. |
| Referencing a parent column that is not unique | A foreign-key target must have a `PRIMARY KEY` or `UNIQUE` constraint. |
| Assuming every `CHECK` rejects `NULL` | Under common SQL semantics, `UNKNOWN` does not reject a row. Add `NOT NULL` or write the null case explicitly. |
| Treating `DEFAULT` as `NOT NULL` | A default supplies an omitted value but does not prevent a later `NULL` or invalid value. |
| Confusing `RESTRICT` with `NO ACTION` | Both reject an invalid parent change, but their checking-time behavior differs. `NO ACTION` may be deferred when the constraint is deferrable. |
| Using `SET NULL` on a mandatory child key | The affected foreign-key columns must allow `NULL`. |
| Assuming `SET DEFAULT` always succeeds | The column needs a default, and the default value must satisfy the foreign key and other constraints. |
| Assuming every DBMS supports deferred checks | PostgreSQL supports deferrable foreign keys. MySQL and SQL Server do not offer the same mechanism. |
| Treating a view as a stored table | An ordinary view stores a query definition, not result rows. |
| Assuming every view is read-only | A common one-table, simple-column view can be updatable. |
| Assuming every one-table view is updatable | Aggregates, grouping, `DISTINCT`, set operations, and other constructs can block automatic updates. |
| Assuming an omitted view column becomes `NULL` | The DBMS uses a default when available and uses `NULL` only when the base column permits it. |
| Assuming `WITH CHECK OPTION` creates updatability | It protects view membership for supported updatable views but cannot make an aggregate view updatable. |
| Claiming that an ordinary view speeds up a query | No speedup is guaranteed. The optimizer may rewrite the query, but the underlying work remains. |
| Treating a view as an audit log | Views do not record access unless the DBMS audit facility is enabled. |
| Forgetting that a materialized view can be stale | A refresh updates the stored result. Choose a refresh policy that fits the workload. |

### 9.11 Revision checklist

Use this checklist for a final self-test.

#### Constraints

- [ ] I can distinguish entity, referential, domain, and user-defined integrity.
- [ ] I can write column-level and table-level `NOT NULL`, `PRIMARY KEY`, `UNIQUE`, `CHECK`, and `FOREIGN KEY` constraints.
- [ ] I can explain why a foreign-key target must be unique.
- [ ] I can state how `CHECK` behaves when an expression evaluates to `NULL`.
- [ ] I can explain the difference between `DEFAULT` and `NOT NULL`.
- [ ] I can name the four main referential actions and their schema requirements.
- [ ] I can distinguish immediate from deferred checking.
- [ ] I can name the constraint types that PostgreSQL can defer.
- [ ] I can explain why deferral does not permit an invalid committed state.

#### Views

- [ ] I can define a view with `CREATE VIEW ... AS ...`.
- [ ] I can explain why an ordinary view is a virtual relation.
- [ ] I can identify direct, indirect, and recursive dependencies.
- [ ] I can expand a view over another view until only base relations remain.
- [ ] I can distinguish an ordinary view from a materialized view.
- [ ] I can state the freshness, storage, and refresh trade-off of a materialized view.
- [ ] I can list the common restrictions on automatically updatable views.
- [ ] I can explain why an aggregate view is normally read-only.
- [ ] I can explain how an insert maps to a base table and what happens to omitted columns.
- [ ] I can explain the purpose of `WITH CHECK OPTION`.
- [ ] I can design column and row restrictions with views.
- [ ] I can explain why base-table privileges must also be controlled.
- [ ] I can explain why an ordinary view does not guarantee query optimization.
- [ ] I can explain why a view does not create an audit trail by itself.

---

## 10. SQL Data Definition and Aggregate Functions

### SQL data definition

SQL Data Definition Language (DDL) defines database objects and their structure. Common DDL statements are:

| Statement | Purpose | Important effect |
|---|---|---|
| `CREATE TABLE` | Creates a base table and defines its columns and constraints | Establishes the stored schema |
| `ALTER TABLE` | Adds, changes, or removes columns and constraints | Changes an existing table |
| `DROP TABLE` | Removes a table definition and its data | Destructive; Oracle normally commits before and after DDL |
| `TRUNCATE TABLE` | Removes all rows while retaining the table definition | Fast in Oracle; DDL and normally commits |
| `CREATE VIEW` | Stores a query as a named virtual relation | Defines a new object in the data dictionary |
| `CREATE OR REPLACE VIEW` | Creates or replaces a compatible view | Avoids dropping and recreating the view |
| `RENAME TABLE` | Changes a table name in supported DBMSs | Must follow the selected DBMS syntax |

The examples in this section use Oracle syntax unless a label states otherwise.

### Creating a table with constraints

```sql
-- Oracle
CREATE TABLE departments (
    department_id   NUMBER(4)
        CONSTRAINT pk_departments PRIMARY KEY,
    department_name VARCHAR2(100)
        CONSTRAINT uq_departments_name UNIQUE NOT NULL
);

CREATE TABLE employees (
    employee_id   NUMBER(6)
        CONSTRAINT pk_employees PRIMARY KEY,
    employee_name VARCHAR2(100) NOT NULL,
    department_id NUMBER(4),
    salary        NUMBER(10, 2),
    hired_on      DATE DEFAULT SYSDATE,
    manager_id    NUMBER(6),
    CONSTRAINT fk_employees_department
        FOREIGN KEY (department_id)
        REFERENCES departments (department_id),
    CONSTRAINT fk_employees_manager
        FOREIGN KEY (manager_id)
        REFERENCES employees (employee_id),
    CONSTRAINT ck_employees_salary
        CHECK (salary IS NULL OR salary >= 0)
);
```

A table stores persistent rows. A view stores a query definition and derives its rows from base tables when queried.

### Altering and removing a table

```sql
-- Oracle
ALTER TABLE employees ADD (email VARCHAR2(120));

ALTER TABLE employees MODIFY (email VARCHAR2(200));

ALTER TABLE employees
    ADD CONSTRAINT uq_employees_email UNIQUE (email);

ALTER TABLE employees
    DROP CONSTRAINT uq_employees_email;

-- Destructive choices
DROP TABLE employees CASCADE CONSTRAINTS;
TRUNCATE TABLE employees;
```

`DROP TABLE` removes the table definition and its data. `TRUNCATE TABLE` removes the rows but retains the definition. In Oracle, both are DDL operations, and a DDL statement commits the current transaction before it runs. Use `DELETE` when the rows must be recoverable through transaction rollback.

### Aggregate functions

An aggregate function accepts zero or more input values from each row and returns one value for a group. A query without `GROUP BY` treats all selected rows as one group.

| Function | Result | NULL treatment |
|---|---|---|
| `COUNT(*)` | Number of rows | Counts every row, including rows with NULLs |
| `COUNT(expression)` | Number of non-NULL values of the expression | Ignores NULLs |
| `SUM(expression)` | Sum of non-NULL numeric values | Ignores NULLs; returns NULL when no non-NULL value exists |
| `AVG(expression)` | Mean of non-NULL numeric values | Ignores NULLs; returns NULL when no non-NULL value exists |
| `MIN(expression)` | Smallest non-NULL value | Ignores NULLs; returns NULL when every input is NULL |
| `MAX(expression)` | Largest non-NULL value | Ignores NULLs; returns NULL when every input is NULL |

```sql
-- Oracle: department-level salary summary
SELECT
    d.department_id,
    d.department_name,
    COUNT(*) AS employee_count,
    COUNT(e.salary) AS employees_with_salary,
    ROUND(AVG(e.salary), 2) AS average_salary,
    SUM(e.salary) AS total_salary,
    MIN(e.salary) AS minimum_salary,
    MAX(e.salary) AS maximum_salary
FROM departments AS d
LEFT JOIN employees AS e
    ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name
ORDER BY d.department_id;
```

The `LEFT JOIN` keeps every department. For a department without employees, `COUNT(*)` returns 1 for the department-side row, while `COUNT(e.salary)` returns 0. The aggregate salary columns return NULL because they have no non-NULL employee salary to aggregate.

### Aggregate functions with `DISTINCT`

`DISTINCT` removes duplicate values before the aggregate function processes them.

```sql
-- Oracle
SELECT COUNT(DISTINCT department_id) AS represented_departments
FROM employees;

SELECT COUNT(DISTINCT salary) AS distinct_salary_values
FROM employees;
```

`COUNT(*)` and `COUNT(column)` can differ in the same query:

```sql
-- Oracle
SELECT COUNT(*) AS rows_total,
       COUNT(salary) AS rows_with_non_null_salary
FROM employees;
```

### Dialect-specific string aggregation

`GROUP_CONCAT` and `DELIMITER` are MySQL or MariaDB client features, not Oracle syntax.

**MySQL or MariaDB:**

```sql
SELECT GROUP_CONCAT(
           employee_name
           ORDER BY employee_name
           SEPARATOR ', '
       ) AS employee_list
FROM employees;
```

**Oracle:**

```sql
SELECT LISTAGG(employee_name, ', ')
           WITHIN GROUP (ORDER BY employee_name) AS employee_list
FROM employees;
```

| Feature | MySQL or MariaDB | Oracle |
|---|---|---|
| Aggregate that joins strings | `GROUP_CONCAT(expression [ORDER BY ...] [SEPARATOR ...])` | `LISTAGG(expression, delimiter) WITHIN GROUP (ORDER BY ...)` |
| Client statement separator | `DELIMITER //` or `DELIMITER $$` | `/` after a PL/SQL block in SQL*Plus or SQLcl |
| Is `DELIMITER` part of SQL grammar? | No. It is a client command | Not applicable |

For example, a MySQL trigger body uses `DELIMITER //` so the client does not split the body at each internal semicolon. An Oracle trigger uses `/` after `END;`. The slash belongs to the SQL client command sequence, not to the PL/SQL source text.

## 11. GROUP BY, HAVING, and WHERE Processing Order

### GROUP BY

`GROUP BY` divides selected rows into groups with the same values in its grouping expressions. The query then evaluates aggregate functions for each group.

```sql
-- Oracle
SELECT department_id,
       COUNT(*) AS employee_count,
       ROUND(AVG(salary), 2) AS average_salary
FROM employees
WHERE salary IS NOT NULL
GROUP BY department_id
HAVING COUNT(*) >= 3
ORDER BY average_salary DESC;
```

For a grouped query, every selected expression must either:

1. appear in the `GROUP BY` list;
2. be built entirely from grouped expressions; or
3. be an aggregate function.

The following query is invalid because `employee_id` is neither grouped nor aggregated.

```sql
-- Invalid in a grouped query
SELECT department_id, employee_id, AVG(salary)
FROM employees
GROUP BY department_id;
```

A valid grouped query uses an aggregate for `employee_id` or groups by both columns.

```sql
-- Oracle
SELECT department_id, employee_id, salary
FROM employees
GROUP BY department_id, employee_id, salary;
```

The second query usually has little value because each group contains at most one row for that combination. It becomes useful when grouping expressions differ from selected detail columns.

### WHERE versus HAVING

| Property | `WHERE` | `HAVING` |
|---|---|---|
| Filters | Individual rows before grouping | Complete groups after grouping |
| Typical condition | Column comparison, pattern match, date range | Aggregate result or grouped value |
| Can use aggregate functions | No | Yes |
| Can use a `SELECT` alias | No in portable SQL | No in portable SQL; Oracle supports some aliases in `HAVING` |
| Affects groups | Can remove all rows from a group before it forms | Removes a group after its aggregates have been calculated |

```sql
-- Oracle
SELECT department_id,
       COUNT(*) AS employee_count,
       ROUND(AVG(salary), 2) AS average_salary
FROM employees
WHERE salary BETWEEN 5000 AND 100000
GROUP BY department_id
HAVING AVG(salary) > 70000
ORDER BY average_salary;
```

The `WHERE` clause removes low and high salaries before department groups form. The `HAVING` clause then removes departments whose remaining employees do not have an average salary above 70,000.

### Logical processing order

For a non-distinct, non-set-operation query, use this logical order:

1. `FROM` and joins produce candidate rows.
2. `WHERE` filters candidate rows.
3. `GROUP BY` forms groups.
4. `HAVING` filters groups.
5. `SELECT` computes output expressions.
6. Window functions are evaluated for the rows that remain after grouping and `HAVING`.
7. `DISTINCT` removes duplicate output rows.
8. `ORDER BY` sorts the result.

A physical query optimizer may rearrange these operations. Logical order still determines which clauses can refer to which expressions.

### Common traps

- `WHERE AVG(salary) > 50000` is invalid because the aggregate has not been calculated when `WHERE` filters rows.
- `HAVING salary > 50000` is invalid in a grouped query unless `salary` is also a grouping expression.
- `WHERE department_id = 10` filters rows; `HAVING department_id = 10` filters groups after grouping.
- Filtering on `salary > 0` removes NULL salaries because NULL comparisons do not evaluate to TRUE. Use `salary IS NULL OR salary > 0` when NULL must remain.
- `HAVING COUNT(*) > 0` does not repair an empty source table because no group exists to pass the test.
- `GROUP BY department_id` groups by the ID, not the department name. Include names in the grouping list when the name is selected.
- An `ORDER BY` alias is more widely supported than a `HAVING` alias. Repeat the expression for portable `HAVING` clauses.
- `WHERE` does not normally improve performance merely because it appears first. The optimizer chooses an access plan and may push predicates into the execution plan when it is safe.

## 12. Window Functions, Ranking, and Framing

### 12.1 Purpose

A window function computes an aggregate or rank over a set of related rows while still returning one result row per input row. It answers questions such as:

- What is each student's rank within a department?
- How does this month's sales compare with the previous month?
- What is the moving average around each date?
- What is each account's balance after every transaction?

Ordinary aggregation collapses rows into groups. A window function keeps the row context.

```sql
-- Oracle
SELECT employee_id,
       department_id,
       salary,
       RANK() OVER (
           PARTITION BY department_id
           ORDER BY salary DESC
       ) AS salary_rank
FROM employees;
```

The `OVER` clause defines the **window**. `PARTITION BY` divides rows into independent windows. `ORDER BY` establishes the order used by ranking, running totals, and many frame calculations.

### 12.2 Logical processing of window functions

For a query that uses window functions, the useful logical order is:

1. `FROM` and joins produce candidate rows.
2. `WHERE` filters rows.
3. `GROUP BY` forms groups.
4. `HAVING` filters groups.
5. `SELECT` computes non-window expressions.
6. Window functions operate over the remaining rows.
7. `DISTINCT` removes duplicate output rows.
8. `ORDER BY` sorts the final result.

A window function may reference columns that are not in the `GROUP BY` list when its window is defined over the grouped rows. SQL dialects differ here, so state the dialect when presenting such a query.

### 12.3 Anatomy of an `OVER` clause

```text
function(...) OVER (
    [PARTITION BY expression_list]
    [ORDER BY sort_expression_list]
    [ROWS | RANGE | GROUPS frame_clause]
)
```

| Clause | Function |
|---|---|
| `PARTITION BY` | Restarts the calculation for each distinct partition value |
| `ORDER BY` | Defines the window's row order for ranking and running calculations |
| `ROWS` | Frames by a physical number of rows |
| `RANGE` | Frames by logical distance from the current row's `ORDER BY` value |
| `GROUPS` | Frames by peer-group count; support varies by DBMS |

Without `PARTITION BY`, the entire result is one partition. Without `ORDER BY`, order-sensitive functions have no defined ranking order.

### 12.4 Ranking functions

Assume the relation `student_grades(student_id, department_id, gpa)` contains:

| student_id | department_id | gpa |
|---:|---|---:|
| 101 | CSE | 3.90 |
| 102 | CSE | 3.90 |
| 103 | CSE | 3.50 |
| 104 | ECE | 3.80 |
| 105 | ECE | 3.60 |

#### `RANK()`

`RANK()` assigns the same rank to tied rows and leaves gaps after a tie.

```sql
-- Oracle
SELECT student_id,
       department_id,
       gpa,
       RANK() OVER (
           PARTITION BY department_id
           ORDER BY gpa DESC
       ) AS dept_rank
FROM student_grades
ORDER BY department_id, dept_rank;
```

| student_id | department_id | gpa | dept_rank |
|---:|---|---:|---:|
| 101 | CSE | 3.90 | 1 |
| 102 | CSE | 3.90 | 1 |
| 103 | CSE | 3.50 | 3 |
| 104 | ECE | 3.80 | 1 |
| 105 | ECE | 3.60 | 2 |

The CSE partition has ranks `1, 1, 3`. `DENSE_RANK()` would produce `1, 1, 2`.

#### `DENSE_RANK()`

`DENSE_RANK()` gives tied rows the same rank and does not leave gaps.

```sql
SELECT student_id,
       DENSE_RANK() OVER (ORDER BY gpa DESC) AS dense_rank
FROM student_grades;
```

#### `ROW_NUMBER()`

`ROW_NUMBER()` assigns consecutive numbers. Ties have no required order unless the `ORDER BY` includes a unique tie-breaker.

```sql
-- Deterministic tie-breaker
SELECT student_id,
       ROW_NUMBER() OVER (
           ORDER BY gpa DESC, student_id ASC
       ) AS row_num
FROM student_grades;
```

Without the unique tie-breaker, two tied rows may receive different numbers in either order across executions.

#### `NTILE(n)`

`NTILE(n)` divides an ordered partition into `n` groups. With 8 rows and `NTILE(4)`, the first two buckets receive two rows each and the last two receive two rows each when the DBMS distributes the remainder evenly.

```sql
SELECT student_id,
       gpa,
       NTILE(4) OVER (ORDER BY gpa DESC) AS quartile
FROM student_grades;
```

The result identifies quartiles, not exact percentiles.

#### `PERCENT_RANK()`

For a row at zero-based position `p` in a partition of `n` rows:

\[
PERCENT\_RANK = \frac{p}{n - 1}
\]

It returns a value from `0` to `1`. Tied rows normally receive the same percent rank.

#### `CUME_DIST()`

`CUME_DIST()` gives the fraction of rows whose ordering value is less than or equal to the current row's value.

| Concept | Formula or rule |
|---|---|
| `PERCENT_RANK` | `(rank - 1) / (partition_rows - 1)` |
| `CUME_DIST` | `rows_at_or_below_current / partition_rows` |

Both functions use the window's ordering and partition.

### 12.5 Ranking without window syntax

The source also shows a correlated subquery form:

```sql
SELECT ID,
       (1 + (
           SELECT COUNT(*)
           FROM student_grades B
           WHERE B.GPA > A.GPA
       )) AS s_rank
FROM student_grades A
ORDER BY s_rank;
```

This computes a competition rank with ties. It performs more work than the window form. Use it to explain the idea, not as the preferred implementation when the DBMS supports window functions.

### 12.6 Running and moving aggregates

A running total accumulates values from the start of the frame through the current row.

```sql
-- Oracle
SELECT transaction_date,
       account_id,
       amount,
       SUM(amount) OVER (
           PARTITION BY account_id
           ORDER BY transaction_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_balance
FROM transactions
ORDER BY account_id, transaction_date;
```

A centered moving average for the current day and its neighbours:

```sql
SELECT transaction_date,
       AVG(amount) OVER (
           ORDER BY transaction_date
           ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
       ) AS moving_average
FROM daily_sales;
```

### 12.7 Frame units

#### `ROWS`

`ROWS` counts physical rows.

```sql
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
```

This includes every row from the partition start through the current row.

```sql
ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
```

This includes the previous row, current row, and next row.

#### `RANGE`

`RANGE` uses the `ORDER BY` value rather than row count.

```sql
RANGE BETWEEN INTERVAL '10' DAY PRECEDING
          AND CURRENT ROW
```

This includes rows whose ordering value lies within the ten-day interval before the current value.

| Frame | Rows included |
|---|---|
| `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` | Partition start through current row |
| `ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING` | Current row through partition end |
| `ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING` | One row before, current row, one row after |
| `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` | All peers whose order value is at or before the current peer group |
| `RANGE BETWEEN 10 PRECEDING AND CURRENT ROW` | Numeric or date order values within the stated distance before current value |

`ROWS` is appropriate when each physical row is a distinct event. `RANGE` is useful when several rows share an ordering value and should be treated as peers.

### 12.8 `LAG` and `LEAD`

`LAG(value, offset, default)` reads a value from an earlier row. `LEAD` reads from a later row.

```sql
-- Oracle
SELECT transaction_date,
       amount,
       LAG(amount, 1, 0) OVER (
           PARTITION BY account_id
           ORDER BY transaction_date
       ) AS previous_amount,
       LEAD(amount, 1, 0) OVER (
           PARTITION BY account_id
           ORDER BY transaction_date
       ) AS next_amount
FROM transactions;
```

`LAG` and `LEAD` make period-over-period comparisons easier. The order must be deterministic if duplicate timestamps can occur.

### 12.9 Window-function comparison

| Function | Same value for ties? | Gaps after ties? | Typical use |
|---|---|---|---|
| `ROW_NUMBER()` | No guaranteed shared value | No | Unique sequence |
| `RANK()` | Yes | Yes | Competition ranking |
| `DENSE_RANK()` | Yes | No | Rank without gaps |
| `NTILE(n)` | Bucket assignment | Not applicable | Quartiles and deciles |
| `PERCENT_RANK()` | Usually yes | Not applicable | Relative position |
| `CUME_DIST()` | Yes | Not applicable | Cumulative distribution |

### 12.10 Worked Exercise 1: Rank employees within departments

**Relation:**

| employee_id | department_id | salary |
|---:|---|---:|
| 1 | CSE | 70000 |
| 2 | CSE | 90000 |
| 3 | CSE | 70000 |
| 4 | ECE | 60000 |
| 5 | ECE | 80000 |

**Query:**

```sql
SELECT employee_id,
       department_id,
       salary,
       RANK() OVER (
           PARTITION BY department_id
           ORDER BY salary DESC
       ) AS salary_rank,
       DENSE_RANK() OVER (
           PARTITION BY department_id
           ORDER BY salary DESC
       ) AS dense_salary_rank
FROM employees;
```

**Result:**

| employee_id | department_id | salary | salary_rank | dense_salary_rank |
|---:|---|---:|---:|---:|
| 2 | CSE | 90000 | 1 | 1 |
| 1 | CSE | 70000 | 2 | 2 |
| 3 | CSE | 70000 | 2 | 2 |
| 5 | ECE | 80000 | 1 | 1 |
| 4 | ECE | 60000 | 2 | 2 |

### 12.11 Worked Exercise 2: Calculate a running account balance

**Transactions:**

| account_id | transaction_time | amount |
|---:|---|---:|
| 10 | 09:00 | 100 |
| 10 | 10:00 | -30 |
| 10 | 11:00 | 50 |
| 20 | 09:30 | 200 |

**Query:**

```sql
SELECT account_id,
       transaction_time,
       amount,
       SUM(amount) OVER (
           PARTITION BY account_id
           ORDER BY transaction_time
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS balance
FROM transactions;
```

**Result:**

| account_id | transaction_time | amount | balance |
|---:|---|---:|---:|
| 10 | 09:00 | 100 | 100 |
| 10 | 10:00 | -30 | 70 |
| 10 | 11:00 | 50 | 120 |
| 20 | 09:30 | 200 | 200 |

### 12.12 Common window-function traps

1. **Using `RANK()` and expecting consecutive ties.** Use `DENSE_RANK()` when gaps must disappear.
2. **Omitting a unique tie-breaker with `ROW_NUMBER()`.** Add a deterministic final ordering column.
3. **Forgetting `PARTITION BY`.** The calculation then spans the entire result set.
4. **Using `ROWS` for value-based date intervals.** Use `RANGE` when the interval depends on the ordering value.
5. **Filtering before ranking when the business question expects otherwise.** `WHERE` runs before window evaluation.
6. **Calling `NTILE(4)` exact quartiles.** It creates buckets whose membership depends on row count.
7. **Ignoring the default frame.** The default frame varies with the presence of `ORDER BY`; specify a frame when the boundary matters.
8. **Assuming window functions group rows.** They do not reduce the number of output rows.

### 12.13 Revision checklist

- [ ] I can distinguish ordinary aggregation from window aggregation.
- [ ] I can use `PARTITION BY`, `ORDER BY`, and a frame together.
- [ ] I can choose `ROW_NUMBER`, `RANK`, or `DENSE_RANK` from the tie requirement.
- [ ] I can explain why `PERCENT_RANK` and `CUME_DIST` differ.
- [ ] I can build a running total and a centered moving average.
- [ ] I can distinguish a `ROWS` frame from a `RANGE` frame.
- [ ] I know why `LAG` and `LEAD` need a deterministic order.

## 13. NULL Values and Three-Valued Logic

### 13.1 Meaning of NULL

SQL `NULL` represents an unknown value or the absence of a stored value. It does not represent `0`, an empty string, `False`, or the literal text `NULL`.

Use NULL when the schema cannot distinguish:

- an unknown value;
- a value not applicable to a particular tuple;
- a missing value; or
- a pending state that the business permits.

The meaning depends on the domain and the application's rules. The database enforces declared nullability; application code usually interprets why a value is missing.

### 13.2 NULL in comparisons

A comparison involving NULL produces `UNKNOWN` unless the predicate explicitly tests for null.

```sql
SELECT name
FROM instructor
WHERE salary = NULL;       -- Never matches a row
```

Use:

```sql
SELECT name
FROM instructor
WHERE salary IS NULL;
```

Similarly:

```sql
SELECT name
FROM instructor
WHERE salary IS NOT NULL;
```

Do not write `<> NULL` to find non-null values.

### 13.3 NULL in arithmetic

An arithmetic expression with a NULL operand returns NULL.

```sql
SELECT 5 + NULL;    -- NULL
SELECT 10 * NULL;   -- NULL
```

This rule affects calculations, aggregates, checks, and default expressions. A non-null default can still fail a later constraint if its value is outside the allowed domain.

### 13.4 Three-valued logic

SQL conditions can evaluate to `TRUE`, `FALSE`, or `UNKNOWN`.

#### AND

| Left | Right | Result |
|---|---|---|
| TRUE | TRUE | TRUE |
| TRUE | FALSE | FALSE |
| TRUE | UNKNOWN | UNKNOWN |
| FALSE | TRUE | FALSE |
| FALSE | FALSE | FALSE |
| FALSE | UNKNOWN | FALSE |
| UNKNOWN | TRUE | UNKNOWN |
| UNKNOWN | FALSE | FALSE |
| UNKNOWN | UNKNOWN | UNKNOWN |

The rule for `FALSE AND UNKNOWN` is `FALSE` because one false conjunct is enough to make the conjunction false.

#### OR

| Left | Right | Result |
|---|---|---|
| TRUE | TRUE | TRUE |
| TRUE | FALSE | TRUE |
| TRUE | UNKNOWN | TRUE |
| FALSE | TRUE | TRUE |
| FALSE | FALSE | FALSE |
| FALSE | UNKNOWN | UNKNOWN |
| UNKNOWN | TRUE | TRUE |
| UNKNOWN | FALSE | UNKNOWN |
| UNKNOWN | UNKNOWN | UNKNOWN |

#### NOT

| Input | `NOT` result |
|---|---|
| TRUE | FALSE |
| FALSE | TRUE |
| UNKNOWN | UNKNOWN |

### 13.5 WHERE treats UNKNOWN as not selected

A `WHERE` clause keeps a row only when its predicate evaluates to `TRUE`. `FALSE` and `UNKNOWN` both exclude the row.

```sql
-- Keeps rows where salary is known and greater than 50000
SELECT name
FROM instructor
WHERE salary > 50000;
```

A NULL salary does not pass this predicate because `NULL > 50000` is UNKNOWN.

### 13.6 CHECK constraints and NULL

A `CHECK` constraint rejects a row when its predicate evaluates to `FALSE`. A predicate that evaluates to `UNKNOWN` does not reject the row under the SQL standard.

```sql
-- Allows NULL, but rejects a non-null age outside 18..65
CHECK (age IS NULL OR age BETWEEN 18 AND 65)
```

If age must have a value, use both constraints:

```sql
age SMALLINT NOT NULL
    CHECK (age BETWEEN 18 AND 65)
```

The first expression permits NULL. The second does not. This distinction is a common exam trap.

### 13.7 NULL in aggregate functions

| Expression | NULL behavior |
|---|---|
| `COUNT(*)` | Counts every row, including rows with NULLs |
| `COUNT(column)` | Counts only non-NULL values of `column` |
| `SUM(column)` | Ignores NULLs; returns NULL if no non-NULL input exists |
| `AVG(column)` | Ignores NULLs; returns NULL if no non-NULL input exists |
| `MIN(column)` / `MAX(column)` | Ignore NULLs; return NULL if every input is NULL |

Example:

| employee_id | salary |
|---:|---:|
| 1 | 50000 |
| 2 | NULL |
| 3 | 70000 |

```sql
SELECT COUNT(*) AS rows_total,
       COUNT(salary) AS salary_values,
       SUM(salary) AS salary_sum,
       AVG(salary) AS salary_average
FROM employees;
```

**Result:**

| rows_total | salary_values | salary_sum | salary_average |
|---:|---:|---:|---:|
| 3 | 2 | 120000 | 60000 |

### 13.8 NULL and grouping

`GROUP BY` treats NULLs as equal for grouping purposes. Rows with NULL in the grouping expression form one group.

```sql
SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;
```

A missing department identifier is one group. It is not automatically merged with an existing department.

### 13.9 NULL in unique constraints

Most DBMSs permit multiple NULLs in a column with a `UNIQUE` constraint because two unknown values cannot be proven equal. Products differ in optional extensions, so state the product rule when the distinction matters.

```sql
email VARCHAR2(200) UNIQUE
```

Two rows may both contain a NULL email in common implementations. A non-null email cannot duplicate another non-null email.

### 13.10 NULL in joins

`NULL = NULL` evaluates to UNKNOWN, not TRUE. Therefore, standard equi-joins do not match rows whose join values are NULL.

```sql
-- Does not match two NULL department identifiers
SELECT *
FROM employees e
JOIN departments d
  ON e.department_id = d.department_id;
```

Use an explicit null-safe equality expression when the DBMS provides one and the business rule requires NULL-to-NULL matching.

### 13.11 NULL and `NOT IN`

A common trap is:

```sql
SELECT name
FROM instructor
WHERE department_id NOT IN (
    SELECT department_id
    FROM department
);
```

If the subquery returns any NULL, the result can be empty because `x NOT IN` a set containing NULL cannot become true for a non-null `x`.

Safer alternatives include:

```sql
SELECT name
FROM instructor
WHERE NOT EXISTS (
    SELECT 1
    FROM department d
    WHERE d.department_id = instructor.department_id
);
```

`NOT EXISTS` selects correlated rows by existence and avoids the `NOT IN` NULL trap.

### 13.12 NULL in ORDER BY and GROUP BY

The ordering of NULLs is product-dependent unless the DBMS supports explicit null ordering.

```sql
-- Oracle-style explicit ordering
SELECT name, salary
FROM instructor
ORDER BY salary DESC NULLS LAST;
```

Some products use `NULLS FIRST` or `NULLS LAST`; others require a vendor-specific switch. State the rule instead of presenting one dialect as universal.

### 13.13 NULL and boolean columns

A boolean column should normally declare whether NULL is allowed. A nullable boolean creates a third state and complicates predicates.

```sql
active BOOLEAN NOT NULL
```

is easier to query than:

```sql
active BOOLEAN
```

because the latter permits UNKNOWN.

### 13.14 Worked Exercise 1: Predict filter results

**Rows:**

| id | salary | bonus |
|---:|---:|---:|
| 1 | 50000 | NULL |
| 2 | NULL | 10000 |
| 3 | 70000 | 5000 |

**Query:**

```sql
SELECT id
FROM employees
WHERE salary > 60000 OR bonus = 10000;
```

**Result:** row `2` only.

- Row 1: `50000 > 60000` is FALSE; `NULL = 10000` is UNKNOWN; `FALSE OR UNKNOWN` is UNKNOWN.
- Row 2: `NULL > 60000` is UNKNOWN; `10000 = 10000` is TRUE; `UNKNOWN OR TRUE` is TRUE.
- Row 3: both comparisons are TRUE.

### 13.15 Worked Exercise 2: Write two different age constraints

**Requirement A:** age is required and must be from 18 through 65.

```sql
age SMALLINT NOT NULL
    CHECK (age BETWEEN 18 AND 65)
```

**Requirement B:** age may be unknown, but any known age must be from 18 through 65.

```sql
age SMALLINT
    CHECK (age IS NULL OR age BETWEEN 18 AND 65)
```

### 13.16 Worked Exercise 3: Diagnose an empty `NOT IN` query

```sql
SELECT name
FROM instructor
WHERE department_id NOT IN (
    SELECT department_id
    FROM department
);
```

Suppose the subquery returns `{10, 20, NULL}`. For an outer `department_id = 30`, the predicates compare against 10, 20, and NULL. The first two produce FALSE, while the NULL comparison produces UNKNOWN. `NOT IN` therefore cannot yield TRUE, and the outer row is excluded.

Replace the query with `NOT EXISTS` or add `WHERE department_id IS NOT NULL` to the subquery after proving that its null rows should not participate.

### 13.17 Common NULL traps

1. **Using `= NULL`.** Use `IS NULL` or `IS NOT NULL`.
2. **Assuming arithmetic with NULL returns zero.** It returns NULL.
3. **Treating UNKNOWN as FALSE in every clause.** `WHERE` excludes UNKNOWN, but `CHECK` permits a check result of UNKNOWN under the SQL standard.
4. **Using `NOT IN` with a nullable subquery.** Prefer `NOT EXISTS` or remove nulls deliberately.
5. **Assuming NULL never equals NULL.** SQL comparison treats it as UNKNOWN.
6. **Ignoring NULL in `COUNT`.** `COUNT(*)` and `COUNT(column)` count different row sets.
7. **Confusing a missing value with zero or an empty string.** Use a consistent domain and null policy.
8. **Assuming NULL ordering is universal.** State the DBMS rule or use explicit null ordering when supported.

### 13.18 Revision checklist

- [ ] I can explain why SQL uses three-valued logic.
- [ ] I can reproduce the AND and OR truth tables.
- [ ] I know why `WHERE` excludes UNKNOWN.
- [ ] I can distinguish a nullable range check from a required range check.
- [ ] I know how NULL affects arithmetic, aggregates, grouping, joins, and uniqueness.
- [ ] I can explain the `NOT IN` null trap.
- [ ] I can use `IS NULL` and `IS NOT NULL` correctly.

## 14. Nested Subqueries

### 14.1 Meaning

A **subquery** is a `SELECT` query nested inside another SQL statement. A **query expression** may occur in the `FROM`, `WHERE`, or `SELECT` clause of an outer query.

```sql
SELECT department_name
FROM department
WHERE department_id IN (
    SELECT department_id
    FROM instructor
);
```

The inner query produces a set that the outer query uses.

### 14.2 Subquery forms

| Form | Result shape | Typical use |
|---|---|---|
| Scalar | One row and one column | Compare one value with one computed value |
| Row | One row and several columns | Compare a tuple with another tuple |
| Table | Several rows and columns | Use as a derived table in `FROM` |
| Set-returning | A set of rows | Test membership with `IN`, `EXISTS`, `ANY`, or `ALL` |
| Correlated | Depends on the outer row | Find related rows or compare each outer row |

### 14.3 Scalar subquery

A scalar subquery returns one value.

```sql
SELECT name,
       (SELECT AVG(salary)
        FROM instructor) AS average_salary
FROM instructor;
```

The subquery is evaluated once in many execution plans, although the optimizer may rewrite it.

A scalar subquery that returns more than one row causes an error in systems that require one row.

### 14.4 Row-value subquery

```sql
SELECT name, salary, department_id
FROM instructor
WHERE (salary, department_id) = (
    SELECT salary, department_id
    FROM instructor
    WHERE name = 'Watson'
);
```

Row comparison support and semantics vary by DBMS. Keep the compared columns in matching order.

### 14.5 Derived table in FROM

```sql
SELECT department_id, average_salary
FROM (
    SELECT department_id, AVG(salary) AS average_salary
    FROM instructor
    GROUP BY department_id
) AS department_summary
WHERE average_salary > 42000;
```

A derived table needs an alias in most SQL systems. Its select list behaves like a relation schema for the outer query.

### 14.6 Correlated subquery

A correlated subquery refers to a column from the outer query.

```sql
SELECT name, salary
FROM instructor i
WHERE salary > (
    SELECT AVG(salary)
    FROM instructor
)
AND EXISTS (
    SELECT 1
    FROM teaches t
    WHERE t.ID = i.ID
      AND t.semester = 'Spring'
      AND t.year = 2018
);
```

The inner query depends on the current outer row. The DBMS may evaluate it repeatedly, once per outer row, or transform it into a more efficient join.

### 14.7 Non-correlated subquery

A non-correlated subquery does not refer to the outer row.

```sql
SELECT name
FROM instructor
WHERE salary > (
    SELECT AVG(salary)
    FROM instructor
);
```

Its result can serve as a scalar threshold for every outer row.

### 14.8 `IN`, `EXISTS`, `ANY`, and `ALL`

#### `IN`

```sql
SELECT name
FROM instructor
WHERE department_id IN (
    SELECT department_id
    FROM department
    WHERE budget > 100000
);
```

`IN` tests whether the outer value equals a value in the subquery result. It returns UNKNOWN when it finds no equal value and the comparison with NULL is UNKNOWN.

#### `EXISTS`

```sql
SELECT name
FROM instructor i
WHERE EXISTS (
    SELECT 1
    FROM teaches t
    WHERE t.ID = i.ID
);
```

`EXISTS` is true when the subquery returns at least one row. It does not compare the selected value.

#### `ANY` and `ALL`

```sql
SELECT name
FROM instructor
WHERE salary > ANY (
    SELECT salary
    FROM instructor
    WHERE department_id = 'Physics'
);
```

This is true when the outer salary exceeds at least one salary in the set.

```sql
SELECT name
FROM instructor
WHERE salary > ALL (
    SELECT salary
    FROM instructor
    WHERE department_id = 'Physics'
);
```

This is true when the outer salary exceeds every salary in the set. If the set is empty, the result follows the DBMS's SQL-standard `ALL` semantics rather than an intuitive “no comparison exists” rule.

### 14.9 `IN` versus `EXISTS`

| Question | `IN` | `EXISTS` |
|---|---|---|
| Does the outer value occur in the set? | Yes | No direct equality test |
| Can the subquery return several columns? | Normally one column | Column list is irrelevant when using `SELECT 1` |
| NULL pitfall | `NOT IN` can behave unexpectedly with NULL | `NOT EXISTS` avoids the `NOT IN` trap |
| Good fit for | Small membership sets | Existence checks and correlated child rows |

### 14.10 Nested subquery in SELECT, FROM, and WHERE

```sql
-- SELECT: scalar subquery
SELECT name,
       (SELECT COUNT(*)
        FROM teaches t
        WHERE t.ID = instructor.ID) AS courses_taught
FROM instructor;

-- FROM: derived table
SELECT d.department_name, s.total_salary
FROM department d
JOIN (
    SELECT department_id, SUM(salary) AS total_salary
    FROM instructor
    GROUP BY department_id
) s ON s.department_id = d.department_id;

-- WHERE: set-membership subquery
SELECT department_name
FROM department d
WHERE EXISTS (
    SELECT 1
    FROM instructor i
    WHERE i.department_id = d.department_id
);
```

### 14.11 Common subquery errors

1. **Using an aggregate without grouping.** Every selected non-aggregate column must be valid under the grouped query rules.
2. **Forgetting correlation.** If the subquery should use the outer row, add an explicit equality predicate.
3. **Using `NOT IN` with nullable values.** Prefer `NOT EXISTS` unless nulls have been handled deliberately.
4. **Expecting a scalar subquery to return many rows.** A scalar subquery must return at most one row.
5. **Confusing `ANY` with `ALL`.** `ANY` needs one true comparison; `ALL` needs every comparison to be true.
6. **Assuming correlated subqueries always execute once per row.** The optimizer may transform the query.
7. **Omitting a derived-table alias.** Most SQL systems require one.
8. **Using an outer alias that shadows a subquery alias.** Qualify columns when the scope is unclear.

### 14.12 Worked Exercise 1: Find instructors above the average salary

```sql
SELECT name, salary
FROM instructor
WHERE salary > (
    SELECT AVG(salary)
    FROM instructor
);
```

The subquery is non-correlated. It returns one scalar value, which is compared with each outer salary.

### 14.13 Worked Exercise 2: Find departments with no instructor

```sql
SELECT d.department_name
FROM department d
WHERE NOT EXISTS (
    SELECT 1
    FROM instructor i
    WHERE i.department_id = d.department_id
);
```

For each department, the subquery asks whether any instructor references it. `NOT EXISTS` keeps only departments with no matching instructor.

### 14.14 Worked Exercise 3: Find instructors who teach in Spring 2018

```sql
SELECT DISTINCT i.name
FROM instructor i
WHERE EXISTS (
    SELECT 1
    FROM teaches t
    WHERE t.ID = i.ID
      AND t.semester = 'Spring'
      AND t.year = 2018
);
```

`DISTINCT` removes duplicate instructor names if an instructor teaches several qualifying courses.

### 14.15 Worked Exercise 4: Compare a row pair

```sql
SELECT name
FROM instructor
WHERE (salary, department_id) > (
    SELECT salary, department_id
    FROM instructor
    WHERE name = 'Smith'
);
```

Row comparison follows the DBMS's comparison rules. State the dialect and do not assume that this form is supported everywhere.

### 14.16 Exam exercises

**Exercise 1:** Rewrite `department_id NOT IN (SELECT department_id FROM instructor)` without `NOT IN`. Use `NOT EXISTS` with a correlated equality predicate.

**Exercise 2:** Explain why a scalar subquery that returns two rows is invalid. A scalar expression must produce one value.

**Exercise 3:** Give a query that finds instructors whose salary exceeds at least one Physics instructor. Use `> ANY`.

**Exercise 4:** Give a query that finds instructors whose salary exceeds every Physics instructor. Use `> ALL`.

**Exercise 5:** Classify each subquery as scalar, row, derived table, or set-returning:

```sql
(SELECT AVG(salary) FROM instructor)
(SELECT COUNT(*) FROM instructor)
```

Both examples return scalar values in this context. A set-returning subquery becomes a scalar only under a stated single-row guarantee.

### 14.17 Revision checklist

- [ ] I can place a subquery in `FROM`, `WHERE`, and `SELECT`.
- [ ] I can distinguish scalar, row, derived-table, and set-returning forms.
- [ ] I can identify a correlated subquery.
- [ ] I can use `IN` and `EXISTS` for membership and existence.
- [ ] I can distinguish `ANY` from `ALL`.
- [ ] I can avoid the `NOT IN` NULL trap.
- [ ] I know when a scalar subquery is invalid.

---

## 15. PL/SQL Blocks and Stored Procedures

### 15.1 What PL/SQL adds to SQL

PL/SQL is Oracle's procedural extension of SQL. It combines SQL statements with variables, conditional logic, loops, cursors, and exception handling inside a block.

| SQL capability | PL/SQL addition |
|---|---|
| One declarative statement per submission | Multiple statements in one block |
| No local variables | Typed variables, constants, records, and collections |
| Limited procedural control flow | `IF`, loops, `CASE`, and procedures |
| Client-side error handling | Local exception handlers |
| Repeated query text in clients | Stored procedures, functions, packages, and triggers |

PL/SQL does not replace SQL. A data-changing statement inside PL/SQL remains subject to the same table definitions, constraints, transactions, and concurrency rules as the same statement executed directly.

### 15.2 Anonymous block structure

```sql
DECLARE
    -- variable declarations
    v_salary NUMBER(10, 2);
    v_count  INTEGER := 0;
BEGIN
    -- executable statements
    SELECT salary
      INTO v_salary
      FROM employees
     WHERE employee_id = 101;

    IF v_salary >= 50000 THEN
        v_count := v_count + 1;
    ELSE
        v_count := 0;
    END IF;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        v_count := -1;
END;
/
```

The four optional parts are:

1. `DECLARE`: variables, constants, cursors, and exceptions.
2. `BEGIN`: executable statements.
3. `EXCEPTION`: local handlers for runtime errors.
4. `END`: terminates the block.

In SQL*Plus and SQLcl, `/` runs the preceding PL/SQL block. The slash is a client command, not part of PL/SQL source.

### 15.3 Variables and constants

```sql
DECLARE
    v_employee_id employees.employee_id%TYPE;
    v_total_salary NUMBER(12, 2) := 0;
    c_tax_rate CONSTANT NUMBER(5, 4) := 0.0825;
    v_status VARCHAR2(20);
BEGIN
    v_employee_id := 101;
    v_status := 'ACTIVE';
END;
/
```

| Feature | Purpose |
|---|---|
| `%TYPE` | Gives a variable the datatype of a table column or another variable |
| `%ROWTYPE` | Gives a record the structure of a table or cursor row |
| `CONSTANT` | Makes a value immutable after initialization |
| `:name` | Marks a bind or substitution variable in SQL statements and parameters |

Using `%TYPE` reduces type mismatch when a table definition changes.

### 15.4 `SELECT INTO`

`SELECT INTO` stores query results in scalar variables.

```sql
DECLARE
    v_name employees.employee_name%TYPE;
    v_salary employees.salary%TYPE;
BEGIN
    SELECT employee_name, salary
      INTO v_name, v_salary
      FROM employees
     WHERE employee_id = 101;
END;
/
```

If the query returns no row, `NO_DATA_FOUND` is raised. If it returns more than one row, `TOO_MANY_ROWS` is raised.

### 15.5 Conditional control

```sql
DECLARE
    v_balance NUMBER(12, 2);
BEGIN
    SELECT balance
      INTO v_balance
      FROM accounts
     WHERE account_id = 10;

    IF v_balance < 0 THEN
        INSERT INTO overdraft_notice(account_id, message)
        VALUES (10, 'Negative balance');
    ELSIF v_balance = 0 THEN
        INSERT INTO overdraft_notice(account_id, message)
        VALUES (10, 'Zero balance');
    ELSE
        NULL;
    END IF;
END;
/
```

`CASE` provides an alternative form:

```sql
DECLARE
    v_grade VARCHAR2(2);
BEGIN
    v_grade := CASE
        WHEN v_score >= 90 THEN 'A'
        WHEN v_score >= 75 THEN 'B'
        WHEN v_score >= 60 THEN 'C'
        ELSE 'F'
    END;
END;
/
```

### 15.6 Iterative control

```sql
DECLARE
    v_total NUMBER := 0;
BEGIN
    FOR i IN 1 .. 10 LOOP
        v_total := v_total + i;
    END LOOP;

    WHILE v_total < 100 LOOP
        v_total := v_total + 10;
    END LOOP;
END;
/
```

| Loop | Use |
|---|---|
| Numeric `FOR` | Fixed or known numeric range |
| `WHILE` | Repeat while a condition remains true |
| `LOOP ... EXIT` | General loop with explicit exit |
| Cursor `FOR` | Process every row returned by a cursor |
| Bulk `FORALL` | Apply one DML statement to a collection of values |

### 15.7 Exception handling

```sql
DECLARE
    v_salary employees.salary%TYPE;
BEGIN
    SELECT salary
      INTO v_salary
      FROM employees
     WHERE employee_id = 101;

    DBMS_OUTPUT.PUT_LINE('Salary: ' || v_salary);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('Employee not found');
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Unexpected error: ' || SQLERRM);
        RAISE;
END;
/
```

`WHEN OTHERS` catches all exceptions not handled above. It should not silently hide an error. If it does not re-raise, the procedure may report success even though work failed.

| Exception | Typical cause |
|---|---|
| `NO_DATA_FOUND` | `SELECT INTO` returned no rows |
| `TOO_MANY_ROWS` | `SELECT INTO` returned more than one row |
| `DUP_VAL_ON_INDEX` | Unique or primary-key constraint failed |
| `VALUE_ERROR` | Invalid conversion or value |
| `INVALID_NUMBER` | Character data could not convert to a number |
| `LOGIN_DENIED` | Database authentication failed |

### 15.8 Transaction control inside PL/SQL

A stored procedure can execute `COMMIT` or `ROLLBACK` when the procedure is designed for that responsibility. Many application architectures keep transaction control in the caller so one business transaction can call several procedures.

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
    p_from_account NUMBER,
    p_to_account   NUMBER,
    p_amount       NUMBER
) AS
BEGIN
    UPDATE accounts
       SET balance = balance - p_amount
     WHERE account_id = p_from_account;

    UPDATE accounts
       SET balance = balance + p_amount
     WHERE account_id = p_to_account;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/
```

The procedure must also validate the amount, lock the rows in a safe order, and handle the zero-update case. `COMMIT` does not repair invalid business logic.

### 15.9 Stored procedure definition

A **stored procedure** is a named PL/SQL program unit stored in the database data dictionary.

```sql
CREATE OR REPLACE PROCEDURE raise_salary(
    p_employee_id IN employees.employee_id%TYPE,
    p_amount      IN NUMBER,
    p_message     OUT VARCHAR2
) AS
BEGIN
    UPDATE employees
       SET salary = salary + p_amount
     WHERE employee_id = p_employee_id;

    IF SQL%ROWCOUNT = 0 THEN
        p_message := 'Employee not found';
    ELSE
        p_message := 'Salary updated';
    END IF;
END;
/
```

```sql
DECLARE
    v_message VARCHAR2(100);
BEGIN
    raise_salary(101, 5000, v_message);
    DBMS_OUTPUT.PUT_LINE(v_message);
END;
/
```

`EXEC` and `CALL` are also used in some environments.

### 15.10 Parameter modes

| Mode | Direction | Typical use |
|---|---|---|
| `IN` | Caller to procedure | Input value |
| `OUT` | Procedure to caller | Result or status message |
| `IN OUT` | Both directions | Value read and then replaced |

```sql
CREATE OR REPLACE PROCEDURE normalize_phone(
    p_phone IN OUT VARCHAR2
) AS
BEGIN
    p_phone := REGEXP_REPLACE(p_phone, '[^0-9]', '');
END;
/
```

Avoid using `IN OUT` when a separate input and output parameter would make the interface clearer.

### 15.11 Why stored procedures help

| Benefit | Explanation |
|---|---|
| Reuse | One database-resident unit replaces repeated application code |
| Central maintenance | Business logic can be changed in one place |
| Reduced network traffic | Several SQL statements can run in one server-side call |
| Controlled access | Users can receive permission to execute a procedure without direct table privileges |
| Consistent transactions | A procedure can coordinate several DML statements |
| Business validation | Rules can run close to the affected data |

### 15.12 Limitations and responsibilities

- The database administrator must manage definitions, privileges, versions, and deployment.
- Long-running procedures can consume database resources and hold locks.
- Complex business logic in the database can be harder to test and observe than application code.
- A procedure does not make an invalid transaction atomic by itself. It must use transactions and error handling correctly.
- `COMMIT` inside a procedure can conflict with the caller's transaction design.
- Dynamic SQL and dynamic PL/SQL introduce injection and validation concerns.
- Compiled objects can become invalid when referenced objects change and require recompilation.

### 15.13 Procedure privileges

```sql
CREATE ROLE reporting_reader;

GRANT EXECUTE ON raise_salary TO reporting_reader;
GRANT EXECUTE ON transfer_funds TO app_user;
```

Granting `EXECUTE` on a procedure does not automatically grant direct `SELECT` or `UPDATE` privileges on its tables. The procedure's definer's rights or an invoker-rights design determine which underlying privileges apply.

### 15.14 Worked Exercise 1: Count employees in a department

```sql
CREATE OR REPLACE PROCEDURE count_department_employees(
    p_department_id IN employees.department_id%TYPE,
    p_count         OUT NUMBER
) AS
BEGIN
    SELECT COUNT(*)
      INTO p_count
      FROM employees
     WHERE department_id = p_department_id;
END;
/
```

```sql
DECLARE
    v_count NUMBER;
BEGIN
    count_department_employees(10, v_count);
    DBMS_OUTPUT.PUT_LINE('Employee count: ' || v_count);
END;
/
```

### 15.15 Worked Exercise 2: Validate an amount before transfer

```sql
CREATE OR REPLACE PROCEDURE safe_transfer(
    p_from_account IN NUMBER,
    p_to_account   IN NUMBER,
    p_amount       IN NUMBER
) AS
    v_balance NUMBER;
BEGIN
    IF p_amount IS NULL OR p_amount <= 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Amount must be positive');
    END IF;

    SELECT balance
      INTO v_balance
      FROM accounts
     WHERE account_id = p_from_account
       FOR UPDATE;

    IF v_balance < p_amount THEN
        RAISE_APPLICATION_ERROR(-20002, 'Insufficient funds');
    END IF;

    UPDATE accounts
       SET balance = balance - p_amount
     WHERE account_id = p_from_account;

    UPDATE accounts
       SET balance = balance + p_amount
     WHERE account_id = p_to_account;
END;
/
```

The procedure validates its inputs and locks the source row. The caller or procedure must commit or roll back the complete transfer.

### 15.16 Section revision checklist

- [ ] I can label the `DECLARE`, `BEGIN`, `EXCEPTION`, and `END` parts.
- [ ] I can use `SELECT INTO`, `%TYPE`, constants, and bind notation.
- [ ] I can write conditional and iterative control flow.
- [ ] I can handle `NO_DATA_FOUND`, `TOO_MANY_ROWS`, and `OTHERS` correctly.
- [ ] I can distinguish `IN`, `OUT`, and `IN OUT` parameters.
- [ ] I can state the benefits and operational risks of stored procedures.
- [ ] I know why `COMMIT` inside a procedure needs an explicit transaction design.

## 16. Functions, Cursors, and Triggers

### 16.1 Functions

A **function** is a named PL/SQL program unit that returns a value.

```sql
CREATE OR REPLACE FUNCTION square(
    p_value IN NUMBER
) RETURN NUMBER
AS
BEGIN
    RETURN p_value * p_value;
END;
/
```

```sql
SELECT square(12) AS result FROM dual;
```

Oracle uses `dual` for a query that needs one row but no real table.

### 16.2 Procedure versus function

| Property | Procedure | Function |
|---|---|---|
| Return value | No required output | Must return one value |
| Parameter modes | `IN`, `OUT`, `IN OUT` | Usually `IN`; product rules vary |
| Typical invocation | `CALL` or PL/SQL call | SQL expression or PL/SQL call |
| Main use | Execute an action or workflow | Compute a value used by an expression |
| Side effects | May perform DML | Should avoid DML; many systems prohibit it |

A function must obey its DBMS's restrictions. Oracle PL/SQL functions used in SQL must be deterministic enough for the optimizer and cannot commit or roll back the caller.

### 16.3 Function example

```sql
CREATE OR REPLACE FUNCTION employee_level(
    p_age IN NUMBER
) RETURN VARCHAR2
IS
    v_level VARCHAR2(20);
BEGIN
    IF p_age IS NULL THEN
        v_level := 'UNKNOWN';
    ELSIF p_age > 35 THEN
        v_level := 'SENIOR';
    ELSIF p_age >= 30 THEN
        v_level := 'JUNIOR';
    ELSE
        v_level := 'FRESHER';
    END IF;

    RETURN v_level;
END;
/
```

```sql
SELECT employee_id,
       age,
       employee_level(age) AS level
FROM employees;
```

### 16.4 Cursors

A **cursor** is a handle to a result set. It lets procedural code process query results row by row.

#### Implicit cursor

Every SQL statement has an implicit cursor. The DBMS opens, processes, and closes it. After a DML statement, `SQL%ROWCOUNT` gives the number of affected rows.

```sql
DECLARE
    v_count NUMBER;
BEGIN
    UPDATE employees
       SET salary = salary * 1.10
     WHERE department_id = 10;

    v_count := SQL%ROWCOUNT;
    DBMS_OUTPUT.PUT_LINE('Rows updated: ' || v_count);
END;
/
```

#### Explicit cursor

```sql
DECLARE
    CURSOR employee_cursor IS
        SELECT employee_id, employee_name, salary
        FROM employees
        WHERE department_id = 10;
BEGIN
    FOR employee_rec IN employee_cursor LOOP
        DBMS_OUTPUT.PUT_LINE(employee_rec.employee_name);
    END LOOP;
END;
/
```

### 16.5 Explicit cursor lifecycle

| Stage | Statement | Purpose |
|---|---|---|
| Declaration | `CURSOR ... IS SELECT ...` | Defines the query and result structure |
| Opening | `OPEN cursor_name` | Executes the query and makes the result available |
| Fetching | `FETCH cursor_name INTO ...` | Retrieves the next row or a bulk collection |
| Testing | `cursor_name%NOTFOUND` | Indicates that no more rows remain |
| Closing | `CLOSE cursor_name` | Releases cursor resources |
| Exception cleanup | `CLOSE ...` in handler | Ensures closure after an error |

A cursor exists only inside its declarative scope. It should be closed even when processing raises an exception.

### 16.6 Explicit cursor with `FETCH`

```sql
DECLARE
    CURSOR emp_cursor IS
        SELECT employee_id, salary
        FROM employees
        WHERE department_id = 10;

    v_employee_id employees.employee_id%TYPE;
    v_salary employees.salary%TYPE;
    v_total NUMBER := 0;
BEGIN
    OPEN emp_cursor;

    LOOP
        FETCH emp_cursor INTO v_employee_id, v_salary;
        EXIT WHEN emp_cursor%NOTFOUND;
        v_total := v_total + v_salary;
    END LOOP;

    CLOSE emp_cursor;
    DBMS_OUTPUT.PUT_LINE('Total salary: ' || v_total);
EXCEPTION
    WHEN OTHERS THEN
        CLOSE emp_cursor;
        RAISE;
END;
/
```

### 16.7 Cursor attributes

| Attribute | Meaning |
|---|---|
| `%FOUND` | TRUE when the last fetch returned a row |
| `%NOTFOUND` | TRUE when the last fetch returned no row |
| `%ROWCOUNT` | Number of rows fetched so far by the cursor |
| `%ISOPEN` | TRUE while the cursor is open |

`%FOUND` and `%NOTFOUND` are opposites after a fetch. Check `%NOTFOUND` after the fetch, not before it.

### 16.8 Cursor trade-offs

- Row-by-row processing can be slower than a set-based operation.
- A cursor may hold locks or resources while open.
- Large results use memory or temporary storage.
- A `FOR` loop handles opening, fetching, and closing automatically.
- `FORALL` or bulk collection is usually preferable for large DML workloads.

### 16.9 Triggers

A **trigger** is a stored program that runs automatically when a specified event occurs.

| Timing | Event |
|---|---|
| `BEFORE` | Runs before the triggering DML effect |
| `AFTER` | Runs after the triggering DML effect |
| `INSTEAD OF` | Runs instead of a view's direct DML, where supported |

| Event | Examples |
|---|---|
| DML | `INSERT`, `UPDATE`, `DELETE` |
| DDL | `CREATE`, `ALTER`, `DROP`, where supported |
| Database/system | Logon, logoff, startup, shutdown, where supported |

A row trigger can inspect `OLD` and `NEW` values. In an `INSERT`, `OLD` values are unavailable. In a `DELETE`, `NEW` values are unavailable.

### 16.10 Trigger skeleton

```sql
CREATE OR REPLACE TRIGGER employee_salary_audit
AFTER UPDATE OF salary
ON employees
FOR EACH ROW
DECLARE
    v_difference NUMBER;
BEGIN
    v_difference := :NEW.salary - :OLD.salary;

    INSERT INTO salary_audit(employee_id, old_salary, new_salary, difference)
    VALUES (:NEW.employee_id, :OLD.salary, :NEW.salary, v_difference);
END;
/
```

The trigger fires after an update to `salary`. `:OLD.salary` is the previous value and `:NEW.salary` is the new value.

### 16.11 Reorder-stock trigger

```sql
CREATE OR REPLACE TRIGGER medicine_reorder
AFTER UPDATE OF quantity
ON medicines
FOR EACH ROW
BEGIN
    IF :NEW.quantity < 20 THEN
        INSERT INTO new_orders(medicine_id, order_date, quantity)
        VALUES (:NEW.medicine_id, SYSDATE, 200);
    END IF;
END;
/
```

A business rule embedded in a trigger runs on every qualifying update. The table must exist before the trigger can be created or compiled successfully.

### 16.12 Compound and statement triggers

Some DBMSs support:

- **Statement triggers:** fire once per statement rather than once per affected row.
- **Compound triggers:** separate timing sections for statement-level and row-level processing.

Use a statement trigger when the rule concerns the whole statement. Use a row trigger when each row needs separate values.

### 16.13 Trigger advantages

- Automatic enforcement without application changes.
- Centralized audit and history rules.
- Automatic maintenance of derived or summary data.
- Reusable database-side event handling.

### 16.14 Trigger limitations

- Trigger behavior can surprise application developers.
- Recursive or chained triggers can create complex execution paths.
- Errors in a row trigger can roll back the triggering statement.
- Hidden writes can increase contention and storage.
- Debugging and testing are harder when business logic is spread across triggers.
- A constraint is usually better than a trigger for a simple row-level rule.

### 16.15 Constraints versus triggers

| Requirement | Prefer |
|---|---|
| Value in a permitted range | `CHECK` |
| Unique or non-null identifier | `UNIQUE` or `NOT NULL` |
| Parent-child existence | Foreign key |
| Audit every salary change | Row trigger |
| Automatically create a restock order | Trigger or an application workflow |
| Validate a cross-row business rule | Trigger, assertion where supported, or controlled procedure |

### 16.16 Worked Exercise 1: Cursor total by department

```sql
DECLARE
    CURSOR salary_cursor IS
        SELECT salary
        FROM employees
        WHERE department_id = :p_department_id;

    v_salary employees.salary%TYPE;
    v_total NUMBER := 0;
BEGIN
    OPEN salary_cursor;

    LOOP
        FETCH salary_cursor INTO v_salary;
        EXIT WHEN salary_cursor%NOTFOUND;
        v_total := v_total + v_salary;
    END LOOP;

    CLOSE salary_cursor;
END;
/
```

A bind variable shown as `:p_department_id` must be supplied by the client or declared as a host variable. In a standalone block, declare a local variable with that name or pass it as a parameter.

### 16.17 Worked Exercise 2: Prevent negative salary

```sql
CREATE OR REPLACE TRIGGER prevent_negative_salary
BEFORE INSERT OR UPDATE OF salary
ON employees
FOR EACH ROW
BEGIN
    IF :NEW.salary < 0 THEN
        RAISE_APPLICATION_ERROR(-20003, 'Salary cannot be negative');
    END IF;
END;
/
```

The trigger runs before the insert or salary update reaches the table.

### 16.18 Common procedure, function, cursor, and trigger traps

1. **Treating a procedure as a value-producing function.** Use a function when the result must appear in an expression.
2. **Forgetting to close an explicit cursor.** Close it normally and in an exception handler.
3. **Checking `%NOTFOUND` before the fetch.** The status refers to the last fetch.
4. **Using `WHEN OTHERS` without logging or re-raising.** Hiding errors can commit incomplete work.
5. **Accessing `OLD` during an insert or `NEW` during a delete.** The unavailable row version is NULL or invalid for that event.
6. **Calling `COMMIT` from a function.** Most SQL engines prohibit transaction control in functions.
7. **Ignoring trigger recursion.** Use trigger attributes or conditions to prevent unintended recursive firing.
8. **Assuming a trigger preserves atomicity automatically.** The triggering statement and trigger work share the same transaction unless the trigger or caller commits improperly.

### 16.19 Section revision checklist

- [ ] I can state the difference between a procedure and a function.
- [ ] I can label the explicit cursor lifecycle.
- [ ] I can use `FOUND`, `NOTFOUND`, `ROWCOUNT`, and `ISOPEN`.
- [ ] I can write BEFORE, AFTER, and INSTEAD OF triggers.
- [ ] I can use `:OLD` and `:NEW` correctly.
- [ ] I can compare constraints, procedures, and triggers for different business rules.
- [ ] I know the main performance and maintenance risks of row-by-row cursors and triggers.

## 17. Exam Questions with Model Answers

### Question 1 (2 marks): What is a constraint? Give two examples.

**Answer:** A constraint is a schema-level declarative rule that the DBMS enforces when data is inserted, updated, or deleted. Examples: `PRIMARY KEY` prevents duplicate or null key values; `FOREIGN KEY` prevents orphaned child references. Other examples include `UNIQUE`, `NOT NULL`, and `CHECK`.

### Question 2 (2 marks): Differentiate a table from a view.

**Answer:** A table stores rows physically and supports direct DML subject to its constraints. An ordinary view stores a query definition and derives its rows from base tables when queried. Some simple views support updates through automatic rewriting; complex views may require `INSTEAD OF` triggers. A materialized view stores a result and requires refresh maintenance.

### Question 3 (2 marks): What is the difference between `WHERE` and `HAVING`?

**Answer:** `WHERE` filters individual rows before grouping and cannot normally contain aggregate functions. `HAVING` filters complete groups after aggregate values have been calculated and can test aggregates such as `AVG(salary) > 42000`.

### Question 4 (2 marks): State the full null-comparison rule.

**Answer:** A comparison involving a NULL operand evaluates to UNKNOWN, not TRUE or FALSE. Use `IS NULL` and `IS NOT NULL` to test for null. `WHERE` keeps only rows whose predicate is TRUE; both FALSE and UNKNOWN are excluded.

### Question 5 (5 marks): Explain the difference between `RANK`, `DENSE_RANK`, and `ROW_NUMBER`.

**Answer:**

- `ROW_NUMBER` assigns consecutive integers. Tied rows receive different numbers unless the ordering includes a unique tie-breaker.
- `RANK` gives tied rows the same rank and leaves gaps. Two top rows can both rank 1, and the next row can rank 3.
- `DENSE_RANK` gives tied rows the same rank without gaps. Two top rows rank 1, and the next row ranks 2.

All three can use `PARTITION BY` to restart numbering within a group.

### Question 6 (5 marks): What is a window function? Explain its main clauses.

**Answer:** A window function computes an aggregate or rank over a related set of rows while retaining one output row per input row. `OVER` defines the window. `PARTITION BY` divides rows into independent windows. `ORDER BY` defines the order used by ranking, running totals, and many frame calculations. `ROWS`, `RANGE`, or `GROUPS` defines the frame of rows visible to the calculation. Window functions differ from ordinary aggregation because they do not collapse the input into one row per group.

### Question 7 (5 marks): Explain `IN`, `EXISTS`, `ANY`, and `ALL` with examples.

**Answer:**

- `IN` tests whether a value is equal to a value in a subquery result.
- `EXISTS` tests whether a subquery returns at least one row.
- `> ANY` is true when the comparison is true for at least one result value.
- `> ALL` is true when the comparison is true for every result value.

`NOT EXISTS` is often safer than `NOT IN` when the subquery can return NULL.

### Question 8 (5 marks): What is a stored procedure? Explain its benefits and limitations.

**Answer:** A stored procedure is a named PL/SQL program unit stored in the database that contains SQL and procedural logic. It centralizes reusable business operations, reduces network traffic, supports controlled execution permissions, and can coordinate several statements in one transaction. Limitations include administrative overhead, hidden coupling to database objects, possible lock and resource use, difficult debugging, and design conflicts when a procedure commits work that the caller expected to manage as one larger transaction.

### Question 9 (5 marks): Differentiate a stored procedure from a stored function.

**Answer:** A procedure executes an action or workflow and communicates results through parameters. A function computes and returns one value and can appear in a SQL expression. Oracle functions used in SQL must obey restrictions such as avoiding transaction control and side effects. A function should not be used merely to hide a multi-action workflow.

### Question 10 (5 marks): Explain the cursor lifecycle and cursor attributes.

**Answer:** An explicit cursor is declared with a query, opened to execute the query, fetched one row or a collection at a time, tested for exhaustion, and closed to release resources. `%FOUND` is true after a successful fetch; `%NOTFOUND` is true after a fetch returns no row; `%ROWCOUNT` gives the number fetched so far; `%ISOPEN` reports whether the cursor is open. An exception handler should close an open cursor.

### Question 11 (10 marks): What is a trigger? Explain trigger timing, row values, advantages, and limitations.

**Answer:** A trigger is a stored database program that runs automatically in response to an event. `BEFORE` triggers run before the DML effect, `AFTER` triggers run after it, and `INSTEAD OF` triggers can intercept DML against a view. In a row trigger, `:OLD` contains the pre-update or pre-delete values and `:NEW` contains the post-update or post-insert values. Triggers centralize audit, derived-data maintenance, and automatic event handling. Their limitations include hidden writes, lock contention, recursion, difficult debugging, and surprising effects on application code. A declarative constraint is preferable to a trigger for a simple row-level rule.

### Question 12 (10 marks): Explain query optimization. Compare heuristic and cost-based optimization.

**Answer:** Query optimization transforms a declarative query into an executable evaluation plan. The parser and translator produce an internal query form and relational algebra. The optimizer chooses among logically equivalent expressions and physical access algorithms. Heuristic optimization applies rules such as performing restrictive selections and projections early and joining smaller intermediate results first. Cost-based optimization estimates I/O, CPU, and communication cost using statistics about relation sizes, distinct values, index selectivity, and intermediate results, then chooses a low-cost plan. Modern optimizers combine both approaches. A good plan reduces execution time and resource use while preserving the query's result.

### Question 13 (10 marks): Write a PL/SQL procedure that transfers funds safely and explain its error handling.

**Answer:**

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
    p_from_account IN NUMBER,
    p_to_account   IN NUMBER,
    p_amount       IN NUMBER
) AS
    v_balance NUMBER;
BEGIN
    IF p_amount IS NULL OR p_amount <= 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Invalid amount');
    END IF;

    SELECT balance
      INTO v_balance
      FROM accounts
     WHERE account_id = p_from_account
       FOR UPDATE;

    IF v_balance < p_amount THEN
        RAISE_APPLICATION_ERROR(-20002, 'Insufficient funds');
    END IF;

    UPDATE accounts
       SET balance = balance - p_amount
     WHERE account_id = p_from_account;

    UPDATE accounts
       SET balance = balance + p_amount
     WHERE account_id = p_to_account;

    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
/
```

The procedure validates its input, locks the source account row, checks available funds, performs both updates in one transaction, commits only after success, and rolls back and re-raises on an error. Production code must also define account lock ordering, authorization, isolation requirements, and retry behavior.

### Question 14 (10 marks): Explain how `WITH CHECK OPTION` protects a view and why it matters.

**Answer:** `WITH CHECK OPTION` requires every row inserted or updated through a view to remain within the view's defining predicate. It prevents a user from using the view to create a row that the view claims to exclude. The default check scope in PostgreSQL is `CASCADED`, so checks also apply through underlying views. The option does not replace foreign-key or other base-table constraints, and it does not make every complex view updatable.

## 18. MCQs, Practical Exercises, Cheat Sheet, and Rapid-Revision Checklist

### 18.1 MCQs

1. **Which function leaves gaps after tied rows?**
   - A. `ROW_NUMBER`
   - B. `RANK`
   - C. `DENSE_RANK`
   - D. `NTILE`

   **Answer: B.** `RANK` gives ties the same value and skips the next rank.

2. **Which predicate finds rows whose salary is NULL?**
   - A. `salary = NULL`
   - B. `salary != NULL`
   - C. `salary IS NULL`
   - D. `NULL salary`

   **Answer: C.** Use `IS NULL`.

3. **Which clause filters groups after aggregation?**
   - A. `WHERE`
   - B. `GROUP BY`
   - C. `HAVING`
   - D. `ORDER BY`

   **Answer: C.** `HAVING` filters complete groups.

4. **Which expression returns the number of rows, including rows with NULLs?**
   - A. `COUNT(column)`
   - B. `COUNT(*)`
   - C. `COUNT DISTINCT`
   - D. `SUM(*)`

   **Answer: B.** `COUNT(*)` counts rows; `COUNT(column)` counts non-NULL values.

5. **Which subquery form returns one value?**
   - A. Scalar subquery
   - B. Derived table
   - C. Set-returning subquery
   - D. View definition

   **Answer: A.** A scalar subquery returns one row and one column.

6. **What does `EXISTS` test?**
   - A. Whether a subquery returns at least one row
   - B. Whether one value equals another
   - C. Whether a table has a primary key
   - D. Whether all values are NULL

   **Answer: A.** `EXISTS` tests row presence, not a selected value.

7. **Which is an explicit cursor attribute?**
   - A. `%FOUND`
   - B. `%ROWTYPE`
   - C. `%TYPE`
   - D. `%TABLE`

   **Answer: A.** `%FOUND`, `%NOTFOUND`, `%ROWCOUNT`, and `%ISOPEN` are cursor attributes.

8. **Which trigger timing runs before the triggering DML effect?**
   - A. `AFTER`
   - B. `BEFORE`
   - C. `INSTEAD OF` only
   - D. `COMMIT`

   **Answer: B.** `BEFORE` executes before the row change.

9. **What does `:OLD` contain in an UPDATE row trigger?**
   - A. The new row
   - B. The pre-update row
   - C. The commit record
   - D. The SQL code

   **Answer: B.** `:NEW` contains the post-update values.

10. **Which is the safest rewrite of a nullable `NOT IN` test?**
    - A. Add `= NULL`
    - B. Use `NOT EXISTS`
    - C. Use `INNER JOIN` without a condition
    - D. Remove the subquery

    **Answer: B.** `NOT EXISTS` avoids the NULL-related `NOT IN` behavior.

### 18.2 Practical exercises

#### Exercise 1: Department salary summary

Write a query that returns each department name, employee count, and average salary for departments with at least three employees.

```sql
SELECT d.department_name,
       COUNT(e.employee_id) AS employee_count,
       ROUND(AVG(e.salary), 2) AS average_salary
FROM departments d
JOIN employees e
  ON e.department_id = d.department_id
GROUP BY d.department_id, d.department_name
HAVING COUNT(e.employee_id) >= 3;
```

#### Exercise 2: Highest-paid employee per department

Use a window function to show every employee with rank 1 in their department.

```sql
WITH ranked AS (
    SELECT employee_id,
           department_id,
           salary,
           RANK() OVER (
               PARTITION BY department_id
               ORDER BY salary DESC
           ) AS salary_rank
    FROM employees
)
SELECT employee_id, department_id, salary
FROM ranked
WHERE salary_rank = 1;
```

`RANK` keeps all employees tied for first place. `ROW_NUMBER` would select one arbitrary tied employee unless the ordering contains a unique tie-breaker.

#### Exercise 3: Moving average

Write a query that calculates the three-day moving average of daily sales.

```sql
SELECT sale_date,
       AVG(amount) OVER (
           ORDER BY sale_date
           ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
       ) AS centered_moving_average
FROM daily_sales;
```

#### Exercise 4: NULL-safe department filter

Explain why this query may return no rows:

```sql
SELECT name
FROM instructor
WHERE department_id NOT IN (
    SELECT department_id
    FROM department
);
```

If the subquery contains NULL, `NOT IN` cannot produce TRUE for a non-null outer value. Use `NOT EXISTS` or remove nulls from the subquery.

#### Exercise 5: Function with a null input

Write a function that returns `UNKNOWN` for a NULL age and otherwise returns `JUNIOR`, `MID`, or `SENIOR`.

```sql
CREATE OR REPLACE FUNCTION age_band(p_age NUMBER) RETURN VARCHAR2 IS
BEGIN
    IF p_age IS NULL THEN
        RETURN 'UNKNOWN';
    ELSIF p_age >= 50 THEN
        RETURN 'SENIOR';
    ELSIF p_age >= 30 THEN
        RETURN 'MID';
    ELSE
        RETURN 'JUNIOR';
    END IF;
END;
/
```

#### Exercise 6: Cursor with exception cleanup

Complete the cursor loop so it closes on both normal completion and error.

```sql
DECLARE
    CURSOR c IS SELECT employee_id FROM employees;
    v_id NUMBER;
BEGIN
    OPEN c;
    LOOP
        FETCH c INTO v_id;
        EXIT WHEN c%NOTFOUND;
        DBMS_OUTPUT.PUT_LINE(v_id);
    END LOOP;
    CLOSE c;
EXCEPTION
    WHEN OTHERS THEN
        IF c%ISOPEN THEN
            CLOSE c;
        END IF;
        RAISE;
END;
/
```

### 18.3 SQL and PL/SQL cheat sheet

| Topic | Rule or syntax |
|---|---|
| Aggregate | `COUNT`, `SUM`, `AVG`, `MIN`, `MAX` |
| Group filter | `HAVING COUNT(*) > 5` |
| Rank with ties and gaps | `RANK() OVER (ORDER BY value DESC)` |
| Rank with ties, no gaps | `DENSE_RANK() OVER (...)` |
| Unique sequence | `ROW_NUMBER() OVER (...)` |
| Buckets | `NTILE(4) OVER (...)` |
| Running total | `SUM(x) OVER (ORDER BY t ROWS UNBOUNDED PRECEDING)` |
| Null test | `expression IS [NOT] NULL` |
| Subquery existence | `EXISTS (SELECT 1 ...)` |
| Scalar subquery | `(SELECT one_value ...)` |
| PL/SQL block | `DECLARE ... BEGIN ... EXCEPTION ... END;` |
| Procedure call | `procedure_name(parameter, ...)` |
| Function call | `SELECT function_name(expression)` |
| Cursor fetch | `FETEST cursor INTO variable` |
| Cursor exhaustion | `cursor%NOTFOUND` |
| Trigger row versions | `:OLD` and `:NEW` |
| Safe error handler | `WHEN OTHERS THEN ... RAISE;` |

### 18.4 Common exam traps

| Trap | Correct rule |
|---|---|
| `WHERE AVG(salary)` | Use `HAVING` for aggregate filters |
| `salary = NULL` | Use `IS NULL` |
| `NOT IN` with nullable subquery | Prefer `NOT EXISTS` |
| `RANK` after a two-row tie | Next rank is 3; `DENSE_RANK` gives 2 |
| `COUNT(column)` counts all rows | It ignores NULL; `COUNT(*)` counts rows |
| `WHEN OTHERS` without `RAISE` | Can hide a failed operation |
| `OLD` during INSERT | `OLD` is unavailable |
| A trigger always improves integrity | Use a constraint for simple declarative rules |
| A view always stores data | Only a materialized view stores a result |

### 18.5 Rapid-revision checklist

- [ ] I can list the four main constraint families and their SQL mechanisms.
- [ ] I can explain ordinary, materialized, and trigger-updatable views.
- [ ] I can write aggregate queries with `GROUP BY` and `HAVING`.
- [ ] I can use `WHERE` and `HAVING` in the correct logical order.
- [ ] I can choose the correct ranking function for ties and gaps.
- [ ] I can write a window with partition, order, and frame.
- [ ] I can reproduce SQL's three-valued truth tables.
- [ ] I can use scalar, correlated, derived-table, and `EXISTS` subqueries.
- [ ] I can label a PL/SQL block and its exception handler.
- [ ] I can write and call a procedure with `IN` and `OUT` parameters.
- [ ] I can trace an explicit cursor's lifecycle.
- [ ] I can distinguish BEFORE, AFTER, and INSTEAD OF triggers.
- [ ] I know why constraints are often preferable to triggers.
