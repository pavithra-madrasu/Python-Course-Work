a=[10,20,30,40,50]
a.append(60)
print(a)
print(type(a))
a.append([1,2,3])
print(a)

#extend(multiple elements)
a.extend([1,2,3,4])
print(a)

#insert(position,element)
a.insert(0,100)
print(a)

#removing the elements from the list
#remove(element)
a.remove(20)
print(a)
a.remove(101)
print(a)# error
element=101
if element in a:
    a.remove(element)
print("no element")

#pop()
a.pop()
print(a)
a.pop(2)
print(a)

#clear()
a.clear()
print(a)
'''
'''#del()
del a 
print(a)# It will give error because it delete can whole list and its elements also'''

#Built in functions
a=[10,20,67,71,90,16]
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))

#shallow copy
import copy
l1=[10,20,30,[1,2]]
l2=copy.copy(l1)
print(l1)
print(l2)
l1[0]=100
print(l1)
print(l2)
print()
l1[3][1]=1000
print(l1)
print(l2)

#deepcopy()
import copy
l1=[10,20,30,[1,2]]
l2=copy.deepcopy(l1)
print(l1)
print(l2)
l1[0]=100
print(l1)
print(l2)
print()
l1[3][1]=1000
print(l1)
print(l2)

#tuple methods
P=(10,20,30,10,50)
print(P.count(10))
print(P.index(20))

#difference between Sort() and Sorted()
U=[40,10,20,30]
b=sorted(U)
print("original list:",U)
print("Sorted list:",b)
U.sort()
print("After sort():",U)
