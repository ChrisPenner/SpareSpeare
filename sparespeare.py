#!/usr/bin/python3
import random
import pickle

with open('lines.pkl', 'rb') as f:
    lines = pickle.load(f)

def getLines(amount, returnList=False, listSpeaker=False):
    # Start counting from random spot in list, such that there will be enough lines to fulfill amount requested
    index = random.randint(0, len(lines) - amount)
    if returnList:
        result = []
    else:
        result = ''

    for i in range(index, index + amount):
        if returnList:
            if listSpeaker:
                result.append(lines[i][0] + ' ' + lines[i][1] + "\n")
            else:
                result.append(lines[i][1] + "\n")
        else:
            if listSpeaker:
                result = result + lines[i][0] + " " + lines[i][1] + "\n"
            else:
                result = result + lines[i][1] + "\n"
    if returnList:
        result[-1] = result[-1][:-1]
    else:
        result = result[:-1]
    return result