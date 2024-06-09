import datetime

def datama(a):
    timestamp = a
    date_time = datetime.datetime.utcfromtimestamp(timestamp)
    return date_time
