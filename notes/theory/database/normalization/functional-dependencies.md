- A functional dependency `A -> B` means:
  - **A** and **B** are sets of attributes(columns).
  - *'A determines B'* or *'B depends on A'*.
  - A is called *Determinant* and B is called *Dependent*.
  - In a table, wherever column **A** has a value 'x', **B** will always be 'y'.
  - Its very similar to a definition of function; there can only be one *y* for an *x*.
  - However, multiple 'x' can have the same 'y'.
- For example, `employee_id → name` means `employee_id` functionally determines the name of the employee.
- As another example in a time table database, `{student_id, time} → {lecture_room}`, student ID and time determine the lecture room where the student should be.
- For example in the below table `A → B` is true, but `B → A` is not true as there are different values of A for B = 3.

| A   | B   |
| --- | --- |
| 1   | 3   |
| 2   | 3   |
| 4   | 0   |
| 1   | 3   |
| 4   | 0   |

- The **Closure** of a set of attributes `A` is the set of attributes that can be determined from A.
- For example, if we have the following functional dependencies:
  - A -> B
  - B -> CD
  - D -> B
- Then closure(A) = (A)+ = ABCD, because we can reach all these vertices either directly or indirectly while traversing the dependency graph.
- (B)+ = BCD
- (D)+ = BCD
- Note that the closure of A always contains atleast A itself.

## Trivial Functional Dependency
- `X → Y` is trivial when Y is subset of X.
- Pretty obvious :p
- **Examples:**
  - `ABC → AB`
  - `ABC → A`
  - `ABC → ABC`

## Non-Trivial Functional Dependencies
- `X → Y` is non-trivial when Y is not a subset of X.
- `X → Y` is called **completely non-trivial** when X intersect Y is NULL.
- **Examples:**
  - `Id → Name`
  - `Name → DOB`
- `X → Y` is called **semi non-trivial** when X intersect Y is not NULL.
- **Examples:**
  - `AB → BC`
  - `AD → DC`

## Prime vs Non-Prime attribute
- **Prime attributes**: Attributes that are part of **any** of the candidate keys.
- **Non-prime attribute** - Attributes that are not part of **any** candidate key.

### Super key
- Lets say we have a table with attributes `R = {A, B, C, D}`.
- If `(AB)+ -> {R}`, then `AB` cannot have duplicates; it be used to indentify a row uniquely.
- Meaning AB is a **Superkey**.
- A super key is any set of attributes which can uniquely identify a row.

### Candidate key
- But if `(AB)+ -> {R}` and neither `(A)+ -> R` nor `(B)+ -> R`, then `AB` will also be the candidate key.
- Meaning if none of the proper subsets of a super-key are also super-keys, then that super-key is a candidate key.
- Or in other words, the set of **minimal** attributes that can uniquely identify a row.
- Note that if `(ABC)+ -> R` and `(D)+ -> R`, then `ABC` and `D` both are candidate keys.
- Note that every candidate key is a super-key but not every super-key is a candidate key!!

### Primary Key
- Any 1 of the candidate keys can be randomly chosen as the primary key by the DB admin.

## Types of Dependencies
- **Partial dependency**:
  - A **non-prime attribute** is dependent on a **proper subset** of any candidate key of the table.
  - If `ABC` is a candidate key, then `AB -> D` is a partial dependency.
  - `p -> np` (Prime -> Non-Prime).
- **Transitive Dependency**:
  - A **non-prime attribute** is dependent on another non-prime attribute.
  - If `ABC` is a candidate key, then `D -> E` is a partial dependency.
  - `np -> np`.

## Armstrong's Axioms
- **Reflexivity:** If `B` is a subset of `A`, then `A -> B` (Trivial dependency).
- **Augmentation:** If `A -> B`, then `AY -> BY`.
- **Transitivity**: If `A -> B` and `B -> C`, then `A -> C`.
- **Union:** If `A -> B` and `A -> C`, then `A -> BC`.
- **Composition:** If `A -> B` and `X -> Y`, then `AX -> BY`.
- **Decomposition:** If `A -> BC`, then `A -> B` and `A -> C`. (Important!!)
- **Pseudo-Transitivity:** If `A -> B` and `BC -> D`, then `AC -> D`.