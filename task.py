from datetime import date
from datetime import timedelta


def firstrun():
    return "success"


def areacircle(rad):
    return 3.14159*rad*rad


def liststartend(list):
    rtnlist = []
    rtnlist.append(list[0])
    rtnlist.append(list[len(list)-1])
    return rtnlist


def daycounter(date1, date2):
    d1 = date(date1)
    d2 = date(date2)
    timedelta.days = d2 - d1
    return timedelta.days
