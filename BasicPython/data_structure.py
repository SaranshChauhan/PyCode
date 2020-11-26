listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
list3 = [i for i in listOne[1::2]] #[var for var in GivenList condition] 
print(list3)
list4 = [i for i in listTwo[::2]]
print(list4)
print('Final List:',list3+list4)

print("\nGiven an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list.")
list1 = [54, 44, 27, 79, 91, 41]
print("Original List: ",list1)
list1.pop()
print('List After removing last element',list1)

print("\nGiven a two list of equal size create a set such that it shows the element from both lists in the pair.")
flist = [2, 3, 4, 5, 6, 7, 8]
slist = [4, 9, 16, 25, 36, 49, 64]
#with zip() method, it takes iterable & return tuple made of their elements.
result = zip(flist,slist)
print(set(result))
#before converting result into set, result variable of type "ZIP" 
#if you print result then you will get memory address of result object
#print(help(list)) #to know all available methods for this Object

print(dir(set))

