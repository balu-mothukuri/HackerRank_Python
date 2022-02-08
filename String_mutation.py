"""
Task - Read a given string, change the character at a given index and then print the modified string.

Sample Input
************
abracadabra
5 k

Sample Output
*************
abrackdabra
"""

"""
*** The mutate_string_list method converts the string to a list and then mutates the list and then converts it in to string back.
input params
string - String that needs to be changed
position - The index of the String which needs to be replaced.
character - The new character that needs to be replaced at the given index.
"""


def mutate_string_list(string, position, character):
    string_list = list(string)
    string_list[position] = character
    new_string = "".join(string_list)
    return new_string


"""
*** The mutate_string_slice method mutates the string by slicing the string in to 2 parts, left and right of the position given.
    Then the character at the given position is replaced with the new character and the new string is constructed by adding the slices back.
    new_string = left_slice + character + right_slice  
"""


def mutate_string_slice(string, position, character):
    new_string = string[:position] + character + string[position + 1:]
    return new_string


if __name__ == '__main__':
    s = raw_input('Enter the name of the string : ')
    i, c = raw_input('Enter the index to be replaced and the character to be replaced separated by a space : ').split()
    s_new = mutate_string_slice(s, int(i), c)
    print("The new string is {}".format(s_new))
