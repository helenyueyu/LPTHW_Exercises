guest_list = ['Carl', 'Ola', 'Fede', 'Kelly']

for i in guest_list:
  print("Welcome to my home, " + i)
print("I am inviting " + str(len(guest_list)) + " guests for dinner.")


print("Oops, Fede can't make it (cause he's always late).")

guest_list.remove('Fede')
guest_list.append('Udayan')

print("Since Federico can't make it, here's the updated list.")
print("I am inviting " + str(len(guest_list)) + " guests for dinner.")


for i in guest_list:
  print("Welcome to my home, dear friend - " + i)

print("Oops! I forgot a few more people that I'd like to invite.")

guest_list.insert(0, "Harry Potter");
guest_list.insert(len(guest_list) // 2, "Hermione Granger");
guest_list.append("Ronald Weasley");
print("I'm now inviting " + str(len(guest_list)) + " guests for dinner.")


for i in guest_list:
  print("Muggles and non-muggles alike, welcome to my home - " + i)

print("Oops, sorry y'all. I can only invite 2 people for dinner.")
while len(guest_list) > 2: 
  temp = guest_list.pop()
  print("I'm sorry " + temp + ", I can't invite you dinner.")

for i in guest_list:
  print("However, " + i + ", you're still invited!")

del guest_list[0]
del guest_list[0]


print("There is no one left!")
print(guest_list)


