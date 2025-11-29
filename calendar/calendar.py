
def print_calendar(days_in_month, start_day):
    #Days of the week headers for the chart
    days_header = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
    print(' '.join(f"{day:>2}" for day in days_header))

    #Creating spacing
    calendar = ['   '] * start_day

    #Filling in the days of the month
    for day in range(1, days_in_month + 1):
        calendar.append(f"{day:>2}")

    #Print the calendar for each week
    for i in range(0, len(calendar), 7):
        print(' '.join(calendar[i:i+7]))

#Validating user inputs
try:
    days_in_month = int(input("Enter the number of days in the month (28-31): "))
    start_day = int(input("Enter the starting weekday (0=Sunday, 1=Monday, ..., 6=Saturday): "))

    if days_in_month < 28 or days_in_month > 31:
        print("Invalid number of days. Please enter between 28 and 31.")
    elif start_day < 0 or start_day > 6:
        print("Invalid start day. Please enter a value between 0 and 6.")
    else:
        print("\nHere is your calendar:")
        print_calendar(days_in_month, start_day)
except ValueError:
    print("Invalid input. Please enter numeric values only.")
