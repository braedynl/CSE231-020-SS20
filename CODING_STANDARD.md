# The Coding Standard

When you convert a design document into Python source code, one of your primary goals should be to write the source code and internal documentation such that it is easy to verify that the source code conforms to the design. It should be easy to debug, test, and maintain. The coding standard below is designed to assist you in achieving this goal.

**Interjection from Braedyn**

I've included an [example project structure](#example-structure) at the bottom of this document. 

### 1. No Personal Information

Do not include any personal information, such as your name or APID, in any of your source code files. All project solutions are sent off campus to a software system which compares source code files for similarities.

### 2. Source Code Format

Source code lines should be no more than 80 characters long. Break long lines into multiple, shorter lines using the continuation character ("`\`").

Only one statement should be included on a given line of the source code (i.e. don't use "`;`").

Blank lines and spaces should be used to enhance the readability of both source statements and comments where appropriate. 

All `import` statements should appear after the source code header and before any other Python code in the program.

All function definitions should appear after the `import` statements and before any other Python code in the program. 

### 3. Source Code Header

Each source code file should contain an introductory block of comments that identify the assignment, and gives a brief overview of the program. Example:

```python
'''
Computer Project #5

Algorithm
    prompt for an integer
    input an integer
    loop while not end-of-data
        call function to count number of digits in integer
        output the number of digits
        prompt for an integer
        input an integer
    display closing message
'''
```

### 4. Descriptive Comments

The source code should include comments that describe the functionality of significant and/or ambiguous blocks of code. Comments are particularly important before blocks of code that perform major data manipulations or error processing. 

For readability, each comment should be indented at the same level as the block of code that it describes, or, if it fits within the 80 character limit and describes a single line, to the right of that line. 

See Section 3.3.1 - Readability in the text, starting on page 167.

Place comments to indicate:
- The purpose of objects that have ambiguous variable names.
- Where something is "tricky", "clever" or "unusual" -- if it required thought on your part, it should be commented. 

General rule of thumb: if it was hard to write, it is probably hard to read -- a comment is probably necessary.

### 5. Mnemonic Identifiers

Meaningful identifiers taken from the problem domain should be used for all variable names. Furthermore, a name will only be used for one purpose (the same name should not be used for more than one).

### 6. Symbolic Constants

Symbolic constants should be used instead of embedding arbitrary numeric and character constants in the source code. Use "upper with under" style for all symbolic constants. Example:

```python
HEAT_OF_FUSION = 79.71  # calories to melt one gram of ice
```

**Interjection from Braedyn**

You'd typically want to place constants in the global namespace (the indentation level furthest to the left) between your chunk of `import` statements and function definitions. Values declared as constants _should remain constant_ -- otherwise that kind of defeats the purpose, right?   

### 7. Variable and Function Names

Use "lower with under" style for all variable and function names. In some situations, it is appropriate to append type information to variable names as a visual reminder of the purpose of those variables. Example:

```python
student_count = 0  # number of students in class
farenheit_float = 0.0  # temperature in farenheit
```

### 8. Function Header

Using docstrings, (delimited by triple double/single quotes), each function should contain an introductory block of comments that explain the purpose of the function, and describes all information passed, modified, and returned by the function (e.g. parameters and global data objects). It should also describe any assumptions about the information passed in that is needed for it to work correctly. Example:

```python
def count_digits(value):
    '''
    Counts the number of digits in an integer value.
    value : the value to be processed (int)
    returns: the number of digits in value (int)
    '''
```

```python
def add_assignment(grade_book, possible_pts):
    '''
    Adds a new assignment to a given grade_book.
    grade_book: the grade book (dict)
        maps assignment names (str) to grad dicts, where a grade
        dict maps student PIDS (str) to grades (floats)
        grade_book is both read and modified
    possible_pts : the total points possible
        must be positive
    '''
```

**Interjection from Braedyn**

This coding standard is a tad outdated, since there's some newer Python features that allow for in-code type hints. Example:

```python
def my_function(param1:int, param2:str='default') -> list:
#                      ^           ^                 ^ 
#                 expected parameter types      function return type
```

This is purely an aesthetic addition, you can still pass a `str` to `param1`, for example. But, I personally think this is a much cleaner way of showing parameter and return types. Feel free to style it however you want. The most important thing is to explain the function, its parameters, and its return.

I'll also show the way I, personally, create function docs:

```python
def my_function(param1:int, param2:str='default') -> list:
    '''
    Explain what the function does

    Parameters
    ----------
        param1 : brief explanation
        param2 : brief explanation

    Returns
    -------
        list : brief explanation
    
    Notes
    -----
        Any assumptions made, different return cases, etc.
    '''
```

### 9. Global Variables

Variables referenced in a function body should be local to that function. Global variables should never be used (i.e. don't use the `global` keyword).

**Interjection from Braedyn**

It's important to note the difference between "global variables" and "global constants". Global *constants* are allowed as discussed in the [symbolic constants section (same thing as global constants)](#6-symbolic-constants), but global *variables* aren't because it can lead to [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code). There *are* reasons for why the `global` keyword exists, but none of those things apply to what we'll be doing in this course. 

### 10. Class Names

Use "CamelCase" style for all user-defined class names. Example:

```python
class SalariedEmployee():
    ...

class HourlyEmployee():
    ...
```

Guido van Rossum, the creator of Python, has a length style guide: https://www.python.org/dev/peps/pep-0008/

It's an excellent resource for more complex situations not described in this document. 

### Example Structure

User-defined class definitions will generally be in separate files by themselves.

```python
'''
Computer Project #5

Algorithm
    prompt for an integer
    input an integer
    loop while not end-of-data
        call function to count number of digits in integer
        output the number of digits
        prompt for an integer
        input an integer
    display closing message
'''

# all imports grouped together up here
import ...
from ... import ...

# all global constants
GLOBAL_CONSTANT = ...

# all function definitions
def f(x):
    '''
    function docstring
    say what the function does
    
    list parameters and parameter types
    list returns and return types
    note assumptions
    '''
    
    ...

def main():
    '''
    function docstring
    say what the function does
    
    list parameters and parameter types
    list returns and return types
    note assumptions
    '''
    
    ...

if __name__ == "__main__":
    main()
```
