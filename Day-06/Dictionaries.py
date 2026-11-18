#sets
s={1,2,3,5}
s1=set()
s2={}
print(type(s),type(s1),type(s2))

#add(element)
s.add(10)
print(s)

#remove(element)
s.remove(10)
print(s)
'''s.remove(10)
print(s)'''#error

#dicard()
s.discard(5)
print(s)
s.discard(100)
print(s)#no error

#set operations
s1={10,20,30,40}
s2={40,50,60}
#union()
print(s1.union(s2))
print(s1|s2)

#intersection()
print(s1.intersection(s2))
print(s1 & s2)

#difference()
print(s1.difference(s2))
print(s2.difference(s1))

#symmetric_difference()
print(s1.symmetric_difference(s2))
print(s1^s2)

#issuperset()
s3={26,45,18,1,4}
s4={26}
print(s3.issuperset(s4))
print(s3.issubset(s4))
print(s4.issubset(s3))

#dictionaries
d={}
d1=dict()
d2={'a':1,
    'b':2,
    'c':3}
print(type(d),type(d1),type(d2))
print(d2['a'])
print(d2.values())
print(d2.keys())
print(d2.items())
d2['c'] =6
print(d2)
d2['d']=4
print(d2)
d2.update({'e':5})
print(d2)
d2.update(f=6)
print(d2)
print(d2.get('c'))
#print(d2['z'])#error
print(d2.get('z',0))
d2.pop('b')
print(d2)
#d2.pop('b')
d2.pop('b',None)
print(d2)
#popitem()# remove last elements
d2.popitem()
print(d2)
d2.clear()
print(d2)
'''del d2
print(d2)#error
'''
w=20
x=[10,20]
y={1:'r'}
print(id(y))
print(hash(y[1]))
print(id(w))
'''print(hash(w))#it use immutable datatype only
print(hash(x))'''

