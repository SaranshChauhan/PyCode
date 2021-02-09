import re

print(r'\tTab') #r is used to make string row string that means followed string will be treated as it is.
#output will be '\tTab' here

#Pattern 1
nameage = 'Janice is 22 and Theon is 33 Gubbu is 44 and Joey is 43'

age = re.findall(r'\d{1,3}',nameage)
name = re.findall(r'[A-Z][a-z]*',nameage)

agedict = {}
j = 0
for i in name:
	agedict[i] = age[j]
	j+=1
print(agedict)

#Pattern 2
#Both the string and RehEx ahve their own cursor
#search will find only one word in a string
if re.search("word",r"word is the wordological thing."):
   print("Word has been found") #only one will be searched, only in word.

#findall will be searched for all the searched words occurance
allwords = re.findall("word",r"word is the wordological thing.")
count = 0 
for i in allwords:
	count+=1
print("word is "+str(count)+" times presented in given String")


#how to generate an iterator (Indices of both the words)
str = r"word is the wordological thing."
for i in re.finditer("word",str): 
#return starting and ending index of the word
	var = i.span()
	print(var)

#match words with a particular ptrn
str = r"Sat cat mat Wat Zat Xat"
#ptrn will find all A to Z & end with at
foundStr = re.findall('[A-W a-z]at',str) #only print Sat,Mat,Hat
print(foundStr)

str = r"Sat cat mat Wat Zat Xat"
#ptrn will find all except S to Y & end with at
foundStr = re.findall('[^A-W]at',str) #only print Sat,Mat,Hat
print(foundStr)

#Replace a String
fruits = "Banana Papaya Mango Rat"

#compile the RegEx provides us more methods/opertaions to do with Re.
regex = re.compile("[rR]at")
fruits = regex.sub("Litchi",fruits)
print(fruits)

#row String
randStr = r"here is \\drogba"
print(randStr)

'''
\n: whitespace
\b: backspace
\r: carriage return
\f: formfeed
\t: tab
\v: vertical tab
'''
randStr1 = '''
keep the blue flag
flying 
in the sky.
'''
print("Before :",randStr1)
RegEx = re.compile('\n')
randStr1 = RegEx.sub(" ",randStr1)
print("After :",randStr1)


#Remove Single Character
#\d: digits
#\D: Other then Digits
randStr = "1234554321"
print("Matches:", len(re.findall("\d{5}",randStr)))

#find specific length Digits
num = "123 1234 12345 123456 1234567"
print("All Matches:",len(re.findall("\d{5,7}",num)))

