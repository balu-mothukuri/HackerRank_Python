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
    - Use capitalize() function.