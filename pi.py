import sys
import random
import math

def pi(n):
  count = 0
  for i in range(n):
    x = random.random()
    y = random.random()

    if x * x + y * y < 1:
      count += 1

  return count * 4 / n

print("n:", sys.argv[1])
print("円周率:", pi(int(sys.argv[1])))
print("誤差率:", abs(pi(int(sys.argv[1])) - math.pi) / math.pi * 100)
