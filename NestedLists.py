#Nested Lists

"""
Find the names of student(s) who have the 2nd lowest score in a class of N students given their names and scores.
The program should allow the i/ps including the number of students in the class, their names and scores are dynamically
entered from the console.
The o/p is the name of the student who has the 2nd lowest score. If there are multiple students that have the 2nd lowest
score then print their names in alphabetical order.

sample i/p - the user would enter this in the console at run time

4
Balu
80
Sriram
85
Radhika
85
Srividya
90

sample o/p

Radhika
Sriram
"""

if __name__ == '__main__':
    records = []
    for _ in range(int(input("Enter the number of students : "))):
        student_name = str(input("\n Enter the name of the student : "))
        student_score = float(input("\n Enter the score of the student : "))
        records.append([student_name, student_score])
    second_lowest = sorted(list(set([score for name, score in records])))[1]
    print('\n'.join(sorted([name for name, score in records if score == second_lowest])))
