
p = [1, 2, 3, 4]
cash = 7

def maximumToys(prices, k):
    prices.sort()
    spent = 0
    toys = 0
    for i in range(0, len(prices) + 1):
        if spent < k:
            spent += prices[i]
            toys += 1
        else:
            return(toys - 1)

print(maximumToys(p, cash))

        
