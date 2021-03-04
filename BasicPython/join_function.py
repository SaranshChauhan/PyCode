print("Working of the join() method with Lists & Tuples")
# .join() with lists
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

# .join() with tuples
numTuple = ('1', '2', '3', '4')
print(separator.join(numTuple))

s1 = 'ABCD'
s2 = '1234'


# '1'+ 'abc'+ '2'+ 'abc'+ '3'
print('s1.join(s2):', s1.join(s2)) #S2's each element saparated by entire s1

# 'a'+ '123'+ 'b'+ '123'+ 'b'
print('s2.join(s1):', s2.join(s1)) #S1's each element saparated by entire s2

print("\nThe join() method with sets.")
# .join() with sets
test = {'2', '1', '3'}
print(''.join(test)) #test's every element is sparated by the s(String)

test = {'Python', 'Java', 'Ruby'}
s = '->->'
print(s.join(test)) #test's every elem is spatated by the s(String)

print("\nThe join() method with dictionaries")
# .join() with dictionaries
test = {'First': 1, 'Second': 2}
s = '->'

# joins the keys only
print(s.join(test))

test = {'One': 'Value1', 'Two': 'Value2'}
s = '---Goes To---'

# this gives error since key isn't string
print(s.join(test)) #every test element sparated by s

