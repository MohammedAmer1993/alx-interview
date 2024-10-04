#!/usr/bin/python3
''' this module is for returning list of list reprensenting pascal triangl'''


def pascal_triangle(n):
    ''' function to represent pascal triangle
    n (int):
        the number of levels for triangle
    Return:
        list of list represents pascal triangle
    '''
    if n <= 0:
        return []
    else:
        topList = []
        for i in range(1, n + 1):
            levelList = []
            if i == 1:
                levelList.append(1)
                topList.append(levelList)
            elif i == 2:
                levelList.append(1)
                levelList.append(1)
                topList.append(levelList)
            else:
                levelList.append(1)
                for j in range(i - 2):
                    levelList.append(topList[i - 2][j] +
                                     topList[i - 2][j + 1])
                levelList.append(1)
                topList.append(levelList)
        return topList
