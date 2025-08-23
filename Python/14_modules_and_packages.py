# 1. What is a Module?
# -----------------------------------------------------------------------------------------------
'''
A module means a single .py file.
You can import it and use it in other files!

Commonly Used Built-in Modules
| Module Name  | Description                                                   |
|--------------|---------------------------------------------------------------|
| os           | Interact with the operating system (files, directories, etc.) |
| sys          | Access Python interpreter-related functions                   |
| datetime     | Handle dates and times                                        |	
| re           | Support for regular expressions                               |
| random       | Generate random numbers                                       |
| math         | Mathematical functions (trigonometry, logarithms, etc.)       |
| json         | JSON encoding and decoding                                    |
| urllib       | Open and handle URLs and request                              |
| zipfile      | Read and write ZIP files                                      |
| subprocess   | Execute external processes                                    |
| threading    | Create and control threads                                    |
| time         | Time-related functions (delays, measurements, etc.)           |
| collections  | Specialized data structures like deque and Counter            |
| pickle       | Serialize and deserialize Python objects                      |
'''
# Example: math module
import math
print(math.sqrt(25))   # 5.0



# 2. Ways to import modules
# -----------------------------------------------------------------------------------------------
import math                  # Full Import: e.g., math.sqrt()
from math import sqrt        # Partial Import (Import specific function): e.g., sqrt()
from math import sqrt as m   # Aliased Import (Using an alisa): e.g., m.sqrt()



# 3.Importing my own module
# -----------------------------------------------------------------------------------------------
# my-project/
# ├── 14_modules_and_packages.py
# └── my_module.py

# my_module.py
def add(a, b):
    return a + b

# 14_modules_and_packages.py
import my_module
print(mymath.add(3, 4))  # 7

'''
You can import your own module by placing the Python file in the same directory and using the import statement.
For example, if you have a file named my_module.py, you can import it with import my_module.
'''



# 4. Package
# -----------------------------------------------------------------------------------------------
'''
A package is a directory that contains a collection of modules.
'''
# my_project/
# ├── 14_modules_and_packages.py
# └── utils/
#     ├── __init__.py
#     └── calc.py

# calc.py
def square(x):
    return x * x

# 14_modules_and_packages.py
from utils import calc
print(calc.square(5))  # 25

'''
__init__.py :  A file that indicates the folder is a package
               Can be left empty, but it is generally recommended to include it
'''



# 5. `__name__ == "__main__"` pattern
# -----------------------------------------------------------------------------------------------
# module_test.py
def say_hi():
    print("Hi!")

if __name__ == "__main__":
    say_hi()  # This runs only when this file is executed directly

'''
If you import this file from another file, it will not execute.
'''



# 6. Importing the Standard Library
# -----------------------------------------------------------------------------------------------
import datetime
print(datetime.datetime.now())  # Gets the current date and time and prints it.

import random
print(random.randint(1, 10))    # Generates and prints a random integer between 1 and 10 (inclusive).



# 7. Installing External Packages (pip)
# -----------------------------------------------------------------------------------------------
# bash >>> pip install requests

import requests
res = requests.get("https://example.com")
print(res.status_code)

'''
You can manage a list of packages using a `requirements.txt` file.
'''



# Module vs Package vs Library
# -----------------------------------------------------------------------------------------------
'''
| Concept  | Example             | Explanation                                                     |
|----------|---------------------|-----------------------------------------------------------------|
| Module   | `math.py`           | A single `.py` file                                             |
| Package  | `utils/`            | A folder containing multiple modules                            |
| Library  | `requests`, `numpy` | A collection of reusable code (usually distributed as packages) |	
'''
