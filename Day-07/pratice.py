#find out longest word
S="I Love myself"
word=S.split()
longest=max(word,key=len)
print(longest)


#find out the year of that person
name=input("enter a name:")
print(name)
age=input("enter a age:")
year=2026-int(age)
print(year)

#Create a simple ATM withdrawal eligibility program.
balance = 5000

amount = int(input("Enter withdrawal amount: "))

if amount >= 100 and amount <= balance:
    print("Withdrawal Successful")
else:
    print("Withdrawal Not Possible")