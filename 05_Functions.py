
#=========================================================
#            FUNCTIONS
#=========================================================
"""
Functions are a block of code that is designed to perform a specific task.
Reusable block of code.
"""

## some of built in functions.
print("Hello, World!")
len("Hello, World!")


## DEFINING FUNCTIONS

def greet():  # defining a function with function name 'greet'
    print("Hello, World!")  
    pass # shows that the function doesn't return anything
greet() # Calling the function

# Styling guidelines for function names: lowercase with words separated by underscores as necessary to improve readability.
# functions name shouldn't be ending with digits
def fun1():  # Bad function name
    pass
def Function():  # Bad function name
    pass


### CALLING FUNCTIONS
def say_goodbye():
    print("Goodbye!")

#calling function multiple times
say_goodbye()  # Calling the function
say_goodbye()  # Calling the function again
say_goodbye()  # Calling the function again


def check_weather():
    temperature = 30
    if temperature > 25:
        print("It's hot")
    else:
        print("It's cold")

check_weather()  # Calling the function

## PARAMETERS

# Function with parameter

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")  # Using the parameter in the function


greet(name="Ram") # Calling the function with an argument
greet('Krishna') # Calling the function with an argument


# Function with multiple parameters
def greet(first_name, last_name):  # 'first_name' and 'last_name'
    print(f"Hello, {first_name} {last_name}!")  # Using the parameters in the function

greet(first_name="Ravikiran", last_name="Alabana") # Calling the function with arguments
greet('John', 'Doe') # Calling the function with arguments
greet('Alice')  # This is Error - callign with one argument instead of two


# Position of paramenters
greet("Ravikiran", "Alabana")  # Correct order
greet("Alabana", "Ravikiran")  # Incorrect order, but
greet(last_name="Alabana", first_name="Ravikiran")  # Correct order with keyword arguments
greet(first_name="Ravikiran", last_name="Alabana")  # Correct order with keyword arguments




# Default Parameters
# default parameter should be at the end of the parameter list
def greet(first_name, last_name="Alabana"):  # 'last_name' has a default value
    print(f"Hello, {first_name} {last_name}!")  # Using the parameters in the function

greet("Ravikiran")  # Calling the function with one argument
greet("Ravikiran", "Alabana")  # Calling the function with two arguments
greet("Ramana")
greet("Shivakumari", "Alabana")
greet("Shivakumari")
greet("Prasanna")
greet("Prasanna","G") #parameter overwriting
greet(first_name="Prasanna", last_name="G")  # Calling the function with keyword arguments


## KEYWORD ARGUMENTS
def create_profile(name, age, city):
    print(f"{name}, {age}, from {city}")

# Positional arguments (order matters)
create_profile("Alice", 25, "NYC")

# Keyword arguments (order doesn't matter)
create_profile(city="NYC", age=25, name="Alice")
create_profile(name="Bob", city="LA", age=30)



def calculate_total(price,tax_rate,discount):
    total_price = price + (price * tax_rate) - discount
    print(f"Total price: ${total_price}")

calculate_total(price=100, tax_rate=0.08, discount=10)  # Using keyword arguments




## GLOBAL VS LOCAL VARIABLES

discount = 10
def calculate_total(price):
    
    #Default values
    tax_rate = 0.08
    discount = 10
    
    #Calculation
    tax = tax_rate * price
    final_price = price + (price * tax_rate) - discount

    print(f"Total price: ${final_price}")

calculate_total(price=100)

print(discount) 
'''
The above 'discount' is error --> 
It is local variable

Variable defined inside a function --> LOCAL VARIABLE
Variable defined outside a functionm --> GLOBAL VARIABLE
'''



## RETURNING VALUES
def add_numbers(a, b):
    return a + b  # Returning the sum of a and b
result = add_numbers(a=5, b=3)  # Calling the function and getting the return value

print(f"The sum is: {result}")  # Printing the result


# example
def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft


## Return multiple parameters
def simple_function():
    my_list = [1, 2, 3, 4, 5]
    first_number = my_list[0]
    last_number = my_list[-1]
    return first_number, last_number  # Returning multiple values as a tuple

first, last = simple_function()  # Unpacking the returned tuple into two variables
print(f"First: {first}, Last: {last}")  # First: 1, Last: 3
#=========================================================
#            FUNCTIONS
#=========================================================
