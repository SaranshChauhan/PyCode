str1 = "@s3a%$r*a^n$%s%$%h"
str2 = ""
for i in str1:
	if i.isalpha():
		str2 += i  #or yuo can do this too print(i, end='')
 
print("After Removing Symbols from "+str(str1)+" is "+ str(str2))
#print(dir(list))

print("Reverse the words of a String")
list1 = ['Ram','is','a','Good','Boy']
#list1.reverse()
#print(list1[::-1])
#print([i for i in list1 [::-1]])
j = 1
for i in list1:
	print(list1[len(list1)-j],end ='\t')
	j+=1

print("\n")


list2 = ['Ram','is','a','Good','Boy']
print(list2)
print("\n:::::::Reverse words in the sentence:::::")
for i in list2:
	for j in i[::-1]:
		print(j,end='')
	print('',end=' ')



