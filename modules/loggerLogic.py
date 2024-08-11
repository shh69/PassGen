#Imports: 
from datetime import datetime

#Function01: Opens a file, and appends the password generated to it.
def logger(cipheredString): 

	currentTime = datetime.now()
	formattedTime = currentTime.strftime("%m-%d-%y %H:%M:%S")

	with open("data/logs.txt", "a") as file:

		file.write(f"{formattedTime}: {cipheredString}\n") 
