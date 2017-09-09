from datetime import datetime
import time
import parsedatetime
import pytz
from pytz import timezone
import iso8601

# ISO8601 for all input/output
ET = timezone('US/Eastern')

# CONSTANTA
TIMESTAMP = '%Y-%m-%d %H:%M:%S'
DATETIME = '%Y-%m-%d %H:%M'
DATE = '%Y-%m-%d'
MDY = '%m/%d/%Y'
HEADER = '%A, %B %-d, %Y'
DOY = '%j'
TIME = '%I:%M %p'

#def parse(string):


def datetime_from_string(string, is_local):
    cal = parsedatetime.Calendar()
    dt, _ = cal.parseDT(datetimeString=string, tzinfo=pytz.utc)
    if (is_local == 1):
        return dt.astimezone(ET)
    else:
        return datetime_obj

def datetime_from_iso(string, is_local):
    if (is_local == 1):
        return iso8601.parse_date(string).astimezone(ET)
    else:
        return iso8601.parse_date(string)

def epoch_from_datetime(dt):
    epoch = time.mktime(dt.timetuple())
    return epoch

def datetime_from_epoch(epoch):
    dt = datetime.fromtimestamp(epoch)
    return dt.strftime(DATETIME)

def date_from_epoch(epoch):
    dt = datetime.fromtimestamp(epoch)
    return dt.strftime(DATE)

def timestamp_from_epoch(epoch):
    dt = datetime.fromtimestamp(epoch)
    return dt.strftime(TIMESTAMP)

def mdy_from_epoch(epoch):
    dt = datetime.fromtimestamp(epoch)
    return dt.strftime(MDY)

def header_date_from_epoch(epoch):
    dt = datetime.fromtimestamp(epoch)
    return dt.strftime(HEADER)

def doy_from_datetime(dt):
    return dt.strftime(DOY)

def doy_from_epoch(epoch):
    dt = datetime.fromtimestamp(epoch)
    return dt.strftime(DOY)

def tomorrow():
    return datetime_from_string('tomorrow', 1)

def yesterday():
    return datetime_from_string('yesterday', 1)

def today():
    return datetime_from_string('today', 1)

def now():
    return datetime_from_iso(datetime.utcnow().isoformat(), 1)

def dt_format(dt, format):
    if (format == 'ts' or format == 'timestamp'):
        return dt.strftime(TIMESTAMP)
    elif (format == 'dt' or format == 'datetime'):
        return dt.strftime(DATETIME)
    elif (format == 'date'):
        return dt.strftime(DATE)
    elif (format == 'mdy'):
        return dt.strftime(MDY)
    elif (format == 'header'):
        return dt.strftime(HEADER)
    elif (format == 'iso'):
        return dt.isoformat() + 'Z'
    elif (format == 'time'):
        return dt.strftime(TIME)
    else:
        return dt.strftime(DATETIME)
