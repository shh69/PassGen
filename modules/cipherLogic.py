#Imports: 
import random
import string 

#Function01: Replaces random characters, with the 
def cipherText(mappedWords):

	specialChar = string.punctuation + string.digits
	cipheredString = ""

	for char in mappedWords: 

		if random.random() < 0.30:

			cipheredString += random.choice(specialChar)

		else: 

			cipheredString += char

	return cipheredString


