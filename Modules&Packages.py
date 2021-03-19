# Modules are used to organise code in a program making reusable too

import converter   #here we are importing code in the lists module without .py

print (converter.kg_to_lbs(20))               #all defined functions in the Converter module appears


#alternatively we can use this shorter syntax

from converter import kg_to_lbs

print (kg_to_lbs(20))
 
#################### Exercise ########################
'''
numbers = [10,3,6,2]
max = numbers [0]
for number in numbers:
    if number > max:
        max = number
print(max)
'''

# define a function find_max and put it in a seperate module
#import from seperate module and call it from current module and print it on the terminal

numbers = [10,3,6,2]


from references import find_max
max = find_max (numbers)
print (max)



#we also have a built in function in python called maz which does the same job as our code above

# print (max(numbers))
 
################################ PACKAGES ##########################
#Packages contain modules, take modules as files and packages as folders
# a directory is converted to a python package by initiaising the python through creating an __init__ python file


# we can import a whole module from another package or part of the module's procedure


from ecommerce.shipping import calc_shipping  #you can add more functions by using ',' eg calc_shipping,calc_taxing

# or another way of calling a function in a module of a seperate package is:

from ecommerce import shipping
shipping.calc_shipping

