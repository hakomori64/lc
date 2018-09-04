while 1:
  pi = 0
  diff = 0
  n = 0
  for i in range(10):
    n = int(input().split()[1])
    pi += float(input().split()[1])
    diff += float(input().split()[1])

  print("n:", n)
  print("pi:", pi / 10)
  print("diff:", 100.0 - diff / 10)
  print("")
