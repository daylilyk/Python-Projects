#
# Python 3
#
# Encapsulation using private and protected attributes/functions
#
# Requirements: This class should make use of a private attribute or function.

#               This class should make use of a protected attribute or function.

#               Create an object that makes use of protected and private.

#               Add comments throughout your Python explaining your code.

# Creating a class to test protected functions
class Protected:
    # creating protected data
    _fname = "Lily"
    _lname = "Kiousis"
    
    # public function to test results while using protected data
    def Fullname(self):
        print("First Name: ", self._fname)
        print("Last Name: ", self._lname)

    # making a private function
    def __Fullname(self):
        print("First Name: ", self._fname)
        print("Last Name: ", self._lname)

    #calling private method via another method
    def Private(self):
        self.__Fullname()

if __name__ == "__main__":
    #making class object for protected
    obj1 = Protected()
    obj1.Fullname()
    obj1.Private()
