'''Write a Python program to concatenate all elements in a list into a string and return it.
'''

def conc(list):
    ans = ''
    for x in list:
        ans += str(x)
    return ans
print(conc([9,3,0,44]))