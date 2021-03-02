# Finding the percentage

"""
Find the average marks of a given student.
"""

from statistics import mean

if __name__ == '__main__':
    records = {}
    for i in range(int(input('Enter the number of students : '))):
        name, score_str = input('Enter the student and scores : ').split(' ', 1)
        scores = list(map(float, score_str.split()))
        records[name] = scores
    query_name = input('Enter the name of the student who average marks need to be calculated : ')
    print("The average marks of the student {} is {:0.2f}".format(query_name, round(mean(records.get(query_name)),2)))
