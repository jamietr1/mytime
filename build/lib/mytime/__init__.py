import datetime
import Calendar
import time
from dateutil import tz

# Base timezone settings
FROM_ZONE = tz.tzutc()
MY_ZONE = tz.tzlocal    # At some point, make this a setting, or relative to location

def epoch_from_datetime(dt):
    epoch = calendar.timegm(dt.timetuple())
    return epoch


print epoch_from_datetime(datetime.datetime(2016, 04, 20, 0, 0))
