person = {
    "name": "Juan",
    "last_name": "Vidal",
    "edad": 20
}

# keys, show the keys of a dictionary
print(person.keys())

# get, the value of a specifict key
print(person.get("name"))

# pop, delete a value for its key
person.pop("name")
print(person)

# items, get the single dic, not instance of dic
dic = person.items()
print(dic) 

# clear, delete all elements of a dic
person.clear()
print(person)