#  MODULES ~ PACKAGES ~ DIRECTORIES ~ FILES


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


##################### Generating Random Numbers ###########################
#google Python 3 packages index and open link with doc.python
#select random numbers package

import random       #no need to specify module or package because its a built in function


for i in range (3):
    print (random.random())                        #picks a default number between 0 and 1
    print(random.randint(10,20))                   #picks a selected range of number betwen in this case 10 and 20


members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice (members)
print (leader)                                      #picks a random item in the list



######################### Exercise ########################
# Write a program that predicts a dice number

# Create a class called Dice
# it should have a method called roll() and everytime we call this method we should get a tuple
 
import random


class Dice:
    def roll(self):
        first = random.randint (1,6)
        last = random.randint (1,6)
        return first, last                            #in python you dont have to return a tuple in parentheses once its not in cluded in () python knows its a tuple


dice1 = Dice ()
print (dice1.roll())


########################## Files and Directories #####################################
from pathlib import Path                    #built in package and class NB uppercase P in Path

# we can use:
# 1. Absolute path eg c:\Program Files\Microsoft
# 2. Relative Path

path = Path ()              #class Path checks current directory for entered argument file namme or directory
#print (path.exists())                 # returns boolean for existance of a directory
#print (path.mkdir())                   #makes directory
#print (path.rmdir())                   #removes directory

for file in path.glob ('*.py'):
    print (file)                            #generates a list of files with the .py extension 
    