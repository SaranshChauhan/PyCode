# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']

print('Original List: ',py_list)
newlist = sorted(py_list)
print('Sorted List: ',newlist,'\n')

# string
py_string = 'Python'
print('Sorted String Characters: ',sorted(py_string))
print('Original String is : ',py_string,'\n')

# vowels tuple
py_tuple = ('e', 'a', 'u', 'o', 'i')
print('Sorted Tuple: ',sorted(py_tuple))
print('Original Tuple : ',py_tuple, '\n')


print("\n\n::Sort Method in List:::")
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']

# sort the vowels
return_val = vowels.sort()
#print vowels
print('list Before Sort:',vowels)
print('Sorted list:', vowels)
print('After Sort list has been Modified:',vowels)
print('\n\nHere sort Method doesn\'t return anything-->>',return_val)