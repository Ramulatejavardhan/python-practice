# in this we use the init mathod
class student:
    def __init__(self,name,age): #the init is used to we can assign values automatically when object is created in b/w the "()".
        self.name=name
        self.age=age
s1=student("tej",21)#we created a object with the copy of class student and assign the student value.
s2=student("ram",22)
print(s1.age)
print(s2.age)