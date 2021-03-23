# add method
car = {'BMW','audi'}
car.add('rang rower')
print(car)

# clear method
car = {'BMW','audi'}
car.clear()
print(car)

#copy method

car = {'BMW','audi'}
x = car.copy()
print(x)

# difference method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)

#onther way
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

# difference method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# Discard method
x = {"apple", "banana", "cherry"}
x.discard('apple')
print(x)

#intersection method
x = {"a", "b", "c"}
y = {"c", "d", "a"}
z = {"a", "g", "c"}
result = x.intersection(y, z)
print(result)


#intersection upadte method
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)

# isdisjoint method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset method
x = {"a", "b", "c"}
y = {"f", "a", "d", "c", "b"}
z = x.issubset(y)
print(z)

#issuperset method
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

#pop method
fruits = {"apple", "banana", "cherry"}
x = fruits.pop()
print(x)

#remove method
fruits = {"apple", "banana", "cherry"}
fruits.remove('banana')
print(fruits)

# symmetric difference method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

# symmeric difference update method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#union method
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)
