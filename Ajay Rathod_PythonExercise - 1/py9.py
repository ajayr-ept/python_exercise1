'''Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
'''

def checkfunc(chk):
    num = ['1','5','8','3']
    return chk in num
print(checkfunc('1'))
print(checkfunc('-1'))