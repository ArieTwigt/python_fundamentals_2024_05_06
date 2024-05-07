# Create an object, that is a combination of dictionaries and lists, that contains the family of this person. For each person in the family, store the same attributes as with the first person
person_1 = {"name": "James", 
            "age": 50, 
            "hobbies": ["tennis", "sleeping", "darts"]}

person_2 = {"name": "Mary", 
            "age": 50, 
            "hobbies": ["softball", "running"]}

person_3 = {"name": "Martin", 
            "age": 10, 
            "hobbies": ["gaming", "reading", "darts"]}

person_4 = {"name": "Eric", 
            "age": 8, 
            "hobbies": ["tennis", "sleeping", "darts"]}


# create the family object
family_dict = {}

# add a name to the family
family_dict['name'] = "Jones"

# add members
family_dict['members'] = [person_1, person_2, person_3, person_4]

# 
person_5 = {"name": "bobby", 
            "age": 0,
            "hobbies": ['crying']}

# add the new person to the family dict
family_dict['members'].append(person_5)


# zip
names_list = ['John', 'Jim', 'James']
ages_list = [20, 30, 40]

names_ages = dict(zip(names_list, ages_list))


pass