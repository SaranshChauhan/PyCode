'''
Input: this is awesome text.
Output: awesome. (Longest text)
'''

str1 = input()
Maxlen = 0
indx = 0
lst = str1.split(" ")
for i in lst:
    if len(i) > Maxlen:
        Maxlen = len(i)
        indx = lst.index(i) 
print('Max Length text is ::',lst[indx])






