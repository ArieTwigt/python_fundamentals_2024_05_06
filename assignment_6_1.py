# 
# Create a loop that removes the vowels from the following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] . Add the results to a new list.

# initiate the list
names_list = ['Arie', 'Jim', 'John', 'Marc', 'Danny', 'Peter']

# vowels
vowels = "aeoui"

# 
names_list_without_vowels = []

# iterate though the names
for name in names_list:
    for vowel in vowels:
        name = name.lower().replace(vowel, "")
    
    # add the modified name to the new list
    names_list_without_vowels.append(name)


#
for name in names_list:
    for letter in name:
        if letter in vowels:
            name = name.replace(letter, "")
    
    # add to the list
    names_list_without_vowels.append(name)

pass