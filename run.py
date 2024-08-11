# Imports:
from modules.numberGenerator import csvNumbers
from modules.wordFinder import wordFinder 
from modules.cipherLogic import * 
from modules.loggerLogic import * 

import time 


#Logic:

startTime = time.time()

csvNumbers = csvNumbers()
mappedWords = wordFinder(csvNumbers)
cipheredString = cipherText(mappedWords)
logger(cipheredString)

endTime = time.time()

#Output01:
print(f"\nYour password is: {cipheredString}")

#Output02: 
execTime = round(endTime - startTime, 4)
print(f"The execution of the program took {execTime} seconds.\n")

input("Hit ENTER to close the terminal...")