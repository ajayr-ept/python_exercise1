# [[2,4,5],[4,6,8],[3,6,9]]
# Considering the above list, we need to have a sum of all the values of all the inner lists.
# - Find the sum of only even numbers
# - Find the sum of all the numbers from all the inner lists
# Don’t use a loop.


# list1 = [10, 21, 4, 45, 66, 93, 11]
#
# list1 = [[2,4,5],[4,6,8],[3,6,9]]
#
# # we can also print even no's using lambda exp.
# even = list(filter(lambda x: (x % 2 == 0), list1))
# print("Even numbers in the list: ", even)
# print("The sum of my_list is", sum(even))


def column_sum(lst):
    return list(map(sum, zip(*lst)))
# Driver code
lst = [[2,4,5],[4,6,8],[3,6,9]]

even = map(lambda sublist:sum(list(filter(lambda x: x%2 == 0,sublist))),lst)
#ak = list(filter(lambda x : print(x),lst))
print(sum(even))
