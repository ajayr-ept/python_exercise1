# Write a Python program to check if all values are the same in a dictionary.
# Original Dictionary:{'Cierra Vega': 23, 'Alden Cantrell': 23, 'Kierra Gentry': 23, 'Pierre Cox': 23}
# Check all are 23 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False


dic1 =  {'Cirra':23,'Alden':23,'Kierra Gentry':10,'Pierre Cox':23}

def myfunc(dic):
    for p in dic.values():
        if p != 23:
            return False
    return True
print(myfunc(dic1))


