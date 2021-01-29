'''Write a Python program to count the number of strings in a list where the string
length is 2 or more and the first and last character are the same from a given list of strings.
'''

def str(char):
    ctr = 0

    for word in char:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return  ctr
print(str(['abc','xyx','aba','1221']))

