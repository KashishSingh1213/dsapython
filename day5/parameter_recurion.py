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
