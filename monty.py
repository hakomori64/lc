import random

number = 100000000
change_right = 0
notchange_right = 0
change_incorrect = 0
notchange_incorrect = 0
for i in range(number):
  doors = ['a', 'b', 'c']
  answer_index = random.randint(0, 2)
  answer = doors[answer_index]
  choice1_index = random.randint(0, 2)
  choice1 = doors[choice1_index]
  doors[answer_index] = ""
  opened_door = ""
  while opened_door == "":
    opened_index = random.randint(0, 2)
    opened_door = doors[opened_index]

  doors[answer_index] = answer
  doors[opened_index] = ""

  choice2 = ""
  while choice2 == "":
    choice2_index = random.randint(0, 2)
    choice2 = doors[choice2_index]

  doors[opened_index] = opened_door

  if answer == choice2:
    if choice1 == choice2:
      notchange_right += 1
    else:
      change_right += 1

  if answer != choice2:
    if choice1 == choice2:
      notchange_incorrect += 1
    else:
      change_incorrect += 1

print("Change and correct:", change_right / number)
print("Notchange and correct:", notchange_right / number)
print("Change and incorrect:", change_incorrect / number)
print("Notchange and incorrect:", notchange_incorrect / number)



  



