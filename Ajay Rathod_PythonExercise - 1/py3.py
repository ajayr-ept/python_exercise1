''''Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
'''

import datetime # improt the datetime method

x = datetime.datetime.now() #today date
y = datetime.datetime(2020,5,5) # any date of here write
z = x - y # apply here Logic
print(z.days) # print here Number of days
