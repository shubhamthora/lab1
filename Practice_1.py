from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Subtract a week (7 days) from the current date
new_date = current_date - timedelta(days=7)

# Print the new date
print(new_date)
