import Distributions

START = 0


def getArrival(meanValue):
    arrival = START + Distributions.Exponential(meanValue)
    return arrival


def getService(lowerBound, upperBound):
    return Distributions.Uniform(lowerBound, (lowerBound + upperBound) * 0.5) + Distributions.Uniform(lowerBound, (
                lowerBound + upperBound) * 0.5)


def getFeedback(beta):
    if Distributions.getRandom() < beta:
        return True
    else:
        return False
