# Alphabet Rangoli - Alphabet Pattern

"""
Given an integer N, print an alphabet Rangoli of size N (Rangoli is a form of Indian folk art based on creation of
patterns.
Different sizes of Rangoli are shown below

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

The center of the rangoli has the first alphabet letter a, and the boundary has the Nth alphabet letter
(in alphabetical order).

Constraints 0<N<27

Sample Input

5

Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

"""

import string


def print_rangoli(size):
    """
    input : size, integer. No of letters that should be part of the pattern starting with 'a'
    return type: none
    """
    S = string.ascii_lowercase[:size]
    list_alpha = []
    for i in range(size):
        alpha = "-".join(list(S[::-1][:i + 1]))
        list_alpha.append((alpha + alpha[::-1][1:]).center(4 * size - 3, "-"))
    list_alpha.extend(list_alpha[::-1][1:])
    print("\n".join(list_alpha))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
