# Create list that contains the files in your current working directory
import os
import datetime


# define the current date
current_date = datetime.date.today()

# convert the date to a string <Visit> <https://strftime.org>
current_date_str = current_date.strftime("%Y%m%d")

# create a list with the files and folders
files_folders_list = os.listdir()

# add a new directory
#os.mkdir("our_functions")

# add new directory with sub-directories
os.makedirs(f"export/{current_date_str}/data", exist_ok=True)

pass