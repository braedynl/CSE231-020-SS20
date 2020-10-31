'''
CSE231 - Introduction to Programming I
Lab 4
Example Solution

Author: Braedyn Lettinga
'''

def leap_year(year: str) -> bool:
    '''
    Checks if a given year is a leap year.

    Parameters
    ----------
        year : Year to check.
    
    Returns
    -------
        bool : True if year is a leap year,
               False otherwise.
    '''
    # incoming year value is as a string, so
    # conversion to int is necessary here
    year = int(year)

    # this statement could be interpreted as:
    # "if the year is exactly divisible by 400,
    # or exactly divisible by 4 but not 100"
    return (year % 400 == 0) or ( (year % 4 == 0) and not (year % 100 == 0) )


def rotate(s: str, n: int) -> str:
    '''
    Cut-and-pastes the last n characters of
    a given string to the front of the string.

    Parameters
    ----------
        s : The string to rotate.
        n : Number of last characters to rotate.
    
    Returns
    -------
        str : The edited string copy.
    '''

    # if the string is empty or is one character,
    # return back the input string
    if len(s) == 0 or len(s) == 1:
        return s
    
    # the last n characters ([-n:]), concatenated
    # to every character up to, but not including,
    # the nth character ([:-n])
    return s[-n:] + s[:-n]


def digit_count(number: int) -> (int, int, int):
    '''
    Counts the number of even, odd, and zero
    digits inside a number up to the first
    decimal point.

    Parameters
    ----------
        number : The number to count through.
    
    Returns
    -------
        (int, int, int) : A count of the even, odd,
            and zero digits inside the number.
    '''

    # convert to string to iterate through
    number = str(number)

    # initialize counters
    even_count = 0
    odd_count = 0
    zero_count = 0
    
    for digit in number:

        # if character is a decimal point,
        # stop counting
        if digit == '.':
            break
            
        elif digit == '0':
            zero_count += 1
        
        # if exactly divisible by 2, even
        elif int(digit) % 2 == 0:
            even_count += 1
        
        # if not exactly divisible by 2, odd 
        elif int(digit) % 2 != 0:
            odd_count += 1

    return even_count, odd_count, zero_count


def float_check(value: str) -> bool:
    '''
    Tests if a given string value could
    be interpreted as a float.

    Parameters
    ----------
        value : String value to test.

    Returns
    -------
        bool : True if float, False otherwise.
    '''

    # replace a single decimal point with nothing,
    # and check if the resulting value contains all
    # digits
    return value.replace('.', '', 1).isdigit() 