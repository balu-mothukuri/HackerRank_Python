"""
Task - Print the number of times that the substring occurs in the given string
"""

"""
** find_substr_in_str_count - The function counts the number of times a given substring is present in a string.
   Uses find() function to get the index of the substr present in the string. 
** input params
    str - string to searched on
    substr - string to be searched for
** output params
    count  - Returns the number of times a substring is present in a string.
"""


def find_substr_in_str_count(str, substr):
    substr_count = 0
    while substr in str:
        substr_count += 1
        str = str[str.find(substr) + 1:]
    return substr_count


"""
contains_substr_in_str_count() function loops through the string and checks to see each time if the substring is what 
the string starts with.
This function loops through the string and uses startswith() to check if the substring is what the string starts with.
** input params
    str - string to searched on
    substr - string to be searched for
** output params
    count  - Returns the number of times a substring is present in a string.
"""


def contains_substr_in_str_count(str, substr):
    substr_count = 0
    for i in range(0, (len(str) - len(substr) + 1)):
        if str[i:].startswith(substr):
            substr_count += 1
    return substr_count


if __name__ == '__main__':
    str = raw_input('Enter the string to be searched on : ')
    substr = raw_input('Enter the string to be searched for : ')
    count = contains_substr_in_str_count(str, substr)
    print("The number of times the substring is present in the string is {}".format(count))
