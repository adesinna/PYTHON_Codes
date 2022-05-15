import datetime as dt


now = dt.datetime.now()  # shows you the present date and time
print(now)

year = now.year
print(year)

week_day = now.weekday()
print(week_day)

date_of_birth = dt.datetime(year=1994, month=9, day=26, hour=21, minute=10, second=55)  # returns date and time
print(date_of_birth)




