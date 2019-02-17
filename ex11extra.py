print (30 * '-')
print ("     M A I N - M E N U")
print (30 * '-')
print ("1. Backup")
print ("2. User management.")
print ("3. Reboot the server")

choice = raw_input('Enter your choice [1-3] : ')

choice = int(choice)

if choice == 1:
  print ("Starting backup...")
elif choice == 2: 
  print ("Starting user management...")
elif choice == 3: 
  print ("Rebooting the server...")
else: 
  print ("Invalid number. Try again...")
