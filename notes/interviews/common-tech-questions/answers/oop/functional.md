- In functional programming, we have **pure functions** whose output is completely dependent on the input and nothing else.
  They have no **side-effects**.
- Meaning that their return values can be possibly cached.
- Also, no object is ever mutated. Everything is immutable. Which means parallelism is easy.
- Includes functions like `map()`, `reduce()`, `forEach()`, `filter()`.
- Code is shorter.

```java
int sum = widgets.stream()
                      .filter(w -> w.getColor() == RED)
                      .mapToInt(w -> w.getWeight())
                      .sum();
```

```java
Integer sum = integers.reduce(0, (a, b) -> a+b);
```
- Object-oriented languages are good when you have a fixed set of operations on things, and as your code evolves, you primarily add new things.
- This can be accomplished by adding new classes which implement existing methods, and the existing classes are left alone.
- Functional languages are good when you have a fixed set of things, and as your code evolves, you primarily add new operations on existing things.
- This can be accomplished by adding new functions which compute with existing data types, and the existing functions are left alone.
- When evolution goes the wrong way, you have problems:
  - Adding a new operation to an object-oriented program may require editing many class definitions to add a new method.
  - Adding a new kind of thing to a functional program may require editing many function definitions to add a new case.
- Functional languages excel at manipulating symbolic data in tree form.
- A favorite example is compilers, where source and intermediate languages change seldom (mostly the same things), but compiler writers are always adding new translations and code improvements or optimizations (new operations on things).
- Compilation and translation more generally are "killer apps" for functional languages.

- NOTE: In OOP design, if you want to add a new method to an interface, you will have to modify all the subclasses also.
  One way to avoid it is using visitor pattern.