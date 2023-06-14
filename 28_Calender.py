# Program to display the Calender month from a specific year.

import calendar

year = int(input("Enter the year : "))
month = int(input("Enter the month : "))

calendar = calendar.month(year, month)
print(calendar)