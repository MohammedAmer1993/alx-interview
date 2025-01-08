#!/usr/bin/python3
'''this is project to find miniumum coins needed'''


def makeChange(coins, total):
    if total <= 0:
        return 0
    sortedCoins = sorted(coins, reverse=True)
    numberOfCoins = 0
    for coin in sortedCoins:
        while total >= coin:
            total -= coin
            numberOfCoins += 1
    if total == 0:
        return numberOfCoins
    else:
        return -1
