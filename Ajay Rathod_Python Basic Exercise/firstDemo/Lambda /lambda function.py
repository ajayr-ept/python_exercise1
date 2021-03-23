# number of arguments
x = lambda a,b,c : a * b + c
print(x(2,10,2))

# doubler function

def myfunction(n):
    return lambda a : a + n
mydoubler = myfunction(2)
print(mydoubler(11))


