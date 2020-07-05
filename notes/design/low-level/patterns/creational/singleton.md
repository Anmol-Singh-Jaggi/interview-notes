# Singleton

- Type: **Creational**.

## Uses:

- Logger.
- Configuration classes.
- Shared resources (serial port for example).
- Factory methods.<br>
  Let's assume that we design an application with a factory to generate new objects(Acount, Customer, Site, Address objects) with their ids, in an multithreading environment.<br>
  If the factory is instantiated twice in 2 different threads then is possible to have 2 overlapping ids for 2 different objects. If we implement the Factory as a singleton we avoid this problem.<br>
  Combining Abstract Factory or Factory Method and Singleton design patterns is a common practice.

## Problems:

- Thread-safe implementation for multi-threading use.

The standard implementation shown here is a thread safe implementation:

```
class Singleton {
    private static Singleton instance;

    private Singleton() {
        ...
    }

    public static synchronized Singleton getInstance(){

        if (instance == null)
            instance = new Singleton();

        return instance;
    }

    ...

    public void doSomething()
    {
        ...
    }
}
```

But it's not the best thread-safe implementation because synchronization is very expensive when we are talking about the performance.<br>
We can see that the synchronized method `getInstance` does not need to be checked for syncronization after the object is initialized.<br>
If we see that the singleton object is already created we just have to return it without using any syncronized block.<br>
This optimization consist in checking in an unsynchronized block if the object is null and if not to check again and create it in an syncronized block.<br>
This is called **double locking mechanism**.

```
//Lazy instantiation using double locking mechanism.
class Singleton
{
    private static Singleton instance;

    private Singleton()
    {
    System.out.println("Singleton(): Initializing Instance");
    }

    public static Singleton getInstance()
    {
        if (instance == null)
        {
            synchronized(Singleton.class)
            {
                if (instance == null)
                {
                    System.out.println("getInstance(): First time getInstance was invoked!");
                    instance = new Singleton();
                }
            }            
        }

        return instance;
    }

    public void doSomething()
    {
        System.out.println("doSomething(): Singleton does something!");
    }
}
```

Alternatively, we can just do eager loading instead of lazy loading to avoid managing synchronization:

```
//Early instantiation using implementation with static field.
class Singleton
{
    // Will be created as soon as JVM loads the class.
    // So no possibility of race conditions.
    private static Singleton instance = new Singleton();

    private Singleton()
    {
        System.out.println("Singleton(): Initializing Instance");
    }

    public static Singleton getInstance()
    {    
        return instance;
    }

    public void doSomething()
    {
        System.out.println("doSomething(): Singleton does something!");
    }
}
```

- Serialization In java, if a Singleton class implements the `java.io.Serializable` interface, when the singleton is serialized and then deserialized more than once, there will be multiple instances of the Singleton class created.

In order to avoid this the `readResolve()` method should be implemented.

```
public class Singleton implements Serializable {
    ...

    // This method is called immediately after an object of this class is deserialized.
    // This method returns the singleton instance.
    protected Object readResolve() {
        return getInstance();
    }
}
```

- Testing<br>
  Is pretty hard to test, as most of testing frameworks are not designed to test static class.

## Examples:

- Logger.
- Configuration object.

```python
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        return Singleton.__instance

    @staticmethod
    def setInstance(new_data):
        Singleton.__instance = new_data

    def __init__(self):
        raise Exception("This class is a singleton!")


s = Singleton.getInstance()
print(s)

Singleton.setInstance('sd')
s = Singleton.getInstance()
print(s)
```
