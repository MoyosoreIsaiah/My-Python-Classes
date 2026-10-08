# List is similar to variable only that they can contain multiple values. OR contains
# as many variables as you wish
# List can be iterated over in a every similar manner.

# We create a list using [] "square brackets"
myList = []     # empty  list
myList.append(1)
myList.append(2)
myList.append(3)
print(myList)

print(myList[0])
print(myList[1])
print(myList[2])

# List can contain various/different data types
L = [1, 2.718, 'abc', [5,6,7], False]
# integer, float, str, list, boolean
# A list can contain another list.........Nested list
print(L)
print(L[2])
print(L[4])

# Lists functions

numbers = [1,2,3,4,5,6,7,8]
numbers2 = [3,4,1,0,6,3,3]
# sum
sum_of_num2 = sum(numbers2)
print("The sum of list numbers:", sum(numbers))
print(sum_of_num2)

# len - Gets the total number of values in a list
print("The length of this list is:", len(numbers2))

#min - Gets the minimum value in our list
print("The minimum value in the list:", min(numbers))

# max - Gets the maximum value in our list
print("The minimum value in the list:", max(numbers))

average = sum(numbers)/len(numbers)
print("The average of the list values:", average)

#  There are some functions lists

# Append - Used to add values to the already existing values in our list
names = ["Feyi", "Larry", "Jessie", 'tunde', "Collins"]
ages = [30, 24, 50, 32, 20]
print(names)
print(ages)

names.append("Joy")
ages.append(35)

print(names)
print(ages)

# Sort - Will  arrange the datas in ascending order
names.sort()
print(names)

ages.sort()
print(ages)

# COUNT - count the number of occurrence of a particular value
items = ["Bag", "Ball", "Shoe","dress", "shoe", "bottle water", "shoe"]
print(items.count("shoe"))


fruit = ["mango", "banana", "pineapple","cherry", "avocado","pawpaw", "cabbage", "orange", "watermelon", "pear"]
print(fruit[:])
print(fruit[:5])
print(fruit[5:])
print(fruit[4:8])
print(fruit[2:8:2])
print(fruit[-1])
print(fruit[-5])
print(fruit[::-1])

for i in fruit:
    print(i)

for i in fruit:
    print(i.upper())






