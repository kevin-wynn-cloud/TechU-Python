# Importing the 'os' module and using it to execute the 'ls' command
import os
os.system("ls")

# Printing a separator line
print("----------------------------------------------------------")

# Importing the 'subprocess' module and using it to run the 'ls' command
import subprocess
subprocess.run(["ls"])

# Printing a separator line
print("----------------------------------------------------------")

# Using 'subprocess' to run the 'ls -l' command
subprocess.run(["ls","-l"])

# Printing a separator line
print("----------------------------------------------------------")

# Using 'subprocess' to run the 'ls -l README.md' command
subprocess.run(["ls","-l","README.md"])

# Printing a separator line
print("----------------------------------------------------------")

# Defining variables for the 'uname' command and its argument, then executing them with 'subprocess'
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])

# Printing a separator line
print("----------------------------------------------------------")

# Defining variables for the 'ps' command and its argument, then executing them with 'subprocess'
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])
