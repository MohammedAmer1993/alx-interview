#!/usr/bin/python3
'''this is a module to parse stdin line by line
and get the total size and the status code stats'''

import sys
import signal

totalSize = 0
responseState = [200, 301, 400, 401, 403, 404, 405, 500]
responseCount = [0, 0, 0, 0, 0, 0, 0, 0]


def parserStatusCode(line):
    index = line.find('"')
    index = line.find('"', index + 1)
    indexEnd = line.find(' ', index + 2)
    return line[index + 1: indexEnd]


def parserFileSize(line):
    index = line.find('"')
    index = line.find('"', index + 1)
    indexSpace = line.find(' ', index + 2)
    return line[indexSpace:]


def printOutput(responseState, responseCount, totalSize):
    print(f"File size: {totalSize}")
    for item, index in enumerate(responseState):
        if responseCount[index] == 0:
            continue
        else:
            print(f'{item}: {responseCount[index]}')


def sigIntHandler(signum, frame):
    printOutput(responseState, responseCount, totalSize)
    sys.exit(0)


signal.signal(signal.SIGINT, sigIntHandler)

if __name__ == "__main__":

    n = 0
    for line in sys.stdin:
        statusCode = parserStatusCode(line)
        filesize = parserFileSize(line)
        try:
            StatusCodeInt = int(statusCode)
        except ValueError:
            continue
        try:
            fileSizeInt = int(filesize)
        except ValueError:
            continue
        if line.find('"GET /projects/260 HTTP/1.1"') < 0:
            continue

        for item, index in enumerate(responseState):
            if StatusCodeInt == item:
                responseCount[index] = responseCount[index] + 1
                break
        else:
            continue
        totalSize += fileSizeInt
        n += 1
        if n == 10:
            n = 0
            printOutput(responseState, responseCount, totalSize)
