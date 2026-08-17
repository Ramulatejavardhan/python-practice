#polymorphism is same thing that has different forms of behaviour based on the object.
class dog:
    def speak(self):
        print("bark")
class cat:
    def speak(self):
        print("meow")
d=dog()
c=cat()
d.speak()#Here polymorphism is speak onething is bark.
c.speak()#here polymorphism is speak onething is meow.