```java
// This is the part of com.mysql.jdbc.Driver which registers itself with DriverManager
// Register ourselves with the DriverManager
// It should be noted that since ver 1.6 there is no need to explictly load JDBC drivers using Class.forName().
// DriverManager can detect JDBC 4.0 Drivers automatically using Service Provider mechanism.
static {
    try {
        java.sql.DriverManager.registerDriver(new Driver());
    } catch (SQLException E) {
        throw new RuntimeException("Can't register driver!");
    }
}
```

- JDBC 4.0 Drivers must include the file `META-INF/services/java.sql.Driver`.
- This file contains the name of the JDBC drivers implementation of `java.sql.Driver`.
For example, to load the `my.sql.Driver class`, the `META-INF/services/java.sql.Driver` file would contain the entry:
```
my.sql.Driver
```
- Applications no longer need to explictly load JDBC drivers using `Class.forName()`.
- Existing programs which currently load JDBC drivers using `Class.forName()` will continue to work without modification.
- If you check the source code you will see that Java does not try to detect the driver's implementation name (i.e. the driver class) from the url.
- Instead it asks each driver implementation it finds in the classpath if they are able to handle that url or not.
- The order of actions seems to be the following:
  - When you ask for the connection the DriverManager class is loaded.
  - It executes a static block that loads all the classes specified in the system property `jdbc.drivers`.
  - Then the Service Provider Mechanism is invoked and loads all classes of `java.sql.driver` it finds in the classpath.
  - Now when you ask it for a connection it loops through the registered drivers and call the `Driver.connect(String url, Properties info)` method on them, which attempts to make a database connection to the given URL.
  - The driver should return "null" if it realizes it is the wrong kind of driver to connect to the given URL.
  - The driver should throw an SQLException if it is the right driver to connect to the given URL but has trouble connecting to the database.
  - So the first driver that returns a non null connection is the driver that will be used.