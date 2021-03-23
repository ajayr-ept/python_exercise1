# map function for lenth
def myfunc(a):
    return len(a)
x = map(myfunc,('ajay','jigar','jenish'))
print(x)
print(list(x))

# parameter values
def myfunc(a,b):
    return a + b
x = map(myfunc,('ajay','jigar','jenish'),('111','222','333'))
print(x)
print(list(x))


# fillter function

roll_no = [12,2,15,20,77,55,32,34,24,13]
def myfunc(x):
    if x > 20:
        return False
    else:
        return True
ans = filter(myfunc,roll_no)

for x in ans:
    print(x)
