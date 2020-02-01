# Lab04 - Example Answer (Documented)
# Braedyn Lettinga
# Noelle and Vinay for amazing float_check() function

def leap_year(year:str):
    '''
    Checks if a leap year is valid
    Year can either be divisible by 400,
    or divisible by 4 but not 100
    '''

    return (int(year) % 400 == 0) or (int(year) % 4 == 0) and not (int(year) % 100 == 0)

def rotate(s:str, n:int):
    '''
    Takes the last `n` characters of a
    string and concatenates them to the
    front of the string.
    '''

    # Gives back the string if empty or 1 character
    if len(s) == 0 or len(s) == 1:
        return s

    # The last `n` characters ([-n:]) + all characters 
    # up to but not including the `n`th character. ([:-n])
    return s[-n:] + s[:-n]    

def digit_count(number):
    '''
    Counts the number of even numbers, odd numbers 
    and zeros up to the first decimal point.
    '''

    number = str(number)    # String conversion to iterate through characters

    even_count = 0
    odd_count = 0
    zero_count = 0

    for val in number:
        if val == ".":    # If we encounter a '.', stop counting
            break

        elif val == "0":
            zero_count += 1

        elif int(val) % 2 == 0:    # even = divisible by 2
            even_count += 1

        elif int(val) % 2 != 0:    # odd = not divisible by 2
            odd_count += 1
    
    return even_count, odd_count, zero_count

def float_check( value:str ):
    '''
    Checks if a given string value can
    be interpreted as a float
    '''

    # Taken from Noelle and Vinay's code, I never
    # thought of doing it like this

    # Replaces a single '.' with nothing, and checks
    #  if the resulting string is composed of all digits.
    return value.replace('.', '', 1).isdigit()