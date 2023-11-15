# Define a list containing elements of different data types
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Iterate through each item in the list
for item in myMixedTypeList:
    # Print a formatted string displaying the item and its data type
    print("{} is of the data type {}".format(item, type(item)))
