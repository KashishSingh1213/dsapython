#recursion
#lets solve the first question of recursion    
#i want to print kashish 4 times
count = 0

def function():
    global count
    if count == 4:
        return
    print("kashish")
    count += 1
    function()

function()



#head recurion
#📌 Example: Print numbers from 1 to 4 using head recursion

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)  # Recursive call first
    print(n)              # Then do the work

print_numbers(4)

#tail recursion
def function(n):
    if n == 0:
        return
    print(n)         # ✅ Do the work first
    function(n - 1)  # 🔁 Recursive call last
