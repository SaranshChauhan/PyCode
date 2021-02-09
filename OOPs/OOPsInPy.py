import os
# Object Oriented Programming in Python
os.system("clear")

class Dog:
	#__init__ method instantiate
	# self: invisibly pass the reference of the current working object to the method.
 	def __init__(self,name,age):#this method will be called whenever new object is created & it will pass any argument from that object to this method.
 		self.name = name
		self.age = age

	def get_name(self):
		return self.name

	def get_age(self):
		return self.age

	def set_name(self,name):
		self.name = name


d = Dog("Jojo",33)
print(d.get_name(),d.get_age())
d.set_name("Bobbi")
print(d.name)

#
"""def bark(self):
		print("Bark")
		
	def add(self,x):
		return x+1

d = Dog()
d.bark()
print(type(d)) #<class '__main__.Dog'> main is module by default 
print(d.add(5))
print(type(d)) #type instance/Object
"""

#
"""
def hello():
	print("Hello")
print(type(hello)) #type function
"""
 