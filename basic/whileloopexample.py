# -*- coding: utf-8 -*-
# Program to add natural
# numbers upto 
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

num = int(input("Enter a number: "))

# initialize sum and counter
sum = 0
i = 1

while i <= num:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum);
