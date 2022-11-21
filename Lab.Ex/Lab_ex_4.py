import datetime
import calendar
import random
"""
# Print today's date
today = datetime.date.today().strftime("%d %B %Y")
print("Today's date: ", today)

# Print current time
time_now = datetime.datetime.now().strftime("%d %B %Y  %H:%M:%S")
print("Current time: ", time_now)

# Print current day
day = datetime.date.today().day
print("Current day: ", day)

# Print current day of the year
day_of_the_year = datetime.date.today().timetuple().tm_yday
print("Day of the year: ", day_of_the_year)

# Print current week
week = datetime.date.today().isocalendar().week
print("Current week: ", week)

# Print current month
month = datetime.date.today().month
print("Current month: ", month)

# Print current year
year = datetime.datetime.now().year
print("Current year: ", year)

# Check if year is leap or not
day_input = int(input("Enter day: "))
month_input = int(input("Enter month: "))
year_input = int(input("Enter year: "))
print(f"{year_input} is leap year" if calendar.isleap(year_input) else f"{year_input} is not a leap year")

# Print week of selected date
date_input = datetime.datetime(year_input, month_input, day_input)
week_of_year = date_input.isocalendar().week
print("Week of selected date: ", week_of_year)

# Check witch years Christmas is a sunday
start_year = int(input("Enter start year: "))
finish_year = int(input("Enter finish year: "))


for year in range(start_year, finish_year+1):
    if datetime.date(year, 12, 25).weekday() == 6:
        print(year)
"""

"""
arr = list(random.sample(range(10, 1000), 11))
array = random.sample(range(10, 1000), 11)
dict(array)


def get_random_element(arr):
    el = random.choice(arr)
    return el


print("Sum of random elements: ", get_random_element(arr) + get_random_element(array))
"""
