- Inheritence is when an object of class `Dog` reuses or overrides the function `walk()` of the parent class `Animal`.
- Polymorphism is when in a function `walkAnimal(Animal animal)`, we pass an object of type `Dog`, but the JVM still calls `Dog.walk()` rather than `Animal.walk()`. 
- In short, JVM can figure out that this object of type `Animal` is a `Dog` under the hood **at runtime**.
- Note that overriding is also referred to as **Runtime Polymorphism** whereas overloading(function overloading) is called **Static polymorphism**.
- Meaning function overloading is resolved at compile-time itself.
- Note that runtime method binding is only valid for determining the method that will be called in the override heirarchy,
  not for determining the method based on the parameter type.
  For example:

```java
interface Callee {
    public void foo(Object o);
    public void foo(String s);
    public void foo(Integer i);
}

class CalleeImpl implements Callee {
    public void foo(Object o) {
        logger.debug("foo(Object o)");
    }

    public void foo(String s) {
        logger.debug("foo(\"" + s + "\")");
    }

    public void foo(Integer i) {
        logger.debug("foo(" + i + ")");
    }
}

Callee callee = new CalleeImpl();

Object i = new Integer(12);
Object s = "foobar";
Object o = new Object();

callee.foo(i);
callee.foo(s);
callee.foo(o);

// in all the 3 cases, the object method will be called.
```
