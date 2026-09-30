class student:
    def __init__(self,name,age,rollno,dept):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.dept=dept
obj=student("tej",19,83,"AI&DS")
print(obj.name)
print(obj.age)
print(obj.dept)