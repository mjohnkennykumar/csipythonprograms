# -*- coding: utf-8 -*-
#python has five major datatypes
#Numbers
#String
#List
#Tuple
#Dictionary

#examples for number datatype
var1=10
var2=12.00
print(var1);
print(var2);

#string datatype     
str = 'Hello World!'

print(str);          # Prints complete string
print(str[0]);       # Prints first character of the string
print(str[2:5]);     # Prints characters starting from 3rd to 5th
print(str[2:]);      # Prints string starting from 3rd character
print(str * 2);      # Prints string two times
print(str + "TEST"); # Prints concatenated string   

#list datatype

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
list[2]=10.0

print(list);          # Prints complete list
print(list[0]);       # Prints first element of the list
print(list[1:3]);     # Prints elements starting from 2nd till 3rd 
print(list[2:]);      # Prints elements starting from 3rd element
print(tinylist * 2);  # Prints list two times
print(list + tinylist); # Prints concatenated lists  
print(list[2]);     #list can be updated

#dictionary datatype

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print(dict['one']);       # Prints value for 'one' key
print(dict[2]);           # Prints value for 2 key
print(tinydict);          # Prints complete dictionary
print(tinydict.keys());   # Prints all the keys
print(tinydict.values()); # Prints all the values