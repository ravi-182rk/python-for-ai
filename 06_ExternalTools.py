'''
Beyond built-in Python
Python comes with many built-in functions, but its real power comes from external packages. These are pre-written code libraries that add new capabilities.


Python’s ecosystem :
-----------------------
Python has packages for everything:
Web scraping: Extract data from websites
Data analysis: Process spreadsheets and databases
AI/ML: Build intelligent applications
APIs: Connect to online services
Automation: Control your computer




Using packages:
-----------------
Python packages add new functionality to your programs. There are two types:

Built-in: Come with Python (no installation needed)
External: Need to install first with pip



Understanding the terminology:
---------------------------------
Let’s clarify what these terms mean:

Module:     A single Python file (like math.py)
Package:    A folder containing multiple modules
Function:   A reusable block of code (like print() or sqrt())
Class:      A blueprint for creating objects (we’ll cover this later)



    '''

### IMPORTING PATTERNS

# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)
math.sqrt(16)



# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)
sqrt(16)


## Built-in modules

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])


##Common built-in modules

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)


## Import Methods

# Import entire module
import math
result = math.sqrt(16)

# Import specific functions
from math import sqrt, pi
result = sqrt(16)
circle_area = pi * radius ** 2

# Import with alias
import pandas as pd
df = pd.DataFrame(data)

# Import everything (avoid this!)
from math import *



## Installing packages.
# Install a package
pip install requests

# Install specific version
pip install requests==2.28.0

# Install multiple packages
pip install pandas numpy matplotlib


#=======================================================
###  Sharing your project: requirements.txt

#=======================================================

'''
When you share your Python project, others need to know which packages to install. The standard way is using a requirements.txt file:
Creating requirements.txt

List all your project’s packages:

    pip freeze > requirements.txt


This creates a file like:

    certifi==2024.2.2
    charset-normalizer==3.3.2
    idna==3.6
    requests==2.31.0
    urllib3==2.2.0




### Finding Package


Finding packages
Where to find packages:
PyPI - Official Python package index
Awesome Python - Curated list
ChatGPT - Ask “What Python package should I use for [task]?” - Great for recommendations and comparisons
Google “Python package for [task]”



'''


### Working with API

'''

An API (Application Programming Interface) is like a waiter at a restaurant. You tell it what you want, and it brings you the data.
But APIs do more than just fetch information. They’re the bridges that connect your code to other systems. With APIs, you can:
Pull customer data from your CRM (Salesforce, HubSpot)
Get order information from Shopify or WooCommerce
Send messages through Slack or email services
Use AI models from OpenAI or Anthropic
In the context of AI, APIs are essential. They let you connect AI capabilities to real business data and systems.



'''

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

#print data type of 'data'
print(type(data))  # <class 'dict'>

print(data)

data.keys()

temparature = data['current']['temperature_2m']  # Access the 'current' key in the dictionary




# extracting data from API

import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)

print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")