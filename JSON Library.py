import json


# Create the data dictionary

data = {
    'name': 'Kiki Wu',
    'age':20,
    'city':'Seattle,WA',
    'interests': ['dogs', 'coding', 'foodie'],
    'is_student': True
}

# Writing data to a JSON file
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)


print('Data has been written to data.json')

# Opens JSON file, Reading data from the file
with open('data.json', 'r') as json_file:
  
    # loads the data
    loaded_data = json.load(json_file)

print('Data loaded from data.json')
print(loaded_data)


## Change age to 27, calls interests 
loaded_data['age'] = 27
loaded_data['interests'].append('They secretly let me do what I want because they dont have any other coder')

# Write the modifications to the file
with open('data.json', 'w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('Modified data to the data.json file')
