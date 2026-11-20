#if statement
age=23
if age>=18:
    print("vote is eligible")

#if-else statement
num=int(input())
if num>0:
    print("positive")
else:
    print("negative")

#even or odd
num=int(input())
if num%2==0:
    print("even")
else:
    print("odd")

#Create a simple ATM withdrawal eligibility program.
balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount >= 100 and amount <= balance:
    print("Withdrawal Successful")
else:
    print("Withdrawal Not Possible")
 
#if-elif-else statement
marks=90
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
elif marks<=35:
    print("D")
else:
    print("Failed")

#among 3 greatest numbers
#a,b,c=map(int,input().split())
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)

#FizzBuzz
num=6
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")



#nested statement
#greatest among 3 numbers
a=int(input())
b=int(input())
c=int(input())
#a,b,c=map(int,input().split())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
else:
    if b>c:
        print(b)
    else:
        print(c)        
