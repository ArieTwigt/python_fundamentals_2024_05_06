# Create a loop that prints the name of the day for the following 10 days
import datetime


# define the current date
current_date = datetime.date.today()

# iterate trough the next 10 days
for i in range(1, 11):
    # calculate the next date
    next_day = current_date + datetime.timedelta(days=i)

    # format the next date <https://strftime.org>
    next_day_name = next_day.strftime("%A")
    print(next_day_name)

pass