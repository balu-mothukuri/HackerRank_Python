#Find the runner up in a list

"""
If you are given n scores, store them in a list and find the score of the runner up.
"""

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(sorted(list(set(map(int, s.split()))))[-2])