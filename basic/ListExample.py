# -*- coding: utf-8 -*-
my_list = [1, "Hello", 3.4]
print(my_list[1]);
print(my_list[2]);

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][1])    

# Output: 5
print(n_list[1][3])   

my_list = ['p','r','o','g','r','a','m','i','z']
# elements 3rd to 5th
print(my_list[2:5])

# elements beginning to 4th
print(my_list[:-6])

# elements 6th to end
print(my_list[5:])

# elements beginning to end
print(my_list[:])  

# mistake values
odd = [2, 4, 6, 8]

# change the 1st item    
odd[0] = 1            

# Output: [1, 4, 6, 8]
print(odd)

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]  

# Output: [1, 3, 5, 7]
print(odd)  
