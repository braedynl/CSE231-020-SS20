'''
PROBLEM
-------

Create a class called "RipOffSet" that simulates
the functionality of a traditional Python set,
but uses lists internally.

When elements are added, duplicate values should
be discarded (just like a set).

The class should have the following method functions:

__init__(self, li:list=None) -> None

    The constructor can take a list instance (li) to convert
    into a RipOffSet. The constructor defaults this parameter
    to None. If left as None, an empty RipOffSet is created.

__str__(self) -> str

    Represents the RipOffSet as a string. Just like the Python
    set type, curly brackets should be used to represent the
    beginning and end of the contained elements. (Allows
    compatability with the str() and print() functions).

__repr__(self) -> str

    Should be the same as __str__. Allows compatability with the
    repr() function.

__len__(self) -> int

    Returns the number of elements in the RipOffSet (allows 
    compatability with the len() function).

add(self, elem) -> None

    Adds an element of any type to the RipOffSet. If the element
    already exists in the RipOffSet, no appendation occurs.

remove(self, elem) -> None

    Removes an element from the RipOffSet. If the element doesn't
    exist inside the RipOffSet, raise a KeyError.

union(self, other:RipOffSet) -> RipOffSet

    Combines the elements of the RipOffSet and another RipOffSet
    instance. Returns the union of the two (all elements of the
    two operand sets combined into one RipOffSet, remember to 
    remove duplicate elements!).

intersection(self, other:RipOffSet) -> RipOffSet

    Creates a new RipOffSet instance composed of the elements
    shared between the RipOffSet and the passed-in RipOffSet instance.
    (Remember to remove duplicate elements!)

difference(self, other:RipOffSet) -> RipOffSet

    Creates a new RipOffSet instance composed of all elements
    in this RipOffSet but not in the other RipOffSet.

symmetric_difference(self, other:RipOffSet) -> RipOffSet

    Creates a new RipOffSet instance composed of all elements
    unique to both RipOffSets.

EXAMPLE FUNCTIONALITY
---------------------

s = RipOffSet([1, 2, 3, 3, 3])
print(s)  # {1, 2, 3}

s.add(4)
print(s)  # {1, 2, 3, 4}

s.remove(4)
print(s)  # {1, 2, 3}
print(len(s))  # 3

t = RipOffSet([2, 3, 4, 5])
print(t)  # {2, 3, 4, 5}

s_union_t = s.union(t)
print(s_union_t)  # {1, 2, 3, 4, 5}

s_int_t = s.intersection(t)
print(s_int_t)  # {2, 3}

s_diff_t = s.difference(t)
print(s_diff_t)  # {1}

s_symdiff_t = s.symmetric_difference(t)
print(s_symdiff_t)  # {1, 4, 5}

u = RipOffSet()
print(u)  # {}
'''

from __future__ import annotations


class RipOffSet():

    def __init__(self, li:list=None):
        # we'll use this data member to hold all contents
        # of the RipOffSet instance
        self.items = []

        if li is not None:                   # iterate through the list if provided
            for elem in li:
                if elem not in self.items:   # only append if the element isn't
                    self.items.append(elem)  # already in the items list
    
    def __str__(self) -> str:
        out_str = '{'                          # start with an opening curly bracket
        for i, elem in enumerate(self.items):  # iterate through all items
            if i != len(self.items) - 1:       # if it's not the last item in the list,
                out_str += repr(elem) + ', '   # concatenate, add comma between
            else:                              # otherwise,
                out_str += repr(elem)          # concatenate, no comma
        out_str += '}'                         # close off the curly bracket
        
        return out_str

    __repr__ = __str__  # you can make two methods identical by doing this

    def __len__(self) -> int:
        return len(self.items)  # since .items is a list, we can just take the len() of that

    def add(self, elem) -> None:
        if elem not in self.items:   # if not already in the items list,
            self.items.append(elem)  # append it

    def remove(self, elem) -> None:
        try:
            self.items.remove(elem)            # we can use the list remove method!
        except ValueError:                     # it raises ValueError if the element can't be found, so
            raise KeyError("{}".format(elem))  # we'll re-brand it as a KeyError

    def union(self, other:RipOffSet) -> RipOffSet:
        # remember that our constructor method discards duplicate values from a given 
        # list! we can concatenate the two RipOffSet .items members together, and pass 
        # that to the constructor to make a new instance with all potential duplicates removed
        return RipOffSet(self.items + other.items)

    def intersection(self, other:RipOffSet) -> RipOffSet:
        shared_items = []                  # we'll create a list of the shared items

        for elem in self.items:            # iterate through our items
            if elem in other.items:        # check if those elements are in the other set items
                shared_items.append(elem)  # if they are, append to our shared list

        return RipOffSet(shared_items)     # create a new RipOffSet instance from that

    def difference(self, other:RipOffSet) -> RipOffSet:
        diff = []

        for elem in self.items:          # notice how similar difference is to intersection?
            if elem not in other.items:  # only append our elements to a new list if it's not in
                diff.append(elem)        # the other RipOffSet
        
        return RipOffSet(diff)

    def symmetric_difference(self, other:RipOffSet) -> RipOffSet:
        sym_diff = []

        for elem in self.items:          # iterate through our items,
            if elem not in other.items:  # if not in the other RipOffSet,
                sym_diff.append(elem)    # append
        
        for elem in other.items:         # iterate through the other RipOffSet,
            if elem not in self.items:   # if not in our items,
                sym_diff.append(elem)    # append
        
        return RipOffSet(sym_diff)


s = RipOffSet([1, 2, 3, 3, 3])
print(s)  # {1, 2, 3}

s.add(4)
print(s)  # {1, 2, 3, 4}

s.remove(4)
print(s)  # {1, 2, 3}
print(len(s))  # 3

t = RipOffSet([2, 3, 4, 5])
print(t)  # {2, 3, 4, 5}

s_union_t = s.union(t)
print(s_union_t)  # {1, 2, 3, 4, 5}

s_int_t = s.intersection(t)
print(s_int_t)  # {2, 3}

s_diff_t = s.difference(t)
print(s_diff_t)  # {1}

s_symdiff_t = s.symmetric_difference(t)
print(s_symdiff_t)  # {1, 4, 5}

u = RipOffSet()
print(u)  # {}