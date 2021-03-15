names = [ 'John', 'Milton', 'Simba', 'Cathy', 'Sama']
print (names)
print (names[2])      #prints the third name in the list, starting from index = 0
print (names[-1])       #returns the last name in the list
print (names[2:])        #returns names from index 2 unto the end
print (names[2:4])       #returns names from idex 2 and 3 excluding the foruth


# Modifying lists

names[0]='Jon'      #changes string with index 0 to provided string
print (names)

################# Exercise ######################
# Write a program to find the largest number in a list
numbers = [3,6,9,12,56]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print (max)


################### 2D LISTS ######################

# in math  we have matrices eg:
'''
[
    1 2 3
    4 5 6
    7 8 9
]'''

#this is a 3 x 3 matrix and can be presented  in python as:

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print (matrix [0][1])      #the first row has an index of 0, in that row 2 has the index of 1. thats how elements in a matrix are accessed.

matrix[0][1] = 20           #modifying the elements in the matrix
print (matrix[0][1])



#we can use nested loops to iterate elements in the matrix

for row in matrix:             #in this case row will contain one list as an item
    for item in row:           #we used the nested loop to access individual elements inside the rows
        print (item)



######################  LISTS METHODS/FUNCTIONS ##################

#these are a list of operations you can apply to lists

numbers = [5,2,1,7,4]
numbers.append (20)              #adds an element to the list, with index -1
print (numbers)

numbers.insert (0, 10)               #insert adds an element at a specified index position (index:value to be inserted)
print (numbers)

numbers.remove (5)                #removes 5
print (numbers)

#numbers.clear()                # removes everything in the list, disabled to allow following methods
#print (numbers)

numbers.pop()                 #you can remove the last item in the list
print (numbers)

print(numbers.index(2))        #checks index of the given value

print (1 in numbers)           #checks the existence of given item in a list, returns boolean result

numbers.append(7)      #adding an item 
print (numbers.count(7))         #counts the number of item appearances (=7) in the list

print (numbers.sort())     # returns 'none' which in Python means an absence of a value

numbers.sort()
numbers.reverse()          #in descending order if required
print (numbers)            # no longer returns 'none'

numbers2 = numbers.copy      #self explanatory, useful when manipulating list data without need to change the original list
numbers.append(23)
print (numbers)
print (numbers2)

################## Exercise ###################

#Write a program to remove the duplicates in a list
# My solution

replica = [1,1,2,4,6,7,9,8,8]

'''
replica.sort()

min = 1

for clone in replica:
    if clone > min:
        clone = min
        if clone == min:
            replica.remove (clone)
        
print (replica)'''


## Tutor's solution

uniques = []

for clone in replica:
    if clone not in uniques:
        uniques.append(clone)
print (uniques)



