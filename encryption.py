from datetime import datetime

class noteInput:
    def __init__(self, textInput):
        self.textInput = textInput
        
    def getInput(self):
        self.textInput = input("Type Text: ")

    def returnText(self, textInput):
        return self.textInput

def encrpytionFunction(text):

    #converts the text string into a list of every letter's ASCII value

    toASCII = list(bytes(text,'ascii'))

    #this gets the current time as an integer 10 digits long and 
    #then puts every digit into an item in a list.

    now = datetime.now()
    ts = int(now.timestamp())
    timeAsList = list(map(int, str(ts)))

    #loop that changes the input string ASCII values based on the time

    x = 0
    timestampItemNumer = 0

    #while length of string 
    while x < len(toASCII):

        #add value from time to text ASCII
        if ( toASCII[x] + timeAsList[timestampItemNumer] ) < 128:
        
            toASCII[x] = toASCII[x] + timeAsList[timestampItemNumer]
            x += 1 
        
        else: 
            x += 1 

        #if the iteration exceeds 10 items revert it back to 0
        if timestampItemNumer >= 9:
           
            timestampItemNumer = 0

        else:

            timestampItemNumer += 1

    #converts the list BACK into a text string and then adds the time number to the front

    reJoinedText = ''.join(map(chr, toASCII))
    return ( str(ts) + reJoinedText )

def decryptionFunction(text):

    #gets the input string and slpits off the time integer 

    testNumber = int(text[0:10])

    inputTime = list(map(int, str(testNumber)))
    inputText = list(bytes(text[10:],'ascii'))

    #loop that changes the input string ASCII values based on the time

    x = 0
    timestampItemNumer = 0

    #while length of string 
    while x < len(inputText):

        #add value from time to text ASCII

        if ( ( inputText[x] - inputTime[timestampItemNumer] ) + inputTime[timestampItemNumer] ) < 128:

            inputText[x] = inputText[x] - inputTime[timestampItemNumer]
            x += 1 

        else: 
            x += 1 

        #if the iteration exceeds 10 items revert it back to 0

        if timestampItemNumer >= 9:
           
            timestampItemNumer = 0

        else:

            timestampItemNumer += 1

    #converts the list BACK into a text string and then adds the time number to the front

    reJoinedText = ''.join(map(chr, inputText))
    
    return reJoinedText

firstInput = noteInput("place_holder")

firstInput.getInput()
print(firstInput.textInput)

encryptedString = encrpytionFunction(firstInput.textInput)
print(encryptedString)

print(decryptionFunction(encryptedString))

