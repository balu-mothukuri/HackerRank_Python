"""
Minion Game
- Two player Game.
- Both players are given the same string, S.
- Both players have to make substrings using the letters of the string S.
- Player 1 has to make words starting with consonants. (It is not required to check if the words are meaningful)
- Player 2 has to make words starting with vowels. (It is not required to check if the words are meaningful)
- The game ends when both players have made all possible substrings.

Scoring
- A player gets +1 point for each occurrence of the substring in the string S.

Input
- A single line of input containing the string S
- The string S will contain only uppercase letters [A-Z]

Output
- Task is identify the winner of the game. Print the result in the below manner
    *The winner's name and score, separated by a space on one line, or Draw if there is no winner

"""
"""
input - String S
output - Player who won the game and score
"""


def minion_game(S):
    player1_score = 0
    player2_score = 0
    for i in range(len(S)):
        if S[i] not in 'AEIOU':
            # Score to be added = No of substrings that can be formed by starting with that letter
            # No of substrings =  length of the substring - index of that letter
            player1_score += len(S) - i
        if S[i] in 'AEIOU':
            player2_score += len(S) - i
    if player1_score > player2_score:
        print("The winner is - player1. Score - {}".format(player1_score))
    elif player1_score < player2_score:
        print ("The winner is - player2. Score - {}".format(player2_score))
    else:
        print ("Draw")


if __name__ == '__main__':
    S = raw_input('Enter the String which is used by the players : ')
    minion_game(S)
