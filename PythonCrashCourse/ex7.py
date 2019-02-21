numbers = list(range(1,6))
print(numbers)

squares = []
for value in range(1, 11): 
  square = value**2
  squares.append(square)

print(squares)
print("The max of the squares is " + str(max(squares)))
print("The min of the squares is " + str(min(squares)))
print("The sum of the squares is " + str(sum(squares)))

increment = [value + 1 for value in range(1, 11)]
print(increment)


