# Make a dictionary with the names of months and their days
month_days = {
    1: 31,   # January
    2: 28,   # February (non-leap year)
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

# Get month number from player
month = int(input("Enter the month number (1-12): "))

# Check if the given information is correct
if month < 1 or month > 12:
    print("Invalid month number. Please enter a number between 1 and 12.")
else:
    # If the month is February, leap year will be asked.
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
        # Adjust days for February month if it's a leap year
        days = 29 if leap_year == 'yes' else 28
    else:
        # For other months, the input will be taken directly from the dictionary
        days = month_days[month]
   
    # Show the number of days
    print(f"The month has {days} days.")