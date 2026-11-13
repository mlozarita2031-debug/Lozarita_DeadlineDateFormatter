
# Version 2: Deadline and Date Formatter

from datetime import date

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year, month, day)

print("\nFormatted Output:")
print("Event:", event_title.upper())
print("Date:", event_date.strftime("%B %d, %Y").replace(" 0", " "))
print("Year:", year)
print("Month:", event_date.strftime("%B"))
print("Day:", day)
print("Weekday:", event_date.strftime("%A"))
