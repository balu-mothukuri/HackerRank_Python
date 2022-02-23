"""
Task - Capitalize the first letter of each word in the given string.

For example -
'balu mothukuri' needs to be converted to "Balu Mothukuri"
"123ab" should remain as "123ab"
"""

"""
input - string to be capitalized
output - string which has the first letter of each word capitalized. 

Note - title() method capitalizes the first letter of every word in a string and this will avoid looping.

"""
def capitalize(string):
    return(' '.join([word.capitalize() for word in string.split(' ')]))

if __name__=='__main__':
    s = raw_input('Enter the string to be capitalized : ')
    result = capitalize(s)
    print(result)