num1, num2 = raw_input("Enter a number and a divisor.").split()

num1 = int(num1)
num2 = int(num2)

if num2 == 0: 
  raise ValueError('Cannot divide by zero')

if num1 % num2 == 0: 
  print("Divides perfectly!")
else: 
  print("Oops! Still a remainder.")

