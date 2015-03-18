#Assigns variable with four more variables to fill in within a string as raw outputs.
formatter = "%r %r %r %r"
#Prints the variable with numbers assigned within the string...still prints as numbers because %r
print formatter % (1, 2, 3, 4)
#Prints the variable with strings inside the string.
print formatter % ("one", "two", "three", "four")
#Prints the variable with boolean values.
print formatter % (True, False, False, True)
#Prints the variable with the variable filled in...without variables assigned to all the variables.
print formatter % (formatter, formatter, formatter, formatter)
#Prints the variable with four string sentences filled in as a single row.
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)