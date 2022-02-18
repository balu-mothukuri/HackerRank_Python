"""
Task - Given an integer n, print the following values for each integer for each integer i from 1 to n
1. Decimal
2. Octal
3. Hexa Decimal (Capitalized)
4. Binary
"""

"""
Pass an integer n and print all the required formats - decimal, octal, hexa decimal and binary.
Maintain an equal spacing equal to the width of the largest binary number in the list.
"""
def print_formatted(n):
    # your code goes here
    width = len(bin(n)[2:])
    #width = len("{0:b}".format(n))
    for i in range(1,n+1):
        print("{} {} {} {}".format(str(i).rjust(width,' '), str(int(oct(i))).rjust(width,' '), hex(i)[2:].upper().rjust(width,' '), bin(i)[2:].rjust(width,' ')))
        #print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)