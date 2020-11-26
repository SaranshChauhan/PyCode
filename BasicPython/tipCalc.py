print("We went to a hotel Yesterday::")
order = 7000 #int(input())

if (500 > order >= 100 ):
	dis = 10
elif (1000 > order >= 500):
	dis = 25
else:
	dis = 50

total = order - (order * dis)/100
print(total)