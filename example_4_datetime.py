import datetime

# input for the date
selected_date = input("Insert your date (Y-m-d)\n")

# create a date from the string
my_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d")

# get the current date
current_date = datetime.datetime.now()

# subtract number of days
num_days_delta = current_date - my_date

#
num_days = num_days_delta.days

# 
print(f"📅 Wait {num_days} days")