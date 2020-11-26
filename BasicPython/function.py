def greet(name):#name is parameter
    return f"Hey {name}!"
'''
A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.'''
	

print(greet('Rami'))

def concatenate(word1,word2):
	return word1+word2

print(concatenate("Rasik"," Dittor"))

def age_in_dog_year(age):
	return age * 7

print(age_in_dog_year(24)) #24 is argument

def uppercase_and_reverse(string1):
	return string1.upper()[::-1]
	

print(uppercase_and_reverse("bananas")) #SANANAB

#print([7,6,5,4,3,2,1][::-1]) #1234567