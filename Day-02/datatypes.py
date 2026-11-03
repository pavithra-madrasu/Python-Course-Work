# Numeric Data Type
number = 100
percentage = 9.4
c = 2+4j
c2 = complex(number)
print(number,)
print(percentage)
print(c)
print(number, type(number))
print(percentage, type(percentage))
print(c,type(c))
print(c2,type(c2))

# Seqenece Data Types
s="pavi"
lst=[10,20,30]
t=(1,2,3,4)
t2=(12,)
print(type(s),type(lst),type(t),type(t2))


# Boolean Data Types
bool1=True
bool2=False
print(type(bool1))
print(type(bool2))
print(bool1+bool2)


# Mapping Data Type-Dictionary
d= { "name" :"pavithra",
   "roll-no":14,
   "department" :"CSM"}
print(d,type(d))


# Sets
s={1,2,3,4}
print(s,type(s))


# empty list and String , typle, dictionary, set
lst1=[]   # list()
t1=()   # tuple()
str1=""   # str()
d1={}    # dict()
#s1={}  
s1=set()    # set()
print(lst1, type(lst1))
print(t1,type(t1))
print(str1,type(str1))
print(d1,type(d1))
print(s1,type(s1))