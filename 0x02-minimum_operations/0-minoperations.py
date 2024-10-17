#!/usr/bin/python3
''' this is a module for finding minimum number of
 operation to copy a content of a file reapeatdly'''


def minOperations(n):
    ''' function to find mimimum oper
    args:
        n (int): the required target of duplicating
    '''
    if n <= 0:
        return 0
    primeNum = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97, 101, 103,
                107, 109, 113, 127, 131, 137, 139,
                149, 151, 157, 163, 167, 173, 179,
                181, 191, 193, 197, 199, 211, 223,
                227, 229, 233, 239, 241, 251, 257,
                263, 269, 271, 277, 281, 283, 293]
    numberOfOper = 0
    if n == 1:
        return 0
    for i in primeNum:
        if n % i == 0:
            numberOfOper = i + minOperations(n / i)
            break
    return numberOfOper
