try :
    result = 10/0 #Zerodivision error
except:
    print('Hi there')


# This keeps running even if file doesn't exist

import os

try:
    
    with open('data.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Could not find data.txt")
    content = "default data"
print("Done!")  # Always reaches here