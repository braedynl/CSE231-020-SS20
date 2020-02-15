# Lab06 - Example Answer (Undocumented)
# Braedyn Lettinga

in_file = open("scores.txt", "r")

student_matrix = []

exam1_scores = []
exam2_scores = []
exam3_scores = []
exam4_scores = []

for line in in_file:
    line = line.strip()
    
    student_data = line.split()

    student_data.append( 
        sum( [ int(i) for i in student_data[2:] ] ) / len( student_data[2:] )  
        )

    exam1_scores.append(int(student_data[2]))
    exam2_scores.append(int(student_data[3]))
    exam3_scores.append(int(student_data[4]))
    exam4_scores.append(int(student_data[5]))

    student_matrix.append(student_data)

student_matrix.sort()

print("{:20s}{:>6s}{:>6s}{:>6s}{:>6s}{:>10s}".format("Name", "Exam1", "Exam2", "Exam3", "Exam4", "Mean"))
for student_data in student_matrix:
    print("{:20s}{:>6}{:>6}{:>6}{:>6}{:>10.2f}".format(
        " ".join(student_data[0:2]), 
        student_data[2], 
        student_data[3], 
        student_data[4], 
        student_data[5], 
        student_data[6]
        )
    )

print("{:20s}{:>6}{:>6}{:>6}{:>6}".format(
    "Exam Mean", 
    sum(exam1_scores)/len(exam1_scores), 
    sum(exam2_scores)/len(exam2_scores), 
    sum(exam3_scores)/len(exam3_scores), 
    sum(exam4_scores)/len(exam4_scores) 
    )
)