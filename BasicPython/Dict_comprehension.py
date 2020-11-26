#Dictionary
print({x for x in {'Naam':'Jalebi Bai','Age':77,'Id':77}.items()})

#D = dict.fromkeys(['Sam',400,3.5,'@#$342'],'Noni')

print('\nYou can use Expresion, Tuples, Dictionary in Dictionary\'s values too')
rm = {'x':'Jalebi Bai'+' Rama','y':77+11-4*2,(38,8):87,'key':{1:2,3:4,5:6}} 
print(rm)


#Defining a List
print("\nPassing a list of tuples to the built-in dict() function")
d = dict(foo=100, bar=200, baz=300)
print(d,type(d))

print("\nCreating an empty dictionary and then assigning the key-value pairs individually")
d = {}
d['foo'] = 100
d['bar'] = 200
d['baz'] = 300
print(d,type(d))

print("Native Way to defining")
d = {'foo': 100, 'bar': 200, 'baz': 300}
print(d,type(d))
del d['foo']
print(d,type(d))

print("\nSpecifying a list of comma-separated <key>: <value> pairs enclosed in curly braces")
d = dict([
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
])
print(d,type(d))

print("\n Passing keyword arguments to the dict() function (if the key values are simple strings)")
d = dict(foo=100, bar=200, baz=300)
print(d,type(d))

x = ['a','b',{'foo': 1,'bar':{'x' : 10,'y' : 20,'z' : 30},'baz': 3},'c','d']
#What is the expression involving x that accesses the value 30?
print((x[2]['bar']['z']),type(x))
print('\n')

print("Any type of Key accepted but must be immutable i.e Keywords, Complex Number, Integer value , Boolean, Digits, Float, String")
z = {int:34, '(3+2j)':3, ('foo','bar'):69, True:False, 5: 55, 5: 77} #here 77 will override 55
print(z[int],z[True],z[5])
print('\n')


d1 = {'a':1,'b':2,'c':3,'d':4}
#d2 = {} ; d2.update(d1)
#d2 = dict(d1)
d2 = dict(d1.items())
print(d2)




