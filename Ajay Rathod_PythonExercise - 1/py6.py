'''e a Python program to calculate the sum of three given numbers,
 if the values are equal then return three times of their sum.
'''

def myfunc(x,y,z): # define def fuction and variable
    if x == y == z: # define if condition
        return x + y + z
    else:
        print('values is not equal')
print(myfunc(10,10,10)) #print the true condition and false condition