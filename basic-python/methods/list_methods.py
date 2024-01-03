# len, returns the number of elements in the list
list = ["Hola", True, False, 56]
len_list = len(list) # 4, there are four elements

# append, add elements to a list
# insert the value at the end of the list
list.append("Juan")

# insert, add element in a specific index
list.insert( 0, "Vidal")

# extend, add several values to list
# add the values at the end of the list
list.extend(["Mamita", 45])
print(list)

# pop, delete the last value of the list or delete a value for it index
list.pop()

# remove, delete a value by its value
list.remove("Vidal")

# sort, sort the elemnts
numbers = [34, 1, 45, 98, 0, 3, 65]
numbers.sort() # asc [0, 1, 3, 34, 45, 65, 98]
numbers.sort(reverse=True) # des [98, 65, 45, 34, 3, 1, 0]

# reverse, reverse the content of the list
numbers.reverse()


# clear, delete all elements of the list
list.clear()
print(list)