print("A string of odd length greater 7, return a string made of the middle three chars of a given String.")
str1 = "JhonDipPeta"
#str1 = "JauyuyttySonAayuui"
if (len(str1) >= 7):
	leng = len(str1)//2
	for i in range(leng-1,leng+2):
		print(str1[i], end = "")


print("\nGiven 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.")
s1 = "Ault"
s2 = "Kelly"
leng = len(s1)//2
s3 = s1[:leng] + s2 +s1[leng:]
print(s3)

print("\nGiven 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string.")
s1 = "America"
s2 = "Japan"
s3 = s1[ : 1 ] + s2[ : 1 ] + s1[ len(s1) // 2 ] + s2[ len(s2) // 2 ] + s1[ len(s1) - 1 ] +s2[ len(s2) - 1 ]
print(s3)

print("\n Arrange string characters such that lowercase letters should come first")
str1 = "PyNeApple"
lower = []
upper = []
for ch in str1:
	if ch.islower():
		lower.append(ch)
	else:
		upper.append(ch)
print(''.join(lower+upper)) #upper and lower

print("Count all lower case, upper case, digits, and special symbols from a given string.")
str1 = "P@#yn26at^&i5ve"

char = 0
digit = 0
symbols = 0

for i in str1:
	if i.isalpha():
		char+=1
	elif i.isdigit():
		digit+=1
	else:
		symbols+=1
print('Char, Digit, Sysmbols:',char,digit,symbols)

print()