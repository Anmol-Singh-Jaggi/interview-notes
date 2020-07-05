Java 8 ships with several new features but the most significant are the following:

- **Lambda Expressions** − a new language feature allowing treating actions as objects.
- **Method References** − enable defining Lambda Expressions by referring to methods directly using their names.
- **Optional** − special wrapper class used for expressing optionality.
- **Default methods** − give us the ability to add full implementations in interfaces besides abstract methods.
- **Nashorn JavaScript Engine**: Java-based engine for executing and evaluating JavaScript code.
- **Stream API** − a special iterator class that allows processing collections of objects in a functional manner.
- **Date API** − an improved, immutable JodaTime-inspired Date API.
- **Functional Interface** – an interface with maximum one abstract method, implementation can be provided using a Lambda Expression.
- HashMap buckets are red-black trees instead of linked lists.
- Permgen vs Metaspace + String intern.

# Lambda

- A lambda is an expression used to instantiate an object implementing a functional interface.

```java
// A sample functional interface (An interface with single abstract method)
interface FuncInterface 
{ 
	// An abstract function 
	void abstractFun(int x); 
	// A non-abstract (or default) function 
	default void normalFun() 
	{ 
	    System.out.println("Hello"); 
	} 
} 

class Test 
{ 
	public static void main(String args[]) 
	{ 
		// lambda expression to implement above functional interface. 
		FuncInterface fobj = (int x)->System.out.println(2*x); 
		// This calls above lambda expression and prints 10. 
		fobj.abstractFun(5); 
	} 
} 
```

# Method references:
`(o) -> o.toString();` can become `Object::toString();`.

# Optional class:
- Prevents Null Pointer Exceptions or null handling.
```Java
int min1 = Arrays.stream(new int[]{1, 2, 3, 4, 5}).min().orElse(0);
int min2 = Arrays.stream(new int[]{}).min().orElse(0);
```

# Functional interfaces
- **Function** – it takes one argument and returns a result.
- **Consumer** – it takes one argument and returns no result (represents a side effect).
- **Supplier** – it takes no argument and returns a result.
- **Predicate** – it takes one argument and returns a boolean.
- **BiFunction** – it takes two arguments and returns a result.
- **BinaryOperator** – it is similar to a BiFunction, taking two arguments and returning a result. The two arguments and the result are all of the same types.
- **UnaryOperator** – it is similar to a Function, taking a single argument and returning a result of the same type.

# Default method
- Earlier we could not have function implementations in interfaces. Now we can using default methods.

https://www.baeldung.com/java-8-interview-questions
https://www.baeldung.com/java-8-functional-interfaces