n = 11
for row in range(2,n//2+2):
	if row % 2 == 0:
		for col in range(0,5):
			print("0",end = ' ')
	else:
		for col in range(0,5):
			print("1",end = ' ')
	print('\n')