# Data structures to store multiple values.
# these are continer
"""
Types of Data structues used:

Lists: Like a shopping list (ordered items)
Dictionaries: Like a phone book (name > number)
Tuples: Like coordinates (fixed values)
Sets: Like a bag of unique items


"""

## LISTS

my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)

""" List can hold multiple data types
"""
my_list = [1, "hello", 3.14, True]

for i in my_list:
    print(i)

# Accessing items
age = 25
has_license = False
my_list = ["Ravikiran",25,age,True,has_license]

my_list[0]
my_list[1]

my_list[-1]
my_list[-2]

fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])    # "apple" (first item)
print(fruits[1])    # "banana"
print(fruits[-1])   # "orange" (last item)
print(fruits[-2])   # "banana" (second to last)

# Slicing
print(fruits[0:2])  # ["apple", "banana"]
print(fruits[1:])   # ["banana", "orange"]

#Changing lists | overwriting list

fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")      # Add to end
print(fruits)
fruits.insert(1, "kiwi")    # Insert at position
print(fruits)
# Remove items
fruits.remove("banana")     # Remove by value
print(fruits)
last = fruits.pop()        # Remove and return last
print(fruits)
print(last)                # "grape"
del fruits[0]              # Remove by index
print(fruits)






numbers = [3, 1, 4, 1, 5, 9]

#lenght of array

array_lengh = len(numbers) # 6

# Information
print(len(numbers))         # 6 (length)
print(numbers.count(1))     # 2 (count occurrences)
print(numbers.index(4))     # 2 (find position)

# Sorting
numbers.sort()              # Sort in place
print(numbers)              # [1, 1, 3, 4, 5, 9]

numbers.reverse()           # Reverse order
print(numbers)              # [9, 5, 4, 3, 1, 1]

# Copy
new_list = numbers.copy()   # Create a copy

#=======================================
### DICTIONARIES
#=======================================

# Stores data in key:value pair
person = {
    "name": "Ravikiran",
    "age": 25,
    "city": "Hyderabad",
    "is_student": True
}
person
print(person["name"])  # "Ravikiran"
print(person("age"))  # 25  
print(person["city"])  # "Hyderabad"
print(person["is_student"])  # True


## CREATING DICTIONARIES
# Empty dictionary
my_dict = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Different ways to create
scores = dict(math=95, english=87, science=92)

my_dict['status'] = 'active'

## Accessing values
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get values by key
print(person["name"])       # "Alice"
print(person["age"])        # 30

# Safer with get()
print(person.get("job"))    # None (no error)
print(person.get("job", "Unknown"))  # "Unknown" (default)

## Modifying dictionaries
person = {"name": "Alice", "age": 30}

# Add or update
person["email"] = "alice@email.com"  # Add new
print(person)  # {"name": "Alice", "age": 30, "email": "
person["age"] = 31                   # Update existing
print(person)  # {"name": "Alice", "age": 31, "email": "
# Remove items
del person["email"]   # Remove by key
print(person)
age = person.pop("age") 
print(person)
print(age)         # Remove and return
person.clear()         # Remove all items
print(person)

## Dictionaries methods
person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})
person

#=============================================================
### TUPLES
#=============================================================

# Tupels are immutale. They are listis which can't be changed

## Creating tuples
# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")


# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20

## Accessing items
point = (3, 5)
colors = ("red", "green", "blue")

# Get items
print(point[0])      # 3
print(colors[-1])    # "blue"

# Slicing works too
print(colors[0:2])   # ("red", "green")

## Tuple unpacking
# Unpack values
point = (3, 5)
x, y = point  # x = 3, y = 5

# Multiple assignment
a, b, c = 1, 2, 3  # Same as (1, 2, 3)

# Swap variables elegantly
x, y = y, x  # Swaps values!

#=============================================================
### SETS
#=============================================================

# Work with unique collections

## CREATING SETS
# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}
