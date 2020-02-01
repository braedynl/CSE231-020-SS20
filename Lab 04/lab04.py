# Lab04 - Example Answer (No Documentation)
# Braedyn Lettinga
# Noelle and Vinay for amazing float_check() function

def leap_year(year:str):
    return (int(year) % 400 == 0) or (int(year) % 4 == 0) and not (int(year) % 100 == 0)


def rotate(s:str, n:int):
    if len(s) == 0 or len(s) == 1:
        return s

    return s[-n:] + s[:-n]    


def digit_count(number):
    number = str(number)

    even_count = 0
    odd_count = 0
    zero_count = 0

    for val in number:
        if val == ".":
            break

        elif val == "0":
            zero_count += 1

        elif int(val) % 2 == 0:
            even_count += 1

        elif int(val) % 2 != 0:
            odd_count += 1
    
    return even_count, odd_count, zero_count


def float_check( value:str ):
    return value.replace('.', '', 1).isdigit()