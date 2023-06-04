from datetime import datetime

# Current date and time
print("Current date and time: ", datetime.now())

# Current year in full
print("Current year in full: ", datetime.now().strftime("%Y"))

# Month of year full name
print("Month of year full name: ", datetime.now().strftime("%B"))

# Weekday of the week
print("Weekday of the week: ", datetime.now().strftime("%A"))

# Day of year
print("Day of year: ", datetime.now().strftime("%j"))

# Day of the month
print("Day of the month: ", datetime.now().strftime("%d"))

# Day of week in full name
print("Day of week in full name: ", datetime.now().strftime("%A"))
