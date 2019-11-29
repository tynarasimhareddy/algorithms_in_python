
import sys 

# m is size of coins array (number of different coins) 
def minCoins(coins, V):
    table = {}
    table[0] = 0
    for i in range(1, V+1):
        table[i] = sys.maxsize

    for i in range(1, V+1):
        for c in coins:
            if c <= i:
                sub_res = table[i - c]
                if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                    table[i] = sub_res + 1
    return table[V]

coins = [9, 6, 5, 1] 
V = 8
print("Minimum coins required is",minCoins(coins, V)) 
