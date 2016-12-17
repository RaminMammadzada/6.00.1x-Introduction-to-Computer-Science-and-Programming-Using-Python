import math

class Clock(object):
    def __init__(self, time):
        self.time = time
    def __str__(self):
        return "<"+str(self.time)+">"
    def print_time(self):
        time = '6:30'
        print self.time

clock = Clock('5:30')
clock.print_time()


'''
class Clock(object):
    def __init__(self, time):
        self.time = time
    def __str__(self):
        return "<"+str(self.time)+">"
    def print_time(self, time):
        print time

clock = Clock('5:30')
clock.print_time('10:30')


class Clock(object):
    def __init__(self, time):
        self.time = time
    def __str__(self):
        return "<"+str(self.time)+">"
    def print_time(self):
        print self.time

boston_clock = Clock('5:30')
print '1'+str(boston_clock)
paris_clock = boston_clock
print '2'+str(paris_clock)
paris_clock.time = '10:30'
print '3'+str(paris_clock)
boston_clock.print_time()
print '4'+str(boston_clock)
'''
