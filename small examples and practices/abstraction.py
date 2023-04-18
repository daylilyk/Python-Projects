#
# Python 3.10
#
# Abstraction Practice
#
# Requirements: Your class should contain at least one abstract method and one regular method.  
#               Create a child class that defines the implementation of its parents abstract method.
#               Create an object that utilizes both the parent and child methods.
#               Add comments throughout your Python explaining your code.

# import abstraction widget
from abc import ABC, abstractmethod

class Instruments(ABC):
    def cost(self, amount):
        print("I cost: ", amount)
        print("To buy me please pay: ", amount)

    @abstractmethod
    def youPaid(self,amount):
        pass

class BuyMe(Instruments):
    def youPaid(self,amount):
        print('Thank you for your purchase of {}!'.format(amount))


if __name__ == "__main__":
    obj = BuyMe()
    obj.cost("$1,200")
    obj.youPaid("$1,200")

