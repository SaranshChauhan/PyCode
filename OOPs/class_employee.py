class employee:
    def __init__(self,name,age,id,salary):   #creating a function
        self.name = name # self is an instance of a class
        self.age = age
        self.salary = salary
        self.id = id
 
emp1 = employee("harshit",22,1000,1234) #creating objects
emp2 = employee("arjun",23,2000,2234)
print(emp1.__dict__) #Prints dictionary
print('Type: ',type(emp2))#Prints list
print("Module: ",emp2.__module__)
print("Class: ",emp2.__class__)
print("Delattr: ",emp2.__delattr__)
print("dir: ",emp2.__dir__)
print("Doc: ",emp2.__doc__)
print("Eq:  ",emp2.__eq__)
print("Format: ",emp2.__format__)
print("Ge: ",emp2.__ge__)
print("GetAttribute: ",emp2.__getattribute__)
print("Gt: ",emp2.__gt__)
print("Hash: ",emp2.__hash__)
print("init: ",emp2.__init__)
print("init subclass: ",emp2.__init_subclass__)
print("Le: ",emp2.__le__)
print("Lt: ",emp2.__lt__)
print("ne: ",emp2.__ne__)
print("New: ",emp2.__new__)
print("Reduce: ",emp2.__reduce__)
print("Sizeof: ",emp2.__sizeof__)



