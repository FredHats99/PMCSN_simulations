import math
import random

INFINITY = 2147483647


def getRandomSeq(state):
    val = 48271
    mod = 2147483647
    quotient = mod / val
    remainder = mod % val

    t = val * (state % quotient) - remainder * (state / quotient)
    # print("t = {}".format(t))
    return t, state / mod


def get_random():
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


class Distribution:
    def __init__(self, lower_bound, upper_bound, mean, variance):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.mean = mean
        self.variance = variance
        self.std_deviation = math.sqrt(self.variance)


class Exponential(Distribution):
    def __init__(self, lamda):
        assert lamda > 0
        super().__init__(0, INFINITY, 1 / lamda, 1 / (lamda ** 2))
        self.lamda = lamda

    def prob_distribution_func(self, x_value):
        return self.lamda * (math.e ** (- self.lamda * x_value))

    def inverse_distribution_function(self, u_value):
        return -self.mean * math.log(math.e, 1 - u_value)


def exponential(mean_value):
    assert mean_value > 0
    return -mean_value * math.log(math.e, 1 - get_random())


def uniform(lower_bound, upper_bound):
    assert upper_bound > lower_bound
    return lower_bound + (upper_bound - lower_bound) * get_random()


def bernoulli(prob):
    if get_random() < 1 - prob:
        return 0
    else:
        return 1


def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
