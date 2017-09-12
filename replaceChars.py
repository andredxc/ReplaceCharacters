import sys

def main():

	chars1 = ['á', "à", "é", "í", "ó", "ú", "ã", "ç", "Á", "À", "É", "Í", "Ó", "Ú", "Ã", "Ç"]
	chars2 = ["a", "a", "e", "i", "o", "u", "a", "c", "A", "A", "E", "I", "O", "U", "A", "C", ]
	readChar = ''


	if(len(sys.argv) == 1):
		print("Error, usage: python replaceChars.py <inputFileName>")
		print("Output is saved to NEW<inputFileName>")
		exit()
	else:
		inputFileName = sys.argv[1]
		outputFileName = "NEW" + sys.argv[1]
		inputFile = open(inputFileName, "r")
		outputFile = open(outputFileName, "w")

	while True:
		readChar = inputFile.read(1)
		if readChar:
			if(readChar in chars1):
				#Found character to be replaced
				print("Found character to be replaced\'%c\'"%readChar)
				for index, letter in enumerate(chars1):
					if(letter == readChar):
						outputFile.write(chars2[index])
						print("Wrote \'%c\' to output file" %chars2[index])
			else:
				#Character is not to be replaced
				outputFile.write(readChar)
		else:
			#Reached end of file
			break


	print("Replaced characters wrote to file \'%s\'" %outputFileName)

	inputFile.close()
	outputFile.close()

if __name__ == '__main__':
	main()