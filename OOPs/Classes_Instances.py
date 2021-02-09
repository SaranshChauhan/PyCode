# Classes & Instances
#Email Generator
#Class : Blueprint for creating unique(Different location in memory) instances.
class Employee:
    #constractor or Initialize Method
    def __init__(self,fname,lname,pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.mail = fname + "." + lname.lower() +"@gmail.com"
    
    #Class Method
    def info(self):
        print("My Full Name is {} {} and my salary was {}.".format(self.fname,self.lname,self.pay))
    
    def inc(self):
        print("My Increment in salary is ",self.pay*2)

class Owner(Employee): #Derived Class from Class Employee.
    def spAcess(self):
        print("I have full access to files and Systems.")          
'''
emp1 = Employee("Alpha","Joe",2500) #Instance_1
emp2 = Employee("Beta","Nolan",3000) #Instance_2
emp3 = Employee("Gamma","Lerry",5000)

inpt = input("Provide Employee Id.\n")
print(inpt.mail)
inpt.info()
print(inpt.show())
'''
obj = Owner("hey",'hjdwj',4000)
obj.info()
obj.spAcess()
obj.inc()