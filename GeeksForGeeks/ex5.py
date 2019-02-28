import random

string = input("Enter your name below: \n")
alias = ""

while (len(string) > 0):
  random_number = random.randint(0, len(string)-1)
  alias += string[random_number]
  string = string[0:random_number] + string[random_number+1:len(string)-1]

print(alias)


