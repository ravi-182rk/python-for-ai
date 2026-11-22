
### Object Oriented Programming 
'''
Object-oriented programming (OOP) is a way to organize code by grouping related data and functions together. Instead of having separate variables and functions scattered around, you bundle them into objects.
'''
### CLASSES
'''
A class is a blueprint for creating objects. It defines:
Attributes: What data the object stores
Methods: What the object can do

'''
# Without classes - data and functions separate
name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    # Process prompt...
    return response

# With classes - everything bundled together
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def generate_response(self, prompt):
        # Process prompt...
        return response