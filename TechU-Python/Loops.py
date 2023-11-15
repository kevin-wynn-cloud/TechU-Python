# Prompt the user if they need to ship a package
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Check the user's response and provide appropriate feedback
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

# Prompt the user for their preference: stamps, envelope, or copy
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# Check the user's response and provide corresponding information
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    # If the user wants to make copies, prompt for the number of copies
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    # If the user enters an option other than stamps, envelope, or copy
    print("Thank you, please come again.")
