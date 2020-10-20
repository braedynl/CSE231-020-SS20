# Lists Cheatsheet

In computer science, **lists** (`list`) are an ordered sequence of elements, categorized as one of the basic data structures. Lists are a type of **container**. Unlike strings, however, they can hold *any* type including multiple instances of themselves — what would generally be referred to as a **nested list** or a **matrix**.

The `len()` function can be used to determine the number of elements within a list:

```python
my_list = [1, 2, 3]

n = len(my_list)  # n : 3
```

If all of the elements within a given list are type `int` or `float`, the `sum()` function can be used to sum together all values within the list. 

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
