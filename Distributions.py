import math
import random


def getRandomSeq(state):
    val = 48271
    mod = 2147483647
    quotient = mod / val
    remainder = mod % val

    t = val * (state % quotient) - remainder * (state / quotient)
    # print("t = {}".format(t))
    return t, state / mod


def getRandom():
    mod = 2147483647
    state = 1
    count = 0
    sequence = 0
    while count < random.randint(1, 100000):
        count += 1
        sequence = getRandomSeq(state)
        if sequence[0] > 0:
            state = sequence[0]
        else:
            state = sequence[0] + mod
    return sequence[1]


def Exponential(meanValue):
    assert meanValue > 0
    return -meanValue * math.log(math.e, 1 - getRandom())


def Uniform(lowerBound, upperBound):
    assert upperBound > lowerBound
    return lowerBound + (upperBound - lowerBound) * getRandom()