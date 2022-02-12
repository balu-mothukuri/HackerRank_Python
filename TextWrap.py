"""
Task - Given a string and width, wrap the string in to a new line for every width of w
"""

"""
textwrap() takes any string and a width and wraps the string for the given width.
input params
************
str - string, Enter the text to be wrapped.
width - int, Enter the width in number, for which the text needs to be wrapped.
output param
************
string, wrapped text in multiple lines.
"""
def textwrap(str, width):
    return "\n".join([str[i:i+width] for i in range(0, len(str), width)])

if __name__ == '__main__':
    string = raw_input('Enter the string that needs to wrapped in text : ')
    width = int(raw_input('Enter the width after which the string needs to be wrapped : '))
    str_wrap = textwrap(string, width)
    print(str_wrap)