'''
CSE231 - Introduction to Programming I
Lab 6
Example Solution

Author: Braedyn Lettinga
'''

fp = open("scores.txt", "r")

# We're going to store the rows of student data in this list
student_matrix = []

# ...and store all of their exam X scores here
exam1_scores = []
exam2_scores = []
exam3_scores = []
exam4_scores = []

for line in fp:

    # The file contains a lot of whitespace between each value that we want,
    # so using .split() without any arguments works well here.
    # This has the side-effect of making the last and first name separate, but we'll take
    # care of that later. The list will look something like this for all students:
    # ["last_name, ", "first_name", "exam1_score", "exam2_score", "exam3_score", "exam4_score"]
    student_data = line.strip().split()

    # To make this easier for later, I'm going to calculate the average exam score *as we're
    # reading through each row* and append the average exam score for the student to their
    # list of info.
    student_avg = 0

    # remember that the last and first names are occupying indices 0 and 1, all of the exam
    # scores are from index 2 and beyond, thus student_data[2:]
    for exam_score_str in student_data[2:]:
        student_avg += int(exam_score_str)

    student_avg /= 4  # we can assume 4 exam scores
    student_data.append(student_avg)

    # Append all the exam scores to the other lists we had earlier
    exam1_scores.append(int(student_data[2]))
    exam2_scores.append(int(student_data[3]))
    exam3_scores.append(int(student_data[4]))
    exam4_scores.append(int(student_data[5]))

    # append each row of student data to another list for a model of the file
    student_matrix.append(student_data)

# We want to print all of the data organized by student name, and so .sort()
# will compare the first element in each inner-list to each other, automatically
# giving us the alphebatized order since ASCII characters are sequentially numbered internally. 
student_matrix.sort()

# print our header
print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))

# and now we can just iterate through our big list from before to get all of the data
for student_data in student_matrix:
    print("{:20s}{:>6}{:>6}{:>6}{:>6}{:>10.2f}".format(
        " ".join(student_data[0:2]),    # we can use .join() to combine the last and first names
        student_data[2],    # Exam 1
        student_data[3],    # Exam 2
        student_data[4],    # Exam 3
        student_data[5],    # Exam 4
        student_data[6]     # Exam average for student (remember we appended it earlier!)
        )
    )

print("{:20s}{:>6}{:>6}{:>6}{:>6}".format(
    "Exam Mean", 
    sum(exam1_scores)/len(exam1_scores),    # Since we made all of the "examX_scores" lists,
    sum(exam2_scores)/len(exam2_scores),    # we can easily calculate the average just by
    sum(exam3_scores)/len(exam3_scores),    # sum()'ing them and dividing by the len()
    sum(exam4_scores)/len(exam4_scores) 
    )
)
