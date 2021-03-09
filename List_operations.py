# List Operations - append, insert, remove, sort, pop, reverse, print

"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands.
Each command will be of the 7 types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Sample Input :
************

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output :
*************

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""

if __name__ == '__main__':
    sample_list = []
    str = ''
    for i in range(int(input())):
        str = str + input() + '\n'

    # Split the string in to nested lists and then perform the operations.
    for list_op in str.split('\n'):
        if ('append' in list_op):
            sample_list.append(int(list_op.split()[1]))
        elif ('insert' in list_op):
            sample_list.insert(int(list_op.split()[1]), int(list_op.split()[2]))
        elif ('print' in list_op):
            print(sample_list)
        elif ('remove' in list_op):
            sample_list.remove(int(list_op.split()[1]))
        elif ('pop' in list_op):
            sample_list.pop()
        elif ('sort' in list_op):
            sample_list.sort()
        elif ('reverse' in list_op):
            sample_list.reverse()
