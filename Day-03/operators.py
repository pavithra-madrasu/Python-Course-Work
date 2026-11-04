'''# Arithmetic Operators
x=10
y=100
print(x+y,x-y,x*y,x/y,x//y,x%y,y**x)'''

'''# Assignment Operator
x=200
print(x)
x+=100
print(x)
x-=200
print(x)
x*=4
print(x)
x//=2
print(x)
x**=2
print(x)
x%=2
print(x)'''

'''# Comparsion Operator
x=26
y=14
print(x<y,x>y,x==y,x!=y,x<=y,x>=y)'''

'''#Logical Operators
x=26
y=14
print((x<y) and (x==y))
print((x<y) or (x>=y))
print((x>y) and (x!=y))
print(not (x<y))

#Bitwise Operators
num1=45
num2=4
print(num1 & num2)
print(num1 | num2)
print(num1 ^ num2)
print(~num2)
print(num2 <<2)
print(num2 >>1)

# Membership Operator
l=[10,2,3,4,54]
print(100 not in l)
print(4 in l)
print(5 not in l)'''

'''# Identity Operator
x=5
y=5
print(x is y)
a=[1,2,3]
b=a
#b=[1,2,3]
print(a is b)'''

'''#1.Area and perimeter of house
length = float(input("Enter the length of the house: "))
breadth = float(input("Enter the breadth of the house: "))

area = length * breadth
perimeter = 2 * (length + breadth)

print("Area of the house:", area)
print("Perimeter of the house:", perimeter)'''

'''#2.volume of tank
length = float(input("Enter the length of the tank: "))
breadth = float(input("Enter the breadth of the tank: "))
height = float(input("Enter the height of the tank: "))

volume = length * breadth * height

print("Volume of the water tank:", volume, "cubic units")
'''

'''#14. check the number is even using bitwise
num = int(input("Enter a number: "))

if num & 1 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")'''


'''#5.Square of a given number
num=int(input("enter a number:"))
#num=num*num
num=num**2
print(num)'''

'''#15.Swap the numbers
x=10
y=20
x,y=y,x
print(x,y)'''

'''#16.swap the number using third variable
x=100
y=200
print(x,y)
temp=x
x=y
y=temp
print(x,y)'''


'''#9.find the average of three numbers
x=10
y=20
z=30
c=(x+y+z)/2
print(c)
'''

'''#13.check the three sides can form a traingle
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if (a+b)>c:
    print("It is Traingle")
else:
    print("not a triangle")'''

'''#3. Convert minute into seconds
min=int(input("enter a min:"))
seconds= min*60
print("minute in seconds:",seconds)'''


''''#4.books 
t=100
p1=20
p2=30
remaining_pages=t-(p1+p2)
print(f"total pages in book:{t}")
print(f"pages read on day 1:{p1}")
print(f"pages read on day 2:{p2}")
print(f"pages reamining to read:{remaining_pages}")'''

'''#6 Data usage
D=float(input("enter your daily usage:"))
u1=float(input("enter your morning usage:"))
u2=float(input("enter your afternoon usage:"))
remaining_data=D-(u1+u2)
print("remaining data usage:", remaining_data,"GB")'''

'''# 7.bought 3 items.find total amount to pay
a=int(input("enter a first item:"))
b=int(input("enter a second item:"))
c=int(input("enter a third item:"))
total=a+b+c
print(total)'''


'''#8.find last digit of 4 digit number without built in functions
num=int(input("enter a 4 digit number:"))
last_digit=num%10
print("last digit",last_digit)'''


'''#10.check battery status
battery=int(input("enter a battery percentage:"))
if battery<20:
    print("phone charge is low")
else:
    print("phone charge is normal") '''


'''#11.user login age>18,it print true
age=int(input("enter a age:"))
ID=input("do you have ID?(True/false):")
if age>18 and ID=="True":
    print("Access granted")
else:
    print("Access Denied")'''

'''
#12. divisible by both 3 and 5
num=int(input("enter a number:"))
if num%3==0 and num%5==0:
    print("Number is divisble by both 3 and 5")
else:
    print("Number is not divisble by 3 and 5")'''


'''#17.find and return an integer value represents their product of 2 inteerger in 12-hour system
a=int(input("enter A:"))
b=int(input("enter B:"))
product=(a*b)%12
print(product)'''


'''#pratice 12vhour system problems
a=int(input("enter A:"))
b=int(input("enter B:"))
result=(a*b)%12
if result==0:result==12
print("output:",result)'''

#caluculate percentage
num=int(input("enter a number:"))
percentage=num%100
print(percentage)




