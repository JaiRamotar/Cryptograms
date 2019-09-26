# ============================================================
#
# Student Name (as it appears on cuLearn): Jai Ramotar
# Student ID (9 digits in angle brackets): <101094075>
# Course Code (for this current semester): COMP1405B
#
# ============================================================

'''
This is the main function, responsible for the user interface.

@params		none

@return		none

'''
def main():
	
	'''
	This function will load a text file.

	@params		file_name, the name of the file to be loaded

	@return		an uppercase string containing the data read from the file

	'''
#Function to load text file
	def load_text(file_name):

		file_hndl = open(file_name, "r")
		file_data = file_hndl.read()
		file_hndl.close()
		return file_data.upper()

	'''
	This function will save data to a text file.

	@params		file_name, the name of the file to be saved
			file_data, the data to be written to the file

	@return		none

	'''
#Function to save text to a file 
	def save_text(file_name, file_data):

		file_hndl = open(file_name, "w")
		file_hndl.write(file_data)
		file_hndl.close()


	'''
	This function will search the english alphabet for a specific letter, similar to .find() function.

	@params		original_letters, the english alphabet
			letter, letter being searched for in the english alphabet

	@return		index of found letter
	'''
	def search(original_letters, letter):
#Search every letter in english alphabet

		for count in range (len(original_letters)):
#If specified letter is found, return index it is found at

			if original_letters[count] == letter:

				return count

	'''
	This function will encode a phrase into a cryptogram using the provided alphabet.

	@params		original_letters, the english alphabet
			created_alphabet, alphabet created by the user to encrypt the message

	@return		newly encrypted phrase
	'''
		
	def encode(original_phrase, created_alphabet):


		original_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
		new_phrase = ""

#Search every letter in original phrase			 
		for letter in original_phrase:
#If letter in phrase is in the english alphabet, get index of that letter in the english alphabet
			if letter.upper() in original_letters:

				letterIndex = search(original_letters, letter.upper() )
#Find letter in custom alphabet with same index as the orginal letter and add it to the new phrase in the correct casing (or add to new phrase as normal if not a letter)
			if letter.isupper(): 				

				new_phrase += created_alphabet[letterIndex].upper()

			elif letter.islower():

				new_phrase += created_alphabet[letterIndex].lower()
			else:
 	
				new_phrase+= letter

		return new_phrase

	'''
	This function will decode a phrase from a cryptogram to plain english.

	@params		original_phrase, the phrase neeeding to be decoded
			created_alphabet, alphabet created by the user to encrypt the message

	@return		newly decrpyted phrase
	'''

	def decode(original_phrase,created_alphabet):


		original_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
		new_phrase = ""

#Go through every letter in phrase to be decoded			 
		for letter in original_phrase:
#If letter is in custom alphabet, find it's index in the custom alphabet
			if letter.upper() in created_alphabet:

				letterIndex = search(created_alphabet, letter.upper() )
#Find letter in orignal alphabet with same index as the orginal letter and add it to the new phrase in the correct casing (or add to new phrase as normal if not a letter)
			if letter.isupper(): 				

				new_phrase += original_letters[letterIndex].upper()

			elif letter.islower():

				new_phrase += original_letters[letterIndex].lower()
			else:
 	
				new_phrase+= letter

		return new_phrase

	'''
	This function will create a new alphabet for encrpytion by shifting the letters of the alphabet by a user provided amount

	@params		shift, amount of times english alphabet's letters should be shifted to the right 

	@return		newly changed alphabet
	'''

	def caesar_cipher_alphabet(shift):

		

		original_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

		new_alphabet = ""
#Go through each letter in original alphabet
		for letter in original_letters:
#Convert letters to ASCII and change them according to user provided shift value         			
			num = ord(letter)
			num += shift
 #Deals with special cases of letters A and Z             	
			if num > ord("Z"):
				num -= 26
                 		
			elif num < ord("A"):
				num += 26
           			 

			new_alphabet += chr(num)
       
		return new_alphabet

	'''
	This function will create a new alphabet for encrpytion and is created by user input

	@params		none 

	@return		newly changed alphabet
	'''

	def cryptogram_alphabet():

		new_alphabet = ""

		repeat = False

		original_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

		letters = input("Please enter the 26 letters of the English alphabet in any order to create a new alphabet: ")
#Goes through every lettter in user inputted alphabet
	
		for letter in letters:
#If user tries to enter a letter twice, error occurs, otherwise letters are added to a new string 
			num = ord(letter)

			if chr(num) in new_alphabet:

				repeat = True

				break
	
		
			new_alphabet+=chr(num)

#Error checking user inputted alphabet	
		if len(letters)!= 26:

			print("ERROR: Incorrect number of letters found in alphabet (should be 26), regualar alphabet being returned") 

			return original_letters

		elif repeat == True:

			print("ERROR: Duplicate letters found in alphabet, regualar alphabet being returned") 

			return original_letters

		else:

			return new_alphabet.upper() 

	'''
	This function will create a new alphabet for encrpytion and is created by adding a keyword to the beginning and removing all repeat letters.

	@params		keyword, a string that will be used to change the alphabet

	@return		newly changed alphabet
	'''

	def keyword_cipher_alphabet(keyword):

		original_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

		new_keyword = ""
#Go through every letter in the keyword
		for letter in keyword:
#Makes sure keyword is all unique characters
			if letter not in new_keyword:

				new_keyword+= letter

		new_alphabet = new_keyword

#Removes repeating characters from english alphabet and creates new alphabet with keyword
		for letter in original_letters:
	
			num = ord(letter)

	
			for keyword_letters in new_keyword:

				num2= ord(keyword_letters)

				if num == num2:	

					repeat = True
					break

				else:
					repeat = False

			
			if repeat == False:
		
				new_alphabet += chr(num)

		print(new_alphabet)
		return new_alphabet


	initial = ""
	current = ""
	alphabet = ""
	exit = ""

	while True:
#Shows status of initial message and current message		
		if initial == "":

			print("\nThere is no initial unmodified text last loaded by the load function")

		else:

			print("\nThe initial unmofidied text last loaded by the load function is: " + initial)

	
		if current == "":

			print("\nThere is no recently created text")
	
		else:

			print("\nThe most recently created text is: " + current)


		print("")
#Menu options
		option = input("\nPlease enter a letter option for one of the options: \nA. load \nB. save \nC. encode \nD. decode \nE. caesar cipher alphabet \nF. cryptogram alphabet \nG. keyword cipher alphabet \nQ. quit\n ")
#Error checks menu options		
		while option.upper() != "A" and option.upper()!= "B" and option.upper() != "C" and option.upper() != "D" and option.upper() != "E" and option.upper() != "F"and option.upper() != "G" and option.upper() != "Q":

			print("Please enter a valid option from the list: ", end = '')
			option = input()
#Calls load function
		if option.upper() == "A":

			name = input("Please enter a file name: ")

			initial = load_text(name)

#Calls save function			
		elif option.upper() == "B":

			name = input("Please enter a file name: ")

			data = input("Please enter the data to be saved to the file: ")

			save_text(name,data)

#Calls encode function			
		elif option.upper() == "C":
			
			if alphabet == "":

				print("Please create an alphabet for encryption.")

			else:

				if initial == "":

					name = input("Please enter a file name to be loaded as the initial text: ")

					initial = load_text(name)
				
				current = encode(initial,alphabet)

#Calls decode function								
		elif option.upper() == "D":

			if current == "":

				print("Please encode some text first in order to decode text.")

			elif alphabet == "":

				print("Please create an alphabet for decryption.")

			else:

				current = decode(current,alphabet)
#Calls caesar cipher alphabet function
							
		elif option.upper() == "E":


			shift = int(input("Please enter an integer to shift the alphabet: "))

			alphabet = caesar_cipher_alphabet(shift)
#Calls cryptogram alphabet function
			
		elif option.upper() == "F":

			alphabet = cryptogram_alphabet()
#Calls keyword cipher alphabet function	
			
		elif option.upper() == "G":

			keyword = input("Please enter a keyword for creating the new alphabet: ")

			alphabet = keyword_cipher_alphabet(keyword.upper())

#Quits program			exit = input("Keep going? (Y/N) ").upper()

		elif option.upper() == "Q":

			break
#Call main function to run the whole program	
main()





	