- First of all, remember that one major purpose of using design patterns is to avoid excessive code in one class.
- These are just tricks on how to divide code among multiple classes.

# Behavioral

## Strategy
- When we have multiple algorithms to choose to perform an operation.
- Graph routing - Walk/Road/Air.
- Sorting - Bubble/Merge.
- Payment modes - Paypal/Paytm/Card.
- `Comparator` classes in Java.
- HashMap vs BST for an index class.
- Akka supervision.

## Template
- When we have a few functions which can have some default implementation, but the nested functions need to be overriden.
- Generic build tool - `void build(){ Test -> Lint -> Assemble -> Deploy}`.
- Generic data parser - `_openFile()_ -> _extractData()_ -> _parseData()_ -> analyze() -> report() -> compress() ..`
- Event parser generator - Abstract class will have methods `gather_data()`, `send_data()`, `process()`, `wait()`. Children will only implement `gather_data()`.
  Because `send_Data()` is simply creating a json and posting http call, and `process()` is simply calling `gather() -> Send() -> wait()` in a loop.

## Visitor
- When we need to add a new functionality to a collection of classes without modifying those classes.
- XML/CSV/JSON exporter for graphic image.
- Employee report generation.

## State
- When we want to simulate state automaton (too many states and transitions).
- Music player state automaton -> `onPlay(), onPause(), onLock(), onNext(), onRewind() ...`

## Observer
- When we want to do some operations whenever the state of another object changes.
- News publisher -> SMS subscriber, Email subscriber...
- File change listener -> Log subscriber, email subscriber ...

## Memento
- Whenever want to implement `undo` operations.
- Calculator undo.
- Editor undo.
- Paint undo.

## Iterator
- When we want to iterate over a collection without corrupting it by mistake.
- Tree iterator.
- Graph iterator.

## Command
- When there can be multiple places calling the same set of functions of an object.
- Editor commands - copy/cut/paste being called from various buttons.
- Parking lot input parsing (See parking lot design).

## Chain-of-responsibility
- When objects can handle an operation in chains.
- Help menu for a graphic window(button -> dialog -> window).
- Parking lot input parsing. (See the parking lot design).

# Creational

## Singleton
- When we want to allow only a single instance of a class.
- Logger.
- Configuration object.

## Builder
- When the constructor is having too many arguments.
- SQL Builder -> Fantastic example.
- Car builder with director.
- Setting up Camunda ProcessEngineConfig object.

## Prototype
- When we want to clone an object.
- Just implement `clone()` on any class.

## Simple Factory
- When object creation is very complicated.
- Any situation where creation of object is complex.
- House requires kitchen, TV and LivingRoom. These objects further require their own params.

## Abstract Factory
- When a certain collection of multiple objects are to be always created together.
- Windows/Linux/Max specific GUI elements(buttons/windows/dialogs).
- US and England specific Phone-number and addresses.

## Factory Method
- When a class can perform an operation with objects from many types of (related) objects.
- Content writer -> `encrypt()` and `compress()` abstract methods + `save_to_file()` default method.
- Document creator - PDF/HTML -> `createDocument()` abstract + `write()` and `read()` default methods.
- Social network posters - Facebook/Linkedin/Orkut -> `login()`, `logout()`, `publishPost()` abstract + `post()` default method.
- Hiring manager + Interviewer - Developer/Marketing/Accountant -> `makeInterviewer()` abstract + `takeInterview()` default.
- Dialog(Windows/Linux/Web) rendered - `createButton()` abstract + `renderDialog()` default.

# Structural

## Adapter
- Basically creating a new class having the necessary interface to be sent to an API requiring that interface.
- Notification -> Email vs Slack API.
- XML to JSON adapter for an api which only accepts JSON.

## Bridge
- When we have 'n' varieties(subclasses) of class A and 'm' of class B, and we can combine them.
- So instead of creating n * m different classes, just create n+m classes.
- Windows/Mac/Linux dialog + Dark/White/Monokai theme.
- Dialog/Button/Window + Dark/White/Monokai theme.

## Composite
- When we have to model a tree-like structure of objects, and the operation on the root can be done by aggregating the results of the operations on the children.
- HTML form -> Fieldset, InputBox, Button -> `render()`.
- Composite graphics -> Dot, Image, CompoundGraphic. -> `draw()`/`move()`.

## Decorator
- When we want to add/enhance a functionality to an object at runtime.
- Encryptor + Compressor read/write decorator.
- Comment filter decorator -> AbusiveTextFilter -> MarkdownToHtml -> HtmlTagStripping -> JSFilter
- Notifier -> Facebook + Slack + SMS.

## Facade
- Basically encapsulating the major functionality of a class in a single method.
- VideoConverter -> `convertVideo()` -> Internally does a lot of stuff.

## Proxy
- When we want to control the creation/destruction or do certain pre/post checks.
- Caching.
- Remote method invocation.
- Security check.

## Flyweight
- When too many heavy objects are created which share some data.
- Bullets in game -> Intrinsic(texture, sprite) and extrinsic(velocity, position, src, dst).
- Font characters in a text editor -> Intrinsic(font, texture) and intrinsic(position, size).

# Favourite patterns:
- Strategy
- Template
- Observer
- Prototype
- Builder
- Composite
- Acronym -> **STOP BC!!**