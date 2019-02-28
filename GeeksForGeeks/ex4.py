import random 

your_health = 100
opp_health = 100
coins = 0
potions = 0

print("#"*50)
print("You chose mage! You begin with 100 health")

turn = 0;

while (your_health > 0 and opp_health > 0):
  turn += 1;
  if turn % 2 != 0:
    choice = raw_input("Press enter to attack.\n Press 'b' to buy a potion.\n Press 't' to take a potion.")
    if choice == "":
      your_attack = random.randint(1,10)
      opp_health -= your_attack
      coins += 1 if (random.randint(1,10) > 5) else 0
      print(str(your_attack) + " damage!")
      print("OPP HEALTH: " + str(opp_health/2*"#"))
      print("GOLD: " + str(coins) + " coins")
    elif choice == 'b':
      if coins >= 10:
        potions += 1
      else: 
        print("You're too poor to purchase potions!")
    elif choice == 't':
      if potions >= 1:
        potions -= 1
        potency = random.randint(10,15)
        your_health += potency
        print("You regained " + str(potency) + " health!") 
    else: 
      print("You ran away!")
      break
  else:
    opp_attack = random.randint(1,10)
    your_health -= opp_attack
    print(str(opp_attack) + " damage!")
    print("YOUR HEALTH: " + str(your_health/2*"#"))

if your_health < 0:
  print("You lose!")

if opp_health < 0:
  print("You win!")



