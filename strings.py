#What is a string?
# A string is a sequence of character enclosed in quotes
# Think of it as text in your program

# Types of string
# 1. single-quotes ('')
# 2. Double-quotes ("")
# 3. multiline-quotes (""")

# Single-quotes
text1 = 'Hello'

# Double-quotes
text2 = "Its a beautiful day"

# Triple quotes (for multiline text)
text3 = """this is line 1
this is line 2
this is line 3"""

# String operations
# 1. Concatenation (Joining strings)
first = "Hello"
last = "world"
full = first + " " + last
print(full)

# 2. Repetition

echo = "Ha" * 3
print(echo)

fame = "Yum" * 2
print(fame)

# length (counting character)
text = "Python"
length = len(text)
print(length)

name = "Moyosore"
length = len(name)
print(length)

# Accessing characters (Indexing)
# Python uses 0-based indexing - the first character is at position 0

word = "python"
# Index:     0 1 2 3 4 5
# character: p y t h o n

print(word[0])
print(word[3])
print(word[-1])
print(word[-2])

# Escape characters
# Special characters that start with backslash \:

print("Hello\nWorld")    #New line
print("Hello\tWorld")    #Tab
print("She said \"Hello\"") #She said "Hello"
print("It\'s raining")    #It's raining
print("C:\\Users\\Name")  #C:\Users\Name (backslash)
print("Hello\bWorld")     #Backspace (Hellworld)


    # String formatting
name = "Alice"
age = 25
print(f"Hello {name}, you are {age} years old")
print(f"Next year you'll be {age + 1}")
#
sport = "football"
ID = "John"
print("My name is " + ID + ", i love " + sport)
print(f"My name is {ID}, i love {sport}")

name = "Bob"
age = 30
print("Hello {}, you are {} years old".format(name, age))
print("Hello {0}, you are {1} years old".format(name, age))

# % Formatting (Old style)
name = "Charlie"
age  = 35
print("Hello %s, you are %d" % (name,age))

        # Checking if string contains something
text = "Hello World"
print("World" in text)   #True
print("Python" in text)   #False
print("Hello" not in text)   #False

# case-insensitive check
print(text.lower().find("world")) # 6 (converts to lowercase first)

# Create an email validator and
# password strength checker
# at least 8 characters must contain numbers, uppercase and lowercase

email = str(input("Enter your email address "))
if "@" in email and ".com" :
    print("Valid email")
else:
    print("Invalid email")

correct_password = input("Enter your password ")
if len(correct_password) < 8:
    print("Weak password")
elif len(correct_password) >= 8:
    print("strong password")


password = input("Enter your password ")

if password.isupper():
    print("Password must contain lowercase, uppercase and digits")
elif password.islower():
    print("Password must contain lowercase, uppercase and digits")
elif password.isdigit():
    print("Password must contain lowercase, uppercase and digits")
else:
    print("Access granted")










