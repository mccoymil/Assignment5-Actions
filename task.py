from datetime import date


def firstrun():
    return "success"


def areacircle(rad):
    return 3.14159*rad*rad


def liststartend(list):
    rtnlist = []
    rtnlist.append(list[0])
    rtnlist.append(list[len(list)-1])
    return rtnlist


def daycounter(year1, mon1, day1, year2, mon2, day2):
    d1 = date(year1, mon1, day1)
    d2 = date(year2, mon2, day2)
    timedelta = d2 - d1
    return timedelta
