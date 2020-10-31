# Lists Cheatsheet

[List/Tuple Lectures](https://www.cse.msu.edu/~cse231/Online/lists.html)

In computer science, **lists** (type name: `list`) are an ordered sequence of elements, categorized as one of the basic data structures. Lists are a type of **container**. Unlike strings, however, they can hold *any* type, including multiple instances of themselves — what would generally be referred to as a **nested list** or **matrix**.

The `len()` function can be used to determine the number of elements within a list:

```python
my_list = [1, 2, 3]

n = len(my_list)  # n : 3
```

If all of the elements within a given list are type `int` or `float`, the `sum()` function can be used to add together all values within the list. 

```python
my_list = [1, 2, 3]

s = sum(my_list)  # s : 6
```

If all of the elements within a given list can be compared to one another, the `max()` and `min()` functions can be used to determine the maximum and minimum element of a list, respectively. 

```python
my_list = [1, 2, 3]

maximum = max(my_list)  # maximum : 3
minimum = min(my_list)  # minimum : 1
```

Lists are **mutable**, meaning that they pass by reference. (Don't worry if you don't know what that means yet, it will be explained during week 7)

Jump to section:
1. [Initialization](#initialization)
2. [Operations](#operations)
3. [Indexing](#indexing)
4. [Iteration](#iteration)
5. [Common Methods](#common-methods)
6. [List Comprehensions](#list-comprehensions)

Want to learn more? [Check out Programiz's article on lists!](https://www.programiz.com/python-programming/list)

## Initialization

In Python, lists can be declared using square brackets (`[]`).

```python
# empty list
my_list = []

# list with initial values
my_list = [1, 2, 3]

# list with initial values, multi-line
my_list = [
    1,
    2,
    3
]
```

A list can also be declared via its constructor function, or as a conversion from a different type. 

```python
# empty list, equivalent to `my_list = []`
my_list = list()

# string conversion
my_list = list('123')  # my_list : ['1', '2', '3']
```

## Operations

Lists interact with two of the mathematical operators, `+` and `*`.

The `+` operator will concatenate two lists together. The compound assignment variation, `+=`, is also compatible. 

```python
my_list = [1, 2, 3] + [4, 5]  # my_list : [1, 2, 3, 4, 5]

my_list += [6, 7]  # my_list : [1, 2, 3, 4, 5, 6, 7]
```

The `*` operator repeats, and concatenates multiple instances of the given list together. It's compound assignment, `*=`, is also compatible.

```python
my_list = [1, 2] * 2  # my_list : [1, 2, 1, 2]

my_list *= 2  # my_list : [1, 2, 1, 2, 1, 2, 1, 2]
```

## Indexing

Lists can be indexed to extract particular elements or subsets of elements (typically called **sublists**). 

If we had some list, `['Hello, world!', 3.14, 1, [1, 2, 3], False]`, the indices for it would be as follows:

<table>
    <thead>
        <th><code>'Hello, world!'</code></th>
        <th><code>3.14</code></th>
        <th><code>1</code></th>
        <th><code>[1, 2, 3]</code></th>
        <th><code>False</code></th>
    </thead>
    <tbody align="center">
        <tr>
            <td>0</td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
        </tr>
        <tr>
            <td>-5</td>
            <td>-4</td>
            <td>-3</td>
            <td>-2</td>
            <td>-1</td>
        </tr>
    </tbody>
</table>

To index, you use square brackets (`[]`) with an `int` to denote which index, or set of indices you wish to extract. The arguments are:

<div align="center"><code>[start : stop : step]</code></div><br>

Where `stop` and `step` are optional. The `stop` index is treated as an uninclusive bound, mathematically notated as [start, stop).

```python
my_list = ['Hello, world!', 3.14, 1, [1, 2, 3], False]

my_elem = my_list[0]   # my_elem : 'Hello, world!'
my_elem = my_list[-1]  # my_elem : False

my_sublist = my_list[0:3]    # my_sublist : ['Hello, world!', 3.14, 1]
my_sublist = my_list[-4:-1]  # my_sublist : [3.14, 1, [1, 2, 3]]

# 0 -> 2
my_sublist = my_list[0:4:2]  # my_sublist : ['Hello, world!', 1]

# 4 -> 2
my_sublist = my_list[4:0:-2]  # my_sublist : [False, 1]

# my_list[0] -> 'Hello, world!'
# my_list[0][0] -> 'H'
my_elem = my_list[0][0]  # my_elem : 'H'

# my_list[-2] -> [1, 2, 3]
# my_list[-2][-1] -> 3
my_elem = my_list[-2][-1]  # my_elem : 3

# changing my_list with a more complicated example
my_list = [[1, 2, 3], [4, [4.2, 4.4, 4.6], 5, 6]]

# my_list[1] -> [4, [4.2, 4.4, 4.6], 5, 6]
# my_list[1][1] -> [4.2, 4.4, 4.6]
# my_list[1][1][2] -> 4.6
my_elem = my_list[1][1][2]  # my_elem : 4.6
```

If an index is left ungiven, the rest of the list is obtained beyond, or up to a certain starting, or ending index respectively.

```python
my_list = ['Hello, world!', 3.14, 1, [1, 2, 3], False]

my_sublist = my_list[1:]    # my_sublist : [3.14, 1, [1, 2, 3], False]
my_sublist = my_list[:3]    # my_sublist : ['Hello, world!', 3.14, 1]

# effectively a copy
my_sublist = my_list[:]     # my_sublist : ['Hello, world!', 3.14, 1, [1, 2, 3], False]

# easy way to reverse
my_sublist = my_list[::-1]  # my_sublist : [False, [1, 2, 3], 1, 3.14, 'Hello, world!']
```

## Iteration

A list can be iterated through by index, by element, or by both simultaneously with the help of the `enumerate()` function.

```python
my_list = ['Hello, world!', 3.14, 1, [1, 2, 3], False]

for i in range(len(my_list)):  # i : 0 -> 1 -> 2 -> ...
    print(my_list[i])

for elem in my_list:  # elem : 'Hello, world!' -> 3.14 -> 1 -> ...
    print(elem)

# i : 0 -> 1 -> 2 -> ...
# elem : 'Hello, world!' -> 3.14 -> 1 -> ...
for i, elem in enumerate(my_list):
    print(elem)
```

## Common Methods

### `.append(x)`

Add an item, `x`, to the end of the list. 

```python
my_list = [1, 2, 3]

my_list.append(4)  # my_list : [1, 2, 3, 4]
```

### `.extend(iterable)`

Appends all items from `iterable` to the end of the list. Equivalent to the `+=` operator.

```python
my_list = [1, 2, 3]

my_list.extend( [4, 5, 6] )  # my_list : [1, 2, 3, 4, 5, 6]
```

### `.insert(i, x)`

Inserts the element, `x`, into the list at index `i`.

```python
my_list = [1, 2, 3]

my_list.insert(1, 1.5)  # my_list : [1, 1.5, 2, 3]
```

### `.remove(x)`

Removes the first element of the list whose value is equal to `x`. Raises `ValueError` if no such item exists.

```python
my_list = [1, 2, 3]

my_list.remove(2)  # my_list : [1, 3]
```

### `.pop([i])`

Removes and returns the element at index `i`. If `i` is not given, the last item of the list will be removed (equivalent to `i=-1`).

```python
my_list = [1, 2, 3]

my_val = my_list.pop(1)  # my_list : [1, 3], my_val : 2

my_list.pop()  # my_list : [1]
```

### `.clear()`

Removes all elements from the list.

```python
my_list = [1, 2, 3]

my_list.clear()  # my_list : []
```

### `.index(x[, start[, end]])`

Returns the index of the first item whose value is equal to `x`. Raises `ValueError` if no such item exists.

Optional parameters `start` and `end` can be invoked to search within a particular subset of the list from index `start` to index `end`. The returned index is relative to the beginning of the full sequence, rather than the `start` argument. If `start` is given, and `end` is ungiven, the remaining portion of the list will be searched beginning from `start`. 

```python
# note the extra 'a' strings
my_list = ['a', 'b', 'a', 'd', 'e', 'f', 'a']

i1 = my_list.index('b')        # i1 : 1
i2 = my_list.index('a', 3)     # i2 : 6
i3 = my_list.index('a', 1, 3)  # i3 : 2
```

### `.count(x)`

Returns the number of times `x` appears in the list. 

```python
# note the extra 'a' strings
my_list = ['a', 'b', 'a', 'd', 'e', 'f', 'a']

c = my_list.count('a')  # c : 3
```

### `.sort(key=None, reverse=False)`

Sorts the elements of the list in-place. Ascending order by default.

`key` specifies a function of one argument that returns what each value's order should be determined by.

If `reverse` is set to `True`, the list will be sorted in descending order.

```python
my_list = [5, 2, 4, 3, 1]

my_list.sort()  # my_list : [1, 2, 3, 4, 5]
my_list.sort(reverse=True)  # my_list : [5, 4, 3, 2, 1]
```

```python
from operator import itemgetter

# with nested lists, you can supply a function to 'key'
# to tell .sort() which element of the nested list should
# be used to determine the order. in this example, we could
# choose the first elements (the character strings), or the
# second elements (the numbers)

my_list = [
    ['b', 3],
    ['d', 1],
    ['c', 2],
    ['a', 4],
    ['e', 0]
]

# we create a function that takes one parameter -- that 
# parameter should expect each element of the list to
# be passed into it. in this case: ['a', 4], ['b', 3], 
# ['c', 2], etc.

# if we want to sort by the character strings, then that
# would be the 0th element of each nested list. thus, we
# return the element at index 0

def sort_by_char_string(nested_list: list):
    return nested_list[0]

# if we wanted to sort by the numbers, then that would be
# the 1st element of each nested list. thus, we return the
# element at index 1

def sort_by_number(nested_list: list):
    return nested_list[1]

my_list.sort(key=sort_by_char_string)  # only supply the function name
# my_list : [['a', 4], ['b', 3], ['c', 2], ['d', 1], ['e', 0]]

my_list.sort(key=sort_by_number)
# my_list : [['e', 0], ['d', 1], ['c', 2], ['b', 3], ['a', 4]]

'''
For CSE 231 particularly, we recommend using
the 'itemgetter()' function. This function
does exactly what was just shown, but doesn't 
require that you create functions. You can 
simply give an argument to itemgetter().

If you wanted to sort by the character strings,
(index 0 of each nested list), you'd call 
itemgetter(0). 

my_list.sort(key=itemgetter(0))

This is the default behaviour when sorting nested
lists (meaning key=itemgetter(0) is unnecessary)

If you wanted to sort by the numbers, (index 1 of 
each nested list), you'd call itemgetter(1).

my_list.sort(key=itemgetter(1))
'''
```

### `.reverse()`

Reverses the elements of the list in-place.

```python
my_list = [1, 2, 3]

my_list.reverse()  # my_list : [3, 2, 1]
```

### `.copy()`

Returns a shallow copy of the list. Equivalent to `list[:]`.

```python
my_list = [1, 2, 3]

# equivalent to 'my_list_copy = my_list[:]'
my_list_copy = my_list.copy()  # my_list_copy : [1, 2, 3]

my_list[0] = 100
# my_list : [100, 2, 3]
# my_list_copy : [1, 2, 3]

# the copy is unaffected by changes to the original
```

## List Comprehensions

List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

For example, assume we want to create a list of squares.

```python
squares = []
for x in range(10):
    squares.append(x**2)
```

We can write this more concisely with a list comprehension, as:

```python
squares = [x**2 for x in range(10)]
```

A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new list resulting from evaluating the expression in the context of the `for` and `if` clauses which follow it. For example, this list comprehension combines the elements of two lists if they are not equal:

```python
listcomp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# listcomp : [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

This would be equivalent to:

```python
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append( (x, y) )
```

More examples:

```python
MY_LIST = [-4, -2, 0, 2, 4]

# a : [-8, -4, 0, 4, 8]
a = [x * 2 for x in MY_LIST]

# b : [0, 2, 4]
b = [x for x in MY_LIST if x >= 0]

# c : [4, 2, 0, 2, 4]
c = [abs(x) for x in MY_LIST]

# d : [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
d = [(x, x**2) for x in range(6)]

# e : [0, 0, 0, 0, 0]
e = [0 for i in range(5)]
```
