import random, string 

def generator():
  letter1 = random.choice(string.ascii_lowercase)
  letter2 = random.choice(string.ascii_lowercase)
  letter3 = random.choice(string.ascii_lowercase)
  letter4 = random.choice(string.ascii_lowercase)
  letter5 = random.choice(string.ascii_lowercase)
  name = letter1+letter2+letter3+letter4+letter5
  return(name)

print(generator())

vowels = 'aeiouy' 
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase 


letter_input_1 = input("Choose a letter, 'v' for vowels, 'c' for consonants, 'l' for other.")
letter_input_2 = input("Choose a letter, 'v' for vowels, 'c' for consonants, 'l' for other.")
letter_input_3 = input("Choose a letter, 'v' for vowels, 'c' for consonants, 'l' for other.")
letter_input_4 = input("Choose a letter, 'v' for vowels, 'c' for consonants, 'l' for other.")
letter_input_5 = input("Choose a letter, 'v' for vowels, 'c' for consonants, 'l' for other.")

if letter_input_1 == "v":
  letter1 = random.choice(vowels)
elif letter_input_2 == "c": 
  letter1 = random.choice(consonants)
elif letter_input_1 == "l":
  letter1 = random.choice(letter)
else:
  letter1 = letter_input_1
