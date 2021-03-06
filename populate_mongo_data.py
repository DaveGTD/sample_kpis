#!/Users/adave/anaconda3/bin/python

from pymongo import MongoClient
import datetime

client = MongoClient("mongodb://")
db = client.testdb

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
    return strTimeProp(start, end, '%m/%d/%Y %H:%M:%S', prop)

def randomTimestamp(start, end):
    rd = randomDate(start, end, random.random())
    # print rd
    return time.mktime(datetime.datetime.strptime(rd, '%m/%d/%Y %H:%M:%S').timetuple())


# print randomTimestamp("1/1/1991 1:30:32", "1/12/2016 4:50:12")

for num in range(0,1000):
    key = 'my_key'
    ts = int(randomTimestamp("1/1/1991 1:30:32", "1/12/2016 4:50:12"))
    n = randint(0,100)
    a = n*n
    b = n*n*n
    c = n*n*n*n

    result = db.sample.insert_one(
    {
        "key":key,
        "timestamp":ts,
        "a":a,
        "b":b,
        "c":c,
        "current_timestamp":time.time()
    }
    )

    print (result.inserted_id)
