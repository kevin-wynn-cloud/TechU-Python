         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

This list comprises some lab activities done during the TechU Python module. 

# Caesar Cipher 
This program demonstrates a simple Caesar cipher encryption and decryption. The getDoubleAlphabet function is used to create a double alphabet, which is needed for handling wrap-around when shifting characters in the encryption process. The user is prompted to enter a message and a cipher key, and the program then encrypts and decrypts the message using the Caesar cipher algorithm.

# Categorizing Values
For each iteration of the loop, it prints a message indicating what the item is and what data type it belongs to. This is a simple way to inspect and display the data types of elements in a mixed-type list.

# Composite Data
The code initializes a template vehicle called myVehicle with default values for various attributes like VIN, make, model, year, range, top speed, zero to sixty acceleration time, and mileage. It then prints the default values of this template vehicle. Subsequently, the code reads data from a CSV file named 'car_fleet.csv' that presumably contains information about different vehicles. For each row in the CSV file, it prints the details of the vehicles, extracts the information, creates a copy of the template vehicle, assigns the values from the CSV to the corresponding attributes of the copied vehicle, and appends it to the myInventoryList. Lastly, it iterates through the list of vehicles in myInventoryList, printing the details of each vehicle in a formatted manner, separated by dashes for clarity. This script serves as a basic demonstration of reading CSV data into Python dictionaries and managing a list of structured data.

# Conditionals
The code is a simple interactive game called "Guess the Number." The program generates a random number between 1 and 10 using the random module. The user is prompted to guess the number through a loop, and the program provides feedback on whether the guess is correct or not. If the user correctly guesses the randomly generated number, a winning message is displayed, and the loop terminates. 

# File Handler
The given Python code defines a function named 'readJsonFile' that reads JSON data from a specified file. The 'json' module is imported to facilitate handling JSON data. Inside the function, a variable 'data' is initialized to store the JSON content. A try-except block is employed to handle potential errors, particularly an IOError that may occur if the specified file cannot be opened or read. The function then returns the loaded JSON data if successful, or an empty string if an error occurred during the file reading process.

#Insulin Net Charge
This Python script analyzes the net charge of a human insulin sequence at different pH levels. The amino acid sequence of human preproinsulin, along with specific segments denoted as lsInsulin, bInsulin, and aInsulin, is defined. Additionally, pKa values for relevant amino acid residues are stored in the pKR dictionary. The script then iterates through pH values from 0 to 14 using a 'while' loop. Inside the loop, it counts the occurrences of key amino acids in the insulin sequence and calculates the net charge based on the Henderson-Hasselbalch equation. The results, consisting of pH values and corresponding net charges, are printed with two decimal places. This analysis aids in understanding how changes in pH impact the charge distribution of the insulin molecule, providing insights into its biochemical behavior under different environmental conditions.

# Lists, Tuples, Dictionaries
The provided Python script demonstrates the usage of lists, tuples, and dictionaries to organize and manipulate data. Firstly, a list named myFruitList is created to store three fruit names, followed by prints displaying the entire list, its data type, and individual elements. The script then modifies an element in the list and prints the updated version. Next, a tuple named myFinalAnswerTuple is defined with three fruit names, and similar to the list, the entire tuple, its data type, and individual elements are printed. Lastly, a dictionary named myFavoriteFruitDictionary is created, associating individuals ("Akua," "Saanvi," and "Paulo") with their favorite fruits. The script prints the dictionary, its data type, and accesses specific entries using keys.

# Loops
This script engages with the user through a series of prompts and provides tailored responses based on their input. Initially, the user is asked if they need to ship a package, and the script responds accordingly. If the user expresses a need for shipping, a message assures assistance; otherwise, a polite prompt encourages them to return when they do require shipping services. Subsequently, the script inquires about the user's specific needs among buying stamps, purchasing an envelope, or making a copy. Depending on the response, it provides relevant information about stamp designs, available envelope sizes, or prompts for the number of copies desired. The script concludes with a friendly message if the user enters an option other than the provided choices.

# Numeric Data Types
This script provides a concise demonstration of basic variable assignments and dynamic typing in the language. It begins by printing a "Hello, World" message and then showcases a variable named myValue taking on different data types. The variable is initially assigned an integer (1), and its value, data type, and a concatenated message are printed. Subsequently, the variable is updated to a float (3.14), then to a complex number (5j), and finally to a boolean (True), with each change being accompanied by corresponding print statements. 

# Numeric Weight
This script performs several tasks related to the analysis of insulin data. It imports a custom module, 'File_Handler', which contains a function named 'readJsonFile' to read data from a JSON file ('files/insulin.json'). The script then checks if the data was successfully loaded and extracts specific information about insulin, including the sequences of its chain components (bInsulin and aInsulin) and the actual molecular weight. It calculates the rough molecular weight of insulin based on the count of amino acids and their corresponding weights. The script prints relevant information, such as the sequences and molecular weights, and calculates the percentage error between the calculated and actual molecular weights. Additionally, it stores and prints the sequences of human preproinsulin and specific chain elements of insulin.

# String Data
The code involves string manipulation and user input. It begins by defining a string variable, myString, and prints its content. The script then prints the data type of myString and concatenates it with additional text describing its data type. The next section concatenates two strings, "water" and "fall," storing the result in a variable called thirdString and printing it. Subsequently, the code prompts the user for their name, stores the input in the variable name, and prints it. Similarly, it prompts the user for their favorite color and animal, then formats and prints a message using the entered values. 

# System Admin
This Python utilizes the 'os' and 'subprocess' modules to execute various system commands. The 'os.system("ls")' command is used to run the 'ls' command, which lists the files in the current directory. Subsequently, the 'subprocess.run(["ls"])' and 'subprocess.run(["ls","-l"])' commands demonstrate using the 'subprocess' module to run the 'ls' command and 'ls -l' command, respectively. The script also showcases running commands with specific arguments, such as 'ls -l README.md'. Additionally, the 'uname -a' command and 'ps -x' command are executed using variables to specify the command and its arguments, providing system information and active process information, respectively.

