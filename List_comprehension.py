# This is a python script that is used to depict list comprehensions.

"""
You are given three integers x,y,z, representing the dimensions of a cuboid along with an integer.
Print a list of all possible coordinates given by  on a 3D grid where the sum of i+j+k is not equal to n.
Here 0<=i<=x, 0<=j<=y, 0<=k<=z

Example
x=1, y=1, z=2, n=3
All permutations of [i,j,k] -
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]
Print an array of the elements that do not sum to n=3
[[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list_c = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n] #List comprehension
    print(list_c)