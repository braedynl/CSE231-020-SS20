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

def read_file_with_lists(fp):

    fp.readline()  # skips header line

    # we create two lists, one to hold all of the GPAs, and one
    # to hold all of the exam scores
    gpas = []
    exam_scores = []

    # iterates through each line (type: str) beginning from Bobby,
    # since we skipped (or "read") the header on line 25
    for line in fp:  
        
        # extract the necessary information from the line,
        # converting to appropriate types
        name = line[0:8]
        exam_score = int(line[8:11])
        gpa = float(line[24:27])

        # add our exam score and GPA to the lists 
        exam_scores.append(exam_score)
        gpas.append(gpa)
    
    # with all of the GPAs and exam scores grouped together in lists,
    # we can use some of the standard Python functions to do the
    # arithmetic for us

    # the length of the lists, in this case, is equivalent to the
    # number of students in the file, since there will only be
    # an appended score/GPA if the student was in the file at all
    avg_exam_score = sum(exam_scores) / len(exam_scores)
    max_exam_score = max(exam_scores)
    min_exam_score = min(exam_scores)

    avg_gpa = sum(gpas) / len(gpas)
    max_gpa = max(gpas)
    min_gpa = min(gpas)

    # we're done!
    print("EXAM_SCORE")
    print("Average: {}, Max: {}, Min: {}".format(avg_exam_score, max_exam_score, min_exam_score))
    print()
    print("GPA")
    print("Average: {}, Max: {}, Min: {}".format(avg_gpa, max_gpa, min_gpa))


fp = open('Scripts/read_file_data.txt', 'r')

read_file_with_lists(fp)  # example call
