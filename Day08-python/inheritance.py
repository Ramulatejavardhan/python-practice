class parent:#this is the parent class
    def speak(self):
        print("hello")
class child(parent):#this is the child class which inherits the parent class properties.
    pass
d1=child()#object created
d1.speak()#the object having the parent class value or properties because the child inherits from the parent.