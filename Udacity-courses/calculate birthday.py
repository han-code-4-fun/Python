# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    return daysCount(year2,month2,day2)-daysCount(year1,month1,day1)
    
def monthToDays(m, y):
    if(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        days = 31
    if(m == 4 or m == 6 or m == 9 or m == 11):
        days =30
    if(m == 2):
        days = 28
        if(y  % 4 ==0):
            days = 29
            if(y % 100 == 0):
                if(y % 400 ==0):
                    days = 29
                else:
                    days = 28
        else:
            days =28
    if(m == 0):
        days = 0
    return days
    
    
def yearCheck(a):
    if(a  % 4 ==0):
        if(a % 100 == 0):
            if(a % 400 ==0):
                a = 366
            else:
                a = 365
        else:
            a = 366
    else:
        a =365
    return a
    
def daysCount(year,month,day):
    countNum = 0
    m = month
    y = year
    while(m>0):
        m = m -1
        d2 = monthToDays(m, y)
        countNum = countNum + d2
        
    while(y>0):
        y = y - 1
        d3 = yearCheck(y)
        countNum = countNum + d3
        
    countNum = countNum + day
    return countNum
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

####################official way

def isLeapYear(year):
	if year %400 ==0:
		return True
	if year %100==0:
		return False
	if year %4 ==0:
		return True
	return False
	
def daysInMonth(year,month):
	if month ==1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
		return 31
	else:
		if month ==2:
			if isLeapYear(year):
				return 29
			else:
				return 28
		else:
			return 30
			
def nextDay(year, month, day):
	if day< daysInMonth(year,month):
		return year,month,day+1
	else:
		if month <12:
			return year, month +1,1
		else:
			return year +1,1,1
			
def dateIsBefore(year1,month1,day1,year2,month2,day2):
	if year1<year2:
		return True
	if year1 == year2:
		if month1<month2:
	 		return True
	 	if month1 ==month2:
	 		return day1<day2
	return False
	 
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    days = 0
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
			
	
	
