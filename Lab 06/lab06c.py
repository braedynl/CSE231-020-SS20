# Lab06 - Example Answer (Documented)
# Braedyn Lettinga

in_file = open("scores.txt", "r")

# We're going to store the rows of student data into this list here
student_matrix = []

# ...and store all of their examX scores here
exam1_scores = []
exam2_scores = []
exam3_scores = []
exam4_scores = []

for line in in_file:
    line = line.strip()
    

    # The file contains a lot of whitespace between each value that we want,
    # so using .split() without any arguments works well here.
    # This has the side-effect of making the last and first name separate, but we'll take
    # care of that later. The list will look something like this:
    # ["last_name", "first_name", "exam1_score", "exam2_score", "exam3_score", "exam4_score"]
    student_data = line.split()


    # The upcoming line is complicated, I'll try my best to explain.
    # What I want to do is find the mean of all exam scores for some student, X, 
    # and append that mean to X's student_data list. Since the first two indices of the list
    # are always going to be the last and first name, we need to extract index 2 onwards, student_data[2:]. 

    # What I'm doing here, then, is creating another list just of student[2:], but where each exam
    # score is converted to an int since it was originally a string. I'm then using the sum() and len()
    # functions to add all of the scores up and divide that by the number of scores, or in other words, the average.
    student_data.append( 
        sum( [ int(i) for i in student_data[2:] ] ) / len( student_data[2:] )  
        )

    # Append all the exam scores
    exam1_scores.append(int(student_data[2]))
    exam2_scores.append(int(student_data[3]))
    exam3_scores.append(int(student_data[4]))
    exam4_scores.append(int(student_data[5]))

    # ..and appending the student_data list to our bigger list from the top
    student_matrix.append(student_data)

# We want to print all of the data organized by student name, and so .sort()
# will compare the first element in each inner-list to another, automatically
# giving us the alphebatized order since ASCII characters are sequentially numbered. 
student_matrix.sort()

print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))

# We can just iterate through our big list from before to get all of the data
for student_data in student_matrix:
    print("{:20s}{:>6}{:>6}{:>6}{:>6}{:>10.2f}".format(
        " ".join(student_data[0:2]),    # ..and we can use .join() to re-combine the last and first name
        student_data[2],    # Exam 1 
        student_data[3],    # Exam 2
        student_data[4],    # Exam 3
        student_data[5],    # Exam 4
        student_data[6]     # Mean Score
        )
    )

print("{:20s}{:>6}{:>6}{:>6}{:>6}".format(
    "Exam Mean", 
    sum(exam1_scores)/len(exam1_scores),    # Since we made all of the examX_scores lists,
    sum(exam2_scores)/len(exam2_scores),    # we can easily calculate the average just by
    sum(exam3_scores)/len(exam3_scores),    # sum()'ing them and dividing by the len()
    sum(exam4_scores)/len(exam4_scores) 
    )
)