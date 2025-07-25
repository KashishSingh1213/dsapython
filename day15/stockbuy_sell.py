#stock buy and cell
prices=[7,2,1,5,6,4,8]
n= len(prices)
max_profit=0
for i in range(n):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            profit=prices[j]-prices[i]
            max_profit=max(max_profit,profit)
print("Maximum Profit:", max_profit)


#if i can only sell the price
prices=[7,2,1,5,6,4,8]
n=len(prices)
max_profit=1
for i in range(0,n):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            profit=prices[j]-prices[i]
            max_profit=max(max_profit,profit)
        else:
            break  # Stop if the price does not increase


#optimal solution
prices=[7,2,1,5,6,4,8]
n=len(prices)
max_profit=0
for i in range(1,n):
    if prices[i]>prices[i-1]:
        profit=prices[i]-prices[i-1]
        max_profit+=profit
print("Maximum Profit (Optimal):", max_profit)
