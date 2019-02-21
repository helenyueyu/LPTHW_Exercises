characters = ['Sherlock', 'John', 'Molly', 'Mrs. Hudson']
print(characters)

characters.append('Moriarty')
print(characters)

characters[0] = 'Irene'
print(characters)

characters.insert(0, 'Detective Lestrade')
print(characters)

del characters[0]
print(characters)

popped_character = characters.pop()
print(characters)
print(popped_character)

first_char_left = characters.pop(0)
print(characters)
print(first_char_left)


john = characters.remove('John')
print("Since Sherlock is no longer here, John must also be on a mystery hunt!")
print(characters)

