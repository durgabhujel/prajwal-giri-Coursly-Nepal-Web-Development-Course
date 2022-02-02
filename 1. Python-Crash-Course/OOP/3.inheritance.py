# Inheritance
# Inheritance is a way to create new classes based on existing classes.
# It is a way to reuse code.
# Iheritance is the capability of one class to derive or inherit the properties(data members/attributes/variables and methods) from another class

# Parent class => Base class or Super class
# Child class => Sub class or Sub class

class Person:
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def isEmployee(self):
		return False

# p1 = Person('Bickky')
# p1.getName()  #=> 'Bickky'
# p1.isEmployee()  #=> False

# Inherited or Subclass (Note Person in bracket)
class Employee(Person):
	
	def isEmployee(self):
		return True



emp = Person("Bickky") # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Coursly") # An Object of Employee
print(emp.getName(), emp.isEmployee())