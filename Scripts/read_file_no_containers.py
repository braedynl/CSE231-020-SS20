'''
PROBLEM
-------

Given a text file with the following content:

NAME    EXAM_SCORE      GPA
Bobby   90              3.8
Dina    92              3.9
Wungus  84              3.5
Donald  72              3.4
Kyle    100             4.0
Jack    60              3.0
Lily    80              3.4
Eva     85              3.9

Find/calculate the average, maxmimum, and minimum
EXAM_SCORE and GPA across the entire student base.

For each row, you may assume that the NAME column
is within the index bounds of [0:8], the EXAM_SCORE
column is within the index bounds of [8:11], and the
GPA column is within the index bounds of [24:27].
'''

def read_file_no_containers(fp):

    fp.readline()  # skips header line

    # initialize some variables to hold our information as
    # we find it. we'll start min variables arbitrarily high
    # to keep minimizing with each row
    avg_gpa = 0
    max_gpa = 0
    min_gpa = 10**6

    avg_exam_score = 0
    max_exam_score = 0
    min_exam_score = 10**6

    # we'll have this variable to keep track of the number of
    # students in the file
    n = 0

    # iterates through each line (type: str) beginning from Bobby,
    # since we skipped (or "read") the header on line 25
    for line in fp:  
        
        # extract the necessary information from the line,
        # converting to appropriate types
        name = line[0:8]
        exam_score = int(line[8:11])
        gpa = float(line[24:27])

        avg_gpa += gpa  # continually add together all GPAs
        if gpa > max_gpa:  # if we find a new, greater GPA
            max_gpa = gpa  # that becomes the new max GPA
        if gpa < min_gpa:  # similarly, if we find a new, lesser GPA
            min_gpa = gpa  # that becomes the new min GPA

        # same sort of deal with the exam scores
        avg_exam_score += exam_score
        if exam_score > max_exam_score:
            max_exam_score = exam_score
        if exam_score < min_exam_score:
            min_exam_score = exam_score

        n += 1  # increment number of students
    
    # we've now summed up all of the scores and GPAs,
    # so we divide those sums by the number of students
    avg_gpa /= n
    avg_exam_score /= n

    # we're done!
    print("EXAM_SCORE")
    print("Average: {}, Max: {}, Min: {}".format(avg_exam_score, max_exam_score, min_exam_score))
    print()
    print("GPA")
    print("Average: {}, Max: {}, Min: {}".format(avg_gpa, max_gpa, min_gpa))


fp = open('Scripts/read_file_data.txt', 'r')

read_file_no_containers(fp)  # example call
