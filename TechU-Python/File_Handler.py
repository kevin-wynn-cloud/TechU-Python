# Import the 'json' module for handling JSON data
import json

# Define a function to read JSON data from a file
def readJsonFile(fileName):
    data = ""  # Initialize a variable to store the JSON data
    try:
        # Attempt to open and read the specified JSON file
        with open(fileName) as json_file:
            data = json.load(json_file)  # Load the JSON data into the 'data' variable
    except IOError:
        print("Could not read file")  # Handle an IOError (e.g., file not found)
    return data  # Return the loaded JSON data (empty string if an error occurred)
