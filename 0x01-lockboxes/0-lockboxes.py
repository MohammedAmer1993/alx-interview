#!/usr/bin/python3
''' this is a function to solve dynamic programming problem the
problem is we have boxes of boxes and we need to know
if we have every key for a box'''


def canUnlockAll(boxes):
    array = [0]

    def recfunc(count):
        for i in boxes[count]:
            if i in array:
                return
            else:
                array.append(i)
                recfunc(i)
    recfunc(0)
    if len(array) == len(boxes):
        return True
    else:
        return False