#Inheritance : Constructor Overriding
# Constructor of the parent class is available in the child class.
# But if we write constructor in both classes, parent and child class then parent class constructor is not available to the child class.
#in this case only child class constructor is accessible which means child class constructor is replacing parent class constructor

# Calling Constructor of the parent class in the child class is called constructor overriding.
# Constructor with super() => super() is a function that is used to call the constructor of the parent class.


# parent class
class Person:
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# p1 = Person("Bickky", "12345")
# p1.display()        

# child class
class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)
        # or using super()
        #super().__init__(name, idnumber)
    
    def display2(self):
        # print(self.name)
        # print(self.idnumber)
        print(self.salary)
        print(self.post)

    def __str__(self):
        return f'{self.name} {self.idnumber} {self.salary} {self.post}'   

# creation of an object variable or an instance
a = Employee('Bickky', 886012, 50000, "FullStack Developer")

# calling a function of the class Person using its instance
a.display()
a.display2()
# print(a.__str__()) #=> "Bickky 886012 50000 FullStack Developer"