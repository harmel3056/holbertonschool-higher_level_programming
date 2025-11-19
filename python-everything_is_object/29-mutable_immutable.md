# Mutable, Immutable... everything is object!
## Understanding Mutability in Python
![Image](Mutable_Immutable.jpg)

## Introduction

Having just covered mutable and immutable objects, it's important to understand how Python handles these different types and what implications this has for our code.

---

## ID and Type

Every object in Python has two fundamental attributes that can be accessed using built-in functions:
- **`type()`** - returns the class/type of the object
- **`id()`** - returns a unique identifier for that object's memory location

**Example:**
```python
x = 42
print(type(x))  # <class 'int'>
print(id(x))    # 140234567890123
```

### Assignment vs Referencing

Understanding the difference between assignment and referencing will provide context for variable handling in Python:

- **Referencing**: When you assign one variable to another, you're creating a reference to the same object in memory
- **Assignment (copying)**: Creating a new object with the same values

**Example:**
```python
# Referencing - both point to the same object
a = [1, 2, 3]
b = a                # b references the same list as a
print(id(a) == id(b))  # True - same object

b.append(4)
print(a)             # [1, 2, 3, 4] - a is affected!

# Assignment (copying) - creates a new object
a = [1, 2, 3]
c = a[:]             # c is a new list with the same values
print(id(a) == id(c))  # False - different objects

c.append(4)
print(a)             # [1, 2, 3] - a is NOT affected
```

**Memory Schema:**
```
Referencing:
a  ──→  [1, 2, 3]  ←── b    (both point to same object at id: 12345)

Assignment/Copying:
a  ──→  [1, 2, 3]  (id: 12345)
c  ──→  [1, 2, 3]  (id: 67890)  (separate object)
```

---

## Mutable Objects

Mutable objects are those which have a changeable state, they can be altered in place without the need to reassign IDs or variable names. The most common mutable objects are lists, dicts, sets, and byte arrays, which allows flexibility for dynamic data manipulation.

**Example:**
```python
my_list = [1, 2, 3]
original_id = id(my_list)

my_list.append(4)
print(my_list)          # [1, 2, 3, 4]
print(id(my_list))      # Same as original_id - modified in place
```

---

## Immutable Objects

When we say an object is immutable, we are referring to an object whose internal state cannot be changed in-place. Any 'change' to that object will actually result with a new object being created in memory, which implicitly means that any variable name taking that 'change' will have a new object, and in turn a new ID. Some common examples of immutable objects include number (int, float, complex), bool, string, tuples, frozen set, and bytes.

**Important note about tuples and frozen sets:** While tuples and frozen sets themselves are immutable, they can still contain mutable objects. If a tuple or frozen set contains a list, for example, that list can still be modified in-place:

**Example with tuple:**
```python
my_tuple = (1, 2, [3, 4])
print(id(my_tuple))     # Note the ID

my_tuple[2].append(5)   # Modifying the list inside the tuple
print(my_tuple)         # (1, 2, [3, 4, 5])
print(id(my_tuple))     # Same ID - the tuple itself hasn't changed
```

**Example:**
```python
s = "hello"
original_id = id(s)

s += " world"
print(s)            # "hello world"
print(id(s))        # Different from original_id - new object created
```

So when you do `s = "hello"` then `s += " world"`, you're not editing `"hello"` — you're creating a new string object `"hello world"` and reassigning `s` to point to it. The original `"hello"` stays untouched somewhere in memory.

**Memory Schema:**
```
Before s += " world":
s  ──→  "hello"  (id: 12345)

After s += " world":
s  ──→  "hello world"  (id: 67890)  (new object created)
       "hello"  (id: 12345)  (original still in memory, will be garbage collected)
```

---

## Why It Matters: Python's Treatment of Mutable and Immutable Objects

For immutable objects like strings, integers, and tuples, Python will often make two variable names that refer to identical values refer to the same object in memory (so `a is b` returns `True`). Note that `is` checks **identity** (whether two variables point to the same object in memory), not **equality** (`==` checks if values are equal). This is called **interning**, and is an efficiency measure for Python. However, it has its limitations. Interning on immutable objects cannot be assumed, as it seems to only apply to the simplest forms of immutable objects. For longer strings, or more complicated tuples, it seems that interning often won't be applied.

**Example:**
```python
# Simple cases - typically interned
a = "hello"
b = "hello"
print(a is b)       # True - same object

# Complex cases - often NOT interned
x = "hello world with lots of text"
y = "hello world with lots of text"
print(x is y)       # Often False - different objects
```

If one required interning for their project, they would be best advised to apply it manually using `sys.intern()`.

### Small Integer Caching and Pre-allocation

Python pre-allocates small integers as an optimization. When CPython starts, it creates integer objects for commonly used values and reuses them throughout the program's lifetime. This is controlled by two constants:

- **`NSMALLNEGINTS`** = 5 (integers from -5 to -1)
- **`NSMALLPOSINTS`** = 257 (integers from 0 to 256)

This means integers in the range **-5 to 256** are pre-created and always refer to the same object in memory.

**Why these specific values?** These are statistically the most commonly used integers in typical programs (loop counters, array indices, small calculations, etc.), making this optimization highly effective.

**Example:**
```python
a = 100
b = 100
print(a is b)        # True - both reference the pre-allocated integer object

x = 1000
y = 1000
print(x is y)        # Often False - outside the cached range
```

### Aliases

When multiple variables refer to the same object, they are called **aliases**. For small integers (within the cached range), Python automatically creates aliases:

**Example:**
```python
a = 50
b = 50
c = 50
# a, b, and c are all aliases - they point to the same pre-allocated integer object
print(id(a) == id(b) == id(c))  # True
```

For objects outside the cached range, aliases only occur if you explicitly assign one variable to another:

```python
x = 1000
y = 1000  # Different objects (usually)
z = x     # z is an alias of x
print(x is y)  # False
print(x is z)  # True - z is an alias
```

It matters that Python does this, and that we are aware of it, because it means **it is not safe to assume that an operation is changing an object**. If we undertake to 'change' an immutable object, we must understand that the object is being replaced rather than changed, and ensure that the new object is re-bound to the variable name.

**Example:**
```python
def try_modify_string(s):
    s += " modified"    # Creates new string, only affects local variable

text = "hello"
try_modify_string(text)
print(text)             # Still "hello" - unchanged!
```

---

## How Arguments Are Passed to Functions and What That Implies for Mutable and Immutable Objects

Python uses **pass-by-object-reference** (also called pass-by-assignment). When you pass an object to a function, you're passing a reference to that object, not a copy. The function parameter becomes a new variable name pointing to the same object.

### Immutable Objects in Functions

**Example:**
```python
def modify_number(x):
    x = x + 10      # Creates new integer, rebinds local x only

num = 5
modify_number(num)
print(num)          # Still 5 - original unchanged
```

In order to use the 'changed' value, you must return and re-assign (or re-bind) it:

```python
def modify_number(x):
    return x + 10

num = 5
num = modify_number(num)    # Must reassign
print(num)                  # Now 15
```

### Mutable Objects in Functions

**Example:**
```python
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] - Changed in place
```
