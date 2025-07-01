#Time complexity
#three case's are in the time complexity
#1.best case  2.average case    3. worst case
#1. for checking best case the the tc is 2
age=90
if age >=80:
    print("super senior")
if age>=60 and age<80:
    print('senior')
if age >=24 and age<60:
    print("working")
if age>=16 and age<24:
    print("students")
else:
    print("child")

# checking the worst time complexity
#in the worst case the tc take time 5 
age=10
if age >=80:
    print("super senior")
if age>=60 and age<80:
    print('senior')
if age >=24 and age<60:
    print("working")
if age>=16 and age<24:
    print("students")
else:
    print("child")


#for average time:- best case + worst case / 2