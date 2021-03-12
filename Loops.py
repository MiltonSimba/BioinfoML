############################## WHILE LOOPS #################################

#while <condition>:
# ....         'Whilst the condition is true the .... code will be executed.
i = 1     #i is short for index
while i <=5:
  print (i)
  i=i+1
print ('Done')

#making things more interesting
i = 1    
while i <=5:
  print ('*' * i)
  i=i+1
print ('Interestingly Done')

################# Exercise ###############
#Guessing Game

#My Solution, which did not work because i hadn't been introduced to the other terms

'''i = 1

while i<=3:
    secret_number = input (int('Guess the number: '))
    if secret_number = 9:
       print ("You've won")
    else:
        print("Try Again")
       i=i+1
    print ("You've used all your chances")'''

secret_number=9
guess_count=0
guess_limit = 3

while guess_count<guess_limit:
    guess = int (input('Guess: '))
    guess_count+=1
    if guess == secret_number:
        print ("You won")
        break       #the keyword 'break' breaks the loop in case the user got the secret number there wont be need to re-ask
    
else: 
    print ('Sorry you failed')                     #in python the 'while: ' loop can get its own else like 'if'

##################### Car Game ####################
'''Make a program which starts, stops, quit a car. when the user inputs
>help 
start - to start the car
stop - to stop the car
quit - to exit

>asd    #thats an unknown command
I dont understand that...
>start 
Car started...Ready to go!
>stop
Car stopped.
>quit      #exits the application'''

#My solution
car = input ('> ')      #car is a variable that stores the given command by the user
while car != "":
    if car.lower()=='start':
         print ('Car started')
         break
    
    
    elif car.lower() == 'stop':
        print ('Car Stopped')
        break

    elif car.lower()== 'quit':
        break

    elif car.lower()=='help':
        print ('''start - to start the car
stop - to stop the car
quit - to exit''')
        break 
    
    else: 
        print ('I dont understand that... Please Enter  "Start", "Stop", "Quit", "Help" commands only ')
        break

################ Corrections ##################3
#dry = don't repeat yourself 

# the method .lower() is being repeated in my solution so the shorter way would be to use
# car = input (> ).lower()

######################### Exercise #########################
 
'''The app should then detect whether the car is already started so it can start else it should print 'car already started
# This goes to all of the conditions too.'''

####################### My Solution  ############################
'''Make a program which starts, stops, quit a car. when the user inputs
>help 
start - to start the car
stop - to stop the car
quit - to exit

>asd    #thats an unknown command
I dont understand that...
>start 
Car started...Ready to go!
>stop
Car stopped.
>quit      #exits the application'''

car = input ('> ').lower()  
car_started = True        # A new boolean variable is declared to test whether the car is already started

while car == '> ':      
    if car=='start':
        if car_started:
            print ('Car already started')

        else:
            print ('Car started...')
            car_started=False
    
    elif car == 'stop':
        if not car_started:
        print ('Car already Stopped')

        else:
            print ('Car stopped')
            car_started = False


    

    elif car== 'quit':
        break

    elif car=='help':
        print ('''
start - to start the car
stop - to stop the car
quit - to exit''')
    break
    
    else:
        print ('I dont understand that... Please Enter "Start", "Stop", "Quit", "Help" ')
        break






########################### FOR LOOPS #######################################
#For loops are used iterate elements in a collection

for item in 'Python':     #item counts every character seperately in the 'Python' string
    print (item)

for item in ['Milton', 'Simbarashe', 'Kambarami']:
    print (item)                           #in a list [] item returns the list element

for item in [1,2,3,4]:
    print (item)

# range is a python function which returns a range of number as compared to listing them one by one

for item in range (10):
    print (item)          #default is 0 without 10 being included in the list

for item in range (5,10):      #range is from 5 to 10
    print (item)

for item in range(5,10,2):              # range from 5 to 10 with 2 steps
    print (item)

###################### Exercise #####################################

#Calculate the sum of the items with prices provided as:

prices = [ 10, 20, 30]
'''
for item in prices:                        #item is just a PLACE HOLDER term, we can ot prices or anything
    total = sum (item)
    print (total)
    
Well my code returned an error'''

################# Teacher's Solution #############################

total = 0                             #we define a new variable that holds the sum

for price in prices:
    total += price                    #rem its the same as 'total = total + price' and it adds or prices in the given list
print (total)
print (f'Total: {total}')             #same statement but with different approaches to mix different data types.


#################################### NESTED LOOPS ####################################################

#Lets generate random coordinates
''' (x,y)
    (0,0)
    (0,1)
    (0,2)
    (1,0)
    (1,1)
    (1,2) '''

#these coordinates can be generated easily using 'Nested Loops

for x in range (4):
    for y in range (3):                    # y is nested in x loop, so for x = 0 there are 3 y iterations which is printed as different coordinates. next x =  1 upto x = 3
        print (f' ({x}, {y})')


################################### Challenge ##########################

''' *****
    **
    *****
    **
    **
Draw this F shape using loops 


Hints
numbers = [5, 2, 5, 2, 2] '''


''' numbers = [5, 2, 5, 2, 2]
asterisk = [*]
for num in numbers:
    for * in asterisk:
print (f'{num}* '*'')    '''

# Teacher's Solution

numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ""
    for count in range (x_count):
        output = output + "*"
    print (output)

#Print Letter L

numbers = [2,2,2,2,5]

for Letter in numbers:
    draw = ""
    for x in range (Letter):
        draw += "x"
    print (draw)




