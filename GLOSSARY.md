# Glossary

__Alternative title: What the f**k is Braedyn saying?__

As you learn the basics of programming, you'll come to find that there is a *copious* amount of vocabulary to know. I tend to use proper jargon a lot, not because I'm trying to get you to read the book (though you should), but because it's extremely difficult to explain the concepts *without* the vocab in my mind. Obviously, this can be a hindrance at times, and so here is a complete guide to the programming vocab.

(Note that you won't be tested on vocab, I made this just so you can understand me and my slides better)

Jump to section:
1. [General](#general)
2. [Functions](#functions)
3. [Containers](#containers)
4. [Classes](#classes)

## General

**Assignment/Initialization** - The process of giving a variable some value to hold. In Python, this is denoted by the equals (`=`) sign.

Example:
```python
my_variable = 1  # my_variable is being *assigned* the value 1
```

**Declaration/Definition** - A variable, function, or class' meaning to the program.

Example:
```python
class MyClass(object):  # everything encapsulated within this
                        # class is the class' *definition*
    def __init__(self):
        self.a = 1
        self.b = 2

def my_function(a, b):  # everything encapsulated within this
    c = a + b           # function is the function's *definition*
    return c

my_variable = 1  # my_variable's *definition*
```

**Global Namespace** - The indentation level furthest to the left side of the Python script. Variables declared in this region can be accessed everywhere else in the program.

**Immutable** - Describes a class that passes by copy. See [question 5 of the FAQ's Programming section](FAQ.md#programming) for an example on the difference between mutable and immutable types.

**Keyword** - A word that the programming language interprets as the programmer defining, or examining some portion of code.

Examples: `def`, `in`, `return`, `self`, `class`, `if`, `elif`, `else`, `while`, `for`

**Library** - A set of modules. The [Python Standard Library](https://docs.python.org/3/library/index.html) is a good example.

**Module/Package** - A set of pre-built classes, functions, or constants that can be imported into another program script. 

Example:
```python
# 'string' is a module included with the Python standard library
import string
import math  # as is 'math'
```

**Mutable** - Describes a class that passes by reference. See [question 5 of the FAQ's Programming section](FAQ.md#programming) for an example on the difference between mutable and immutable types.

**Operator** - A character, or small set of characters that the programming language interprets as the programmer performing some arithmetic, or short-hand operation with regards to an overloaded class. 

Examples: `+`, `-`, `/`, `*`, `=`, `<`, `>`, `<=`, `>=`, `==`

**Reference** - The address of a variable's location in computer memory.

**Scope** - The area for which a name is defined. There are two types of scope that we discuss in this class: *local scope*, and *global scope*.

Local scope refers to names defined within the boundaries of a confined area of the program, usually being discarded after use by the programming language. Function parameters are always within local scope to the function, as an example.

Example:
```python
def my_function(a, b):
    c = a + b  # 'a' and 'b' are *local* to 'my_function'
    return c

print(a)  # raises NameError
```

Global scope refers to names defined in all areas of the program, and are only discarded once the program has completed its execution.

Example:
```python
my_global_variable = 1

def my_function():
    print(my_global_variable)  # works in function's scope

print(my_global_variable)  # works in same scope
```

**Suite** - A line or collection of lines that only run in specific conditions or calls. In Python, a suite is denoted by (consistent) indentation. Many other programming languages use curly brackets (`{}`) to denote what lines are contained within a suite.

Example:
```python
def my_function(a, b):
    c = a + b  # part of my_function suite (will only run if my_function is called)
    return c   # part of my_function suite (will only run if my_function is called)

a = 1
b = 2

if a > 1:
    my_function(a, b)  # part of 'if a > 1:' suite (will only run if a > 1)
else:
    my_function(a, b)  # part of 'else:' suite (will only run if a <= 1)
```

**Value** - A representation of some entity that can be manipulated by the programming language. This is often confused with variables — variables *hold* values, but values *do not hold* variables.

Example:
```python
my_variable = 1  # '1' is the value
my_variable = 'Hello, world!'  # "Hello, world!" is the value
my_variable = [1, 2, 3]  # '[1, 2, 3]' is the value
```

**Variable** - A name that holds a particular value. 

Example:
```python
a = 1  # 'a' is the variable
my_variable = 2  # 'my_variable' is the variable
BIG_TEXT = 3  # 'BIG_TEXT' is the variable
```

## Functions

**Function** - A set of generalized actions (usually) performed on a collection of arguments passed by the caller. A programming function is not too dissimilar from a mathematical one.

Example:
```python
# 'def' keyword, function name, (parameters, ...) :
def my_function(a, b):
    # these two lines make up the function's "suite"
    c = a + b  # action
    return c   # action
               
# example call, with a=1, b=2
c = my_function(1, 2)

# the return would then be stored in the variable, 'c'
```

**Argument** - A value passed to a certain parameter. 

Example:
```python
def my_function(a, b):
    c = a + b
    return c

# my *arguments* are '1' and '2'
c = my_function(1, 2)
```

**Call** - The action of passing arguments to a function.

Example:
```python
def my_function(a, b):
    c = a + b
    return c

# *calling* my_function with arguments a=1, b=2
c = my_function(1, 2)
```

**Parameter** - A name given to some argument that typically generalizes to the type or shape of the incoming value(s).

Example:
```python
# my *parameters* here are 'a' and 'b'
def my_function(a, b):
    c = a + b
    return c
```

**Pass** - The action of supplying an argument to some parameter.

Example:
```python
def my_function(a, b):
    c = a + b
    return c

# I am *passing* '1' and '2' to 'my_function' 
c = my_function(1, 2)
```

**Return** - The output value of a function, usually based on actions performed on the arguments.

Example:
```python
def my_function(a, b):
    c = a + b  # c = 1 + 2 = 3
    return c   # return 3 <-- the *return* value

# my_function call with a=1, b=2
c = my_function(1, 2)
```

## Containers

**Container** - A type that has the ability to hold a multitude of values, often including ones of the same type and other types. Python's `str`, `list`, `dict`, and `set` types would all be considered containers.

**Index** - An integer value that denotes the order in which a value is placed within a sorted container. In most programming languages, indices begin counting from 0. 

In Python, the only containers that have indices are the `str` and `list` types. While the `dict` can be sorted as of Python 3.5, it does not have indices — only keys and values.

Example:
```python
my_variable = [1, 2, 3]

# value 1 is at *index* 0 of my_variable
value1 = my_variable[0]

my_variable = "Hello, world!"

# value 'l' is at *index* 2 of my_variable
value3 = my_variable[2]
```

**Iterable** - A container that can be traversed via a loop. Python's `str`, `list`, `dict`, and `set` types would all be considered iterables.

**Key** - With a dictionary (`dict`), a key is a value for which some other, associated value can be obtained via invocation of the dictionary instance.

Example:
```python
# 'a', 'b', and 'c' are the *keys* to 'my_dict'
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict['a'])  # prints: 1

# 'a' is the key, 1 is the value associated with that key
```

**Value** - With a dictionary (`dict`), a dictionary value is a value that can only be obtained via invocation of the dictionary instance with a key. 

Example:
```python
# 1, 2, and 3 are the *values* to 'my_dict'
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict['a'])  # prints: 1

# 'a' is the key, 1 is the value associated with that key
```

## Classes

**Class/Type/Object** - A structure that contains particular attributes and methods catered to the style of data for which it holds. In Python, all three of these words (essentially) mean the same thing. This differs between programming languages.

Example:
```python
class MyClass(object):  # 'MyClass' is a type/class/object

    def __init__(self, a, b):
        self.a = a
        self.b = b

# 'my_variable' is holding an instance of an 'int',
# 'int' being the type/class/object
my_variable = 1

# 'my_variable' is holding an instance of a 'str',
# 'str' being the type/class/object
my_variable = "Hello, world!"
```

**Attribute/Data Member** - A variable that stores data relating to the class instantiation. One is signified by a leading "`self.`" prefix. This is alike the "`this.`" prefix that many other programming languages use.

Example:
```python
class MyClass(object):

    def __init__(self, a, b):
        self.a = a  # 'self.a' is an attribute 
        self.b = b  # 'self.b' is an attribute

my_variable = MyClass(1, 2)

attribute_a = my_variable.a  # example invocation 
attribute_b = my_variable.b  # example invocation
```

**Constructor** - A magic method that describes how an instance of the class can be initialized. In Python, the name of the constructor must always be "`__init__`". This varies between programming languages.

Example:
```python
class MyClass(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

# call with self=MyClass, a=1, b=2
my_variable = MyClass(1, 2)

# the call to self=MyClass is implicit/hidden, however
# you want to think about it
```

**Instance** - A value created from, or grouped by a particular class.

Example:
```python
class MyClass(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

my_variable = MyClass(1, 2)  # 'my_variable' holds a 'MyClass' instance
my_variable = 1  # 'my_variable' holds an 'int' instance
my_variable = "Hello, world!"  # 'my_variable' holds a 'str' instance
```

**Instantiation** - The process of creating an instance of a particular class.

Example:
```python
class MyClass(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

my_variable = MyClass(1, 2)  # stating 'MyClass()' created a 'MyClass' instance
my_variable = 1  # stating '1' created an 'int' instance
my_variable = "Hello, world!"  # stating "Hello, world!" created a 'str' instance 
```

**Magic Method** - A method name that overrides particular behaviours of the class with respect to the programming language. A listing of all of them can be found [here](https://rszalski.github.io/magicmethods/).

**Method/Method Function** - A function dedicated to manipulating the class' data.

Example:
```python
class MyClass(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sum(self):  # method function, 'sum'
        c = self.a + self.b
        return c

my_variable = MyClass(1, 2)
my_method_return = my_variable.sum()  # example call
```

**Overload** - A magic method that defines how an operator will interact with respect to the class and its data.

Example:
```python
class MyClass(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __neg__(self):  # overload of '-' symbol to instead add self.a and self.b
        c = self.a + self.b
        return c

my_variable = MyClass(1, 2)
my_overload_return = -my_variable  # example call
```
