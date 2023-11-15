# Import necessary modules
import csv
import copy

# Define a template vehicle with default values
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Print the default values of the template vehicle
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Create an empty list to store vehicle data
myInventoryList = []

# Open and read a CSV file named 'car_fleet.csv'
with open('files/car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0

    # Iterate through each row in the CSV file
    for row in csvReader:
        # Check if it is the first line (header)
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            # Print the details of each vehicle in the CSV
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            
            # Create a deep copy of the template vehicle
            currentVehicle = copy.deepcopy(myVehicle)

            # Assign values from the CSV to the current vehicle
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = int(row[3])
            currentVehicle["range"] = int(row[4])
            currentVehicle["topSpeed"] = int(row[5])
            currentVehicle["zeroSixty"] = float(row[6])
            currentVehicle["mileage"] = int(row[7])

            # Append the current vehicle to the inventory list
            myInventoryList.append(currentVehicle)

            # Increment the line count
            lineCount += 1

    # Print the total number of lines processed
    print(f'Processed {lineCount} lines.')

# Print details of each vehicle in the inventory list
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
    print("-----")
