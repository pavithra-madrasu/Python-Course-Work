# find the missing numbers
s1={10,45,62,75,43}
s2={45,10,1}
print(s1.symmetric_difference(s2))

#find unique elements
word="Innovation"
print(set(word))

#create a dictionary from two list
l1=[1,2,3]
l2=[4,5,6]
c=dict(zip(l1,l2))
print(c)

#calculate total marks
marks={"python":85,
       "aptitude":90,
       "soft skills":65}
print(marks.values())
total=sum(marks.values())
print(total)