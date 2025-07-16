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
