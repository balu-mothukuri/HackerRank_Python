"""
Task - Given a String S, task is to find out if the string  contains atleast one alphanumeric character,
one alphabetical character, one digit, one lowercase and one uppercase characters.

Input Format
************
A single line containing a string S.

Output Format
*************
In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
"""

"""
** string_validator() function loops through each character of a string and checks to see if each character is 
alphanumeric, alphabetic etc.
If any character in the string matches the criteria then print the result as True, else print the result as False.
"""


def string_validator(str):
    print('Are there any alpha numeric characters in the string : {}'.format(any([c.isalnum() for c in str])))
    print('Are there any alphabetical characters in the string : {}'.format(any([c.isalpha() for c in str])))
    print('Are there any digits in the string : {}'.format(any([c.isdigit() for c in str])))
    print('Are there any lowercase characters in the string : {}'.format(any([c.islower() for c in str])))
    print('Are there any uppercase characters in the string : {}'.format(any([c.isupper() for c in str])))


if __name__ == '__main__':
    s = raw_input('Enter the string to check : ')
    string_validator(s)