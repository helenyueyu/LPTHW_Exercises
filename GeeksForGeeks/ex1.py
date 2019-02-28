# Python program to print all prime numbers in an interval 

def primes(a,b): 
  for x in range(a, b+1):
    if x > 1:
      for n in range(2, x):
        if (x % n) == 0:
          break
      else:
        print(x)


primes(11, 25)
