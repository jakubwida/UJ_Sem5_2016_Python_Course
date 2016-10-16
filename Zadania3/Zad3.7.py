class Time:

    def __init__(self, seconds=0):
        self.s = seconds

    def __str__(self):
        return "%s sec" % self.s

    def __repr__(self):
        return "Time(%s)" % self.s

time1 = Time(12)
time2 = Time(3456)
print (str(time1), str(time2))            # Python wywołuje str()
print (repr(time1), repr(time2))          # Python wywołuje repr()


