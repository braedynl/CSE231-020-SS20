# Lab02 - Example Answer (Undocumented)
# Braedyn Lettinga

in_int = int(input("Input an integer (0 terminates): "))

odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0

while in_int != 0:

    if in_int < 0:
        pass

    else:
        if in_int % 2 == 0:
            even_sum += in_int
            even_count += 1
        
        else:    
            odd_sum += in_int
            odd_count += 1

        positive_int_count += 1
    
    in_int = int(input("Input an integer (0 terminates): "))

print()
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
