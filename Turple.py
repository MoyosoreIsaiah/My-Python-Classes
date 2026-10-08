# TUPLE
# A tuple is a collection of ordered, immutable elements in python.
# It's similar to a list, but you can't change (modify) the values once defined.
# Tuples are created by placing elements inside parentheses ()


my_tuple = (10, 20, 30)
print(my_tuple)


# You can also have a tuple without a parentheses using just commas:


my_tuple = 10, 20, 30, 40, 50
print(my_tuple)


# Tuple characteristics
# Ordered items have a fixed position
# Immutable: You can't change items after creation
# Allow duplicates
# Can contain diffrent data types

mixed_tuple = (1, "Hello", True, 3.5)
print(mixed_tuple)
print(mixed_tuple[1])
print(type(mixed_tuple[2]))


# Tuple operations
# length: len(my_tuple)
# Count: my_tuple.count(value)
# Index: my_tuple.index(value)
# Slicing: my_tuple[1:3]

example = (5, 10, 15, 20, 10)
print(len(example))               #5
print(example.count(10))          #2
print(example.index(15))          #2
print(example[::-1])              #(10 -5)
print(example[0])                 #5



# Tuple unpacking
# You can assign tuple items to variables directly:


a, b, c = (1, 2, 3)
print(a, b, c)
print(b)
print(c)


grade = (40, 45, 46, 47, 48, 50)
print(grade[3])
grade1, grade2, grade3, grade4, grade5, grade6 = grade
print(grade4)


# Nested tuples
# Tuple can contain  other tuples:

nested = ((1, 2), (3, 4))
print(nested[1][1])         #Output: 4
print(nested[0][1])



# When to use tuple
# When data should not change(e.g. Coordinates, Constant setting).
# When you want faster performance.
# As dictionary keys (tuples are hashable, list are not)

# tuple as dictionary keys
scores = {
    ("Alice", "Math"): 85,
    ("Bob", "Science"): 90,
    ("Alice", "Science"): 88
}

print(scores[("Bob", "Science")])









# Exercise 1
# Tech (Software Licensing Tracker)
# Task: Create a dictionary using
# (user_email, software_name) as keys,
# and store the license expiration date as values.










