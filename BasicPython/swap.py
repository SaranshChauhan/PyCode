#1
print("1nd way\n")
a,b = 2,3
a,b = b,a
print(a,b)

#2
print("2nd way\n")
x = 7
y = 9
temp = x
x = y
y = temp
print(x,y)

#3
print("3nd way\n")
m = 4
n = 5
n = m + n #9
m = n - m #5
n = n - m #4
print(m,n)