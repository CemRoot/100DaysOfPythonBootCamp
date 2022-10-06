rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
#Write your code below this line 👇
print("Welcome to Rock Paper Scissors")

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.") )
# This code long way so we can write this shortly 
select = (0,1,2)
pc_choose = random.choice(select)
while 1:
  if choose == 0 and pc_choose == 0:
    print("You choose: ",rock)
    print("PC choose: ", rock)
    print("DRAW")
  elif choose == 0 and pc_choose == 1:
    print("You choose: ",rock)
    print("PC choose: ", paper)
    print("PC WIN")
  elif choose == 0 and pc_choose == 2:
    print("You choose: ",rock)
    print("PC choose: ", scissors)
    print("YOU WIN")
  elif choose == 1 and pc_choose == 0:
    print("You choose: ",paper)
    print("PC choose: ", rock)
    print("YOU WIN")
  elif choose == 1 and pc_choose == 1:
    print("You choose: ",paper)
    print("PC choose: ", paper)
    print("DRAW")
  elif choose == 1 and pc_choose == 2:
    print("You choose: ",paper)
    print("PC choose: ", scissors)
    print("PC WIN")
  elif choose == 2 and pc_choose == 0:
    print("You choose: ",scissors)
    print("PC choose: ", rock)
    print("PC WIN")
  elif choose == 2 and pc_choose == 1:
    print("You choose: ",scissors)
    print("PC choose: ", paper)
    print("YOU WIN")
  elif choose == 2 and pc_choose == 2:
    print("You choose: ",scissors)
    print("PC choose: ", scissors)
    print("DRAW")
  else:
    print("You entered an incorrect number!")
#short code will like this 


