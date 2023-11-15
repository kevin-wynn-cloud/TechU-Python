# Defining a string variable
myString = "This is a string."

# Printing the string
print(myString)

# Printing the data type of the string
print(type(myString))

# Concatenating strings and printing the result along with its data type
print(myString + " is of the data type " + str(type(myString)))

# Concatenating two strings and storing the result in a third variable
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Taking user input for their name
name = input("What is your name? ")
print(name)

# Taking user input for their favorite color and animal, then formatting and printing the result
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name, color, animal))
