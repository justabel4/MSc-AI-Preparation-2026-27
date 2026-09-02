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

## Concepts covered so far

- Variables
- Strings
- Integers
- Arithmetic
- `print()`
- `def`
- Functions
- Function calls
- Parameters
- Arguments
- `return`
- Local variables
- `import`
- Comments
- Indentation

## Next concepts to add

This file will be expanded as we learn new material, including:

- Lists
- Dictionaries
- `for` loops
- `while` loops
- `if / elif / else`
- Boolean values
- Reading files
- JSON
- CSV
- Classes
- Error handling
- NumPy
- Pandas
