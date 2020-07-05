Consider, for a moment, this simple function:

```python
def foo(num):
    num += 15
    return bar(num)
```

- So, what can you, or rather your language compiler, do?
- Well, what it can do is turn code of the form `return somefunc();` into the low-level sequence `pop stack frame; goto somefunc();`.
- In our example, that means before we call `bar`, `foo` cleans itself up and then, rather than calling `bar` as a subroutine, we do a low-level `goto` operation to the start of `bar`.
- `Foo`'s already cleaned itself out of the stack, so when `bar` starts it looks like whoever called `foo` has really called `bar`, and when `bar` returns its value, it returns it directly to whoever called `foo`, rather than returning it to `foo` which would then return it to its caller.

- **Tail recursion** happens if a function, as its last operation, **returns the result of calling itself**.
- Tail recursion is easier to deal with because rather than having to jump to the beginning of some random function somewhere, you just do a goto back to the beginning of yourself, which is a darned simple thing to do.

So that this:

```python
def foo (a, b):
    if (b == 1):
        return a
    else:
        return foo(a*a + a, b - 1)
```
 
gets quietly turned into:

```python
def foo(a, b):
    while True:
        if b == 1:
            return a
        else:
            a = a*a + a
            b = b - 1
```

Example 2:

```python
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
```
- This function does things besides call another function in its return statement.
- This below function is TCOptimizable:
```python
def fact_h(n, acc):
    if n == 0:
        return acc
    return fact_h(n-1, acc*n)

def fact(n):
    return fact_h(n, 1)
```