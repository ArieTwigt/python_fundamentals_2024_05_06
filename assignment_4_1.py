# Assign a variable that holds the number of days until your next birthday
import datetime

# define the date of today
current_date = datetime.date.today()

# define the birthday
birthday = datetime.date(2024, 12, 5)

# define the days until the next birthday
days_until_birthday = birthday - current_date

# print the number of days
print(f"Nog {days_until_birthday.days} dagen voor de sint 🎁")

pass