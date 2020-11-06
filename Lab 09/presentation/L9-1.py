# Let's pretend we have a CSV file of students with their names, ages, 
# genders and years. However, there are duplicate entries in the file 
# that we're given, in which the LATEST entry is the most recent (and
# therefore desired) information for that student.

# We're then tasked with creating a program that will print the LATEST
# information for ALL students. The order in which students are printed
# should be alphabetically-organized by their name. The order in which the
# info for each student is printed should also be alphabetically-organized.

# Sometimes, there are name entries filled-in as "null". Our document
# says to ignore these entries entirely. 

import csv 

def update_dict(reader, student_dict):

    next(reader)  # skips header line

    for line_list in reader:

        # extract all necessary info
        name = line_list[0]
        age = int(line_list[1])
        gender = line_list[2]
        year = int(line_list[3])

        if name == 'null':  # skip row if name is 'null'
            continue
        
        # if the name isn't a key in the outer-most dict,
        # we insert the name-key, with a dictionary of that individual's
        # attributes for the CURRENT row
        if name not in student_dict:
            student_dict[name] = { 'age': age, 'gender': gender, 'year': year }
        
        # else if the name is ALREADY A KEY in the outer-most dict,
        # we access all of the attributes and overwrite them, since 
        # the LATEST entries in the CSV file are the "correct" ones.
        elif name in student_dict:
            student_dict[name]['age'] = age
            student_dict[name]['gender'] = gender
            student_dict[name]['year'] = year
    
    # Notice how I don't have a return here!
    # Dictionaries are MUTABLE, remember. The student_dict
    # parameter is referencing the same student_dict in main(). 

def print_dict(student_dict):

    # we can take the list of student names (the keys
    # of the outer-most dictionary), sort them, and then
    # iterate through that sorted list of student names
    sorted_names = sorted(student_dict.keys())

    for name in sorted_names:
        print(name)

        # then, we sort the attributes associated with the student
        # i.e. 'age' first, 'gender' second, 'year' third.
        # This is a dictionary, remember!
        sorted_attributes = sorted(student_dict[name].keys())

        for attribute in sorted_attributes:
            print('- {} : {}'.format(attribute.title(), student_dict[name][attribute]))
        
        print()  # prints a newline between each student

def main():
    student_dict = {}
    reader = csv.reader(open('students.csv', 'r'))

    update_dict(reader, student_dict)
    print_dict(student_dict)

if __name__ == "__main__":
    main()