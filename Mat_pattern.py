"""
Task - Draw a mat pattern.
The mat needs to be of size - size X 3*size.
The design string and center text should be shown as below

---------------.|.---------------
------------.|..|..|.------------
---------.|..|..|..|..|.---------
------.|..|..|..|..|..|..|.------
---.|..|..|..|..|..|..|..|..|.---
-------------WELCOME-------------
---.|..|..|..|..|..|..|..|..|.---
------.|..|..|..|..|..|..|.------
---------.|..|..|..|..|.---------
------------.|..|..|.------------
---------------.|.---------------


"""
def draw_mat_pattern(size, string, center_string):
    result_string = ""
    result_string += "\n".join([((2*i+1)*string).center(3*size,'-') for i in range(size//2)]) + "\n"
    result_string += center_string.center(size*3,'-') + "\n"
    result_string += "\n".join([((2 * i + 1) * string).center(3 * size, '-') for i in reversed(range(size//2))])
    return result_string

if __name__ == '__main__':
    size = int(raw_input('Enter the pattern size (odd number) : '))
    string = raw_input('Enter the string in the pattern : ')
    center_string = raw_input('Enter the center text on the mat : ')
    result_string = draw_mat_pattern(size, string, center_string)
    print(result_string)