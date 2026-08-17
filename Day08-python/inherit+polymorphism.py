class animal:
    def speak(self):
        print("animal sound")
class dog:
    def speak(self):
        print("dog sounds bark")
class cat:
    def speak(self):
        print("cat sounds meow")
d=dog()
c=cat()
animals=[d,c]
for i in animals:
    i.speak()