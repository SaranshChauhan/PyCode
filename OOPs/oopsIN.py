#class and objects
'''
Bottom up approach
More data security
Data accessing
Data overloading

#class: Collection of similar type of objects,template,blueprint of object.
#object: Instance of the class, a real wprld entity that we can see & touch.
'''
#Example1: class without constractor
class Cars():
	pass

#create an object
honda = Cars() #Car honda = new Car() in java
tata = Cars()
honda.modelname = 'City'
honda.yearmf = 2020
honda.price = 1000000

tata.modelname = 'Bolt'
tata.yearmf = 2019
tata.price = 600000

print(honda.price)



#Example2: with the use of constractor

# Self(Convention not a keyword) is the reference to the object which is going to calling this function(__init__ ).
# Self is used to represent the instance of the class & we can use any word except self(eg. abcd, srone etc)
#with self we can easily access all the instances defined within a class. 

#__init__() is the not a constructor (initialize newly created objects).
#__new__() is the constractor that called implicitly before __init__(), we can override it but normally no need to do that.
class Car():
    def __init__(self,modelname,yearmf,price):
        self.modelname = modelname
        self.yearmf = yearmf
        self.price = price
    def price_inc(self):
        self.price = self.price*1.5

#object creation
obj1 = Car('City',2020,2000000)
obj2 = Car('Bolt',2017,1000000)

print(obj1.__dict__)
print(obj2.__dict__)
print("Price Before",obj1.price)
obj1.price_inc()
print("Price After",obj1.price)

#Example3: without self & __init__() method, by making the methods static
class ClassWithoutSelf():

    @staticmethod #function Decorator
    def static_meth():
        print("Static Method Called:: "," Here, without self because static method is accessible through out all instances.")

#creating new object
newObj = ClassWithoutSelf()
#calling class method
newObj.static_meth()


#Example4: Inheritance

class SuperCar(Car):
    pass

#object creation
obj1 = SuperCar('City',2020,2000000)
obj2 = SuperCar('Bolt',2017,1000000)

print(honda.__dict__)
print(help(honda))


