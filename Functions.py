#Topics included in this module : 'FUNCTIONS, EXCEPTIONS, COMMENTS
 

# functions contain code that will be used to build an application
#so far we have learnt about built in Python functions like print () and input ()

def greet_users():
#always use descriptive and meaningful function names for your own good
#'def' is a reserved keyword in python which means 'define', this tells python that there is a function to be defined.                                    

    print ('Hi there!')                  #so in case we use these statements in different application there is no need to repeat the function.
    print('Welcome aboard')              #everything that is indented pelongs under the function 'greet_user'


print ('Start')
greet_users()                  #Py generates an error if we use a function before we have defined it
print ('Finish')


######################### Parameters ###########################
# parameters are place holders in a function eg in print (first name) function, name is a parameter
def greet_user(first_name, last_name):           #if a parameter is passed to a function we are obligated to provide a valiue for that parameter or else an error is returned
    print (f'Hi {first_name}, {last_name}!')                #parameters and arguments are different in the sense that, a parameter is passed on the function and an argument is the actual value passed to the parameter, "name" = parameter, "milton" = argument
    print ('Welcome aboard')

print ('Start')
greet_user('Milton', 'Kambarami')
greet_user('Simba', 'Kambarami')
print ('Finish')

########################## Keyword Arguments #####################################

def greet_user(first_name, last_name): 
    print (f'Hi {first_name}, {last_name}!')          
    print ('Welcome aboard')

print ('Start')
greet_user('Kambarami', 'Milton')       # here the first name is placed last and python doesnt care enough to know which is which,thats where keyword arguments come to the rescue.
greet_user(last_name='Kambarami', first_name = 'Milton')    
print ('Finish')

#the printed result is positional, whether you start with the first or last name the result just prints whats provided.
#when using mixed arguments, positional arg comes first then keyword arg

######################### Return Statement ###############################
def square(number):
    return number * number         # without the return statement in a function procedure, python returns none

result = square(3)
print (result)              #OR

print (square(3))           #same result from shorter code


######################## Exercise: Creating a re-usable function ###########################
#from our past tutorial of emoji converter we would like to automate this code so it can be reusable

def emoji_converter (message):
    words = message.split (' ')          
    emojis = {
        ':)' : '😁',
        ':(' : '😒'
    }
    output = ''
    for word in words:
        output += emojis.get (word, word) + ' ' 
    return output


message = input ('>')                              #the input() cannot be included because we can get input from different sources
print (emoji_converter(message))                                     #on the same token, the output cannot be limmited to printing but perhaps to emailing etc

###################   Exceptions/Errors ############################
# How to handle errors
#we use try...except to hadle errors, instead of the program crushing it continues to run the program without crushing and rather print a message to notify the user of the problem

try:
    age = int (input ('Age: '))
    print (age)
except ValueError:                         #the error is obtained from terminal 
    print ('Invalid value')

#we can also handle different errors/exceptions

try: 
    age = int (input ('Age: '))
    income = 20000
    risk = income/age
    print (risk)
except ZeroDivisionError:
    print ('Age cannot be 0')

except ValueError:
    print ('Invalid value')

############################# Comments ##################################
#Comments are used to communicate with other developers or clear things up or as a reminder, they wont be executed by python

#Don't write repetitive comments which repeat what you've written already in your code
#Keep it simple
