# 

# list of vowels
vowels_tuple = ('a', 'e', 'o', 'u', 'i', 'y')

# define the name
name = 'Arinanna'

# check and change the vowel or non-vowel
if name[0].lower() in vowels_tuple:
    new_name = name.replace(name[0], "B", 1)
else:
    new_name = name.replace(name[0], "A", 1)

# your new name is
print(new_name)
pass

