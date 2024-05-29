import Distributions
import Simulator


class times:
    def __init__(self, arrival, completion, current, next, last):
        self.arrival = arrival  # next arrival time
        self.completion = completion  # next completion time
        self.current = current  # current time
        self.next = next  # next event time
        self.last = last  # last arrival time


class area:
    def __init__(self, node, queue, service):
        self.node = node  # time integrated number in the node
        self.queue = queue  # time integrated number in the queue
        self.service = service  # time integrated number in the service


# CONSTANTS
STOP = 20000
START = 0
INFINITY = 100 * STOP
# PARAMETERS (change these...)
meanArrival = 2
lowerBoundUniform = 1
upperBoundUniform = 2
beta = 0.1
CAPACITY = INFINITY
# MAIN
index = 0
arrival = START
reject = 0
departure = START
t = times(0, 0, 0, 0, 0)
area = area(0, 0, 0)
number = 0  # number in the node

t.current = START  # set the clock
t.arrival = Simulator.getArrival(meanArrival) # schedule the first arrival
t.completion = INFINITY  # the first event can't be a completion
while t.arrival < STOP or number > 0:
    t.next = Distributions.Min(t.arrival, t.completion) # next event time
    if number > 0:  # update integrals
        area.node += (t.next - t.current)*number
        area.queue += (t.next - t.current)*(number-1)
        area.service += (t.next - t.current)
    t.current = t.next  # advance the clock

    if t.current == t.arrival:  # process an arrival
        if number < CAPACITY:
            number += 1
            if number == 1:
                t.completion = t.current + Simulator.getService(lowerBoundUniform, upperBoundUniform)
        else:
            reject += 1
        t.arrival = Simulator.getArrival(meanArrival)
        if t.arrival > STOP:
            t.last = t.current
            t.arrival = INFINITY
    else:  # process a completion
        if not Simulator.getFeedback(beta):
            index += 1
            number -= 1
        if number > 0:
            t.completion = t.current + Simulator.getService(lowerBoundUniform, upperBoundUniform)
        else:
            t.completion = INFINITY

print("\nfor {} jobs".format(index))
print("average interarrival time = {}".format(t.last / index))
print("average wait = {}".format(area.node / index))
print("average delay = {}".format(area.queue / index))
print("average service time = {}".format(area.service / index))
print("average # in the node = {}".format(area.node / t.current))
print("average # in the queue = {}".format(area.queue / t.current))
print("utilization = {}".format(area.service / t.current))