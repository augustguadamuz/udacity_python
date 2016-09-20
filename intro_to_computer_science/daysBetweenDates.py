def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
    
def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
    or month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
                           
def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month <12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year2 > year1:
        return True
    if year2 == year1 and month2 > month1:
        return True
    if year2 == year1 and month2 == month1 and day2 > day1:
        return True
    else:
        return False
    
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days