# python match

# The match statement is used to perform
# different actions based on different conditions

# Instead of writing many if....else statement, you can use the match statement

# The match statement selects one of many code blocks to be executed


day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Default value

# Use the underscore character _ as the last case value if you want a code block
# to execute when there are no other matches:

day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the weekend")

# Combine values
# use the pipe character | as an or operator in the case evaluation to check for
# more than one value match in one case:

day = 3
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is weekday")
    case 6 | 7:
        print("I love weekends!")


# If statements as Guards
# You can add if statements in the case evaluation as extra condition_check:

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekend in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekend in May")
    case _:
        print("No match")

num = 48
if num >= 70:
     print("A")
elif num >= 60:
    print("B")
elif num >= 50:
    print("C")
elif num >= 45:
    print("D")
else:
    print("E")

score = 40
match score:
    case x if x >= 70:
        print("A")
    case x if x >= 60:
        print("B")
    case m if m >= 50:
        print("C")
    case _:
        print("E")




