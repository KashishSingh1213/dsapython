#parameter of recursion
def function(count):
    if count == 4:
        return              # Agar 4 baar print ho gaya toh ruk jaao
    print("kashish")        # Print karo
    function(count + 1)     # count + 1 karke fir se function call karo

function(0)  # Start count from 0


#15 ko 3 bar print krna hai using recursion
def function(count):
    if count == 3:
        return
    print(15)
    function(count + 1)

function(0)



#print 1 to n using recursion
def function(i, n):
    if i > n:
        return
    print(i)
    function(i + 1, n)

function(1, 4)

#print 1 to n using recursion
#backtracking
def function(i, n):
    if i > n:
        return
    function(i + 1, n)  # Recursive call first
    print(i)            # Backtracking: print after the call

function(1, 4)
