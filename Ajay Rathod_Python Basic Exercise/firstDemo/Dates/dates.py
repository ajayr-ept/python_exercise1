import datetime
import datetime as DT
import dateutil.relativedelta as REL

# Find no of Days between two dates / datetime
x = datetime.datetime.now()
y = datetime.datetime(2018,6,23)
z = x - y
print('No of Days between two dates / datetime :')
print(z.days)

# Find Day of the date / datetime
x = datetime.datetime.now()
print('Day of the date / datetime')
print(x.strftime('%A'))

# Find month of the date / datetime
x = datetime.datetime.now()
print('Month of the date / datetime')
print(x.strftime('%B'))

# Find year of the date
x = datetime.datetime.now()
print('Year of the date')
print(x.strftime('%Y'))


# Convert string to date / datetime
x = 'Dec 4 2018 10:09AM'
format = '%b %d %Y %I:%M%p'  # The format
str1 = datetime.datetime.strptime(x,format)
print(str1)

# Subtract n no of days from a date and find that date
x = datetime.datetime(2015,10,10)
d = datetime.timedelta(5)
ans = x - d
print('N no of days from a date and find that date')
print(ans)

#Add year to a date

x = datetime.datetime(2015,10,10)
d = datetime.timedelta(days=730)
ans = x + d
print('Add year to a date')
print(ans)

# Find date of next Tuesday or Wednesday
today = DT.date.today()
print('Today Date :',today)


rd = REL.relativedelta(days=1, weekday=REL.TU)
next_tues = today + rd
print('date of next Tuesday :',next_tues)
rd = REL.relativedelta(days=1, weekday=REL.WE)
next_wed = today + rd
print('date of next Wednesday',next_wed)



#Add month to a date

x = datetime.datetime(2015,10,10)
d = datetime.timedelta(days=30+31)
ans = x + d
print('Add Month to a date')
print(ans)


# Find no of Month between two dates / datetime
def months(d1, d2):
    return d1.month - d2.month + 12*(d1.year - d2.year)

d1 = datetime.datetime.now()
d2 = datetime.datetime(2020, 4, 26)

print('total month :',months(d1, d2))

# Find no of years between two dates / datetime
from dateutil.relativedelta import relativedelta

myBirthday = datetime.datetime(2010,5,20,0,0,0,0)
now = datetime.datetime.now()

difference = relativedelta(now, myBirthday)
print("My years: "+str(difference.years))
