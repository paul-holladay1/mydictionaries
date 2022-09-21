person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]                 #list
person["pets"] = {"dog": "Fido", "cat": "Sox"}                  #dictionary

print(person)                                                   #gets whole dictionary

print(person['children'][1])                     

print(person['pets']['cat'])

# print names of children using for loop

for child in person['children']:
    print(child)


# print out names of dog and cats

for p in person['pets']:
    print(person['pets'][p])