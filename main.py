import Distributions
import Simulator

# CONSTANTS
LAST = 10000
START = 0
# PARAMETERS (change these...)
meanArrival = 2
lowerBoundUniform = 1
upperBoundUniform = 2
# MAIN
index = 0
arrival = START
delay = 0
service = 0
wait = 0
departure = START
sum = [0, 0, 0, 0]  # [delay, wait, service, inter_arrival]

while index < LAST:
    index += 1
    arrival = Simulator.getArrival(meanArrival)
    if arrival < departure:
        delay = departure - arrival
    else:
        delay = 0
    service = Simulator.getService(lowerBoundUniform, upperBoundUniform)
    wait = delay + service
    departure = arrival + wait
    sum[0] += delay
    sum[1] += wait
    sum[2] += service
sum[3] = arrival - START

print("\nfor {} jobs".format(index))
print("average interarrival time = {}".format(sum[3] / index))
print("average wait = {}".format(sum[1] / index))
print("average delay = {}".format(sum[0] / index))
print("average service time = {}".format(sum[2] / index))
print("average # in the node = {}".format(sum[1] / departure))
print("average # in the queue = {}".format(sum[0] / departure))
print("utilization = {}".format(sum[2] / departure))
