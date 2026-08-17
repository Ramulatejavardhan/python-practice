#Encapsulation is used to protect data from the direct access to a data.
#It is used to protect the data from unauthorized access and modification.
#Encapsulation is hiding data and controlling access with methods.
class Bank:
    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

b = Bank()
print(b.get_balance())