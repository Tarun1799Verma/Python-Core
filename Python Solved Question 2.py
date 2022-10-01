#!/usr/bin/env python
# coding: utf-8

# # Python Solved Question 2

# Q.1 A year is a leap year if it is divisible by 4, except that year
# divisiable by 100 are not leap year unless they are also divisible 
# by 400. Write a program that asks the user for a year and prints out 
# whether it is leap year or not.

# In[1]:


year = int(input("Enter a year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("Yes", year, "is a leap year")
    else:
        print("No", year, "is not a leap year")
elif year % 4 == 0:
    print("Yes", year, "a leap year")
else:
    print("No", year, "is not a leap year")


# Q.2 Write a short program to print first n odd numbers in 
# descending order.

# In[3]:


how_many = int(input("Enter a number: "))
odd = how_many * 2
ls = []
for i in range(1, odd):
    if i % 2 != 0:
        ls.append(i)

ls.reverse()
print(ls)


# Q3. Write a program that accepts a sentence and calculate the number of 
# letters and digits. Suppose the input is supplied to the program:
#  hello world! 123 Then, the output should be: LETTERS 10 and Digits 3.

# In[4]:


sentence = input("Enter your sentence: ")
letters = 0
digits = 0
for i in sentence:
    if i.isalpha() == True:
        letters += 1
    elif i.isdigit() == True:
        digits += 1

print('Letters', letters, "Digits", digits)


# Q4. Write a program that computes the net amount of a bank account based a 
# transaction log from console input. The transaction log format is shown as 
# following: 
# D 100 
# W 200 
# --D means deposit while W means withdrawal. 
# Suppose the input is supplied to the program: 
# D 300
# 
# D 300 
# W 200 
# D 100 
# Then, the output should be: 500 

# In[11]:


Account_Balance = 0

while True:
    yorno = int(input("Enter 1 for continue and 2 for done: "))
    if yorno == 1:
        user_activity, amount = input("Please enter your transaction: ").split()
        if user_activity == 'D':
            Account_Balance += int(amount)
        if user_activity == 'W':
            if Account_Balance <= 0:
                print("Insufficiant Balance")
            else:
                Account_Balance -= int(amount)

    elif yorno == 2:
            print("Your Account Balance",Account_Balance)
            break


# In[ ]:




