x = "There are %d types of people." % 10 

# Defining x as a string that holds a digit placeholder, to be filled in with 10

binary = "binary"
# Define binary as a string 
do_not = "don't"
# Define don't as another string 
y = "Those who know %s and those who %s." % (binary, do_not)

# Create another string which holds two string placeholders, one for the variable binary and one for the variable do_not
# 2 places (one for x and one for y)

print x 
print y

# Print both of these statements 

print "I said: %r." % x # And one more here
print "I also said: '%s'." % y # And one more here

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious 

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
# Concatenation creates a longer string 
