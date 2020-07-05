**Sources**:

- _Dive Into Design Patterns_ by Alexander Shvets.
- <https://sourcemaking.com>
- <https://www.oodesign.com>

--------------------------------------------------------------------------------

# OOP basics

- **Abstraction**<br>
  Abstraction is a model of a real-world object or phenomenon, limited to a specific context, which represents all details relevant to this context with high accuracy and omits all the rest.
- **Encapsulation**<br>
  Encapsulation is the ability of an object to hide parts of its state and behaviors from other objects, exposing only a limited interface to the rest of the program.<br>
  Also refers to bundling of data and methods.
- **Inheritence**<br>
  Code reuse.
- **Polymorphism**<br>
  Objects of subclass being passed as objects of superclass.

## UML diagram relation types

- **Association**

  - An object uses or interacts with another.
  - In general, used to represent something like a field in a class.<br>
    ![UML association example](assets/UML_Association.png)

- **Dependency**

  - A weaker variant of association.
  - Typically implies that an object accepts another object as method parameter.
  - A change in the child class might lead to code change in the method of the parent class.<br>
    ![UML Dependency example](assets/UML_Dependency.png)

- **Composition**

  - One class contains an instance of another class.
  - A person has a name. And that name object is not present in any other class.<br>
    It is created and destroyed along with the parent object.<br>
    ![UML Composition example](assets/UML_Composition.png)

- **Aggregation**

  - A weaker variant of composition, where one object merely contains reference to another.
  - Container does not manage the lifecycle of the component.
  - A person has a house. Other people might also own the same house object.<br>
    The house existed even before the person was born, and will remain after their death.<br>
    ![UML Aggregation example](assets/UML_Aggregation.png)

--------------------------------------------------------------------------------

# Design patterns

- A solution to commonly recurring problems.
- A blueprint to be used after customization. Unlike an algorithm, which can be used verbatim.
- Can be classified on the basis of complexity:

  - Idioms (most basic; usually language specific)
  - Architectural patterns (most complex)

## Features of good design

- Code reuse. 3 levels:

  - Reuse classes, libraries.
  - Design patterns.
  - Frameworks (jUnit).

- Extensibility -> Because change is inevitable.

## Design principles

- Encapsulate what varies. Meaning if a function(or class) does some complicated task, try to do that in a separate function instead.
- Program to an interface, not an implementation:

  - Determine exactly what methods are needed by one object from another.
  - Describe these methods in a new interface or abstract class.
  - Make the dependent class implement this iterface.
  - Now make the parent class depend on the interface.

- Favour composition over inheritance. Problems with inheritance:

  - Subclass must implement all superclass methods, even though only a few are required.
  - The overriden method's behaviour is compatible with the parent.
  - Breaks encapsulation of the parent class, as the members are available to the child class.
  - Any change in the super class might break child class.
  - Can lead to inheritance combinatorial explosion.

--------------------------------------------------------------------------------

# SOLID Principles

## (S) Single Responsibilty.

A class should have just one reason to change.

## (O) Open/Closed Principle.

Classes should be open for extension but closed for modification.

## (L) Liskov Substitution Principle.

- Parameter types in a method of a subclass should match or be more abstract than parameter types in the method of the super-class.

```
class Human:
    def feed(cat):
        cat.eat(Food())

class ZooKeeper(Human):
    def feed(bengalCat):
        bengalCat.feedOnlyAtNight(Food())

def clientCode(human, cat):
    human.feed(cat)

zk = ZooKeeper()
cat = Cat()
clientCode(zk, cat)

# Will fail since `zookeeper.feed()` will fail on generic cats.
# This is so because generic Cat() does not have a `feedOnlyAtNight()` method.
```

- The return type in a method of a subclass should match or be a subtype of the return type in the method of the superclass.<br>
  When extending a class, remember that you should be able to pass objects of the subclass in place of objects of the parent class without breaking the client code.

```
class Human:
    def feed(cat):
        cat_mood = cat.eat(Food())

class ZooKeeper(Human):
    def feed(cat):
        cat_weight = cat.eat(Food())

def clientCode(human, cat):
    cat_mood = human.feed(cat)
        assert(cat_mood in ['happy', 'sleepy'])

zk = ZooKeeper()
cat = Cat()
clientCode(zk, cat)

# Will fail since `cat_mood` will be an integer rather than string.
```

- A method in a subclass shouldn't throw types of exceptions which the base method isn't expected to throw.<br>
  Otherwise the signature of the client code will not reflect all the possible exceptions possible.
- A subclass shouldn't strengthen (narrow down) pre-conditions.<br>
  If the parent method accepts a number, the subclass shouldn't demand only negative numbers, since it might fail on some client code which does not about this limitation.
- A subclass shouldn't weaken post-conditions.<br>
  If the parent class always closes the files opened at the end of a method, the subclass should also do that, as the client code will expect that the object always closes files by itself.
- Invariants of the superclass must be preserved.<br>
  Do not mess with the existing fields of the class. Make new ones.
- Subclass shouldn't change the values of the private fields of the superclass (some languages support it strangely).

## (I) Interface segregation

An interface should define the least number of methods, otherwise the child class will have to implement unnecessary methods.

## (D) Dependency inversion

- High-level classes shouldn't depend on low-level classes.<br>

- Both should depend on abstractions.<br>

- Abstractions shouldn't depend on details.<br>

- Details should depend on abstractions.
