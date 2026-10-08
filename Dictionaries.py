# Dictionary
# Dictionaries are used to store data values in key: value pairs.
# A dictionary is a collection which is stored, changeable, and do not allow duplicates

# Dictionaries are written in curly brackets, and have keys and values:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
print(thisdict["brand"])


print(thisdict)

# Dictionary length
# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# Dictionary data types
# The values in dictionary items can be of any data type:


vehicle = {
    "brand": "Toyota",
    "electric": False,
    "year": 1965,
    "colors": ["silver", "black", "wine"]
}

# using the dict() constructor method to make a dictionary:

thisdict = dict(name="john", age=36, country="Norway")
print(thisdict)

# Accessing items
# You can access the items of a dictionary by referring to it's key name,
# Inside square brackets:

car = {
    "brand": "Lambhorghini",
    "model": "Revuelto",
    "year": 2025
}
x = car["model"]
print(x)

y = car["year"]
print(y)

z = car["brand"]
print(z)

# There is also a method called get() that will give you the same result:

y = car.get("model")
print(y)

# Get keys
# The keys() method will return a list of all the keys in the dictionary.
x = car.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets
# updated as well:

phone = {
    "brand": "Apple",
    "model": "iphone 15 pro max",
    "year": 2024
}

x = phone.keys()
print(x)    #before the change

phone["color"] = "pink"    #Value to our dictionary
print(phone)
print(x)  #After change


# Get values
# The values() method will return a list of all the values in the dictionary

print(phone)
x = phone.values()
y = phone.keys()

print(x)
print(y)

# Change values

# You can also change  the value of a specific item by referring to its key name:

house = {
    "type": "Bungalow",
    "color": "Brown",
    "rooms": 3
}

print(house)

house["color"]="White"
print(house)

#  Update dictionary
#  The update() method will update the dictionary with the items from the given argument

# The argument must be a dictionary, or an iterable object with key: value pairs,
# Update the "rooms" of the house by using the update() method:

house.update({"rooms":5})
print(house)

# Removing items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:
house.pop("type")
print(house)

# The popitems() method removes the last inserted item
house.popitem()
print(house)


# The del keyword removes the item with the specified key name:
print(vehicle)
del vehicle["brand"]
print(vehicle)
# The del keyword can also delete the dictionary completely:
del vehicle
# print(vehicle)    # this will cause an error because "vehicle" no longer exist

# The clear() method empties the dictionary
print(car)
car.clear()
print(car)

# Copy a dictionary
# dict1 = dict2 -- Won't work
# The copy() method
thisdict = {
    "name": "Feyi",
    "Courses": ["HTML", "CSS", "JAVASCRIPT", "PYTHON"]
}

print(thisdict)
mydict = thisdict.copy()
print(mydict)

thisdict["Courses"].append("SQL")
print(thisdict)
print(mydict)

# Nested Dictionaries
myFamily =  {
    "child1":{
        "name":"Emil",
        "year":2004
    },

    "child2":{
        "name":"Tobias",
        "year":2007
    },

    "child3":{
        "name":"Linus",
        "year":2011
    },
}

child1 = {
    "name":"Emil",
    "year":2004
}

child2 = {
        "name":"Tobias",
        "year":2007
}

child3 = {
        "name":"Linus",
        "year":2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myFamily)
print(myfamily)


# Access items in Nested Dictionaries
print(myFamily["child2"]["name"])



# Dictionaries Methods
# clear(): Removes all the elements from a dictionary
# copy(): Returns a copy of the dictionary
# fromkeys(): Returns a dictionary with the specified keys and value
# get(): Returns the value of the specified key
# items(): Returns a list containing a tuple for each key value pair
# keys(): Returns a list containing the dictionary's key
# pop(): Removes the element with the specified key
# popitem(): Removes the last inserted key-value pair














