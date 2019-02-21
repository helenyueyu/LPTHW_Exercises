MyStack = [] 
StackSize = 3

def DisplayStack(): 
  print("Stack currently contains:")
  for Item in MyStack: 
    print(Item)

def Push(Value): 
  if len(MyStack) < StackSize:
    MyStack.append(Value)
    print("Adding: ", Value)
  else: 
    print("Stack is full!")

def Pop(): 
  if len(MyStack) > 0: 
    print("Popping: ", MyStack.pop())
  else: 
    print("Stack is empty.")

Push('Sherly')
Push('John')
Push('Ms. Huds')
DisplayStack()

Push('Lesty')
Pop()
DisplayStack()

Pop()
Pop()
Pop()

