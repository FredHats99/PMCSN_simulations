import Distributions

START = 0


def getArrival(meanValue):
    arrival = START + Distributions.Exponential(meanValue)
    return arrival


def getService(lowerBound, upperBound):
    return Distributions.Uniform(lowerBound, upperBound)
