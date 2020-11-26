str1 = 'ABCDCDC'
str2 = 'CDC'
count = 0
for i in range(len(str1)):
	if str1[i:].startswith(str2):
		count += 1

print(str(str2)+" is "+str(count)+" times present in "+str(str1))
