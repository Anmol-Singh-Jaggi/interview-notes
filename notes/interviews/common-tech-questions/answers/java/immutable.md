# How to make any class immutable
- Make all the fields final and private.
- Dont provide setter methods.
- In getter methods, while returning mutable types like `List`, return a deep copy instead.
- Make the class itself final so that nobody can extend it.

## Reason for making the class final:

```java
public class Immutable{
     private final int value;

     public Immutable(int value) {
         this.value = value;
     }

     public int getValue() {
         return value;
     }
}

public class Mutable extends Immutable {
     private int realValue;

     public Mutable(int value) {
         super(value);
         realValue = value;
     }

     public int getValue() {
         return realValue;
     }
     public void setValue(int newValue) {
         realValue = newValue;
     }
}

public void foo(Immutable imm){
    // In thread 1
    imm.getValue();
    // Note that apart from this race condition, there is one more concern.
    // This object imm which is actually a Mutable cannot be used in a hashmap since its value changes.
    // However since the object is marked as Immutable, someone might get confused.
}

public static void main(String[] arg){
        Mutable obj = new Mutable(4);
        foo(obj);

        // In thread 2.
        obj.setValue(8);
}
```