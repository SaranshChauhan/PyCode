n = 5
for row in range(1,n+1):
	for col in range(1, row+1):
		print("*", end = " ")
	print(" ")

for row in range(n,0, -1): #start = n i.e 5 & goes till 0 with -1 difference
	for col in range(0,row-1): #column decreases with -1 row value.
		print("*",end = " ")
	print(" ")

