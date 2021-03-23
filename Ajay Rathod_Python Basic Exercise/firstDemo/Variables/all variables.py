# simple hello world

print('helo world11') # note a print function
age = 10 # type of int values
name = 'ajay' # type of string values
print(name, age) # one type print the datas
print('my name is {0} and my age is {1}'.format(name, age)) # second type print the datas

# veriables

a = int(200)  # this is a int veriable
b = str('RK')  # this is a string veriables
c = float(3)  # this is a float veriables
# this are all veriable print
print(a)
print(b)
print(c)

# how to get type veriables

c = 5
d = 'AB'

print(type(c))
print(type(d))

# double values

x = 'AB'
print(x)
x = 'AB'
print(x)

# gloable veriables

m = "RK University"


def myfunc():
    print("MCA form " + m)

    myfunc()

