str1="  if you trouble the trouble,trouble will troubles you. I am not the trouble, I am truth --Jai@999"
lower= str1.lower()
print(lower)
upper=str1.upper()
print(upper)
capitalize=str1.capitalize()
print(capitalize)
title=str1.title()
print(title)
print(str1.title())

#checking methods
print(str1.islower())
print(str1.isupper())
print(str1.isalpha())
print(str1.isalnum())
print("asgdfagj".isalnum())
print(str1.isdigit())
print("8246675".isdigit())
print(str1.isspace())
print(str1.count("trouble"))

#Modification methods
print(str1)
print(str1.strip())
print(str1.lstrip())
print(str1.rstrip())
print(str1.replace("trouble","hai"))
words=str1.split()
print(type(words))
print(str1.count("trouble"))

words=str1.split()
print(len(str1))
print(len(words))

combined_string="-".join(words)
print(combined_string)