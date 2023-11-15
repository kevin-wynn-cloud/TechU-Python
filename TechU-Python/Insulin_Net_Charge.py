# Specify the Python version and character encoding
# Store the human preproinsulin sequence in a variable called preproinsulin:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
insulin = bInsulin + aInsulin

# Define the pKa values for different amino acid residues
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Initialize pH value
pH = 0

# Iterate through pH values from 0 to 14
while (pH <= 14):
    # Count occurrences of each amino acid in the insulin sequence
    seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}
    
    # Calculate net charge at the given pH
    netCharge = sum((seqCount[x] * (10 ** pKR[x]) / ((10 ** pH) + (10 ** pKR[x])) for x in ['k', 'h', 'r'])) - sum((seqCount[x] * (10 ** pH) / ((10 ** pH) + (10 ** pKR[x])) for x in ['y', 'c', 'd', 'e']))
    
    # Print pH value and net charge with two decimal places
    print('{0:.2f}'.format(pH), netCharge)
    
    # Increment pH for the next iteration
    pH += 1
