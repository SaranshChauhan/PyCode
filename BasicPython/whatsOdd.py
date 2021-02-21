'''
Size of List : 5

12
21
10
7
9

Ignore the odd ones & do sum of even ones only i.e 22
'''

N = int(input('Input the size of list?')) #sizeOfList

lst = []
sum = 0
while N != 0:
    lst.append(int(input()))
    N -= 1

for i in lst:
    if i % 2 == 0:
        sum = sum + i
    else:
        continue

print('Sum evans is equal to ::',sum)