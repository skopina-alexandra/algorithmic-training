from datetime import datetime
import calendar

holidays_count = int(input())
year = int(input())

holydays = [0,0,0,0,0,0,0]

for i in range(holidays_count):
    holydays[datetime.strptime(input() + ' ' + str(year), '%d %B %Y').weekday()] += 1

start_of_the_year_name = input()


weekdays_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

start_of_the_year = weekdays_name.index(start_of_the_year_name)

weekdays = [52,52,52,52,52,52,52]

weekdays[start_of_the_year] += 1

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    weekdays[(start_of_the_year + 1) % 7] += 1

min = 55
min_day = 0
max = -1
max_day = 0

for i in range(7):
    holidayless = weekdays[i] - holydays[i]

    if holidayless < min:
        min_day = i
        min = holidayless
    if holidayless > max:
        max_day = i
        max = holidayless

print(weekdays_name[max_day], weekdays_name[min_day])
