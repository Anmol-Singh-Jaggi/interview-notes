- Permanent Generation was a memory area which was different from the main JVM heap area.
- It was used to store things like class objects and interned string.
- It was replaced by something called as `Metaspace` in Java 8.
- In Java 8, all the interned strings are stored in main JVM area, not metaspace.
- Each classloader has its own metaspace.
- Memory of a metaspace is reclaimed only after the classloader is garbage collected.
- Back when PermGen was introduced, there was no Java EE or dynamic class(un)loading, so once a class was loaded it was stuck in memory until the JVM shut down - thus Permanent Generation.
- Nowadays classes may be loaded and unloaded during the lifespan of the JVM, so Metaspace makes more sense for the area where the metadata is kept.
- We can use it if we want to quickly compare 2 strings using `==` which will just compare the memory address rather than calling `.equals()` which will compare char by char.
- We rarely used it as interning happened  in perm gen earlier which had limited memory size.
- The intern string pool is maintained by the `String` class.

# String intern

```java
// String literals are automatically interned.
String s1 = "Arul";
String s2 = "Arul";
if (s1 == s2)
    System.out.println("equal"); // Prints equal.

String n1 = new String("Arul");
String n2 = new String("Arul");
if (n1 == n2)
    System.out.println("equal"); // No output.


n1 = n1.intern();
n2 = n2.intern();
if (n1 == n2)
    System.out.println("equal"); // Prints equal.
```

# Permgen Leak

https://plumbr.io/blog/memory-leaks/what-is-a-permgen-leak