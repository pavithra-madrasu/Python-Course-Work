'''#1
length=int(input("enter an length:"))
breadth=int(input("enter an breadth:"))
area=length*breadth
perimeter=2*(length+breadth)
print("Area of house:",area)
print("Perimeter of house:",perimeter)
'''

'''#2.
length=float(input("enter an length:"))
breadth=float(input("enter an breadth:"))
height=float(input("enter an height:"))
Volume=length+breadth+height
print("Volume of water tank:",Volume)'''

'''#3.
min=int(input("enter a minute:"))
seconds=min*60
print(seconds)'''

'''#4.
t=100
p1=30
p2=20
remaining_pages=t-(p1+p2)
print(f"enter total pages:",{t})
print(f"enter first day pages:",{p1})
print(f"enter second day pages:",{p2})
print(f"remaining pages:",remaining_pages)
'''
'''#5
num=int(input("enter a number:",))
#num=num*num
num=num**2
print(num)'''

'''#6.
D=float(input("enter your daily usage:"))
u1=float(input("enter your morning usage:"))
u2=float(input("enter your afternoon usage:"))
remaining_data=D-(u1+u2)
print("remaining data usage:", remaining_data,"GB")'''

'''#7.
a=int(input("enter a 1st item:"))
b=int(input("enter a 2nd item:"))
c=int(input("enter a 3rd item:"))
total=a+b+c
print(total)
'''
'''#8
num=int(input("enter a 4 digit number:"))
last_digit=num%10
print("last digit",last_digit)'''

'''#9
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
average=(a+b+c)/2
print(average)
'''

'''#10.
battery=int(input("enter a battery percentage:"))
if battery<20:
    print("phone charge is low")
else:
    print("phone charge is normal") '''

'''#11.
age=int(input("enter a age:"))
ID=input("do you have ID?(True/False):")
if age>18 and ID=="True":
    print("Access granted")
else:
    print("Access Denied")'''

'''#12
num=int(input("enter a number:"))
if num%3==0 and num%5==0:
    print("Number is divisble by both 3 and 5")
else:
    print("Number is not divisble by 3 and 5")
'''
'''#13
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if (a+b)>c:
    print("It is Traingle")
else:
    print("not a triangle")'''

'''#14
num = int(input("Enter a number: "))

if num & 1 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")
'''
'''15.
x=10
y=20
print(x,y)
x,y=y,x
print(x,y)'''

'''#16
x=10
y=200
print(x,y)
temp=x
x=y
y=temp
print(x,y)'''

'''#17,18,19
a=int(input("enter A:"))
b=int(input("enter B:"))
product=(a*b)%12
print(product)
'''

#20
num=int(input("enter a number:"))
percentage=num%100
print(percentage)
