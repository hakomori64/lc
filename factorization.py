import math
import sys

factor_array = []

def factorize(number):
  max_number = math.floor(math.sqrt(number))
  for i in range(2, max_number + 1):
    if number % i == 0:
      if not factorize(i):
        factor_array.append(i)

      if not factorize(number // i):
        factor_array.append(number // i)

      return True

  return False

number = int(sys.argv[1])

factorize(number)

for i in factor_array:
  print(i)
