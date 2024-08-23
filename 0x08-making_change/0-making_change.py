#!/usr/bin/python3
"""
function to determine the fewest number of coins needed
to meet a given amount total
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # Initialize the dp array with a large number representing infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to achieve a total of 0

    # Iterate over each amount from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means we cannot make up the total
    return dp[total] if dp[total] != float('inf') else -1
