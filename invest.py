#!/usr/bin/python
import sys

def invest(amount, rate, time):
    growth = (amount * rate)
    # range generates a list, thus using memory
    # xrange is a generator so it doesn't use all memory
    for i in xrange(1, time + 1):
        print 'Year {0}: {1}'.format(i, amount + (growth * i))

    return growth

def compound(amount, rate, time, additional=0):
    # range generates a list, thus using memory
    # xrange is a generator so it doesn't use all memory
    for i in xrange(1, time + 1):
        amount += additional
        amount = int(amount + (amount * rate))
        print 'Year {0}: {1}'.format(i, amount)

if __name__ == '__main__':
    args = sys.argv
    time = 5
    if len(args) > 1:
        amount = int(args[1])
        rate = float(args[2])
        time = int(args[3])
        additional = int(args[4])

        compound(amount, rate, time=time, additional=additional)
        #growth = invest(2000, .025, time=time)

