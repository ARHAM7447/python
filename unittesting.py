# Save the content as a Python file with all details in comments for GitHub

unittest_notes_code = '''\
"""
✅ Python Unittest Library – Running Tests

📘 What is Unittest in Python?

`unittest` is a built-in Python module used for writing and running tests.
It helps verify that code works correctly by checking if functions return expected results.

🧪 Why Use Unittest?

- Automatically test your code
- Catch bugs early
- Ensure code changes don’t break existing functionality (regression)
- Support test automation
"""

# 🔹 1. Writing Your First Test

# Example function
def add(x, y):
    return x + y

# Import unittest
import unittest

# Create a test case by subclassing unittest.TestCase
class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        # ✅ Basic usage of assertEqual
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

# 🔹 2. Commonly Used Assertions (used in practice):
# - assertEqual(a, b)
# - assertNotEqual(a, b)
# - assertTrue(x)
# - assertFalse(x)
# - assertIsNone(x)
# - assertIsNotNone(x)
# - assertIn(a, b)

# 🔹 3. Example: Testing Multiple Functions
def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

# Define test cases
class TestCalc(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertIsNone(divide(10, 0))  # division by zero returns None

# 🔹 4. Run Unittest from terminal or VS Code
# Option 1: python test_file.py
# Option 2: python -m unittest test_file.py

# 🔹 5. Output:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# OK

# ✅ Each dot (.) means one test passed
# ❌ Failures will show detailed errors

# 🔹 6. Best Practices
# - Keep test files prefixed with "test_"
# - Each test method should start with "test_"
# - Separate test code from main code (e.g., test_calc.py and calc.py)

# ✅ Summary
# - unittest.TestCase: Base class for testing
# - test_ prefix: Needed to identify test methods
# - assert methods: Used to verify behavior
# - unittest.main(): Runs all test cases

# Run the test suite
if __name__ == '__main__':
    unittest.main()
'''

with open("/mnt/data/unittest_notes.py", "w") as f:
    f.write(unittest_notes_code)

"/mnt/data/unittest_notes.py"

# this is the seconr file to be saved

# Rewriting the file after code state reset

unittest_notes_code = '''\
"""
✅ Python Unittest Library – Running Tests

📘 What is Unittest in Python?

`unittest` is a built-in Python module used for writing and running tests.
It helps verify that code works correctly by checking if functions return expected results.

🧪 Why Use Unittest?

- Automatically test your code
- Catch bugs early
- Ensure code changes don’t break existing functionality (regression)
- Support test automation
"""

# 🔹 1. Writing Your First Test

# Example function
def add(x, y):
    return x + y

# Import unittest
import unittest

# Create a test case by subclassing unittest.TestCase
class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        # ✅ Basic usage of assertEqual
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

# 🔹 2. Commonly Used Assertions (used in practice):
# - assertEqual(a, b)
# - assertNotEqual(a, b)
# - assertTrue(x)
# - assertFalse(x)
# - assertIsNone(x)
# - assertIsNotNone(x)
# - assertIn(a, b)

# 🔹 3. Example: Testing Multiple Functions
def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return None
    return x / y

# Define test cases
class TestCalc(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertIsNone(divide(10, 0))  # division by zero returns None

# 🔹 4. Run Unittest from terminal or VS Code
# Option 1: python test_file.py
# Option 2: python -m unittest test_file.py

# 🔹 5. Output:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s
# OK

# ✅ Each dot (.) means one test passed
# ❌ Failures will show detailed errors

# 🔹 6. Best Practices
# - Keep test files prefixed with "test_"
# - Each test method should start with "test_"
# - Separate test code from main code (e.g., test_calc.py and calc.py)

# ✅ Summary
# - unittest.TestCase: Base class for testing
# - test_ prefix: Needed to identify test methods
# - assert methods: Used to verify behavior
# - unittest.main(): Runs all test cases

# Run the test suite
if __name__ == '__main__':
    unittest.main()
'''

with open("/mnt/data/unittest_notes.py", "w") as f:
    f.write(unittest_notes_code)

"/mnt/data/unittest_notes.py"

