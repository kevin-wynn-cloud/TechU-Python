# Function to duplicate the provided alphabet to create a double alphabet
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Function to get the message to be encrypted from the user
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Function to get the cipher key (shift amount) from the user
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

# Function to encrypt a given message using the Caesar cipher
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()

    # Loop through each character in the uppercase message
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)

        # Check if the character is in the provided alphabet
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            # If not in the alphabet, keep the character unchanged (e.g., space or punctuation)
            encryptedMessage = encryptedMessage + currentCharacter

    return encryptedMessage

# Function to decrypt a given message using the Caesar cipher
def decryptMessage(message, cipherKey, alphabet):
    # To decrypt, use a negative shift (opposite direction)
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Function to run the Caesar cipher program
def runCaesarCipherProgram():
    # Define the standard English alphabet
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Print the original alphabet
    print(f'Alphabet: {myAlphabet}')

    # Create a double alphabet for the Caesar cipher (used for wrap-around)
    myAlphabet2 = getDoubleAlphabet(myAlphabet)

    # Print the double alphabet
    print(f'Alphabet2: {myAlphabet2}')

    # Get the message from the user
    myMessage = getMessage()
    print(myMessage)

    # Get the cipher key from the user
    myCipherKey = getCipherKey()
    print(myCipherKey)

    # Encrypt the message using the Caesar cipher
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    # Decrypt the message using the Caesar cipher
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decrypted Message: {myDecryptedMessage}')

# Run the Caesar cipher program
runCaesarCipherProgram()
