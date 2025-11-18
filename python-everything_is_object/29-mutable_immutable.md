# Python3: Mutable, Immutable... everything is object!
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

---

## Mutable Objects

Mutable objects are those which have a changeable state, they can be altered in place without the need to reassign IDs or variable names. The most common mutable objects are lists, dicts, and sets, which allows flexibility for dynamic data manipulation.

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

When we say an object is immutable, we are referring to an object whose internal state cannot be changed in-place. Any 'change' to that object will actually result with a new object being created in memory, which implicitly means that any variable name taking that 'change' will have a new object, and in turn a new ID. Some common examples of immutable objects include int, float, bool, string, and tuples.

**Example:**
```python
s = "hello"
original_id = id(s)

s += " world"
print(s)            # "hello world"
print(id(s))        # Different from original_id - new object created
```

So when you do `s = "hello"` then `s += " world"`, you're not editing `"hello"` — you're creating a new string object `"hello world"` and reassigning `s` to point to it. The original `"hello"` stays untouched somewhere in memory.

---

## Why Does It Matter and How Differently Does Python Treat Mutable and Immutable Objects?

For immutable objects like strings, integers, and tuples, Python will often make two variable names that refer to identical values refer to the same object in memory (so `a is b` returns `True`). This is called **interning**, and is an efficiency measure for Python. However, it has its limitations. Interning on immutable objects cannot be assumed, as it seems to only apply to the simplest forms of immutable objects. For longer strings, or more complicated tuples, it seems that interning often won't be applied.

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

## How Arguments Are Passed to Functions and What Does That Imply for Mutable and Immutable Objects

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

# Understanding Mutability in Python

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

---

## Mutable Objects

Mutable objects are those which have a changeable state, they can be altered in place without the need to reassign IDs or variable names. The most common mutable objects are lists, dicts, and sets, which allows flexibility for dynamic data manipulation.

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

When we say an object is immutable, we are referring to an object whose internal state cannot be changed in-place. Any 'change' to that object will actually result with a new object being created in memory, which implicitly means that any variable name taking that 'change' will have a new object, and in turn a new ID. Some common examples of immutable objects include int, float, bool, string, and tuples.

**Important note about tuples:** While tuples themselves are immutable (you cannot add, remove, or replace elements), they can contain mutable objects. If a tuple contains a list, for example, that list can still be modified in-place:

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

---

## Why It Matters: Python’s Treatment of Mutable and Immutable Objects

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
print(my_list)  # [1, 2, 3, 4] # Changed in place
```
