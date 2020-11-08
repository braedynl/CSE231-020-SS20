# Dictionaries Cheatsheet

[Dictionary Lectures](https://www.cse.msu.edu/~cse231/Online/dictionaries.html)

In computer science, **dictionaries** (type name: `dict`, sometimes referred to as "maps" in other languages) define a set of key-value pairs, where access to a certain value can only be done through invocation of the dictionary instance with an associated key. 

In Python, dictionary keys can *only* be immutable objects, whereas dictionary values can be either mutable or immutable objects. Dictionaries do *not* have indices, though they will maintain order upon initialization, pair removal, and pair appendation.

The `len()` function can be used to determine the number of key-value pairs within a dictionary:

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

n = len(my_dict)  # n : 3
```

If all of the keys in a given dictionary are type `int` or `float` (try not to make your keys floats), the `sum()` function will add together all keys without any method calls.

```python
my_dict = {1: 'a', 2: 'b', 3: 'c'}

s = sum(my_dict)  # s : 6
```

Likewise, the `max()` and `min()` functions will determine the maximum or minimum element between all keys without any method calls, respectively. 

```python
my_dict = {1: 'a', 2: 'b', 3: 'c'}

maximum = max(my_dict)  # maximum : 3
minimum = min(my_dict)  # minimum : 1
```

Dictionaries are **mutable**, meaning that they pass by reference.

Jump to section:
1. [Initialization](#initialization)
2. [Accessing](#accessing)
3. [Iteration](#iteration)
4. [Common Methods](#common-methods)
5. [Sorting a Dictionary](#sorting-a-dictionary)

Want to learn more? [Check out Programiz's article on dictionaries!](https://www.programiz.com/python-programming/dictionary)

There is one operator compatible with dictionaries (`|`, new in Python 3.9), though you will not see it on any of our material because of its niche use and recency. There is also dictionary comprehension, though it is too complicated for the purposes of this course.

There are many things we do not cover in CSE 231 regarding dictionaries because not everything is vitally important to solving the problems we give. Feel free to browse the [official Python documentation on dictionaries](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) for extra knowledge (I've put everything you'll want to know for CSE 231 on here).

## Initialization

In Python, dictionaries can be declared using curly brackets (`{}`).

```python
# empty dictionary
my_dict = {}

# dictionary with initial values;
# key-value pairs are denoted by the colon (:) character
my_dict = {'a': 1, 'b': 2, 'c': 3}

# dictionary with initial values, multi-line
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
```

A dictionary can also be declared via its constructor function, or as a conversion from a list of tuples, where the 0th index of each tuple represents the key, and the 1st index of each tuple represents the value.

```python
# empty dictionary, equivalent to `my_dict = {}`
my_dict = dict()

# the dict() function can take a variable amount of custom parameters as declaration,
# parameter names will be converted to strings
my_dict = dict(a=1, b=2, c=3)  # my_dict : {'a': 1, 'b': 2, 'c': 3}

# conversion from list of tuples
my_dict = dict( [('a', 1), ('b', 2), ('c', 3)] )  # my_dict : {'a': 1, 'b': 2, 'c': 3}

# typical, recommended initial value declaration using curly brackets
my_dict = {'a': 1, 'b': 2, 'c': 3}  # my_dict : {'a': 1, 'b': 2, 'c': 3}
```

## Accessing

Accessing dictionary values is alike indexing with regards to notation style. This kind of language manipulation is also how one adds or removes key-value pairs.

```python
my_dict = {}

# create a key of 'a', with value 1
my_dict['a'] = 1  # my_dict : {'a': 1}

# accessing value from key
my_val = my_dict['a']  # my_val : 1

# you can of course use different types (as appropriate),
# key of 'Wungus' with value [123, 'abc']
my_dict['Wungus'] = [123, 'abc']  # my_dict : {'a': 1, 'Wungus': [123, 'abc']}

# accessing value from key
my_val = my_dict['Wungus']  # my_val : [123, 'abc']

# (one way of) removing a key-value pair
del my_dict['Wungus']  # my_dict : {'a': 1}
```

It's fairly common to encounter problems where the programmer needs to access the same key-value pair multiple times to enact some sort of manipulation or appendation to the value, while also needing to simultaneously add *new* key-value pairs if they don't already exist within the dictionary instance.

In many such circumstances, the `in` keyword with conditional expressions must be used to determine if a key already exists within a dictionary, lest Python raise a `KeyError`. A `KeyError` occurs when attempting to access a key that does not exist in some dictionary.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict['d'])  # raises KeyError; key of 'd' does not exist in my_dict 
```

For an example, let's assume we are attempting to count the number of characters in a given word string. We need to cover the following problems in order to avoid a `KeyError`:
- If a character in the word *does not* exist inside the dictionary, initialize it with a count of 1
- Else, if a character in the word *does* exist inside the dictionary, access that character's value in the dictionary and increment it by 1

```python
def count_characters(word: str) -> dict:
    
    # start with an empty dictionary
    char_count = {}

    # begin iterating through the characters in `word`
    for char in word:

        # if a character in the word *does not* exist 
        # inside the dictionary, initialize it with a count of 1
        if char not in char_count:
            char_count[char] = 1
        
        # else, if a character in the word *does* exist 
        # inside the dictionary, access that character's value 
        # in the dictionary and increment it by 1
        else:
            char_count[char] += 1

            # remember that `var += int` is short-hand for `var = var + int`,
            # meaning that this operation is accessing the value at char_count[char],
            # and thus wouldn't work without checking if char is in the dictionary
            # before-hand
    
    return char_count

c = count_characters('mirror')  # c : {'m': 1, 'i': 1, 'r': 3, 'o': 1}
```

[PythonTutor Execution](http://pythontutor.com/visualize.html#code=def%20count_characters%28word%3A%20str%29%20-%3E%20dict%3A%0A%20%20%20%20%0A%20%20%20%20%23%20start%20with%20an%20empty%20dictionary%0A%20%20%20%20char_count%20%3D%20%7B%7D%0A%0A%20%20%20%20%23%20begin%20iterating%20through%20the%20characters%20in%20%60word%60%0A%20%20%20%20for%20char%20in%20word%3A%0A%0A%20%20%20%20%20%20%20%20%23%20if%20a%20character%20in%20the%20word%20*does%20not*%20exist%20%0A%20%20%20%20%20%20%20%20%23%20inside%20the%20dictionary,%20initialize%20it%20with%20a%20count%20of%201%0A%20%20%20%20%20%20%20%20if%20char%20not%20in%20char_count%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20char_count%5Bchar%5D%20%3D%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20%23%20else,%20if%20a%20character%20in%20the%20word%20*does*%20exist%20%0A%20%20%20%20%20%20%20%20%23%20inside%20the%20dictionary,%20access%20that%20character's%20value%20%0A%20%20%20%20%20%20%20%20%23%20in%20the%20dictionary%20and%20increment%20it%20by%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20char_count%5Bchar%5D%20%2B%3D%201%0A%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20remember%20that%20%60var%20%2B%3D%20int%60%20is%20short-hand%20for%20%60var%20%3D%20var%20%2B%20int%60,%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20meaning%20that%20this%20operation%20is%20accessing%20the%20value%20at%20char_count%5Bchar%5D,%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20and%20thus%20wouldn't%20work%20without%20checking%20if%20char%20is%20in%20the%20dictionary%0A%20%20%20%20%20%20%20%20%20%20%20%20%23%20before-hand%0A%20%20%20%20%0A%20%20%20%20return%20char_count%0A%0Ac%20%3D%20count_characters%28'mirror'%29%20%20%23%20c%20%3A%20%7B'm'%3A%201,%20'i'%3A%201,%20'r'%3A%203,%20'o'%3A%201%7D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

The method of appendation would of course depend on the type of your dictionary values, and what you're attempting to accomplish. Structuring the conditional clauses *surrounding* the appendation to a particular dictionary is the main takeaway here.

## Iteration

Iteration through a dictionary is typically done by invocation of one of the three method functions: `.keys()`, `.values()`, or `.items()`. See the descriptions for these methods in the [Common Methods](#common-methods) section for more details.

When doing typical iteration by element, the keys are traversed by default.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# typical iteration by element, key traversal
# by default
for key in my_dict:  # key : 'a' -> 'b' -> 'c'
    print(key)

# using .keys()
for key in my_dict.keys():  # key : 'a' -> 'b' -> 'c'
    print(key)

# using .values()
for value in my_dict.values():  # value : 1 -> 2 -> 3
    print(value)

# using .items() yields both the key and value
# simultaneously

# key : 'a' -> 'b' -> 'c'
# value : 1 -> 2 -> 3
for key, value in my_dict.items():
    print(key, value)
```


## Common Methods

### `.clear()`

Removes all key-value pairs from the dictionary.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.clear()  # my_dict : {}
```

### `.copy()`

Returns a shallow copy of the dictionary.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict_copy = my_dict.copy()

my_dict['d'] = 4

# my_dict : {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# my_dict_copy : {'a': 1, 'b': 2, 'c': 3}

# the copy is unaffected by changes to the original
```

### `.get(key[, default])`

Returns the value for `key` if `key` is in the dictionary, else `default`. If `default` is not given, it defaults to `None`, so that this method never raises a `KeyError`.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# key that is in the dictionary
my_val = my_dict.get('a')  # my_val : 1

# key that is not in the dictionary, with None default
my_val = my_dict.get('d')  # my_val : None

# key that is not in the dictionary, with set default
my_val = my_dict.get('d', -1)  # my_val : -1
```

### `.items()`

Returns a list-of-tuples-like object of the dictionary's key-value pairs.

(This method returns what's called a "view object", where changes to the dictionary instance will be reflected in the view. These can simply be converted to lists with the `list()` function if you're wanting to do more advanced manipulation)

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

items = my_dict.items()  # items : dict_items([('a', 1), ('b', 2), ('c', 3)])
```

### `.keys()`

Returns a list-like object of the dictionary's keys.

(This method returns what's called a "view object", where changes to the dictionary instance will be reflected in the view. These can simply be converted to lists with the `list()` function if you're wanting to do more advanced manipulation)

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

keys = my_dict.keys()  # items : dict_keys(['a', 'b', 'c'])
```

### `.pop(key[, default])`

If `key` is in the dictionary, remove it and return its value, else return `default`. If `default` is not given and `key` is not in the dictionary, a `KeyError` is raised.

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# key that is in the dictionary
my_val = my_dict.pop('c')  # my_dict : {'a': 1, 'b': 2}, my_val : 3

# key that is not in the dictionary, set default
my_val = my_dict.pop('d', None)  # my_val : None

# key that is not in the dictionary, no default
my_val = my_dict.pop('d')  # KeyError; 'd' is not a key in my_dict
```

### `.values()`

Returns a list-like object of the dictionary's values.

(This method returns what's called a "view object", where changes to the dictionary instance will be reflected in the view. These can simply be converted to lists with the `list()` function if you're wanting to do more advanced manipulation)

```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

values = my_dict.values()  # items : dict_values([1, 2, 3])
```

## Sorting a Dictionary

Dictionaries do not have a method function dedicated to sorting as lists do. A dictionary can, however, be transformed into a list-of-tuples, where *that* can be sorted, and turned back into a dictionary with the `dict()` function.

In essence, the sorting of a dictionary is synonymous to the sorting of a list-of-tuples, which you should hopefully be familiar with already.

Suppose we had the following dictionary...

```python
student_scores = {
    'Eva': 95,
    'Wungus': 82,
    'Jon': 87,
    'Lily': 99,
    'Bob': 64,
    'Hasan': 85,
    'Samantha': 100
}

# we can transpose this down to a list-of-tuples
# using the .items() method...
items = student_scores.items()  # items : dict_items([('Eva', 95), ('Wungus', 82), ('Jon', 87), ('Lily', 99), ('Bob', 64), ('Hasan', 85), ('Samantha', 100)])

# we can then give this to the sorted() function
# to obtain a sorted version (output as a list,
# 0th item of each tuple used to determine order
# by default)...
sorted_items = sorted(items)  # sorted_items : [('Bob', 64), ('Eva', 95), ('Hasan', 85), ('Jon', 87), ('Lily', 99), ('Samantha', 100), ('Wungus', 82)]

# we finally give this version to dict() to re-create 
# our dictionary in a sorted order
sorted_student_scores = dict(sorted_items)  # sorted_student_scores : {'Bob': 64, 'Eva': 95, 'Hasan': 85, 'Jon': 87, 'Lily': 99, 'Samantha': 100, 'Wungus': 82}


# if we wanted to do all of this in one line, we can say:
sorted_student_scores = dict(sorted(student_scores.items()))
```

This would be equivalent to sorting a dictionary by *key*, but what if we wanted to sort by *value*? Just as with sorting nested lists, we can use `itemgetter()` to specify the index of the inner structure we want to sort by, after we've transposed it down into a list-of-tuples.

```python
from operator import itemgetter  # remember to import!

student_scores = {
    'Eva': 95,
    'Wungus': 82,
    'Jon': 87,
    'Lily': 99,
    'Bob': 64,
    'Hasan': 85,
    'Samantha': 100
}

items = student_scores.items()

# each value will be at index 1, so we call itemgetter(1)
# as our 'key' argument
sorted_items = sorted(items, key=itemgetter(1))

sorted_student_scores = dict(sorted_items)  # sorted_student_scores : {'Bob': 64, 'Wungus': 82, 'Hasan': 85, 'Jon': 87, 'Eva': 95, 'Lily': 99, 'Samantha': 100}


# if we wanted to do all of this in one line, we can say:
sorted_student_scores = dict(sorted(student_scores.items(), key=itemgetter(1)))

# (careful with your parenthesis placement here ^
# `student_scores.items()` and `key=itemgetter(1)` are 
# the arguments to sorted(), and the entire call to 
# sorted() is the argument to dict() -- it can get messy)
```

It might help to reference back to the [Lists Cheatsheet, under the `.sort()` method](https://github.com/braedynl/CSE231-GITHUB/blob/master/Cheatsheets/lists.md#sortkeynone-reversefalse) if you're having trouble understanding the operations taking place here. I go through an example *without* using `itemgetter()` to sort a nested structure -- `itemgetter()` is a quicker way of doing what I showcase there, but it might help to see what `itemgetter()` is actually doing when written out from scratch.
