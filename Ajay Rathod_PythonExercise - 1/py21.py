'''Create a function which takes a value. Define a global dictionary. The function
should be able to display a statement whether the passed value is in the dictionary or not.
'''

# decalre global dic
dic = {}

# define funtion to add value to dic
def add_dic(key,value): # key: take key for dic, value : take value of dic
    # access global dic
    global dic
    # add value to dic
    dic[key] = value
    # print statement
    print("passed value to dic")
    # return dic
    return dic

# call function
print(add_dic("name","Ajay"))