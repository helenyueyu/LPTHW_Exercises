import random

print("***** RANDOM NUMBER GUESSING GAME *****")
print("\n")
print("I'm thinking of a number between 1-10.")
print("Can you guess it?")

my_number = random.randint(1,10)
your_number = input("Try below: \n")

while (your_number != my_number):
  your_number = input("Try again: \n")

if (your_number == my_number): 
  print("You got it!")


