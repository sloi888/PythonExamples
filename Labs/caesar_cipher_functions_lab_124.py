# Double the given alphabet
def getDoubleAlphabet(alphabet):
   doubleAlphabet = alphabet + alphabet
   return doubleAlphabet

# Get a message to encrypt
def getMessage():
   stringToEncrypt = input("Please enter a message to encrypt: ")
   return stringToEncrypt

# Request cipher key from user
def getCipherKey():
   shiftAmount = input( "Please enter a key (whole number from 1-25): ")
   return shiftAmount

# Algorithm to encrypt message
def encryptMessage(message, cipherKey, alphabet):
   encryptedMessage = ""
   uppercaseMessage = ""
   uppercaseMessage = message.upper()
   for currentCharacter in uppercaseMessage:
      position = alphabet.find(currentCharacter)
      newPosition = position + int(cipherKey)
      if currentCharacter in alphabet:
         encryptedMessage = encryptedMessage + alphabet[newPosition]
      else:
         encryptedMessage = encryptedMessage + currentCharacter
   return encryptedMessage

# Decrypt a message
def decryptMessage(message, cipherKey, alphabet):
   decryptKey = -1 * int(cipherKey)
   return encryptMessage(message, decryptKey, alphabet)

# Main function combining all user-defined functions
def runCaesarCipherProgram():
   myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   print(f'Alphabet: {myAlphabet}')
   myAlphabet2 = getDoubleAlphabet(myAlphabet)
   print(f'Alphabet2: {myAlphabet2}')
   myMessage = getMessage()
   print(myMessage)
   myCipherKey = getCipherKey()
   print(myCipherKey)
   myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
   print(f'Encrypted Message: {myEncryptedMessage}')
   myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
   print(f'Decypted Message: {myDecryptedMessage}')

# Call the Main function
runCaesarCipherProgram()