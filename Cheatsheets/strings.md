# Strings Cheatsheet

[String Lectures](https://www.cse.msu.edu/~cse231/Online/strings.html)

In computer science, **strings** (type name: `str`) are an ordered sequence of characters considered to be one of the fundamental data types (the others are `int`, `float` and `bool`). It is the only fundamental data type that is implemented as an array of bytes, making it a type of **container**.

As with all containers, you can count the number of items within by using the `len()` function, (in this case, the number of characters in the string). This can be helpful in many circumstances:

```python
my_str = "Hello, world!"

n = len(my_str)  # n : 13
```

Important to note, is that punctuation and spaces *do* count towards the total number of characters. 

Strings are **immutable**, meaning that they pass by copy. (Don't worry if you don't know what that means yet, it will be explained during week 7)

Jump to section:
1. [Initialization](#initialization)
2. [Operations](#operations)
3. [Indexing](#indexing)
4. [Iteration](#iteration)
5. [Common Methods](#common-methods)

Want to learn more? [Check out Programiz's article on strings!](https://www.programiz.com/python-programming/string)

## Initialization

In Python, strings can be declared using double or single quotation marks. A multi-line string can be declared with a set of three double/single quotation marks. 

```python
# empty string
my_str = ''

# string with initial values (single quotes)
my_str = "Hello, world!"

# string with initial values (double quotes)
my_str = 'Hello, world!'

# multi-line string
my_str = '''
    Hello,
    world!
'''
```

A string can also be declared via its constructor function, or as a conversion from a different type. 

```python
# int conversion
my_str = str(123)  # my_str : '123'

# float conversion
my_str = str(3.14)  # my_str : '3.14'
```

## Operations

Strings interact with two of the mathematical operators, `+` and `*`, and all of the comparison operators, `<`, `>`, `<=`, `>=`, `==`. 

The `+` operator concatenates two strings together. The `+` operator's compound assignment counterpart, `+=`, is also compatible with strings.

```python
my_str = "Hello, " + "world"  # my_str : "Hello, world"
my_str += "!"                 # my_str : "Hello, world!"
```

The `*` operator repeats, and concatenates multiple instances of the given string together. It's compound assignment, `*=`, is also compatible with strings.

```python
my_str = "Hello, " * 2  # my_str : "Hello, Hello, "
my_str *= 2             # my_str : "Hello, Hello, Hello, Hello, "
```

The comparison operators yield `True` or `False`, depending on alphabetical order. The upper-case variant of the alphabet is treated as "earlier" in the alphabet over the lower-case variant. You can think of the comparison sign as an arrow that asks "does this character come before the other?"

```python
# does 'a' come before 'b'?
print('a' < 'b')  # True
```

When longer strings are being compared to each other, Python will compare letter-by-letter if the leading characters are equivalent. 

```python
# 'h' == 'h'
# 'e' == 'e'
# 'y' < 'l' ?
print('hey' < 'hello')  # False
```

## Indexing

Strings can be indexed to extract particular characters or subsets of characters (typically called **substrings**). 

If we had some string, `"Hello, world!"`, the indices for it would be as follows:

<table>
    <thead>
        <th>H</th>
        <th>e</th>
        <th>l</th>
        <th>l</th>
        <th>o</th>
        <th>,</th>
        <th> </th>
        <th>w</th>
        <th>o</th>
        <th>r</th>
        <th>l</th>
        <th>d</th>
        <th>!</th>
    </thead>
    <tbody align="center">
        <tr>
            <td>0</td>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
            <td>5</td>
            <td>6</td>
            <td>7</td>
            <td>8</td>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
        </tr>
        <tr>
            <td>-13</td>
            <td>-12</td>
            <td>-11</td>
            <td>-10</td>
            <td>-9</td>
            <td>-8</td>
            <td>-7</td>
            <td>-6</td>
            <td>-5</td>
            <td>-4</td>
            <td>-3</td>
            <td>-2</td>
            <td>-1</td>
        </tr>
    </tbody>
</table>

Note that indices always begin from 0, and spaces are counted as characters!

To index, you use square brackets (`[]`) with an `int` to denote which index, or set of indices you wish to extract. The arguments are: 

<div align="center"><code>[start : stop : step]</code></div><br>

Where `stop` and `step` are optional. The `stop` index is treated as an uninclusive bound, mathematically notated as [start, stop).

```python
my_str = "Hello, world!"

my_substr = my_str[0]      # my_substr : 'H'
my_substr = my_str[-1]     # my_substr : '!'

my_substr = my_str[0:5]    # my_substr : 'Hello'
my_substr = my_str[-6:-1]  # my_substr : 'world'

# 0 -> 2 -> 4 -> 6 -> 8
my_substr = my_str[0:9:2]  # my_substr : 'Hlo o'

# 9 -> 7 -> 5 -> 3 -> 1
my_substr = my_str[9:0:-2]  # my_substr : 'rw,le'
```

If an index is left ungiven, the rest of the string is obtained beyond, or up to a certain starting, or ending index respectively.

```python
my_str = "Hello, world!"

my_substr = my_str[7:]    # my_substr : 'world!'
my_substr = my_str[:7]    # my_substr : 'Hello, '

# effectively a copy
my_substr = my_str[:]     # my_substr : 'Hello, world!'

# easy way to reverse
my_substr = my_str[::-1]  # my_substr : '!dlrow ,olleH'
```

## Iteration

A string can be iterated through by index, by character, or by both simultaneously with the help of the `enumerate()` function. 

```python
my_str = "Hello, world!"

for i in range(len(my_str)):  # i : 0 -> 1 -> 2 -> ...
    print(my_str[i])

for char in my_str:  # char : 'H' -> 'e' -> 'l' -> ...
    print(char)

#  i   :  0  ->  1  ->  2  -> ...
# char : 'H' -> 'e' -> 'l' -> ...
for i, char in enumerate(my_str): 
    print(char)
```

## Common Methods

### `.capitalize()`

Converts the first character to upper-case.

```python
my_str = 'jack'

my_str = my_str.capitalize()  # my_str : 'Jack'
```

### `.count(sub[, start[, end]])`

Finds the number of occurrences of the substring, `sub`. Optional `start` and `end` index arguments to search within a particular range of the string.

```python
my_str = 'This is an example string!'

c1 = my_str.count('is')        # c1 : 2
c2 = my_str.count('is', 4, 7)  # c2 : 1
```

### `.find(sub[, start[, end]])`

Returns the lowest index where the substring, `sub` is found. Optional `start` and `end` index arguments to search within a particular range of the string. Returns `-1` if `sub` is not found.

```python
my_str = 'This is an example string!'

i1 = my_str.find('is')        # i1 : 2
i2 = my_str.find('is', 4, 7)  # i2 : 5
i3 = my_str.find('hello')     # i3 : -1
```

### `.format(*args, **kwargs)`

Formats a string that contains fields delimited by curly braces (`{}`). Fields can take character-based arguments that adjust the value's presentation.

<div align="center"><code>{:[fill][align][field_width][,][.precision][style]}</code></div><br>

(This has been simplified for the purposes of this course, there are more arguments here that I've omitted since you won't need to know about them, or they're too complicated).

- `fill` - Fills remaining field width space with any given character.
- `align` - Aligns value to the left, right, or in the center of the field width space. 
    - `'<'` - Align left.
    - `'>'` - Align right.
    - `'^'` - Align center.
- `field_width` - An integer value that denotes the amount of space the value is allowed to occupy. 
- `,` - Comma to signify insertion of thousand separators in large numeric values.
- `.precision` - A decimal point followed by an integer value that denotes the number of decimal places to round to.
- `style` - A character that denotes the presentation of the value.
    - String styles
        - `'s'` - String presentation.
        - None - Same as `'s'`. 
    - Integer styles
        - `'d'` - Integer presentation, base 10.
        - `'b'` - Binary presentation, base 2. 
        - `'o'` - Octal presentation, base 8.
        - `'x'` - Hexadecimal presentation, base 16.
        - None - Same as `'d'`.
    - Float styles
        - `'f'` - Float presentation. Default precision is `6`. 
        - `'e'` - Scientific notation presentation. 
        - `'%'` - Percentage presentation. Multiplies the number by 100 and displays in float (`'f'`) format, followed by a percent sign.
        - None - Uses an algorithm to determine a reasonable rounding point that is at least one digit past the decimal point.

```python
my_str = "{}, {}!".format("Hello", "world")  # my_str : 'Hello, world!'
my_str = "{} : {} : {}".format(1, 2, 3)      # my_str : '1 : 2 : 3'
```

```python
# {:[fill][align][field_width][,][.precision][style]}

# [align='>'] [field_width='10'] [,] [style='d']
my_str = "{:>10,d}".format(2000)         # my_str : '     2,000'

# [align='^'] [field_width='20'] [,] [.precision='.2'] [style='f']
my_str = "{:^20,.2f}".format(2459.4678)  # my_str : '      2,459.47      '

# [fill='#'] [align='>'] [field_width='20'] [.precision='.3'] [style='f']
my_str = "{:#>20.3f}".format(3.1415)     # my_str : '###############3.142'
```

### `.index(sub[, start[, end]])`

Similar to `.find()`, but raises `ValueError` when `sub` is not found.

### `.isalnum()`

Returns `True` if all characters in the string are alphanumeric, and there is at least one character, `False` otherwise. A character, `c`, is alphanumeric if one of the following are true: `c.isalpha()`, `c.isdecimal()`, `c.isdigit()`, or `c.isnumeric()`. 

### `.isalpha()`

Returns `True` if all characters in the string are alphabetical and there is at least one character, `False` otherwise.

### `.isdecimal()`

Returns `True` if all characters in the string are decimal characters and there is at least one character, `False` otherwise. 

### `.isdigit()`

Returns `True` if all characters in the string are digits and there is at least one character, `False` otherwise. 

### `.islower()`

Returns `True` is all alphabetical characters in the string are lowercased, and there is at least one alphabetical character.

### `.isnumeric()`

Returns `True` if all characters in the string are numeric characters, and there is at least one character, `False` otherwise.

### `.isupper()`

Returns `True` is all alphabetical characters in the string are uppercased, and there is at least one alphabetical character.

### `.join(iterable)`

Returns a string that is the concatenation of the strings in `iterable`. Raises `TypeError` if there are any non-string values in `iterable`. 

```python
my_list = ["hello", "there", "lad"]

my_str = "--".join(my_list)  # my_str : 'hello--there--lad'
```

### `.lower()`

Returns a copy of the string with all lowercased characters.

```python
my_str = 'HeLLo WoRlD'

my_str = my_str.lower()  # my_str : 'hello world'
```

### `.replace(old, new[, count])`

Returns a copy of the string with all occurrences of `old` replaced by `new`. If the optional `count` argument is given, only the first `count` occurrences are replaced.

```python
my_str = 'This is an example string!'

r1 = my_str.replace('is', 'iz')     # r1 : 'Thiz iz an example string!'
r2 = my_str.replace('is', 'iz', 1)  # r2 : 'Thiz is an example string!'
```

### `.rfind(sub[, start[, end]])`

Returns the highest index where the substring, `sub` is found. Optional `start` and `end` index arguments to search within a particular range of the string. Returns `-1` if `sub` is not found.

```python
my_str = 'This is an example string!'

i1 = my_str.rfind('is')        # i1 : 5
i2 = my_str.rfind('is', 0, 4)  # i2 : 2
i3 = my_str.rfind('hello')     # i3 : -1
```

### `.rindex(sub[, start[, end]])`

Similar to `.rfind()`, but raises `ValueError` when `sub` is not found.

### `.split(sep=None, maxsplit=-1)`

Returns a `list` of the words in the string, using `sep` as the delimiter string. If `maxsplit` is given, at most `maxsplit` splits are performed (thus, the list will have at most `maxsplit + 1` elements). If `maxsplit` is not specified or `-1`, then there is no limit on the number of splits (all possible splits are made).

If `sep` is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings. If `sep` is not specified or `None`, consecutive whitespaces are regarded as separators. 

```python
my_list = '1,2,3'.split(',')     # my_list : ['1', '2', '3']
my_list = '1,2,3'.split(',', 1)  # my_list : ['1', '2,3']
my_list = '1,2,,3,'.split(',')   # my_list : ['1', '2', '', '3', '']
```

```python
my_list = '1    2   3'.split()          # my_list : ['1', '2', '3']
my_list = '1   2  3'.split(maxsplit=1)  # my_list : ['1', '2  3']
```

### `.strip([chars])`

Returns a copy of the string with the leading and trailing characters removed. The `chars` argument is a string specifying the set of characters to be removed. If omitted or `None`, the `chars` argument defaults to removing whitespace. 

```python
my_str = '    spacious    '.strip()         # my_str : 'spacious'
my_str = 'www.example.com'.strip('cmowz.')  # my_str : 'example'
```

### `.title()`

Returns a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase. 

```python
my_str = 'hello world'

my_str = my_str.title()  # my_str : 'Hello World'
```

### `.upper()`

Returns a copy of the string with all uppercased characters.

```python
my_str = 'HeLLo WoRlD'

my_str = my_str.upper()  # my_str : 'HELLO WORLD'
```

### `.zfill(width)`

Returns a copy of the string with padding `'0'` digits until the length of the string is equal to `width`. 

```python
my_str = '42'

my_str = my_str.zfill(5)  # my_str : '00042'
```