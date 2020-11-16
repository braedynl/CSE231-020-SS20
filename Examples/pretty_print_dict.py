'''
This file contains a function that prints a dictionary 
with prettier indentation and newline spacing.

If you use print() to debug your code a lot, feel free 
to bring this function into your program and use it!
'''

def pretty_print_dict(D: dict, info: bool=False) -> None:
    '''
    Prints a dictionary with indentation and newline separation. This
    function does not return anything.

    Copy and paste this function into your program to get a better
    look at your dictionary!

    Parameters
    ----------
    D: dict
        The dictionary instance to print.
    info: bool=False
        Option to print additional information about the dictionary.
        Defaulted to False.

    Notes
    -----
    The "Number of Key-Value Pairs" considers the number of pairs in
    the outer-most dictionary only.

    The "Maximum Nesting Depth" is the maximum number of times a
    dictionary is nested in D, i.e., the number of traversals one would
    have to perform in order to obtain the "deepest" nested dictionary.
    A dictionary that does not have any nested dictionaries as values
    has a maximum nesting depth of 0.
    '''

    if not isinstance(D, dict):
        raise TypeError("argument {} not supported, must be <class 'dict'>".format(type(D)))

    max_depth = 0

    def helper(D: dict, depth: int) -> None:
        nonlocal max_depth
        if depth > max_depth:
            max_depth = depth
        print('{')
        for key, value in D.items():
            print(depth * 4 * ' ' + '{} : '.format(repr(key)), end='')
            if isinstance(value, dict):
                helper(value, depth + 1)
            else:
                print(repr(value) + ',')
        print((depth - 1) * 4 * ' ' + '}', end='')
        if depth > 1:
            print(',')
        else:
            print()

    helper(D, 1)

    if info:
        key_list = list(D.keys())
        print("Number of Key-Value Pairs: {}".format(len(D)))
        print("Maximum Nesting Depth: {}".format(max_depth - 1))
        print("First Key: {} (type: {})".format(repr(key_list[0]), type(key_list[0])))
        print("Last Key: {} (type: {})".format(repr(key_list[-1]), type(key_list[-1])))


# fully capable of handling nested dictionaries!
example = {
    'a' : 1,
    'b' : [1, 'test', '123', 5],
    'c' : {
        'a' : (1, 2, 3, 4, 5),
        'b' : {
            'a' : 1, 
            'b' : 2,
            'c' : {
                'a': {'a', 'b', 'c'}
            }
        }
    }
}

# example call
pretty_print_dict(example)

# to print extra information, supply True to the second argument
# pretty_print_dict(example, True)