def greet():
    print("Hello!")
greet()
greet()

# Parameter and arguments
def greet(name):
    print("Hello", name)
greet("Aisha")

def ask(age):
    print("My age is", age)
ask(18)

# Multiple parameters
def add_numbers(a,b):
    print(a + b)
add_numbers(10,5)

def introduce(name,age):
    print(name, age)
introduce("John", 12)

# Default argument
def greet(name="David",message="Welcome"):
    print(name,message)
greet()
greet("David","Welcome")

# Why Use Default Arguments?
# They make functions flexible while reducing the number of values the caller must provide.
def order_food(food,quantity=1):
    print("food:",food)
    print("quantity:",quantity)
order_food("Pizza")
order_food("burger")
# Important: required parameters normally come before parameters with default values.


def student(name, age=16):          #correct
    print(name, age)

# def student(age=16, name):          #incorrect
#     print(name, age)

# Keyword Arguments
# A keyword argument passes a value by explicitly writing the parameter name.This makes
# function calls easier to read and allows arguments to be supplied in a different order.

def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(age=17, course="Python", name="Tunde")

# Python identifies each value by its parameter name, so the order of these keyword
# arguments does not have to match the definition.

# Positional vs Keyword Arguments
def describe(name, age):
    print(name, age)
describe("Musa", 17)            # positional
describe(name="Musa", age=17)    # keyword

# You can also combine positional and keyword arguments, but positional arguments
# must come first.
def profile(name, age, city):
    print(name, age, city)

profile("Musa", age=17, city="Lagos")


# 5. *args — Accepting Many Positional Arguments
# *args allows a function to accept any number of extra positional arguments.
# Inside the function, args behaves like a tuple.
def add_all(*args):
    total = 0
    for number in args:
      total += number
    return total

print(add_all(2, 4))
print(add_all(1, 2, 3, 4, 5))


# The name args is a convention; the important part is the *.
# You could technically use another name, but *args is the standard and clearest choice.

# Inspecting *args
def show_items(*args):
    print(args)
    print(type(args))

show_items("Pen", "Book", "Bag")

# The output is a tuple containing all positional arguments.

# kwargs Accepting Many Keyword# Arguments
# kwargs allows a function to accept any number of extra keyword arguments.
# Inside the function, kwargs behaves like a dictionary.

def show_profile(**kwargs):
    print(kwargs)

show_profile(name="Sarah", age=18, city="Lagos")
# The keys are the parameter names and the values are the supplied arguments.

# Looping Through **kwargs
def show_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_profile(name="Sarah", age=18, city="Lagos")

# *args and **kwargs Together
def example(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)
example(10, 20, 30, name="John", age=17)
# Here, args collects positional values, while kwargs collects keyword values.


# When Are They Useful?
# They are useful when you do not know in advance how many values a function will receive.
# They are common in reusable libraries, wrappers, decorators, and flexible APIs.

# 7. Return Values
# The return statement sends a result from a function back to the place where the
# function was called. This is different from simply printing a result.
def add(a, b):
    return a + b
result = add(10, 5)
print(result)

# The function calculates 15, returns it, and the returned value is stored in result.

# print() vs return
def add_print(a, b):
    print(a + b)

def add_return(a, b):
        return a + b

x = add_print(2, 3)
y = add_return(2, 3)

print("x =", x)
print("y =", y)

# The first function displays the answer but does not return it, so x becomes None.
# The second returns the answer, so y becomes 5.


# Using a Returned Value in Another Calculation
def square(number):
    return number * number

answer = square(5) + 10
print(answer)

# Because square(5) returns 25, the expression becomes 25 + 10.

# Returning Multiple Values

def calculate(a, b):
    return a + b, a - b

sum_result, difference = calculate(10, 3)
print(sum_result)
print(difference)

# Python packages the returned values together and allows you to unpack them into
# separate variables.


# 8. Scope
# Scope describes where a variable can be accessed in a Python program.
# Understanding scope prevents errors caused by trying to use variables where they
# do not exist.

# Local Scope
# A variable created inside a function normally belongs to that function and is called
# a local variable.

def test():
    message = "Hello"
    print(message)

test()

# print(message)  # NameError
# The variable message exists inside test(), but it is not available outside the function.

# Global Scope
# A variable created outside functions has global scope. Functions can usually read
# a global variable.

school = "Brainpoint College"

def show_school():
    print(school)

show_school()

# The function can read school because it exists in the global scope.


# Local and Global Variables With the Same Name
name = "Global"

def show_name():
    name = "Local"
    print(name)

show_name()
print(name)

# Inside the function, Python uses the local name. Outside the function, the global
# name remains unchanged.

# The global Keyword
# If you deliberately need to change a global variable from inside a function,
# Python provides the global keyword. For beginners, avoid relying heavily on global
# variables; returning values and passing parameters usually produces cleaner programs.

score = 10

def increase_score():
    global score
    score += 5


increase_score()
print(score)
# The global keyword tells Python that score refers to the global variable
# rather than creating a new local variable.


# 9. Putting Everything Together
# The following example combines parameters, a default argument, keyword arguments,
# *args, **kwargs, return values, and local scope.

def student_report(name, age=16, *scores, **details):
    total = sum(scores)
    average = total / len(scores) if scores else 0

    print("Name:", name)
    print("Age:", age)
    print("Average:", average)

    for key, value in details.items():
        print(key, ":", value)
    return average


average = student_report(
"Amina",
    17,
    80, 75, 90,
    class_name="SS2",
    subject="Computer Science"
)

print("Returned average:", average)


# What happens here: name is a normal parameter; age=16 is a default argument;
# the scores are collected by *scores; extra named information is collected by **details;
# average is a local variable; and the average is returned to the caller.


# 10. Quick Comparison

# 11. Common Mistakes to Avoid
# 1. Forgetting required arguments: make sure every required parameter receives a value.
# 2. Putting a required parameter after a default parameter: required parameters
# should come first.
# 3. Confusing print() with return: use return when another part of the program
# needs to use the result.
# 4. Forgetting the * or **: *args and **kwargs have different purposes.
# 5. Trying to use a local variable outside its function: local variables normally
# exist only inside the function.
# 6. Overusing global variables: pass information into functions through parameters
# and send results out with return whenever practical.







































































































