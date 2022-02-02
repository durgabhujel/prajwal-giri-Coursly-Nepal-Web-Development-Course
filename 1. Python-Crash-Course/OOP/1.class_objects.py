
  
# Class and Objects
# Class is a user defined data type/structure 
# Class contains data members and member functions
# Data members are variables that are part of the class, also called as attributes
# Member functions are functions that are part of the class, also called as methods

# Objects are instances of a class
# Objects can access the data members and member functions of a class

# A Single Class can have multiple objects/instances
# All the objects of a class share the same data members and member functions
# But the objects have different states i.e different values of data members

# self is a reference variable that refers to the current instance of the class
# class methods must have self as the first argument


"""
class syntax:
class ClassName:
    <statement-1> variables, functions
    .variable  => data members / attributes
    function() => member functions / methods
    .
    .
    <statement-N>
object creation:
object_name = ClassName()
"""


class Car:
    # data members/attributes:
    a = 'BMW'
    b = 'Audi'
    c = 'Mercedes'
    # members functions/methods:
    def bmw(self):    #self = obj1
        #a1 = 'randomcar'
        print(f'Hello, I am a {self.a}!')  #obj1.a
    def audi(self):
        print(f'Hello, I am a {self.b}!')
    def mercedes(self):
        print(f'Hello, I am a {self.c}!')
    def tesla(self):
        print(f'Hello, I am a Tesla!')
        

obj1 = Car()  #object creation or instance creation
obj2 = Car()
# obj1.tesla()    
# obj1.bmw()
# obj1.audi()

# obj2.tesla()
# obj2 = Car()
# obj3 = Car()    

# c = obj1.bmw()
# print(c)
# obj1.bmw()  #=> Car.bmw(obj1)
# print(obj1.a)
# obj1.audi()  #=> Car.audi(obj1)
# obj1.mercedes()
# obj1.tesla()  #=> Car.tesla(obj1)

# print(obj1.a)
# obj1.hello()
# obj2.hello()
print(type(obj1))
print(type(obj2))
