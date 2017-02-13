#!/Users/adave/anaconda3/bin/python
import datetime
from influxdb import InfluxDBClient
from random import randint
import random
import time
import json

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
    return strTimeProp(start, end, "%Y-%m-%dT%H:%M:%S", prop)

def randomTimestamp(start, end):
    rd = randomDate(start, end, random.random())
    # print rd
    return time.mktime(datetime.datetime.strptime(rd, '%m/%d/%Y').timetuple())


def main(host='localhost', port=8086):
    user = 'root'
    password = 'root'
    dbname = 'mydb'
    query = 'select value from cpu_load_short;'
    # json_body = [
    #     {
    #         "measurement": "cpu_load_short",
    #         "tags": {
    #             "host": "server02",
    #             "region": "us-west"
    #         },
    #         "time": datetime.datetime.now(),
    #         "fields": {
    #             "Float_value": 0.64,
    #             "Int_value": 3,
    #             "String_value": "Text",
    #             "Bool_value": True
    #         }
    #     }
    # ]


    host = '54.201.42.94'
    client = InfluxDBClient(host, port, dbname)


    client.switch_database(dbname)

    # print (randomDate("2015-03-04T21:08:12", "2016-03-04T21:08:12", random.random()))

    for i in range(1,1000):
            json_body = [
            {
                "measurement":"School",
                "tags": {"division":"BusinessSchool", "manager":"David"},
                "time": randomDate("2015-03-04T21:08:12", "2016-03-04T21:08:12", random.random()),
                "fields": {
                            "percent_extended":randint(0,100),
                            "percent_accepted":randint(0,100),
                            "inquiry":randint(10,100),
                            "website":randint(50,200),
                            "finance_events":randint(50,400),
                            "advisor_on_location":randint(10, 80),
                            "percent_grad":randint(50,400),
                            "percent_undergrad":randint(10,45),
                            "percent_management":randint(20,40),
                            "percent_employed": randint(30,70)
                          }

            }
            ]

            client.write_points(json_body)


    # result = client.query(query)

    # client.switch_user(user, password)


    # client.drop_database(dbname)


main()
