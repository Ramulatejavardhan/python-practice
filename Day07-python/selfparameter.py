#About the self it represents the current object.if we call print(p1.name)now self is p1 object. 
class person1:
    def __init__(self,name):#self is the parameter it represent current object which is currently called.(like p1.greet())
        self.name=name
    def greet(self):
        print("hello"+self.name)
p1=person1("tej")
p1.greet()# self become the p1 in place of self.


#basic versiom
class hello:
    def __init__(self,name):
        self.name=name
p1=hello("tej")
print(p1.name)