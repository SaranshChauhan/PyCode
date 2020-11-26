arr = [11,2,33,4,55,6]
arr.pop() #6 removed
print("After pop(), the array is "+str(arr)+"\n")

arr.remove(55) #5 removed
print("After remove(), the array is "+str(arr)+"\n")

#print(dir(arr))
print(dir(arr))

print(arr2 := arr.copy()) #here := means that first the expresion i.e copying items from arr to arr2 performed then assign to arr2
print("After copy() into arr2 , the array is "+str(arr2)+"\n")

arr.insert(4,8)
print("After insert(), the array is "+str(arr))
print(arr)

arr.sort()
print("After sort(), the array is "+str(arr)+"\n")

print("Index of 33 is "+str(arr.index(33)))

arr.append(66)
print("After append(), the array is "+str(arr)+"\n")

print("After insert(), the array is "+str(arr))

arr.clear()
print("All deleted from Array"+str(arr))