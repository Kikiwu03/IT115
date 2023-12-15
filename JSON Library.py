import json


#Create the data dictionary

data = {
    'name': 'Kiki Wu',
    'age':20,
    'city':'Seattle,WA',
    'interests': ['dogs','coding','foodie']
    'is_student': True
}

# Writing data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

#making changes