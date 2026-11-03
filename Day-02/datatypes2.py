'''num3=int(input())
print(num3)

#implicit
num1=100
num2=3.5
c= num1+num2
print(c,type(c))'''

'''#explicit
n=input()
print(type(n))
#n2=input()
n2=int(n)
print(type(n2))

str1="pavi"
print(str1)
lst2=list(str1)
print(lst2)
t2=tuple(lst2)
print(t2)
set2=set(lst2)
print(set2)'''

#read the int,set,list
num=int(input())
s=input()
list1=list(map(int,input().split(",")))
tuple1=tuple(map(int,input().split()))
set1=set(map(int,input().split()))
print(num)
print(s)
print(list1)
print(tuple1)
print(set1)