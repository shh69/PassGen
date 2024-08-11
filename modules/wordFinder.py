#Imports: 


#Function01: Creates a dictionary of words, with a number as a key, and the word as the value. 
def wordlistMaker(): 

	with open("data/wordlist.txt", "r") as file: 

		wordList = {}

		for line in file: 

			key,value = line.strip().split(":")
			wordList[key] = value

	return wordList
	

#Function02: Returns a string, after mapping each number of the 'csvNumbers' string, to its key in the 'wordList' dictionary.
def wordFinder(csvNumbers):

	csvNumberList = csvNumbers.split(",")

	mappedWords = []

	for number in csvNumberList: 

		wordList = wordlistMaker()
		mappedWord = wordList.get(number)

		if mappedWord: 

			mappedWords.append(mappedWord)

	return "".join(mappedWords)

