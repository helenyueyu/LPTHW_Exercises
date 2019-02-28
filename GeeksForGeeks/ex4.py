import random 

your_health = 100
opp_health = 100

print("You chose mage! You begin with 100 health")

turn = 0;

while (your_health > 0 and opp_health > 0):
  turn += 1;
  if turn % 2 != 0:
    attack = random.randint(1,10)
    opp_health = opp_health - attack 
    print("Your health is: " + str(your_health))
    print("Your opponent's health is: " + str(opp_health))
  else:
    attack = random.randint(1,10)
    your_health = your_health - attack 
    print("Your health is: " + str(your_health))
    print("Your opponent's health is: " + str(opp_health))

if your_health < 0:
  print("You lose!")

if opp_health < 0:
  print("You win!")


