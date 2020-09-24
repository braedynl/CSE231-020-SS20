'''
This file simply contains a function that prints a 
dictionary with proper indentation and newlines.

If you use print() to debug your code a lot, please
feel free to bring this function into your program and
use it for yourself. Python unfortunately doesn't do
a good job of printing large and/or nested dictionaries, 
so we have to make functions that will.

The function uses some fairly advanced Python that is
unnecessary for you to know for the purposes of this
course. Feel free to look into the concepts used here on
your own, though — it takes advantage of recursion and 
closures/inner-functions:
https://www.programiz.com/python-programming/recursion
https://www.programiz.com/python-programming/closure
'''

def pretty_print_dict(dictionary: dict) -> None:
    '''
    Prints a dictionary instance with better formatting.

    Copy and paste this function into your program!
    '''

    if not isinstance(dictionary, dict):
        raise TypeError("argument {} not supported, must be <class 'dict'>".format(type(dictionary)))

    def helper(dictionary: dict, layer: int) -> None:
        print('{')
        for key, value in dictionary.items():
            print(layer * 4 * ' ' + '{} : '.format(repr(key)), end='')
            if isinstance(value, dict):
                helper(value, layer + 1)
            else:
                print(repr(value) + ',')
        print((layer - 1) * 4 * ' ' + '}', end='')
        if layer > 1:
            print(',')
        else:
            print()

    helper(dictionary, 1)


# fully capable of handling nested dictionaries!
example = {
    'a' : [1, 2, 3, 4, 5],
    'b' : [1, 'test', '123', 5],
    'c' : {
        'a' : (1, 2, 3, 4, 5),
        'b' : {
            'a' : 1, 
            'b' : 2,
            'c' : 3
        }
    }
}

pretty_print_dict(example)