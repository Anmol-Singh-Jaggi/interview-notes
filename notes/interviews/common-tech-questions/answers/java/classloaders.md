# Types of classloaders:

## Bootstrap ClassLoader
- This classloader prime responsibility is to load internal core java classes present in the `rt.jar` and other classes present in the `java.lang.*` package.
- This class loader is shipped with every JVM and is written in native language.
- This class loader has no parent classloader.

## Extension ClassLoader
- This classloader responsibility is to load classes from `jre\lib\ext` folder.
- The parent of this class loader is Bootstrap classloader.
- Java extensions are also referred to as optional packages.

## System ClassLoader
- The parent of this class loader is Extension classloader.
- Responsible for loading the classes from the system classpath.

# Classloading flow
- Each classloader has a parent classloader.
- Each classloader has 2 methods `loadClass()` and `findClass()`.
- The `loadClass()` method does this:
  - Returns the class if it is already loaded.
  - Otherwise, delegates to parent; `parent.loadClass()`.
  - If parent is not able to find, then calls `findClass()` to find and load the class.
- The class `java.net.URLClassLoader` serves as the basic class loader for extensions and other JAR files, overriding the `findClass` method of to search one or more specified URLs for classes and resources.
- Note: Class is loaded into memory only once even if you try to load multiple times.