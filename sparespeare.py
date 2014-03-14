#!/usr/bin/python3
import random
import pickle

with open('lines.pkl', 'rb') as f:
    lines = pickle.load(f)

def getLines(amount, returnList=False, listSpeaker=False, newLine=True):
    # Start counting from random spot in list, such that there will be enough lines to fulfill amount requested
    index = random.randint(0, len(lines) - amount)
    if returnList:
        result = []
    else:
        result = ''

    if newLine:
        nl = "\n"
    else:
        nl = ' '

    for i in range(index, index + amount):
        if returnList:
            if listSpeaker:
                result.append(lines[i][0] + ' ' + lines[i][1] + nl)
            else:
                result.append(lines[i][1] + nl)
        else:
            if listSpeaker:
                result = result + lines[i][0] + " " + lines[i][1] + nl
            else:
                result = result + lines[i][1] + nl
    if returnList:
        result[-1] = result[-1].rstrip()
    else:
        result = result.rstrip()
    return result

def getWords(amount, returnList=False):
    """
    Extracts amount of words from list of lines
    """
    # Start at a random index
    i = random.randint(0, len(lines) - 1)
    result = []
    while len(result) < amount:
        result.extend(lines[i][1].split(' '))
        i = (i + 1) % len(lines)
    result = result[:amount]
    if returnList:
        return result
    else:
        return ' '.join(result)