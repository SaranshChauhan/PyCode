n = 5
arr = [0]*n
i = 0
while n > 0:
    arr[i] = (n % 2)
    n = int(n/2)
    i+=1

print(arr[::-1])
