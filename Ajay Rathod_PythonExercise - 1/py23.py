'''Write a Python program to multiply all the items in a list.
'''


def multi(myList):
    # Multiply elements one by one
    ans = 1
    for x in myList:
        ans = ans * x
    return ans


# Driver code
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multi(list1))
print(multi(list2))

