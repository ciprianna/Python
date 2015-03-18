#Assigns a string with a variable inside to another variable, x, 
# followed by what the variable inside the string should be assigned.
x = "There are %d types of people." %10
#Assigns a string to a variable
binary = "binary"
#Assigns a string to a variable
do_not = "don't"
#Assigns a string to a variable, followed by variables to fill into the string.
# Case 1 of a string inside a string.
y = "Those who know %s and those who %s." %(binary, do_not)
#Prints the string assigned to x
print x
#Prints the string assigned to y
print y
#Prints the string, with a variable x filled in.
# Case 2 of a string inside a string.
print "I said: %r." % x
#Prints the string, with a variable y filled in.
# Case 3 of a string inside a string.
print "I also said: '%s'." % y
#Assigns a binary T/F value to a variable.
hilarious = False
#Assigns a string with a missing variable to another variable.
joke_evaluation = "Isn't that joke so funny?! %r"
#Prints the variables joke_evaluation and uses the variable hilarious to fill into the string.
# Case 4 of a string inside a string.
print joke_evaluation % hilarious
#Assigns a string to a variable
w = "This is the left side of..."
#Assigns a string to a variable
e = "a string with a right side."
#Prints two strings joined together
print w + e