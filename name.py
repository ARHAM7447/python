# Save the detailed explanation as a commented Python file for GitHub

name_main_explained_code = '''\
"""
✅ Understanding __name__ and "__main__" in Python – Beginner Friendly Guide

📘 What is __name__?

Every Python file has a built-in variable called __name__.

- When you run the file directly using `python filename.py`, Python sets:
    __name__ = "__main__"
- When you import the file in another script, Python sets:
    __name__ = "module_name" (i.e., the name of the file without `.py`)

👉 This helps Python know whether the file is being run directly or being imported.

---

🔍 Why do we use `if __name__ == "__main__"`?

This is a common Python idiom that tells Python:
    "Only run this block of code if the script is being run directly, not if it’s imported."

This is useful when:
- You want to test functions within the same file
- You want to avoid executing code when the file is imported elsewhere

---

✅ Example 1: Running a File Directly
"""

# file: hello.py
print("Hello file's name is:", __name__)

if __name__ == "__main__":
    print("✅ This runs only when you run hello.py directly")

"""
🔸 When you run: python hello.py
Output:
Hello file's name is: __main__
✅ This runs only when you run hello.py directly

🔸 When you import it in another file:
# file: main.py
import hello

Output:
Hello file's name is: hello
(Notice that the code inside `if __name__ == "__main__"` does NOT run.)

---

✅ Real-Life Example: Testing a Function
"""

# file: calculator.py

def add(a, b):
    return a + b

# Only run this block when executed directly
if __name__ == "__main__":
    print("Testing add():", add(2, 3))  # Output: 5

"""
In another file:
# file: main.py
from calculator import add
print(add(10, 5))  # This works fine, and the test code in calculator.py does NOT run

---

📌 Summary Table

| Situation                      | __name__ value   | Will `if __name__ == "__main__"` block run? |
| ----------------------------- | ---------------- | -------------------------------------------- |
| Run file directly             | "__main__"       | ✅ Yes                                       |
| Import file into another file | "filename"       | ❌ No                                        |

---

🧠 Best Practice:

Always use:
    if __name__ == "__main__":
        # put test code or main program logic here

This ensures your module can be reused and tested cleanly without unintended side effects.
"""
'''

with open("/mnt/data/name_main_explained.py", "w") as f:
    f.write(name_main_explained_code)

"/mnt/data/name_main_explained.py"

