"""
Swap Case
*********
initialize the result string.
loop through chars in the input string.
	check if the char is a letter:
		check if the char is upper case:
			then make it the lower case 
			and set it to result string.
		check if the char is lower case:
			then make it the upper case 
			and set it to result string.
	else:
		set it to the result string.

call the swap_case() function (instead of swap_case_listcomp()) in main block to execute the list comprehension code.

"""


def swap_case(word):
    result = ""
    for i in range(len(word)):
        if word[i].isalpha():
            if word[i].isupper():
                result = result + word[i].lower()
            elif word[i].islower():
                result = result + word[i].upper()
        else:
            result = result + word[i]
    return result


"""
Implement using list comprehension. 
for each char in string, check if upper, then return lower else return upper.
call the swap_case_listcomp function (instead of swap_case()) in main block to execute the list comprehension code.
"""


def swap_case_listcomp(word):
    return "".join([char.lower() if char.isupper() else char.upper() for char in word])


if __name__ == '__main__':
    s = input('Enter the string to be swapped case : ')
    result = swap_case_listcomp(s)
    print ("Swapped case result - " + result)
