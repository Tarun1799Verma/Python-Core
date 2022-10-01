#!/usr/bin/env python
# coding: utf-8

# # Python Questions

# Q.1 Write a program to generate the sequence: -5, 10, -15, 20...... upto n where n is 
#  integer input by user.

# In[1]:


user_input = int(input("Enter a number: "))
a = -1
for i in range(5, user_input + 1, 5):
    print(i * a, end = " ")
    a = a * -1


# Q.2 Write a program to find the sum of 1 + 1/8 + 1/27 + ...1/n**3, where n is the 
# number input by the use.

# In[2]:


user_input = int(input("Enter a value for n: "))
addition = 0
for i in range(1, user_input + 1):
    q = i ** 3
    addition += 1/q
print(addition)


# Q.3 Write a program to find the sum of digits of an integer number, input by the user.
# 

# In[3]:


user_input = (input("Enter a number: "))
input2 = int(user_input)
digit = 0
sum_of_digit = 0
for i in range(len(user_input)):
    digit = input2 % 10
    sum_of_digit += digit
    input2 = input2 // 10
print("sum of digit", sum_of_digit)


# Q.4 Write a program that check wherher an unput number is a palindrome or not(same in
# reverse order).

# In[4]:


user_input = (input("Enter a number: "))
int_input = int(user_input)
input2 = int(user_input)
reverse = 0
for i in range(len(user_input)):
    reverse = (reverse * 10) + input2 % 10
    input2 = input2 // 10

if reverse == int_input:
    print(user_input, "is a palindrome number")
else:
    print(user_input, "is not a palindrome number")


# Q.5 Write a python script that asks user to enter lenght in centimetres. If the user
# enters a negative length the program should tell the user that the entry is invalid.
# Otherwise, the program should convert the length to inches and print out the result. 
# There are 2.54 centimeters in an inch.

# In[6]:


height = float(input("Enter length in centimeters: "))
if height < 0:
    print("Your entry is invalid")
else: 
    inche = height / 2.54
    print("Your height in inches is", inche)    


# In[ ]:




