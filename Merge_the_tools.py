"""
Task - Split the string s in to n/k substrings where n is the length of the string and k is the length of each substring
Print each substring in a new line.

For a complete description of the problem refer to the below link
https://www.hackerrank.com/challenges/merge-the-tools/problem
"""

"""
input
string - to be split
k - length of each substring

output - print n/k substrings with each substring of length k in a new line. 

"""
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s_result = ''
        for c in string[i:i+k]:
            if c not in s_result:
                s_result += c
        print(s_result)



if __name__=='__main__':
    s = raw_input('Enter the string to be split : ')
    k = int(raw_input('Enter the no of parts the string needs to be split in to : '))
    merge_the_tools(s,k)