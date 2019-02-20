ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: 
  next_one = more_stuff.pop()
  print "Adding: ", next_one
  stuff.append(next_one)
  print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])


iinclude <bits/stdc++.h>

using namespace std; 

int search(int arr[], int n, int x)
{
  int i; 
  for (i = 0; i < n; i++)
  {
    if (arr[i] == x)
      return i; 
  }
  return -1; 
}

int main() 
{
  int arr[] = {1, 10, 30, 15}; 
  int x = 30; 
  int n = sizeof(arr)/sizeof(arr[0]); 

  getchar(); 
  return 0; 
}


