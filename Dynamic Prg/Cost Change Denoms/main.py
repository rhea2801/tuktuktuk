# O (N) T | O(N) S
def costChange(denoms, n):
    ways = [0 for counter in range(n+1)]
    ways[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount-denom]
        return ways[n]
