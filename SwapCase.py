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
"""
def swap_case(word):
	result = ""
	for i in range(len(word)):
		if word[i].isalpha():
			if word[i].isupper():
				result = result+word[i].lower()
			elif word[i].islower():
				result = result+word[i].upper()
		else:
			result = result+word[i]
	return result


if __name__ == '__main__':
	s = input()
	result = swap_case(s)
	print ("Swapped case result - " + result)
