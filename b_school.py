#!/Users/adave/anaconda3/bin/python

import random
import time
import datetime
from random import randint

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)

def randomTimestamp(start, end):
    rd = randomDate(start, end, random.random())
    # print rd
    return time.mktime(datetime.datetime.strptime(rd, '%m/%d/%Y').timetuple())


# print randomTimestamp("1/1/1991 1:30:32", "1/12/2016 4:50:12")

for num in range(0,10):
    key = 'offers'
    n = randint(300, 1000)
    ts = int(randomTimestamp("1/1/1991", "1/12/2016"))
    a = randint(0,100)
    tag_a = 'percent_extended=' + str(a)
    b = randint(0,100)
    tag_b = 'percent_accepted=' + str(b)
    print (key, ts, n, tag_a, tag_b)


for num in range(0,10):
    key = 'inquiry'
    ts = int(randomTimestamp("1/1/1991", "1/12/2016"))
    a = randint(10,100)
    tag_a = 'website=' + str(a)
    b = randint(50,200)
    tag_b = 'finance_events=' + str(b)
    c = randint(50,100)
    tag_c = 'women_events=' + str(c)
    d = randint(50,400)
    tag_d = 'mixers=' + str(d)
    e = randint(10, 80)
    tag_e = 'advisor_on_location=' + str(e)
    n = a + b + c + d + e
    print (key, ts, n, tag_a, tag_b, tag_c, tag_d, tag_e)

for num in range(0,10):
    key = 'demographics'
    n = randint(300, 600)
    ts = int(randomTimestamp("1/1/1991", "1/12/2016"))
    a = randint(10,45)
    tag_a = 'percent_grad=' + str(a)
    b = randint(20,40)
    tag_b = 'percent_undergrad=' + str(b)
    c = randint(20,40)
    tag_c = 'percent_employed=' + str(c)
    d = randint(30,70)
    tag_d = 'percent_management=' + str(d)
    print (key, ts, n, tag_a, tag_b, tag_c, tag_d)
