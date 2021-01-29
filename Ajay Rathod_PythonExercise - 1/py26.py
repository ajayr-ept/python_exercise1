'''Define a global dictionary. Define a function which takes 2 values 1st as key and 2nd as value.
 The function should add those key values to the global dictionary.'''

dic = {}

def addfonc(key,value):
    global  dic
    dic[key] = value
    return dic
print(addfonc('ajay','22'))