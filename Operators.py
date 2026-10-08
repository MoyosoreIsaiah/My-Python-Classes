# Operators allows us to perform operations
from operator import truediv

# Types of operators
# 1. arithmetic operators
# 2. comparison operators
# 3. logical operators

# 1. Arithmetic operators
# + addition
# - subtraction
# * multiplication
# / division
# // floor division
#  % modulus
# ** exponent


# 2. Comparison operators
# == equals
# != not equals
# < less than
# > greater than
# <= less than or equals
# >= greater than or equals


# 3. Logical operators
# and
# or
# not

# Arithmetic operators

# this are mathematical symbol that are used to perform operators
num1 = 20
num2 = 10
print(num1 + num2)
num1 = 20
num2 = 10
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

# 2. comparison operators

# they compare two values and evaluate to a boolean result(true or false)
# == equals
# != not equals
# < less than
# > greater than
# <= less than or equals
# >= greater than or equals

# greater than
age = 18
print(age >18)

# less than
print(age <18)

# not equals
print(age !=18)

# less than or equals
print(age <=18)

# greater than or equals
print(age >=18)

# logical operators
# and
# or
# not

# and operator
# returns true only for the "and" operator to return true both conditions must be true

driver_age = 18
driver_license = True

# both must be true
can_drive = (age >= 18) and driver_license
print(can_drive)

admin = True
employed = False
granted = admin and employed
print(granted)

#  or operator
#  for the "or" operator one of the statement must be true

is_weekend = False
is_holiday = True

can_relax = is_weekend or is_holiday
print(can_relax)

# not operator
# the "not" operator flips the boolean false to true

is_raining = True
go_outside = not is_raining
print(go_outside)

name = "moyo"
print(name)