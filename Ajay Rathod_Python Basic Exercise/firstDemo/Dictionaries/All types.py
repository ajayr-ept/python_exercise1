# Clear method
Emipro = {'Employee':'Ajay','Age':'21','City':'Thangadh','Employee':'Ajay'}
print(Emipro)
Emipro.clear()
print(Emipro)

# fromkey method

S = ['Student1','Student2','Student3','Student4']
Datas = dict.fromkeys(S)
print(Datas)

# get method

Student = {'Student1':'Ajay','Student2':'Jigar','Student3':'Sanjay'}
s = Student.get('Student1')
x = Student.get('age',21)
print(s,x)


#item method
Subject = {'C++':'111','Java':'222','C':'333'}
s = Subject.items()
print(s)

#change the item in items method

Subject = {'C++':'111','java':'222','C':'333'}
s = Subject.items()
print(s)
Subject['C'] = 444
print(s)

# Keys method
Subject = {'C++':'111','Java':'222','C':'333'}
s = Subject.keys()
print(s)
Subject['Python'] = 123
print(s)

# pop method
Subject = {'C++':'111','java':'222','python':'333'}
Subject.pop('C++')
print(Subject)
s = Subject.pop('java')
print(s)

#popitems method
Subject = {'C':'AK','Python':'AB','C++':'12121'}
Subject.popitem()
print(Subject)

#setdefualt method

Details = {'Name':'Ajay','Age':'22','City':'Thangadh'}
d = Details.setdefault('Name','Vikash')
print(d)
d = Details.setdefault('Color','White')
print(d)

#update method
Details = {'Name':'Ajay','Age':'22','City':'Thangadh'}
Details.update({'Name':'Vikash'})
print(Details)
