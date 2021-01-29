#Define a global empty dictionary. Iterate from 1 till 10 and fill the dictionary with the
# key as the number and value as the square of that number.

dic = {}
def func():
    global dic
    for x in range(1,11):
        dic[x] = x*x

func()
print(dic)


