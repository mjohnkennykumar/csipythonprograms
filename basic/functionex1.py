# -*- coding: utf-8 -*-

# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print(str);
   return;

# Now you can call printme function
printme( str = "My string")

def printinfo( name, age ):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age ", age)
   return;

# Now you can call printinfo function
printinfo( age=50, name="miki" )


# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print("Inside the function : ", total);
   return total;

# Now you can call sum function
total = sum( 10, 20 );
print("Outside the function : ", total); 
