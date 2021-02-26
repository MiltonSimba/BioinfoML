

#course = "Python's course for Beginners" 
#in this example we are trying to use single qoutes in a string thus using double qoutes to opne string,
#this goes back to back with when in need to use " inside a ' ' enclosed string

#However when you want to generate a multiline string we use triple qoutes/triple double qoutes for enclosing the string see below
#Addtionally when a string contains both double qoutes and single qoutes we use triple qoutes.

mail = '''
Hi Milton, here is the confirmatory email 

from the boss's office

Regards
Boss "Simba" 😁😁 
'''
print (mail)

course = 'Python for Beginners'
         #01234567....     -2-1 These are indexes of Str Xters observe
print (course[0])     #Very useful when working with DNA sequences ;)
                        #only P is printed in the above example.
print (course[-1])  #prints the last number
print (course[0:3]) #prints char from 0-2, if no end index is added then Python prints from starts index to end of Str
                        #if no start index is added then Python prints from index 0 to supplied index
print (course[:])    #However when using this expression is used to clone/copy a Str

print (course[1:-1])  #prints the char index 1 to just before the last char

another = course [0:6] #Here the char in course Str are used to define another Var
                        #this could be useful when extracting a gene say Spike from the whole genome of CoV
print(another)  
print (len(course))   #len() function calculates number of char in a string or in a list
                    #Used to limit number of char input by user.
print (course.upper())       # Changes all the char in a str to Upper case, its a method because it can be accessed by Str
                            # course.  gives all the methods available to the var
                            # A method does not change the variable, it returns a value unlike the function like print

print (course.lower())  #lower case

print (course.find ('P'))     #the find method searches the given character and returns th char index value
                            #However the find method is case sensitive. Might be useful in finding start/stop codons.
print (course.find ('Beginners'))        #Returns the index of Find(word) characters.
lower_course = course.lower()
print (lower_course.find ('beginners'))   #now you can find the word even when its in mixed cases.

print (course.replace('Beginners', 'Data Scientist'))   #replace method for strings,seprated by a comma

######Checking the existence of a char or sequence of characters in a str
print ('Python' in course)    #Boolean expression, additioanlly it is case sensititve.
                               # find() method returns index value, in operator returns the boolean true/false value
print('python' in lower_course)    #returns true because all the char have been corrected to lower case.
print (course.title())     ###The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

                           #If the word contains a number or a symbol, the first letter after that will be converted to upper case.


########Formatting Strings##########

first = 'John'
last= 'Smith'
#John [Smith] is a coder, this  would the format avoiding the formatting of list[]
print (first +' ['+last+'] is a coder')  #However when dealing with larger strings this would be tedious. Observe the shortcut:

first_name = 'Milton'
last_name='Kambarami'
    #In this Tut we want to print a string 'Milton [Kambarami] is a coder
message = f' {first_name} [{last_name}] is a coder' #this is a formatted str
          # using 'f' you can add values of variables in {} to strings

print(message)



