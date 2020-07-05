# parking-lot

# Dependencies:
- Python3.

# How to run:
- cd into `solution/parking_lot`.
- Execute `python3 Driver.py /foo/in.txt` for file input.
- Execute `python3 Driver.py` for interactive session.
- You can also execute `bin/parking_lot` to do the same.

# Automated tests
- The ruby automated tests are throwing an error `No such file or directory - fork failed`, even though the `bin/parking_lot` command is running perfectly.
- I am not able to debug the error as I am not familiar with Ruby.
- I have setup multiple automated tests in Python including the one present in the ruby fixtures directory.
- To execute them: cd into `solution/tests` and run `export PYTHONPATH='../parking_lot' && python tests.py`.

# Design patterns used:
- Strategy.
- Chain of responsibility.
- Command.
- Template.

----

- Thank you for the extremely interesting problem.
- I had a lot of fun designing it :)