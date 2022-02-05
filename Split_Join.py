"""
Problem - Given a sentence, replace the white spaces in between with a dash "-".
Approach
    a. split the sentence in to a list of words delimited by space.
    b. join the list of words with a dash between them.
"""


def split_and_join(sentence):
    return "-".join(sentence.split(" "))


if __name__ == '__main__':
    sentence = raw_input('Enter a sentence : ')
    result = split_and_join(sentence)
    print(result)
