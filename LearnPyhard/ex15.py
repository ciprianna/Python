#Imports the argv module (argument variable)
from sys import argv

#Tells the argv module what needs to be input, here the script to run and the name of a file
script, filename = argv

#Opens the file and assigns that file to "txt" variable
txt = open(filename)

#Prints a string with a raw input then uses the filename unpacked from 
# the argv inputs as the raw input in the string
print "Here's your file %r:" % filename
#Prints the txt variable and tells the text variable to be read
print txt.read()

#Prints a string
print "Type the filename again:"
#Assigns a variable name to the raw_input the user will enter 
# and gives the symbol > to indicate input to the user
file_again = raw_input("> ")

#Assigns a variable name to open the raw_input file the user just entered
txt_again = open(file_again)

#Prints the file the user entered and tells it to be read
print txt_again.read()

txt.close()
txt_again.close()