# create a class and object
class Student:
    def __init__(self,name,age):
         self.Name = name
         self.Age = age

    def myfunc(self):
        print('Hello My Name is ' + self.Name)
        print('My age is ' + self.Age)

s1 = Student('Ajay','22')
s1.myfunc()