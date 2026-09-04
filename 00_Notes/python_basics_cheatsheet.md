# Python Basics Cheat Sheet

This file is a running reminder of the basic Python syntax and concepts used during MSc AI preparation. It will be updated as new Python concepts are introduced.

## 1. Variables

Variables store values.

```python
player_name = "Alex"
health = 100
score = 2400
current_xp = 320
```

General pattern:

```python
variable_name = value
```

Use clear lowercase names with underscores:

```python
player_name
current_xp
xp_required
points_earned
```

---

## 2. Strings

Text is stored inside quotation marks.

```python
player_name = "Alex"
course = "BSc Game Technology"
```

Strings can use double quotes or single quotes:

```python
name = "Alex"
name = 'Alex'
```

---

## 3. Integers

Whole numbers are integers.

```python
health = 100
score = 2400
level = 4
```

---

## 4. Basic arithmetic

### Addition

```python
new_score = score + points_earned
```

### Subtraction

```python
xp_remaining = xp_required - current_xp
```

Other basic operators we will use later:

```python
+   # addition
-   # subtraction
*   # multiplication
/   # division
```

---

## 5. `print()`

`print()` displays information in the terminal.

```python
print("Hello")
```

Print text with a variable:

```python
print("Player name:", player_name)
```

Print several values:

```python
print("Player:", player_name, "Health:", health, "Score:", score)
```

Print a calculation:

```python
print("XP needed:", xp_required - current_xp)
```

Important: `print()` displays a value. It does not return a value from a function.

---

## 6. `def` — creating a function

`def` defines a function.

```python
def show_player():
    print("Player:", player_name)
```

General pattern:

```python
def function_name():
    # code inside the function
```

The indented code belongs to the function.

---

## 7. Calling a function

Defining a function does not run it.

This defines it:

```python
def show_player():
    print("Player:", player_name)
```

This runs it:

```python
show_player()
```

---

## 8. Function parameters

Parameters allow information to be passed into a function.

```python
def add_score(current_score, points_earned):
    new_score = current_score + points_earned
    return new_score
```

Here:

```text
current_score
points_earned
```

are parameters.

They are names used by the function to receive values.

---

## 9. Function arguments

Arguments are the actual values or variables supplied when calling a function.

```python
add_score(score, point_earned)
```

Here:

```text
score
point_earned
```

are arguments.

Parameter vs argument:

```python
def add_score(current_score, points_earned):  # parameters
    return current_score + points_earned

add_score(score, point_earned)                 # arguments
```

The order matters.

For example:

```python
def calculate_xp_needed(current_xp, xp_required):
    return xp_required - current_xp
```

Correct:

```python
calculate_xp_needed(current_xp, xp_required)
```

If the arguments are reversed, the result will be wrong.

---

## 10. `return`

`return` sends a value back from a function.

```python
def add_score(current_score, points_earned):
    new_score = current_score + points_earned
    return new_score
```

A returned value should normally be stored or used:

```python
new_score = add_score(score, point_earned)
```

Then it can be printed:

```python
print("New score:", new_score)
```

Important difference:

```python
print(value)
```

shows a value on screen.

```python
return value
```

sends a value back to the code that called the function.

---

## 11. Local variables inside functions

A variable created inside a function normally belongs to that function.

```python
def calculate_xp_needed(current_xp, xp_required):
    xp_remain = xp_required - current_xp
    return xp_remain
```

`xp_remain` is created inside the function.

Outside the function, store the returned result:

```python
xp_remain = calculate_xp_needed(current_xp, xp_required)
```

---

## 12. `import`

`import` loads a Python module or library so its features can be used.

Used so far:

```python
import numpy
import pandas
import matplotlib
```

Example:

```python
import numpy
print(numpy.__version__)
```

---

## 13. Comments

A comment begins with `#`.

Python ignores comments when running the program.

```python
# This is a comment
score = 2400
```

Use comments to explain code when the reason for something is not obvious.

---

## 14. Indentation

Python uses indentation to show which code belongs inside a function or other block.

Correct:

```python
def show_player():
    print("Player:", player_name)
```

Incorrect:

```python
def show_player():
print("Player:", player_name)
```

Use consistent indentation, normally 4 spaces.

---

## 15. Current function pattern

A useful pattern from the exercises so far:

```python
score = 2400
point_earned = 129
current_xp = 320
xp_required = 1000


def add_score(current_score, points_earned):
    new_score = current_score + points_earned
    return new_score


def calculate_xp_needed(current_xp, xp_required):
    xp_remain = xp_required - current_xp
    return xp_remain


new_score = add_score(score, point_earned)
xp_remain = calculate_xp_needed(current_xp, xp_required)

print("New score:", new_score)
print("XP remaining:", xp_remain)
```

Flow:

```text
variables
   ↓
function call
   ↓
parameters receive values
   ↓
calculation
   ↓
return
   ↓
result stored in variable
   ↓
print/use result
```

---

## 16. Lists

Lists store multiple values in order.

```python
inventory = ["key", "phone", "wallet"]
```

Access items with an index:

```python
print(inventory[0])
print(inventory[-1])
```

Useful list operations:

```python
inventory.append("mug")
inventory.remove("phone")
print(len(inventory))
```

---

## 17. `for` loops

A `for` loop repeats code for each item in a collection.

```python
for item in inventory:
    print(item)
```

---

## 18. Dictionaries

Dictionaries store values using keys.

```python
player = {
    "name": "Alex",
    "level": 5,
    "score": 1200
}
```

Access and update values:

```python
print(player["name"])
player["score"] += 500
player["weapon"] = "rifle"
```

A dictionary can contain a list:

```python
player = {
    "name": "Alex",
    "inventory": ["key", "wallet"]
}

player["inventory"].append("mug")
```

---

## 19. Lists of dictionaries

A dataset can be represented as a list containing dictionaries.

```python
players = [
    {"name": "Alex", "score": 1200},
    {"name": "Sam", "score": 1800}
]
```

Loop through the records:

```python
for player in players:
    print(player["name"], player["score"])
```

---

## 20. Conditions: `if / elif / else`

Conditions control which code runs.

```python
if score >= 1500:
    print("High scorer")
elif score >= 1000:
    print("Medium scorer")
else:
    print("Low scorer")
```

Common comparison operators:

```text
==   equal to
!=   not equal to
>    greater than
>=   greater than or equal to
<    less than
<=   less than or equal to
```

---

## 21. Boolean values

A Boolean is either:

```python
True
False
```

Example:

```python
valid_input = False
```

---

## 22. `while` loops

A `while` loop repeats while its condition is true.

```python
health = 100

while health > 0:
    print(health)
    health -= 20
```

The condition must eventually become false unless the loop is intentionally stopped with `break`.

---

## 23. `input()` and type conversion

`input()` reads text from the user.

```python
name = input("Enter player name: ")
```

`input()` returns a string. Convert numeric input when needed:

```python
level = int(input("Enter level: "))
score = int(input("Enter score: "))
```

---

## 24. `try / except`

Use `try / except` to handle errors without crashing the program.

```python
try:
    score = int(input("Enter score: "))
except ValueError:
    print("Invalid number")
```

`ValueError` is raised when a conversion such as `int("hello")` cannot be completed.

Prefer catching the specific error:

```python
except ValueError:
```

rather than a broad:

```python
except:
```

---

## 25. `break`

`break` immediately exits the current loop.

```python
while True:
    score = int(input("Enter score: "))

    if score >= 0:
        break
```

`while True:` creates a loop that continues until something explicitly stops it.

---

## 26. `continue`

`continue` skips the rest of the current loop iteration and moves to the next one.

```python
scores = [1200, -50, 1800]

for score in scores:
    if score < 0:
        continue

    print(score)
```

---

## 27. List comprehensions

A list comprehension creates a list in a compact form.

Normal loop:

```python
valid_scores = []

for score in scores:
    if score >= 0:
        valid_scores.append(score)
```

List comprehension:

```python
valid_scores = [score for score in scores if score >= 0]
```

Transform values:

```python
doubled_scores = [score * 2 for score in valid_scores]
```

---

## 28. Function + input validation pattern

A function can repeatedly ask for input until it receives a valid value and then return it.

```python
def get_valid_score():
    while True:
        try:
            score = int(input("Enter player score: "))

            if score < 0:
                print("Score cannot be negative")
            else:
                return score

        except ValueError:
            print("Invalid number, try again")
```

Call the function once and store the returned value:

```python
player_score = get_valid_score()
```

Avoid calling the function multiple times if it asks for input, because each call runs the function again.

---


---

## 29. f-strings

f-strings let you insert variables directly into text.

```python
name = "Alex"
score = 1800

print(f"Player: {name}")
print(f"Score: {score}")
```

They are especially useful when writing values to files because `file.write()` expects a string.

```python
file.write(f"Score: {score}\n")
```

---

## 30. Reading and writing text files

Use `open()` with `with` so Python closes the file automatically when the block ends.

Write mode:

```python
with open("player_report.txt", "w") as file:
    file.write("Player: Alex\n")
```

Read mode:

```python
with open("player_report.txt", "r") as file:
    content = file.read()

print(content)
```

Common modes:

```text
"w"   write
"r"   read
```

A newline is written with:

```python
"\n"
```

Important: `print()` can receive several values, but `file.write()` expects one string.


## Concepts covered so far

- Variables
- Strings
- Integers
- Arithmetic
- `print()`
- Functions
- Function calls
- Parameters
- Arguments
- `return`
- Local variables
- `import`
- Comments
- Indentation
- Lists
- `.append()`
- `.remove()`
- `len()`
- `for` loops
- Dictionaries
- Nested lists and dictionaries
- Lists of dictionaries
- Counters and totals
- `if / elif / else`
- Comparison operators
- Boolean values
- `while` loops
- `input()`
- `int()`
- `try / except ValueError`
- `break`
- `continue`
- List comprehensions
- Input validation inside functions
- f-strings
- Reading and writing text files
- `with open(...)`
- File modes `"w"` and `"r"`
- `file.write()`
- `file.read()`

## Next concepts to add

- JSON
- CSV
- NumPy
- Pandas
- Classes
