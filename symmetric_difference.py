"""
Task - In a college students have subscribed to both English and French Newspapers.
Identify the number of students who have subscribed to only English or French newspapers but not both.

Input
*****
First line - No of students who have subscribed to the English Newspaper
Second line - List of student roll numbers who have subscribed to English Newspaper
Third line - No of students who have subscribed to the French Newspaper
Fourth line - List of student roll numbers who have subscribed to French Newspaper

Output
******
Total number of students who have subscriptions to the English or the French newspaper but not both.

"""

if __name__ == '__main__':
    _, r1 = raw_input(), set(raw_input().split())
    _, r2 = raw_input(), set(raw_input().split())
    print(len(r1.symmetric_difference(r2)))