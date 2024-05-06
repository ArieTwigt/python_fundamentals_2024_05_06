first_name = "Erling"
last_name  = "Haaland"

full_name = "{} {}".format(first_name, last_name)

#
full_name_new = f"{full_name} .Jr"
print(full_name_new)


second_name = "Herman"

# split the full name
full_name_seperate = full_name.split(" ")

# show the full name, including second name
full_name_second = f"{full_name_seperate[0]} {second_name} {full_name_seperate[1]}"

print(full_name_second)