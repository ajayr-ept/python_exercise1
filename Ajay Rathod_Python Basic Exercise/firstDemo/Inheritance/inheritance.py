class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print('super')
    def details(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
    def std(self):
        print(self.firstname,self.lastname)

s1 = Student('ajay ','rathod')
s1.std()

