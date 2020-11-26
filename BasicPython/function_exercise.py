print("-Accept a variable length of Args and print all arguments value-\n")
def func1(*args): #Used astrict to accept any numbers of Arguments.
	print(args)

func1(True,445,'String',99.99)




print("-------------------function with default Value------------------\n")

def showEmployee(name,salary=9000): #set function default value to 9k
	print("Employee {0} salary is: {1}".format(name,salary))

showEmployee("Ben", 6000)
showEmployee("Bico")

print("---------------------Inner and Outer function--------------------\n")
def outerFunc(a,b): #outer function with parameters

	def innerFunc(a,b): #inner function also needs the parameters
	    return a + b
	return innerFunc(a,b) + 5 # call innerfunction from outer function
	

#function call
print(outerFunc(5,5))

print("------------Assign different Name to Function & call it------------\n")
def displayStudent(name, age):
    print(name, age)

displayStudent("Emmy", 26)
showStudent = displayStudent
#with new assigned name
showStudent("Robbie Cole",34)


print("\n------Addition and subtraction in a single return call---\n")
def calculation(a, b):
	    return (a + b),(a - b)


res = calculation(40, 10)
print(res)
print("------------------T H A N K YOU---------------------")
print("---------------------------------------------------")

