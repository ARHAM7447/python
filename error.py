# Save the content as a commented Python file for GitHub repo use in VS Code

from pathlib import Path

# Define path and content
file_path = Path("/mnt/data/errors_and_exception_handling_notes.py")

commented_content = """\
# 🐍 Python Errors and Exception Handling – Beginner Notes with Examples

# 📘 Introduction
# Errors are problems in a program that can cause it to crash.
# In Python, exception handling is used to catch and manage errors so the program can continue running.

# 🔹 1. Types of Errors in Python

# ✅ Syntax Error
# Occurs when the code structure is incorrect.
# Example:
# print("Hello"

# ✅ Runtime Error (Exception)
# Occurs during program execution.
# Example:
# x = 10 / 0

# 🔹 2. Common Exceptions in Python

# | Exception Type      | Description                           |
# | ------------------- | ------------------------------------- |
# | ZeroDivisionError   | Division by zero                      |
# | ValueError          | Invalid value for data type           |
# | TypeError           | Unsupported operation between types   |
# | IndexError          | Invalid list index                    |
# | KeyError            | Accessing non-existent dictionary key |
# | FileNotFoundError   | File not found                        |
# | NameError           | Using an undefined variable           |

# 🔹 3. Exception Handling Using try-except

# ✅ Basic Syntax
# try:
#     # Code that might raise an exception
# except ExceptionType:
#     # Code to handle the exception

# ✅ Example
try:
    a = int(input("Enter a number: "))
    result = 10 / a
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
except ValueError:
    print("❌ Please enter a valid number.")

# 🔹 4. Handling Multiple Exceptions
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

# 🔹 5. Catching All Exceptions
try:
    a = int(input("Enter a number: "))
    b = 10 / a
except Exception as e:
    print("An error occurred:", e)

# 🔹 6. Using else with try-except
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("You entered:", x)

# 🔹 7. finally Block
try:
    file = open("sample.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs.")

# 🔹 8. Raising Exceptions Manually
age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("You must be at least 18 years old.")
else:
    print("Access granted.")

# 🔹 9. Creating Custom Exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception.")
except CustomError as ce:
    print("Caught custom exception:", ce)

# 🔹 10. Full Practice Program
def divide_numbers():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    except ValueError:
        print("❌ Please enter valid numbers.")
    else:
        print("✅ Result:", result)
    finally:
        print("✔️ Program ended.")

divide_numbers()

# 📌 Summary of Exception Handling Blocks
# try:     Wraps code that may cause an error
# except:  Catches and handles the error
# else:    Executes if no exception occurs
# finally: Always runs regardless of error
# raise:   Used to manually throw an exception

# ✅ Best Practices
# - Always catch specific exceptions.
# - Use `finally` for cleanup tasks like closing files or freeing resources.
# - Avoid catching all exceptions unless necessary.
# - Use logging instead of print statements in real-world projects.
"""

# Write to file
file_path.write_text(commented_content)
file_path

