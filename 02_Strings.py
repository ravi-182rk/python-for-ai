##Creating Strings

# Single quotes
first = 'Python'

# Double quotes  
second = "Python"

# Triple quotes for multiple lines
paragraph = """This is
a multi-line
string"""


## COMBINING STRINGS


# Concatenation
first_name = "Ravikiran"
Last_name = "Alabana"

full_name = first_name + " " + Last_name

# Using f-strings (modern Python way!)
greeting = f"Hello, {first_name}!"  # "Hello, Jane!"

# Repetition
stars = "*" * 5


## STRING LENGTH

message = 'hello'
len = len(message) #lenght of the string

## CONVERT TO STRING
age = 25
mesasge = 'I am ' + str(age) + ' years old'

# Or use f-strings (we'll learn more later)
message = f"I am {age} years old"

# Multiple variables
age = 25
intro = f"I'm {first_name} and I'm {age} years old"


### STRING METHODS
##Changing case
text = "Python Programming"
print(text.upper())  # "PYTHON PROGRAMMING" 
print(text.lower())  # "python programming"
print(text.title())  # "Python Programming"

## Cleaning strings
messy = "   Hello, World!   "
print(messy.strip())  # "Hello, World!" (removes leading/trailing

price = "$19.4"
print(price.strip("$"))  # "19.4" (removes leading/trailing characters)

## FINDING AND REPLACING
message  = "I love Python programming with python"

#check if something exists
print('python' in message)  # True
print(message.find('Python'))  # 7 (index of first occurrence)
print(message.endswith('python'))  # True

#Find position
print(message.find('Python'))  # 7 (index of first occurrence
print(message.count('python'))  # 2 (number of occurrences)

#Replace
new_message = message.replace('python', 'Java')
print(new_message)  # "I love Python programming with Java  "