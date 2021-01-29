'''ake 3 global dictionaries as follows. Define a function, which ta    kes those 3
 dictionaries and concatenate them.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Output should be - {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''


dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
def myfunc():
    global dic1
    dic1.update(dic2)
    dic1.update(dic3)

myfunc()
print(dic1)