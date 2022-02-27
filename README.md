# HackerRank_Python
Solutions to Python programming problems in Hacker Rank website


12. String_validators.py -- Checks to see if a given String contains any of the following
    - atleast one alphanumeric character - using isalnum()
    - atleast one alphabetical character - using isalpha()
    - atleast one digit - using isdigit()
    - atleast one lowercase letter - islower()
    - atleast one uppercase letter - isupper()

13. TextAlignment_logo.py -- Construct a logo in a desired format using Text Alignment functions.
    They include the following
    - rjust(width, '-'')
    - ljust(width, '-'')
    - center(width, '-'')

14. TextWrap.py -- Wrap a given text in to a paragraph based on a given width.
    - Use range(start_index, stop_index, step)
    - Loop the String in steps of 'width' 
    - Slice the string in to the size of provided 'width' and join with a new line character.

15. Mat_pattern.py -- Draw a mat in a specific pattern. The matt is of size MXN where N=3*M.
    - There is a design string that should be repeated in a certain way.
    - Also, the center line includes a WELCOME text.
    - used text alignment methods to align the string to achieve the desired pattern.

16. String_Formatting.py -- For a given integer, print the following formats - decimal, octal, hexadecimal, binary.
    - Use oct(n), hex(n), bin(n) for changing the formats.
    - Adjust the spacing so that every format is right aligned and has a width equal to size of the binary number.
      - rjust(width,' ')

17. Capitalize.py -- Capitalize the first letter of each word in the given string
    - For example 'balu mothukuri' needs to be converted to "Balu Mothukuri". "123ab" should remain as "123ab"
    - capitalize() - Capitalizes the first char in each word if the word starts with an alphabet, else it does not.

18. MinionGame.py - make words starting with each consonant and each vowel in a String and count their occurrences total.
    - The same string is given to 2 players
    - 1st player has to make all the possible words starting with consonants and count the number of occurrences.
    - 2nd player has to make all the possible words starting with vowels and count the number of occurrences.
    - Declare the winner depending on the count.
    - Note - Count for the no of words starting with any letter = Length of String - index of the letter.

19. Merge_the_tools.py - Split the string s in to n/k substrings and remove repeating alphabets in each substring.
    - where n is the length of the string and k is the length of each substring
    - Print each substring in a new line.
    - https://www.hackerrank.com/challenges/merge-the-tools/problem

