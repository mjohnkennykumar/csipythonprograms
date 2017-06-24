# -*- coding: utf-8 -*-
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

#concatenation

str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2);

# using *
print('str1 * 3 =', str1 * 3);
     
#iterating through a string
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')  

#string membership test
'a' in 'program'
print("True");
'at' not in 'battle'
print("False");
     
#built in functions to work with python

str = 'cold'

# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate);

#character count
print('len(str) = ', len(str));     
