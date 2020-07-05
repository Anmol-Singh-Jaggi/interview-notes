# 2D Arrays Initialization

**Wrong way**<br>
`arr = [[0]*cols]*rows`<br>
`arr[0][0] = 5` will change the first element in all the rows.

What happens is that initially all the elements are referring to an object at the memory location, say `m1` with value `0`. When we execute `arr[0][0] = 5`, the reference `arr[0][0]` points to the object at the memory `m2`.

**Right way**<br>
`arr = [[0 for j in range(cols)] for i in range(rows)]`

[Source](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)

# `a+=b` is not same as `a = a + b` all the time

```
>>> list1 = [5, 4, 3, 2, 1]
>>> list2 = list1
>>> list1 += [1, 2, 3, 4]
>>> list2 is list1
True
```

```
>>> list1 = [5, 4, 3, 2, 1]
>>> list2 = list1
>>> list1 = list1 + [1, 2, 3, 4]
>>> list2 is list1
False
```

Basically, `+=` mutates the object if possible, else makes a new one and assigns to the old reference. [Source](https://stackoverflow.com/a/2347423/1925388)

# Taking multiple inputs from line

```
list_in = [int(x) for x in input("Enter multiple value: ").split()]
```

# Commonly-used functions

## Builtins

- `chr(<int>)`

  ```
  >>> chr(75)
  'K'
  ```

- `bin(<int>)`

  ```
  >>> bin(10)
  '0b1010'
  ```

- `divmod(x, y)` => Returns divisor and remainder.

  ```
  >>> divmod(13, 4)
  (3, 1)
  ```

- `any(iterable)` -> True if even 1 element is _Truthy_.
- `all(iterable)` -> True if all the elements are _Truthy_.
- `enumerate(iterable)` -> `(0, elem1), (1, elem2) ...`
- `filter(function, iterable)` -> Same as `(item for item in iterable if function(item))`.
- `hex(int1)` -> Returns the hex representation for `int1`.
- `ord('K')` -> Returns the unique integral unicode codepoint of a character.
- `reversed(seq)`
- `zip(iterable1, iterable2)`

  ```
  >>> x = [1, 2, 3]
  >>> y = [4, 5, 6]
  >>> zipped = zip(x, y)
  >>> list(zipped)
  [(1, 4), (2, 5), (3, 6)]
  >>> x2, y2 = zip(*zip(x, y))
  >>> x == list(x2) and y == list(y2)
  True
  ```

  - `enumerate(iterable) ~~ zip(range(len(iterable)), iterable)`

## Bitwise

- `x | y`
- `x & y`
- `x ^ y`
- `x >> N`
- `x << N`
- `~x`
- `x.bitlength()`

## Floats

- `x.as_integer_ratio()`
- `x.is_integer()`

## list

- `elem in list1`
- `list1 + list2`
- `list1 * 10` -> Be careful!!
- `list1[i]`
- `list1[i:j]`
- `list1[i:j:k]`
- `len(list1)`
- `min(list1)`
- `max(list1)`
- `list1.index(elem, start?, end?)` -> Throws exception if not found! list does not have a `find()` method unfortunately!
- `list1.count(x)`
- `list1[i] = elem`
- `list1[i:j] = [1,2,3]`
- `list1[i:j:k] = [1,2,3]`
- `del list1[i:j]` ~ `list1[i:j] = []`
- `del list1[i:j:k]` ~ `list1[i:j:k] = []`
- `list1.append(elem)`
- `list1.clear()`
- `list1.copy()`
- `list1.extend(list2)` ~ `list1 += list2`
- `list1.insert(i, elem)`
- `list1.pop(i)`
- `list1.remove(elem)` -> Throws exception if not found!
- `list1.reverse()`
- `list1.sort(key=lambda x: x.first, reverse?)`
- `list2 = sorted(list1, key?, reverse?)`

## string

- `str1.capitalize()` -> Only the first char capitalized.
- `str1.casefold()` -> Lower-case everything.
- `str1.count(str2)` -> Only finds non-overlapping substrings!
- `str1.endswith(str2)`
- `str1.startswith(str2)`
- `idx = str1.find(str2, start?, end?)`
- `idx = str1.index(str2, start?, end?)` -> Raises exception if not found!
- `str1.isalpha()` / `str1.isalnum()` / `str1.isdigit()`
- `', '.join(['1', '2', '3'])`
- `'1,2,3'.split(',', maxsplit?)`
- `str1.splitlines()`
- `str1.strip(' .#')`
- `str1.rstrip()` -> Only removes trailing chars.
- `str2 = str1.replace(old, new)`
- `str1.rfind()` -> Starts finding from the end.
- `table = str1.maketrans(old, new, remove?)` and `str2 = str1.translate(table)`

## set

- Is mutable and cannot be used for hashing. Use `frozenset` if mutable required.
- **No order is preserved! Its just a hash-set!**
- `x in set1`
- `len(set1)`
- `set1.isdisjoint(set2)` ~~ `not set1 & set2`
- `set1.issubset(set2)` ~~ `set1 <= set2` => If set1 is a subset of set2 (set1 might also be exactly same as set2).
- `set1 < set2` => If set1 is a _proper subset_ of set2 => Will return `False` if set1 is exactly equal to set2.
- `self.issuperset(other_set)` ~ `set1 >= set2`
- `set1 > set2`
- `set1.union(set2, set3, ...)` ~ `set1 | set2 | set3 & ...`
- `set1.intersection(set2, set3, ...)` ~ `set1 & set2 & set3 & ...`
- `set1.difference(set2)` ~ `set1 - set2` => Elements in set1 which are not in set2.
- `set1.symmetric_difference(set2)` ~ `set1 ^ set2` => Elements in set1 or set2 but not both.
- `set1.update(set2, set3, ...)` ~ `set1 |= set2 | set3 | ...` => Will mutate set1.
- `set1.intersection_update()` ~ `set1 &= ...`
- `set1.difference(set2)` ~ `set1 -= set2`
- `set1.symmetric_difference(set2)` ~ `set1 ^= set2`
- `set1.add(elem)`
- `set1.remove(elem)` => Will give exception if not found!
- `set1.discard(elem)` => Remove if present.
- `set1.pop()` => Remove random element.
- `set1.clear()`

## map

- **No order is preserved! Its just a hashmap!**
- `len(dict1)`
- `dict1[key1]` => Will raise exception if not found!!
- `dict1.get(key1, default_value)` => Will never raise Exception; Returns `None` if not found!
- `del dict1[key1]` => Exception if not found!
- `key1 in dict1`
- `dict1_keys = iter(dict1)` ~ `iter(dict1.keys())`
- `dict1_entries = dict1.items()`
- `dict1_values = dict1.values()`
- `dict1.clear()`
- `dict1.copy()` => Shallow-copy!
- `dict1.popitem()` => Return last inserted pair and remove it.
- The insertion order is preserved in Python 3.7+.

## import math

- `math.gcd(<int>, <int>)`
- `math.floor(<float>)`
- `math.ceil(<float>)`
- `math.factorial(<int>)`
- `math.isclose(<float>, <float>)` -> Are two floats almost equal???
- `math.pow(x, y, mod)` -> Same as `x**y % mod`.
- `math.log(x, base)`

## Global keyword

This works:

```
x = 10
def foo():
    print(x)
foo()
```

But this does not:

```
x = 10
def foo():
    # global x # Uncomment this to make it work!
    x+= 10
foo()
```

**You can only reference to a global variable for reading, not modifying it!**

```
x = 10
def foo():
    x = 5
    print(x)
foo()
print(x)

>>> 5
>>> 10
```

# Transforming a sequence

1. **List comprehensions**

  ```
  xs = []
  [x+2 for x in xs]
  ```

2. **Generators**:

  ```
  (x+2 for x in xs)
  ```

  But we will get an iterable, not a sequence.

3. **map()** We can also use `map`:

  ```
  map(lambda x: x+2, xs)
  ```

  Again, an iterable and not a sequence.

The list comprehension is the fastest.

However, it uses the most memory.

There is one gotcha:

```
>>> funcs = [lambda: x for x in [1, 2, 3, 4, 5]]
>>> [f() for f in funcs]
[5, 5, 5, 5, 5]
```

```
>>> funcs = map(lambda x: lambda: x, [1, 2, 3, 4, 5])
>>> [f() for f in funcs]
[1, 2, 3, 4, 5]
```

# Weak references

Used to not let an object linger in memory if it is being referenced only by caches etc.

```
import gc
import weakref


class MyClass:
    def __del__(self):
        '''
        Will be called when this object is garbage-collected.
        '''
        print('I am no more!!')


my_dict = {}


def foo():
    a = MyClass()
    global my_dict
    my_dict[1] = a
    # When there is a weak reference to `a`, it will be
    # garbage-collected just after this function exits.
    # my_dict[1] = weakref.ref(a)


foo()
gc.collect()
print('Garbage collection done!')
```

# Named Tuples

```
>>> Animal = namedtuple('Animal', 'name age type')
>>> perry = Animal(name="perry", age=31, type="cat")
>>> print(perry)
Animal(name='perry', age=31, type='cat')
>>> print(perry.name)
'perry'
```

# OrderedDict

- `self.popitem(last=True)` The pair is returned in LIFO order if last is true or FIFO order if false.
- `move_to_end(key, last=True)` Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist.

  ```
  # An ordered dictionary variant that remembers the order the keys were last inserted.
  # If a new entry overwrites an existing entry, the original insertion position is
  # changed and moved to the end:
  class LastUpdatedOrderedDict(OrderedDict):
   'Store items in the order the keys were last added'

   def __setitem__(self, key, value):
       super().__setitem__(key, value)
       super().move_to_end(key)
  ```

```
class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]
            # or just simply self.popitem(False)
```

# string

## Constants

- `string.ascii_lowercase` = `'abcdefghijklmnopqrstuvwxyz'`
- `string.ascii_uppercase` = `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'`
- `string.ascii_letters` = `'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'`
- `string.digits` = `'0123456789'`
- `string.hexdigits` = `'0123456789abcdefABCDEF'`
- `string.octdigits` = `'01234567'`
- `string.punctuation`
- `string.whitespace`
- `string.printable` = `digits` + `ascii_letters` + `punctuation` + `whitespace`.

## Formatting

```
"Harold's a clever {0!s}"         # Calls str() on the argument first
"Bring out the holy {name!r}"     # Calls repr() on the argument first
"More {!a}"                       # Calls ascii() on the argument first
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'

>>> '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
'a, b, c'

>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'

>>> '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
'c, b, a'

>>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
'abracadabra'

>>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
>>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
>>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
'Coordinates: 37.24N, -115.81W'
>>> coord = (3, 5)
>>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'

>>> name = "Eric"
>>> age = 74
>>> f"Hello, {name}. You are {age}."
'Hello, Eric. You are 74.'

>>> f"{2 * 37}"
'74'

>>> def to_lowercase(input):
...     return input.lower()

>>> name = "Eric Idle"
>>> f"{to_lowercase(name)} is funny."
'eric idle is funny.'

>>> f"{name.lower()} is funny."
'eric idle is funny.'

>>> name = "Eric"
>>> profession = "comedian"
>>> affiliation = "Monty Python"
>>> message = (
...     f"Hi {name}. "
...     f"You are a {profession}. "
...     f"You were in {affiliation}."
... )
>>> message
'Hi Eric. You are a comedian. You were in Monty Python.'

>>> f"{{74}}"
'{74}'
```

# Hashing

- Dont forget to override `__eq()__` and `__hash()__` methods for custom classes to be used as map/set keys.
- If you want to make an object unhashable, set `self.__hash__ = None`. The intepreter will raise an Exception if someone tries to use this in a hashing container.
- Dont try to reinvent the wheel. Use the hash methods of the builtin types wherever possible:

  ```
  class Point():
   def __init__(self, x, y):
       self._x = x
       self._y = y

   def __eq__(self, other):
       if not isinstance(other, Point):
           return False
       return self._x == other._x and self._y == other._y

   def __hash__(self):
       return hash(self._x) ^ hash(self._y)
  ```

- Hash implementation for builtin types might return different value for the same object in different interpreter runs: ```

  > > > hash("235") -310569535015251310

## Opening new Python console...

> > > hash("235") -310569535015251310 ``` This is because of different seed values as a security feature.

# Queue

- 3 types -> FIFO (`queue.Queue`), LIFO(`queue.LifoQueue`), PriorityQueue(`queue.PriorityQueue`).
- Lifo queue is basically a stack.
- These can be bounded -> `q1 = queue.Queue(max=100)`.

``` import queue
q1 = queue.Queue()
# q1 = queue.LifoQueue()
q1 = queue.Queue()
print(q1.qsize())
q1.put('hello')
q1.put(45)
print(q1.qsize())
print(q1.get())

q1 = queue.PriorityQueue()
print(q1.qsize())
q1.put((1, 'hello'))
q1.put((2, 45))
print(q1.qsize())
print(q1.get())
```

```
- `PriorityQueue` is a wrapper over `heapq` but it does not expose all the methods from heapq like `heappushpop()` and `heapreplace()` and `heapify()`.
- `PriorityQueue` is slower than `heapq` as it is thread-safe. So, in online coding rounds, use `heapq`, but in interviews use `PriorityQueue`.

## Deque
 - Basically a double-ended linked list.
 - Max size can be bounded.
 - `append(x)` -> Append to the right end.
 - `appendleft(x)` -> Append to the left end.
 - `extend(iterable)`
 - `extendleft(iterable)`
 - `pop()`
 - `popleft()`
 - `count(x)` -> Count instances of `x`.
 - `index(x, start?, stop?)` -> Find `x`.
 - `insert(pos, x)` -> Insert new element in between.
 - `remove(x)`
 - `reverse()`
 - `rotate(n=1)`
   - Rotate deque n elements to the right.
   - It is equivalent to:
```

for i in range(n): deq.appendleft(d.pop())

```
- If n is negative, rotate the other direction.
```

def roundrobin(*iterables): "roundrobin('ABC', 'D', 'EF') --> A D E B F C" iterators = deque(map(iter, iterables)) while iterators: try: while True: yield next(iterators[0]) iterators.rotate(-1) except StopIteration:

```
# Remove an exhausted iterator.
        iterators.popleft()
```

```
# Counter
 - Basically a dictionary of `<key>` vs a number, where that number is the frequency of that key.
 - Supports a lot of additional methods to support some statistical processing.
```

> > > # Tally occurrences of words in a list

> > > cnt = Counter() for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']: ... cnt[word] += 1 cnt Counter({'blue': 3, 'red': 2, 'green': 1})

# Find the ten most common words in Hamlet

> > > words = re.findall(r'\w+', open('hamlet.txt').read().lower()) Counter(words).most_common(10) [('the', 1143), ('and', 966), ('to', 762), ('of', 669), ('i', 631), ('you', 554), ('a', 546), ('my', 514), ('hamlet', 471), ('in', 451)]

> > > c = Counter(['eggs', 'ham']) c['bacon'] # count of a missing element is zero 0

> > > c = Counter(a=4, b=2, c=0, d=-2) sorted(c.elements()) ['a', 'a', 'a', 'a', 'b', 'b']

> > > c = Counter(a=4, b=2, c=0, d=-2) d = Counter(a=1, b=2, c=3, d=4) c.subtract(d) c Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})

> > > c = Counter(a=3, b=1) d = Counter(a=1, b=2) c + d # add (keeping only positive counts) Counter({'a': 4, 'b': 3}) c - d # subtract (keeping only positive counts) Counter({'a': 2}) c & d # intersection: min(c[x], d[x]) # doctest: +SKIP Counter({'a': 1, 'b': 1}) c | d # union: max(c[x], d[x]) Counter({'a': 3, 'b': 2}) ```

- **WARNING:** `c1 + c2` is not the same as `c1.update(c2)`!!

# Fractions

```
>>> from fractions import Fraction
>>> Fraction(16, -10)
Fraction(-8, 5)
>>> Fraction(123)
Fraction(123, 1)
>>> Fraction()
Fraction(0, 1)
>>> Fraction('3/7')
Fraction(3, 7)
>>> Fraction(' -3/7 ')
Fraction(-3, 7)
>>> Fraction('1.414213 \t\n')
Fraction(1414213, 1000000)
>>> Fraction('-.125')
Fraction(-1, 8)
>>> Fraction('7e-6')
Fraction(7, 1000000)
>>> Fraction(2.25)
Fraction(9, 4)
>>> Fraction(1.1)
Fraction(2476979795053773, 2251799813685248)
>>> from decimal import Decimal
>>> Fraction(Decimal('1.1'))
Fraction(11, 10)
```

# Decimal

```
>>> getcontext().prec = 28
>>> Decimal(10)
Decimal('10')
>>> Decimal('3.14')
Decimal('3.14')
>>> Decimal(3.14)
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> Decimal((0, (3, 1, 4), -2))
Decimal('3.14')
>>> Decimal(str(2.0 ** 0.5))
Decimal('1.4142135623730951')
>>> Decimal(2) ** Decimal('0.5')
Decimal('1.414213562373095048801688724')
>>> Decimal('NaN')
Decimal('NaN')
>>> Decimal('-Infinity')
Decimal('-Infinity')

>>> data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
>>> max(data)
Decimal('9.25')
>>> min(data)
Decimal('0.03')
>>> sorted(data)
[Decimal('0.03'), Decimal('1.00'), Decimal('1.34'), Decimal('1.87'),
 Decimal('2.35'), Decimal('3.45'), Decimal('9.25')]
>>> sum(data)
Decimal('19.29')
>>> a,b,c = data[:3]
>>> str(a)
'1.34'
>>> float(a)
1.34
>>> round(a, 1)
Decimal('1.3')
>>> int(a)
1
>>> a * 5
Decimal('6.70')
>>> a * b
Decimal('2.5058')
>>> c % a
Decimal('0.77')

>>> getcontext().prec = 28
>>> Decimal(2).sqrt()
Decimal('1.414213562373095048801688724')
>>> Decimal(1).exp()
Decimal('2.718281828459045235360287471')
>>> Decimal('10').ln()
Decimal('2.302585092994045684017991455')
>>> Decimal('10').log10()
Decimal('1')
```

# Functools

## LRU Cache

```
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> [fib(n) for n in range(16)]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

>>> fib.cache_info()
CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
```

## @total_ordering

- Given a class defining one or more rich comparison ordering methods, this class decorator supplies the rest.
- This simplifies the effort involved in specifying all of the possible rich comparison operations:
- The class must define one of `__lt__()`, `__le__()`, `__gt__()`, or `__ge__()`. In addition, the class should supply an `__eq__()` method.

  ```
  @total_ordering
  class Student:
   def _is_valid_operand(self, other):
       return (hasattr(other, "lastname") and
               hasattr(other, "firstname"))
   def __eq__(self, other):
       if not self._is_valid_operand(other):
           return NotImplemented
       return ((self.lastname.lower(), self.firstname.lower()) ==
               (other.lastname.lower(), other.firstname.lower()))
   def __lt__(self, other):
       if not self._is_valid_operand(other):
           return NotImplemented
       return ((self.lastname.lower(), self.firstname.lower()) <
               (other.lastname.lower(), other.firstname.lower()))
  ```

- Note that this is slightly slower than doing it manually.

## Partial functions

- Return a new partial object which when called will behave like `func` called with the positional arguments `args` and keyword arguments `keywords`.
- If more arguments are supplied to the call, they are appended to args.
- If additional keyword arguments are supplied, they extend and override keywords.
- Roughly equivalent to:

  ```
  def partial(func, *args, **keywords):
   def newfunc(*fargs, **fkeywords):
       newkeywords = keywords.copy()
       newkeywords.update(fkeywords)
       return func(*args, *fargs, **newkeywords)
   # Need to set these attributes to comply with the partial function spec.
   newfunc.func = func
   newfunc.args = args
   newfunc.keywords = keywords
   return newfunc
  ```

- The `partial()` is used for partial function application which "freezes" some portion of a function's arguments and/or keywords resulting in a new object with a simplified signature.
- For example, `partial()` can be used to create a callable that behaves like the `int()` function where the base argument defaults to two:

  ```
  >>> from functools import partial
  >>> basetwo = partial(int, base=2)
  >>> basetwo.__doc__ = 'Convert base 2 string to an int.'
  >>> basetwo('10010')
  18
  ```

# operator

- Standard operators as functions.
- `operator.add(x, y)` is equivalent to the expression `x+y`.

  ```
  operator.lt(a, b)
  operator.le(a, b)
  operator.eq(a, b)
  operator.ne(a, b)
  operator.ge(a, b)
  operator.gt(a, b)
  operator.not_(obj)
  operator.truth(obj)
  operator.is_(a, b)
  operator.is_not(a, b)
  # And many more...
  ```

  ## operator.attrgetter(*attrs)

- Return a callable object that fetches an attribute from its operand.
- If more than one attribute is requested, returns a tuple of attributes.
- The attribute names can also contain dots.

  ```
  >>> f = attrgetter('name') # f(b) returns `b.name`.
  >>> f = attrgetter('name', 'date') # f(b) returns (b.name, b.date).
  >>> f = attrgetter('name.first', 'name.last') # f(b) returns (b.name.first, b.name.last)
  ```

Equivalent to:

```
def attrgetter(*items):
    if any(not isinstance(item, str) for item in items):
        raise TypeError('attribute name must be a string')
    if len(items) == 1:
        attr = items[0]
        def g(obj):
            return resolve_attr(obj, attr)
    else:
        def g(obj):
            return tuple(resolve_attr(obj, attr) for attr in items)
    return g

def resolve_attr(obj, attr):
    for name in attr.split("."):
        obj = getattr(obj, name)
    return obj
```

## operator.methodcaller(name[, args...])

```
>>> f = methodcaller('name') # f(b) returns b.name().
>>> f = methodcaller('name', 'foo', bar=1) # f(b) returns b.name('foo', bar=1).
```

## operator.itemgetter(*items)

```
>>> f = itemgetter(2) # f(r) returns r[2].
>>> g = itemgetter(2, 5, 3) #g(r) returns (r[2], r[5], r[3]).
```

# bisect

- `bisect_left(items, val)` is exactly same as c++ `lower_bound()`. Meaning it returns the lowest index such that `items[index] >= val`.
- `bisect_right(items, val)` is exactly same as c++ `upper_bound()`. Meaning it returns the lowest index such that `items[index] > val`.
- We can count the number of occurences of a value in a sorted array by: `bisect_right(items, val) - bisect_left(items, val)`
- Note that `bisect.bisect()` defaults to `bisect.bisect_right()`. ``` def index(a, x): 'Locate the leftmost value exactly equal to x' i = bisect_left(a, x) if i != len(a) and a[i] == x:

  ```
  return i
  ```

   raise ValueError

def find_lt(a, x): 'Find rightmost value less than x' i = bisect_left(a, x) if i: return a[i-1] raise ValueError

def find_le(a, x): 'Find rightmost value less than or equal to x' i = bisect_right(a, x) if i: return a[i-1] raise ValueError

def find_gt(a, x): 'Find leftmost value greater than x' i = bisect_right(a, x) if i != len(a): return a[i] raise ValueError

def find_ge(a, x): 'Find leftmost item greater than or equal to x' i = bisect_left(a, x) if i != len(a): return a[i] raise ValueError

```

```

> > > def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'): ... i = bisect(breakpoints, score) ... return grades[i] ... [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]] ['F', 'A', 'C', 'C', 'B', 'A', 'A'] ```

```
# bisect() does not support `key` parameter!
>>> data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
>>> data.sort(key=lambda r: r[1])
>>> keys = [r[1] for r in data]         # precomputed list of keys
>>> data[bisect_left(keys, 0)]
('black', 0)
>>> data[bisect_left(keys, 1)]
('blue', 1)
```

For a beautiful use-case of this, see [SortedCollection.py](code/SortedCollection.py).

# heapq

- Zero-indexed min-heap.
- `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]`.
- Multiply the numbers by -1 to get a max-heap.
- For other data types, create a custom class wrapper with inverted comparator functions.<br>
  (Just overwrite `__eq__` and `__lt__` and use `@total_ordering`).

  ```
  >>> def heapsort(iterable):
  ...     h = []
  ...     for value in iterable:
  ...         heappush(h, value)
  ...     return [heappop(h) for i in range(len(h))]
  ...
  >>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

```
>>> h = []
>>> heappush(h, (5, 'write code'))
>>> heappush(h, (7, 'release product'))
>>> heappush(h, (1, 'write spec'))
>>> heappush(h, (3, 'create tests'))
>>> heappop(h)
(1, 'write spec')
```

- `heappush(heap, item)`
- `heappop(heap)`
- `heap[0]` -> Just read the smallest element.
- `heappushpop(heap, item)`

  - Faster than `heappush()` followed by `heappop()`.

- `heapify(list1)`' -> Transform list to heap in-place.
- `heapreplace(heap, item)`

  - Faster than `heappop()` followed by `heappush()`.

- `merge(*iterables)` -> Merge multiple sorted **lists** (not heaps).
- `nlargest(n, iterables)` -> Works on any iterable, not only heaps.
- `nsmallest()`

# Itertool

## Infinite iterators

- `count(start, step?)`

  ```
  count(10) --> 10 11 12 13 14 ...
  ```

- `cycle(iterable)`

  ```
  cycle('ABCD') --> A B C D A B C D ...
  ```

- `repeat(elem, n?)`

  ```
  repeat(10, 3) --> 10 10 10
  ```

## Finite iterators

- `accumulate(iterable, func)`

  ```
  accumulate([1,2,3,4,5]) --> 1 3 6 10 15
  accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
  # We can also compute running max, min etc.
  # Also useful for implementing recurrence relations.
  # Note that `functools.reduce()` also does a similar thing but returns only the last value.
  ```

- `chain(*iterables)`

  ```
  chain('ABC', 'DEF') --> A B C D E F
  ```

- `chain.from_iterable(iterable)`

  ```
  chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
  ```

- `compress(iterable, selectors)`

  ```
  compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
  ```

- `dropwhile(pred, iterable)`

  ```
  dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
  ```

- `takewhile(pred, seq)`

  ```
  takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
  ```

- `filterfalse(pred, iterable)`

  ```
  filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
  ```

- `groupby()` - ???
- `islice(seq, start?, stop?, step?)`

  ```
  islice('ABCDEFG', 2, None) --> C D E F G
  ```

- `starmap(func, seq)`

  ```
  starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
  ```

- `tee(iterator, n)` -> ??
- `zip_longest(*iterables)`

  ```
  zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
  ```

## Combinatoric iterators:

- `product(*iterables, repeat=1)` -> Cartesian product, equivalent to a nested for-loop.

  ```
  >>> product('ABCD', repeat=2)
  AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
  ```

- `permutations(iterable, r?)` -> r-length tuples, all possible orderings, no repeated elements.

  ```
  >>> permutations('ABCD', 2)
  AB AC AD BA BC BD CA CB CD DA DB DC
  ```

- `combinations(p, r?)` -> r-length tuples, in sorted order, no repeated elements.

  ```
  >>> combinations('ABCD', 2)
  AB AC AD BC BD CD
  ```

- `combinations_with_replacement()` -> r-length tuples, in sorted order, with repeated elements.

  ```
  >>> combinations_with_replacement('ABCD', 2)
  AA AB AC AD BB BC BD CC CD DD
  ```

# Fast I/O

```
from sys import stdin, stdout

# Instead of input() and print():
num = int(stdin.readline())
stdout.write(str(num) + '\n')
# WARNING: readline() contains a newline at the end !!!
```

```
import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())
```

# Default mutable arguments

```
def foo(a=[]):
    a.append(5)
    return a

>>> foo()
[5]
>>> foo()
[5, 5]
>>> foo()
[5, 5, 5]
>>> foo()
[5, 5, 5, 5]
>>> foo()
```

```
def bar(a=[]):
     print id(a)
     a = a + [1]
     print id(a)
     return a

>>> bar()
4484370232
4484524224
[1]
>>> bar()
4484370232
4484524152
[1]
>>> bar()
4484370232 # Never change, this is 'class property' of the function
4484523720 # Always a new object 
[1]
>>> id(bar.func_defaults[0])
4484370232
```

```
def foo(mutable_default_argument=[]): # make a list the default argument
    """function that uses a list"""
```

is almost exactly equivalent to this:

```
_a_list = [] # create a list in the globals

def foo(mutable_default_argument=_a_list): # make it the default argument
    """function that uses a list"""

del _a_list # remove globals name binding
```

How to properly assign default args:

```
def foo(default_kwarg=None):
    if default_kwarg is None:
        default_kwarg = []
```

On other hand, we can use this for `static variables`, but please no!!

# yield in recursive functions

Lets say we are writing a function to generate all the permutations of a string:

```
def print_permutations_wrapper(str):
    strList = str.split()
    print_permutations(strList, 0, len(strList))


def print_permutations(strList: list, start: int, end: int):
    if start >= end - 1:
        print(strList)
        return

    print_permutations(strList, start+1, end)
    for i in range(start+1, end):
        strList[start], strList[i] = strList[i], strList[start]
        print_permutations(strList, start+1, end)
        strList[i], strList[start] = strList[start], strList[i]


def main():
    str = 'a b c'
    print_permutations_wrapper(str)


if __name__ == "__main__":
    main()
```

But now instead of printing, we need to return it lazily:

```
def print_permutations_wrapper(str):
    strList = str.split()
    yield from print_permutations(strList, 0, len(strList))


def print_permutations(strList: list, start: int, end: int):
    if start >= end - 1:
        yield strList
        return

    yield from print_permutations(strList, start+1, end)
    for i in range(start+1, end):
        strList[start], strList[i] = strList[i], strList[start]
        yield from print_permutations(strList, start+1, end)
        strList[i], strList[start] = strList[start], strList[i]


def main():
    str = 'a b c'
    x = print_permutations_wrapper(str)
    print(list(x))

if __name__ == "__main__":
    main()
```

First of all, notice the use of `yield from`.<br>
Second of all, this will give a wrong answer; the returning list will have the same string `n!` times.<br>
To correct this, replace `yield strList` with `yield list(strList)` to produce a new shallow copy of the list while returning.

# Function static variables

```python
def foo():
    pass

foo.lol = 5
print(foo.lol)
```
