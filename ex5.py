name = 'Zed A. Shaw'
age = 35
height = 74 
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %r." % name
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# String and Unicode objects have the % operator built in# % is known as the string formatting or interpolation operator
# The effect is similar to using sprintf() in the C language
# Values specified are either single or a tuple

