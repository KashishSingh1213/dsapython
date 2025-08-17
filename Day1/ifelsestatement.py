# x=5
# if(x>5):
#     print("x is greater than 5")
# else:
#     print("x is less than 5")


# Example of if-else statement
marks =  75
if(marks>90):
    print("grade A")
elif(marks>80):
    print("grade B")
elif(marks>70):
    print("grade C")
elif(marks>60):
    print("grade D")    
else:   
    print("grade F")


    marks =  75
    if(marks>90):
    print("grade A")

    #explantion
    # if marks is greater than 90, print "grade A"
    elif(marks>80):
    print("grade B")

    # if marks is greater than 80, print "grade B"
    elif(marks>70):
        print("grade C")

    # if marks is greater than 70, print "grade C"
    elif(marks>60):
        print("grade D")

    # if marks is greater than 60, print "grade D"
    else:
        print("grade F")

    # if marks is less than or equal to 60, print "grade F"
    
    #time complexity
# O(1) - constant time complexity, as it checks a fixed number of conditions regardless of input size.
# Space complexity
