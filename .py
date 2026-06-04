# Days in each month (non-leap year)
days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

# Days remaining in December after Christmas
days_after_christmas = days_in_month["December"] - 25

# Add days for January, February, March, and April 18
total_days = (
    days_after_christmas +
    days_in_month["January"] +
    days_in_month["February"] +
    days_in_month["March"] +
    18  # April 18
)

print("Number of days:", total_days)