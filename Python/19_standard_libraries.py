# 1. `math` - Related to Mathematics
# -----------------------------------------------------------------------------------------------
import math

print(math.sqrt(16))       # 4.0
print(math.factorial(5))   # 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)
print(math.pi)             # 3.14159...



# 2. `random` - Random Number Generation
# -----------------------------------------------------------------------------------------------
import random

print(random.randint(1, 10))            # Integer between 1 and 10 (inclusive)
print(random.choice(['a', 'b', 'c']))   # Randomly selects one element from the list
print(random.sample(range(100), 5))     # Picks 5 unique samples from numbers 0 to 99



# 3. `datetime` - Handling Date and Time
# -----------------------------------------------------------------------------------------------
import datetime

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))   # Print formatted date and time string

from datetime import timedelta

tomorrow = now + timedelta(days=1)
print(tomorrow)



# 4. `os` - Operating System Interface
# -----------------------------------------------------------------------------------------------
import os

print(os.getcwd())         # Current working directory
print(os.listdir("."))     # List of files and directories in the current directory
# os.mkdir("test_folder")  # Create a new folder named "test_folder"



# 5. `sys` - System Paprameters / Input and Output
# -----------------------------------------------------------------------------------------------
import sys

print(sys.version)   # Python version
print(sys.argv)      # Command-line arguments



# 6. `time` - Related to Time
# -----------------------------------------------------------------------------------------------
import time

print("Start")
time.sleep(1.5)   # Pause for 1.5 seconds
print("End")



# 7. `collections` - Advanced Data Structures
# -----------------------------------------------------------------------------------------------
from collections import Counter, defaultdict

cnt = Counter("hello")
print(cnt)   # Count the occurrences of each character

dd = defaultdict(int)
dd["a"] += 1
print(dd)    # Automatically creates default values



# 8. `itertools` - Utilities for Iteration
# -----------------------------------------------------------------------------------------------
from itertools import permutations, combinations

print(list(permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), ...]

print(list(combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]



# 9. `json` - Handling JSON Data
# -----------------------------------------------------------------------------------------------
import json

data = {"name": "Hana", "age": 21}
json_str = json.dumps(data)
print(json_str)  # JSON string

parsed = json.loads(json_str)
print(parsed["name"])  # Hana



# 10. `re` - Regular Expression
# -----------------------------------------------------------------------------------------------
import re

text = "My email is aaleuey@gmail.com"
match = re.search(r"\w+@\w+\.\w+", text)
if match:
    print(match.group())   # aaleuey@gmail.com



# 11. `urllib` - Handling URL
# -----------------------------------------------------------------------------------------------
from urllib.request import urlopen

res = urlopen("https://aaleuey.com")
print(res.status)
html = res.read().decode("utf-8")
print(html[:200])



# 12. `pathlib` - Handling File Paths (Python 3.4+)
# -----------------------------------------------------------------------------------------------
from pathlib import Path

p = Path(".")
for file in p.iterdir():
    print(file)



# `statistics` - Mean / Variance / Standard Deviation
# -----------------------------------------------------------------------------------------------
import statistics

data = [1, 2, 3, 4, 5]
print(statistics.mean(data))       # Mean
print(statistics.variance(data))   # Variance
print(statistics.stdev(data))      # Standard Deviation



# 14. `enum` - Enumeration
# -----------------------------------------------------------------------------------------------
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.RED)          # Color.RED
print(Color.RED.value)    # 1



# -----------------------------------------------------------------------------------------------
https://docs.python.org/3/library/
