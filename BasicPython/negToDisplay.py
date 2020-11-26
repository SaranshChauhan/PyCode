i = -10
for num in range(1,11):
	while i < 0:
		print(i)
		i += 1


print("\n-------Negative Ranged Values------\n")
for num in range(-10,0):
	print(num)

print("\n------At Last of Loop Done-------\n")
for i in range(5):
    print(i)
print("Done !")

print("\n-----Table of Two------\n")
start = 2
end = 22
steps = 2
for i in range(start,end,steps):
	print(i)

print("\n------Display only Even Pos List numbers--------\n")
my_list = [10,20,30,40,50,60,70,80,90,100]
for i in my_list[1::2]:
    print(i, end = " ") 

print("\n--------cube of a number------\n")
input_num = 6
for i in range(6+1):
	print("Current Number is : {} and the cube is {}".format(i,(i**3)))

print("\n------------\n")

