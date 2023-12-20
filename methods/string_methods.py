greeting = "Bienvenido"
name = "Juan Vidal"

# upper case and lower case
name_upper = name.upper() # upper Case
name_lower = name.lower() # lower Case

# capitalize
capitalize_name = name.capitalize() # first letter in capitalize

# find, serves to find a string into other string
# returns the index of value
# returns -1 when there isn't a value of searching
find_something = name.upper().find("v".upper())

# if is numeric value
# return true or false
is_numeric = name.isnumeric()

# count. search and storage how many times there is something
sentence = f"{greeting}, {name}" # Bienvenido, Juan Vidal
count_sentence = sentence.count("n") # 3, the are 3 letters n

# know the length of something
length_sentece = len(sentence)

# start with and end with, return true or false
start_with_setence = sentence.startswith("B")
end_with_setence = sentence.endswith("l")

# replace a string for another string
# first param to search and second param to replace
new_name = name.replace("Juan", "Carlos")

# split
# returns a list
split_string = sentence.split(" ")
print(split_string)