import calendar

# Get input from the user
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

# Create a calendar object
cal = calendar.monthcalendar(year, month)

# Print the calendar
print(calendar.month_name[month], year)
print("Mon Tue Wed Thu Fri Sat Sun")
for week in cal:
    for day in week:
        if day == 0:
            print("   ", end="")
        else:
            print(f"{day:2d} ", end="")
    print()
