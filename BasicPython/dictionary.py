# Useful in storing Properties of a Objects

#Key-Value Pair
#We use Keys to access, No Index unlike List
#No Order of Fetching Data
import os
os.system("clear")
states = {'NY':'NewYork','UP':'Uttar Pradesh','MP':'Madhya Pradesh'}
print(states['UP'])

#to Not get Error
print(states.get('YT')) #None
print(states.get('CL'),'Not Found') #Not Found o/w None

print(states.keys()) #states.keys will give you the address of Keys storing in memory
print(states.values())

#Adding Value
states['YT'] = 'YouTube'

# Dict % List can be Inside each Other
animal_sounds = {
	'Cat' : ["meaw", "purr"],
	'Dog' : ["woof","bark"],
	'Fox' : []
}

#List of Dictionary
print("\nList of Dictionary is as Following\n")
Rami = {'nickname':'Rm','age':21,'hair':'Blue'}
Akash = {'nickname':'Ak','age':19,'hair':'Gray'}
Mukesh = {'nickname':'Mj','age':20,'hair':'Brown'}
people = [Rami,Akash,Mukesh]
print(people)

for person in people:
	print(person['age'])