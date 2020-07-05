- Primitive types are `int`, `long` etc.
- Wrapper/Reference types are `Integer`, `Long` etc.
- Primitive types dont extend `Object`.
- They also take less memory.
- Java automatically converts one to another implicitly.
- This is called `boxing`/`unboxing`.

```Java
List<Integer> list = new ArrayList<>();
list.add(5);
int value = list.get(0);
```

# Generics

## Type erasure

- It's basically the way that generics are implemented in Java via compiler trickery.
- The compiled generic code actually just uses `java.lang.Object` wherever you talk about `T` (or some other type parameter) - and there's some metadata to tell the compiler that it really is a generic type.
- When you compile some code against a generic type or method, the compiler works out what you really mean (i.e. what the type argument for T is) and verifies at compile time that you're doing the right thing, but the emitted code again just talks in terms of `java.lang.Object` - the compiler generates extra casts where necessary.
- At execution time, a `List<String>` and a `List<Date>` are exactly the same; the extra type information has been erased by the compiler.
- Compare this with, say, C#, where the information is retained at execution time, allowing code to contain expressions such as `typeof(T)` which is the equivalent to `T.class` - except that the latter is invalid.
- This is done intentionally to preserve backwards compatibility.


```java
lass java.util.Iterator as it is defined in Java SE version 1.4:

public interface Iterator {
    boolean hasNext();
    Object next();
    void remove();
}

Class java.util.Iterator as it is defined in Java SE version 5.0:

public interface Iterator<E> {
    boolean hasNext();
    E next();
    void remove();
}
```

```java
List<String> list = new ArrayList<String>();
list.add("Hi");
String x = list.get(0);

// is compiled into:

List list = new ArrayList();
list.add("Hi");
String x = (String) list.get(0);
```

## Bounded type parameters
- When we use bounded parameters, we are restricting the types that can be used as generic type arguments.
- As an example, let's say we want to force our generic type always to be a subclass of animal:

```java
public abstract class Cage<T extends Animal> {
    abstract void addAnimal(T animal)
}
```

- By using `extends`, we are forcing `T` to be a subclass of `Animal`.
- We could then have a cage of cats - `Cage<Cat> catCage;`.
- But we could not have a cage of objects, as an object is not a subclass of an animal:

```java
Cage<Object> objectCage; // Compilation error
```

- One advantage of this is that all the methods of `Animal` are available to the compiler.
- We know our type extends it, so we could write a generic algorithm which operates on any animal.
- This means we don't have to reproduce our method for different animal subclasses:

```java	
public void firstAnimalJump() {
    T animal = animals.get(0);
    animal.jump();
}
```

- We can support multiple bounds - `public abstract class Cage<T extends Animal & Comparable>`.
- There is also a wildcard type - `public static consumeListOfWildcardType(List<?> list)`.

## Upper Bounded wildcard

```java
public class Farm {
  private List<Animal> animals;
 
  public void addAnimals(Collection<Animal> newAnimals) {
    animals.addAll(newAnimals);
  }
}

farm.addAnimals(cats); // Compilation error
farm.addAnimals(dogs); // Compilation error
// Exact Animal is expected!
```

```java
public class Farm {
  private List<Animal> animals;
 
  public void addAnimals(Collection<? extends Animal> newAnimals) {
    animals.addAll(newAnimals);
  }
}

// Any subtype of Animal will do!
farm.addAnimals(cats); // Works!
farm.addAnimals(dogs); // Works!
```

## Lower bounded wildcard

```java
public static void addDogs(List<? super Animal> list) {
   list.add(new Dog("tom"));
}

// By using super, we could call `addDogs()` on a list of objects:
	
ArrayList<Object> objects = new ArrayList<>();
addDogs(objects);
```

## When to choose upper vs lower wildcard??

- When dealing with collections, a common rule for selecting between upper or lower bounded wildcards is **PECS**.
- PECS stands for *producer extends, consumer super*.
- Producer extends just means that if you are creating a producer of a generic type, then use the extends keyword.

```java
public static void makeLotsOfNoise(List<? extends Animal> animals) {
    animals.forEach(Animal::makeNoise);   
}
```

- Here, we want to call `makeNoise()` on each animal in our collection.
- This means our collection is a producer, as all we are doing with it is getting it to return animals for us to perform our operation on.
- If we got rid of extends, we wouldn't be able to pass in lists of cats, dogs or any other subclasses of animals.
- Consumer super means the opposite to producer extends.

```java
public static void addCats(List<? super Animal> animals) {
    animals.add(new Cat());   
}
```

- The final thing to consider is what to do if a collection is both a consumer and a producer??
- An example of this might be a collection where elements are both added and removed.
- In this case, an unbounded wildcard should be used.

## `<T>` vs `<?>`
- Where type parameters define a sort of variable (e.g., T) that represents the type for a scope, the wildcard does not: the wildcard just defines a set of allowable types that you can use for a generic type.
- The wildcard always come between angle brackets, and it only has meaning in the context of a generic type:

```java
public void foo(List<?> listOfAnyType) {...}  // pass a List of any type
public <?> ? bar(? someType) {...}  // error. Must use type params here
public class MyGeneric ? {      // error
    public ? getFoo() { ... }   // error
    ...
}
```

- Type params can have multiple bounding classes; the wildcard cannot.
- The wildcard can have lower bounds; type params cannot.

```java
public class Foo <T extends Comparable<T> & Cloneable> {...}
public void bar(List<? super Integer> list) {...}
```
- In the above the `List<? super Integer>` defines `Integer` as a lower bound on the wildcard, meaning that the List type must be Integer or a super-type of Integer.
- Finally, here's a method definition which uses the wildcard to do something that I don't think you can do any other way:

```java
public static <T extends Number> void adder(T elem, List<? super Number> numberSuper) {
    numberSuper.add(elem);
}
```