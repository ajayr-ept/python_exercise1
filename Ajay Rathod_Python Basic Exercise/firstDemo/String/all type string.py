#count String method

num = 'ajay rathod ajay' # String values

x = num.count('ajay') #use of count function
print(x) #print of count values

#endswith method

num = 'my name is ajay rathod' # Strng values

x = num.endswith('d')
print(x)

# find method

info = 'my name is ajay rathod form thangadh and study BCA and MCA form RK University Rajkot.'

x = info.find('is')
print(x)

# format method
Ab = 'ajay have {:<5} Banana'
print(Ab.format(21))

Ab = 'ajay have {:>5} Banana'
print(Ab.format(21))

Ab = 'ajay have {:^5} Banana'
print(Ab.format(21))

Ab = 'Chotila to Rajkot {:=5} Kilometers'
print(Ab.format(60))

Ab = 'The temperature is between {:+} and {:+} degrees celsius'
print(Ab.format(-2,13))

Ab = 'The temperature is between {:-} and {:-} degrees celsius'
print(Ab.format(-2,13))

Ab = 'Sunil age is {: } and Ajay age is {: }'
print(Ab.format(21,23))

Ab = 'Total Village in the world {:,}'
print(Ab.format(11200000))

Ab = 'Total Village in the world {:_}'
print(Ab.format(11200000))

Ab = 'The binary version of {0} is {0:b}'
print(Ab.format(105))

Ab = 'Ajay Rathod is a Softwere {0:c} Devloper '
print(Ab.format(1))

Ab = "{:d} Student in My Hostel."
print(Ab.format(0b101))







# index method
info = 'my name is ajay rathod form thangadh and study BCA and MCA form RK University Rajkot.'

x = info.index('ajay')
print(x)

# isspalce method

info = 'my  name is ajay rathod form thangadh and study BCA and MCA form RK University Rajkot.'
text = '    '

y = text.isspace()
x = info.isspace()
print(y)

#lstrip method

info = 'Ajay'
x = info.lstrip()
print('my name is ',x, 'i am form thangadh')

#replace method

collage = 'RK University from Baroda'
x = collage.replace('Baroda','Rajkot')
print(x)

collage = 'I am ajay rathod i am from rajkot and i am study in rajkot'
x = collage.replace('rajkot','Thangadh')
print(x)

# rfind method

collage = 'RK University from Baroda'
x = collage.rfind('from')
print(x)

# rindex method

collage = 'RK University from Rajkot'
x = collage.rindex('Rajkot')
print(x)

# rstrip method
info = 'Ajay'
x = info.rstrip()
print('my name is ',x, 'i am form thangadh')

# zfill method

num = '200'
x = num.zfill(15)
print(x)

# strip method

num = ',,,,,rrtgg.....ajay...rrr'
x = num.strip(',.gra')
print(x)

# join method

details = {'village': 'Dhokalava','Country':'India'}
joinfiled = 'State'
x = joinfiled.join(details)
print(x)