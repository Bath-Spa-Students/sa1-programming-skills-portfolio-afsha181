# Dictionary of months and their days
month_days = {
    1: 31,   # January
    2: 28,   # February
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Ask the user for a month number
month = int(input("Enter a month number (1-12): "))

# Check if the input is valid
if month in month_days:
    print(f"The month has {month_days[month]} days.")
else:
    print("Invalid input! Please enter a number between 1 and 12.")