# Supporting multiple types at once:
 - `Union[int, str]`

# Optionally None
 - `Optional[str]` == `Union[str, none]`
 - `def greeting(name: Optional[str] = None) -> str:`
 - `def greeting(name: str = None) -> str:` => Will also work automagically.

# Common examples
 - `Iterable[str]`
 - `my_global_dict: Dict[int, float] = {}`
 - `age: int = 1`
 - `x: List[Union[int, str]] = [3, 5, "test", "fun"]`
 - `x: Any = mystery_function()`

# Type aliasing
 - `Card = Tuple[str, str]`
 - `Deck = List[Card]`

# Importable types
 - `Mapping`
 - `MutableMapping`
 - `Sequence`
 - `Iterable`
 - `List`
 - `Set`
 - `Dict`
 - `Union`
 - `Any`
 - `Tuple`

# *Sequence* vs *Iterable*
 - Use `Iterable` for generic iterables (anything usable in `for`).
 - Use `Sequence` where a sequence (supporting `len` and `__getitem__`) is required.
```
def f(ints: Iterable[int]) -> List[str]:
    return [str(x) for x in ints]
```

# *Mapping* vs *MutableMapping*
 - `Mapping` describes a dict-like object (with `__getitem__`) that we won't mutate.
 - `MutableMapping` => (with `__setitem__`) that we might mutate.
```
def f(my_dict: Mapping[int, str]) -> List[int]:
    return list(my_dict.keys())
```

# Classes
```
class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[List[str]]
    def __init__(self) -> None:
        self.fuel: int = 100
        ...

x: MyClass = MyClass()
```

# Type-checking only code
 - Can be used to prevent *import cycles*:
```
if TYPE_CHECKING:
    import bar
```

# Templating using *TypeVar*
```
# Allows any type.
T = TypeVar("T")
# Only allows str or float.
T = TypeVar("T", str, float)

def choose(items: Sequence[T]) -> T:
    return random.choice(items)
```

If we had used `Any` instead of a custom TypeVar, then `choose(['a', 'b'])` would have returned a type of `Any` rather than `str`. That is, we would have lost type info.
To preserve type info, we use `Typevar`. It is similar to templating in C++.

```
T = TypeVar('T')

class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value
```

```
T = TypeVar('T')
S = TypeVar('S', int, str)

# Compounding generics.
class StrangePair(Generic[T, S]):
    ...
```

```
from typing import TypeVar, Generic, Sized

T = TypeVar('T')
# Multiple inheritance.
class LinkedList(Sized, Generic[T]):
```

# Protocols
```
from typing_extensions import Protocol

class Sized(Protocol):
    def __len__(self) -> int: ...

def len(obj: Sized) -> int:
    return obj.__len__()
```
We are able to specify a type just by defining the operations that it should support. Similar to typescript!

# Annotations
```
from __future__ import annotations

class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> 'Deck':
        ...
```
 - Useful in cases where the type is not defined completely when we are referencing it.
 - For example in **self-referential** structures.
 - No need to import in Python 3.7+.

# Callables
```
# func is a function which takes a `str` and returns a `str`.
def do_twice(func: Callable[[str], str], argument: str) -> None:
```

# Stubs
 - Stub files are files containing the type information for a Python module.
 - Available by default for for all the builtin packages and a few third-party ones.
 - Are stored in the `typeshed` Github repo which is automatically downloaded while installing `mypy`.

# Ignore checking
```
# Mypy will not complain now!
a = {} # type: ignore
```
[Source](https://realpython.com/python-type-checking/)
