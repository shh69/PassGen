# Imports: 
import random

# Function01: Recreates a dice roll, and iterates it 5 times, and returns a five digit number.
def diceRoll(): 

	diceRolls = [str(random.randint(1,6)) for i in range(5)]
	diceRollOutput = "".join(diceRolls)

	return diceRollOutput

# Function02: Iterates 'Function01', six times, and returns the output. 
def csvNumbers(): 

	multipleNumbers = [diceRoll() for i in range(6)]
	multipleNumberOutput = ",".join(multipleNumbers)

	return multipleNumberOutput
