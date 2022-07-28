#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

#Write your code below this line 👇
import random
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0,2)
if player >= 3 or player < 0:
  print("You enterd a invalid number! You lose")
else:
  li = [rock, paper, scissors]
  print('You choose:\n', li[player], "\n")
  print('Computer choose:\n', li[computer])
  if player == computer:
    print("Tie")
  elif player == 0:
    if computer == 1:
      print('You lose')
    else:
      print('You win')
  elif player == 1:
    if computer == 2:
      print('You lose')
    else:
      print('You win')
  elif player == 2:
    if computer == 0:
      print("You lose")
    else:
      print("You win")


# In[ ]:




