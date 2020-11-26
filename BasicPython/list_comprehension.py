#list comprehension
# [returnValue For x in range(10) condition]
'''
print(101 % 2) #Remainder (1)
print(101 // 2) #Integer Part (50)
print(101 / 2) #Float Value (50.5)
'''
print("\nDivision")
list1 = [x**2 for x in range(10) if x%2==0]
print(list1)

print("\nAddition")
print([ i+2 for i in range(1,20) if i % 2 == 0])

print('\nisdigit()')
print([i for i in 'Stri67ngs' if not i.isdigit()])

print('\nislower()')
print([i for i in 'ScHoOl PaSsEd' if i.islower()]) #isupper()

print('\nisalpha()')
print([i for i in ['@','B','D','()','L','@F'] if not i.isalpha()])

print('\nstartswith()')
print([i for i in "Ram is a good Boy."])

print('Iterate over a list and pull element indices at the same time.')
my_list =['a','b','c']
for i,ch in enumerate(my_list):
	print(i, ch)

print("List comprehension to create Tuples")
my_list=[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2+y**2==z**2]
print(my_list)


