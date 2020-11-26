str1 = "String to Count including Whitespace."
count = 0
alpha = 0
for i in str1:
	count += 1

for i in str1:
	if 't' in i:
		alpha += 1


print("Length of String is "+ str(count)+".")
print("Alpha in String is "+str(alpha)+" times.")