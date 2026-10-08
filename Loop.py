for i in range(5):
    print("Hello")

for number in [1, 2, 3, 4, 5]:
    print(number)

# Using range() with for loop

for i in range(5):
    print(i)

for x in range(10):
    print(10)


# Different form of range
# range(stop)
for i in range(5):
    print(i)
# produces 0 to 4

# range(start, stop)
for i in range(2, 7):
    print(i)
# produces 2, 3, 4, 5, 6. The stop value 7 is not included

# range(start, stop, step)
for i in range(2, 11, 2):
    print(i)

#     counting backwards
for i in range(5, 0, -1):
    print(i)

# looping through a list
fruits = ["Apples", "Banana", "Carrot"]
for fruit in fruits:
    print(fruit)


# Looping through a string
name = "John"
for letters in name:
    print(letters)



                            #The while loop
# A while loop repeats a block of code as long as its condition is True.

# count = 1
# while count <= 5:
#     print(count)
# count = count + 1

# Break
# To stop he number instantly
for number in range(1, 11):
    if number == 6:
        break
    print(number)

# continue
# to skip the number
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# pass
# To ignore the error
for number in range(5):
    pass

# Nested loops
# A nested loop is a loop inside another loop
for row in range(3):
    for column in range(2):
        print("Row:", row, "column:", column)


# looping with a condition
numbers  = [2, 7, 4, 9, 10]
for i in numbers:
    if i % 2 == 0:
        print(i)






























