'''Write a Python program to remove the first item from a specified list.
color = ["Red", "Black", "Green", "White", "Orange"]
num = [255,3678,95,158,759,157]
'''

def myfunc(): # create def function for myfunc function
    color_list = ['Red','Green','White','Black'] # list of object and write the String in list
    num = ['255','3678','95','158','759','157']
    color_list.pop(0)
    num.pop(0)
    print(color_list) # print color first color and last color
    print(num)
myfunc() # calling def function

