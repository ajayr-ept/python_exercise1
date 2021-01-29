'''Write a Python program to get the difference
 between a given number and 17, if the number is greater than
 17 return double the absolute difference'''

def fun(n): #create def function and declear a variable
    if n > 17: # apply if condition and logic
        return 2*abs(17 - n) # return value and apply logic here and condition true
    else: # else part
        return -1 # return value and condition false

print(fun(20))

