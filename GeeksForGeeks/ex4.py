import random 

your_health = 100
opp_health = 100

print("You chose mage! You begin with 100 health")

turn = 0;

while (your_health > 0 and opp_health > 0):
  turn += 1;
  if turn % 2 != 0:
    choice = raw_input("Press enter to attack.")
    if choice == "":
      your_attack = random.randint(1,10)
      opp_health -= your_attack
      print("You inflicted " + str(your_attack) + " damage! Your opponent's health is: " + str(opp_health))
    else: 
      print("You ran away!")
      break
  else:
    opp_attack = random.randint(1,10)
    your_health -= opp_attack
    print("Your opponent inflicted " + str(opp_attack) + " damage! Your health is: " + str(your_health))

if your_health < 0:
  print("You lose!")

if opp_health < 0:
  print("You win!")


