list = []
for i in range(1, 21): 
  list.append(i)
print(list)


list2 = [value for value in range(1,21)]
print(list2)

'''
million = [val for val in range(1, 1000001)]
for number in million: 
  print(number)
'''

million = [val for val in range(1, 1000001)]
print("The max of a million is " + str(max(million)))
print("The min of a million is " + str(min(million)))
print("The sum of a million numbers is " + str(sum(million)))

print("Now I will print the odd numbers from 1 to 20.")
for i in range(1, 21, 2):
  print(i)

print("Now I will print out multiples of 3 from 3 to 30.")
for i in range(3, 31, 3): 
  print(i)

print("Now I will write the first 10 positive cubes.")
for i in range (1, 11): 
  print(i**3)

cubes = [i**3 for i in range(1, 11)]
print(cubes)

