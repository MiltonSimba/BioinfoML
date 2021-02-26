#########Intro to Arithmetic Operators in Python########################

print (10+3)        #Addition
print (10-3)        #Subtraction
print (10*3)        #Multiplication
print (10/3)        #Normal Division, gives a remainder
print (10//3)       #Returns the integer of result
print (10%3)        #Modulus returns the remainder of the division 3 r 1
print (10**3)       #10 to the power 3

############Assignment Operator###############

x=10            #the integer 10 has been to variable x
x=x+3           #now the variable is no longer 10 but 10 +3
x+=3            #Augmented assignment operator, same as above but shorter
x-=3            #Same as above and can be augmented for all arithmetic operators in the above section
print (x)       #this is how we can increment a number

y = 10+3*2      #multiplies first then adds called operatr precedent, just like BOMDAS
y = 10+3*2**2   #exponentiates then multiplies and add
y = (10+3)*2**2  #however brackets have the first preference
print (y)       #exponentiation > multipllication/division > addition/subtraction
