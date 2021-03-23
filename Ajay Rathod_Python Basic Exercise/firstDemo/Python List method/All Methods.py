#append method

Branch = ['BA','BCOM','BCA','MA','MCOM'] # write a list of branch
Collage = 'RKU','Marvadi','Mission'
Branch.append(Collage) #applying append method
print('add your name ?')
#Branch.append(input())


print(Branch) #print All branch

#clear method

Branch = ['BA','BCOM','BCA','MA','MCOM']
Branch.clear()
print(Branch)

#Copy method
print('enter your collage name ? ')
#name = input()
#print(name)
Collage = ['RK University','Marvadi']
Collage.copy()
print(Collage)


#Count method

abcd = ['a','b','c','d','a','a','c']
x = abcd.count('a')
print(x)

#extend method

City = ['Rajkot','Surendranagar','Baroda','Surat']
Collage = ['RK University','Marvadi','Atmiay','Bhimrav']
Num = ['1','2']
City.extend(Collage)
City.extend(Num)
print(City)

# Index method
City = ['Rajkot','Surendranagar','Baroda','Surat']
Collage = ['RK University','Marvadi','Atmiay','Bhimrav']
Num = ['1','2']
City.extend(Collage)
City.extend(Num)
x = Collage.index('Bhimrav')
print(City)
print(x)

#Insert method

City = ['Dhokalva','Surendranagar','Gujarat','India']
City.insert(1,'Chotila')
print(City)

#pop method
City = ['Dhokalva','Surendranagar','Gujarat','India']
City.pop(0)
print(City)

#Remove method

City = ['Dhokalva','Surendranagar','Gujarat','India']
City.remove('India')
print(City)

# Revers method

City = ['Dhokalva','Surendranagar','Gujarat','India']
City.reverse()
print(City)

#Sort method
for x in range(3):
    x = input('your name')

City = ['Rajkot','Surat','Ahemdabad','Thangadh']
x.sort()
print(x)

