# Importing a custom module 'File_Handler' that contains a function 'readJsonFile'
import File_Handler

# Reading data from a JSON file using the 'readJsonFile' function from the imported module
data = File_Handler.readJsonFile('files/insulin.json')

# Checking if the data was successfully loaded from the JSON file
if data != "":
    # Extracting specific information about insulin from the loaded JSON data
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    
    # Printing extracted information
    print('bInsulin:', bInsulin)
    print('aInsulin:', aInsulin)
    print('molecularWeightInsulinActual:', molecularWeightInsulinActual)
    
    # Calculating the rough molecular weight of insulin
    aaWeights = data['weights']
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in ['A','C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T','V', 'W', 'Y']}
    
    # Multiply the count by the weights  
    molecularWeightInsulin = sum({x: aaCountInsulin[x] * aaWeights[x] for x in
    ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R','S', 'T', 'V', 'W', 'Y']}.values())
    
    # Printing calculated molecular weight and percent error
    print("The rough molecular weight of insulin:", molecularWeightInsulin)
    print("Percent error:", ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100)
else:
    print("Error. Exiting program")

# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" + \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# Printing "the sequence of human insulin" to the console using successive print() commands:
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Printing to the console using concatenated strings inside the print function (one-liner):
print("The sequence of human insulin, chain a:", aInsulin)

# Calculating the molecular weight of insulin  
# Creating a list of the amino acid (AA) weights  
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Count the number of each amino acid in preproinsulin
aaCountInsulin = {x: float(preproInsulin.upper().count(x)) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}

# Multiply the count by the weights and sum them
molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y'])

print("The rough molecular weight of insulin:", molecularWeightInsulin)

molecularWeightInsulinActual = 5807.63
print("Error percentage:", ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100)