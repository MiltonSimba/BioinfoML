# so far we've dealt with the following classes
'''
Numbers
Strings
Booleans
----
Lists
Tuples
Dictionaries
'''
#these classes cannot always be used to handle complex operations
#we can use classes to define new types to model real concepts

####################### DEFINING CLASSES ########################

class Point:                     # the naming conventions of classes is Uppercase letter for every new word opposed to variables etc where we put underscores _ also know as Pascal naming convention from Pascal language
    def move (self):             # define a method called move, under Point class
        print ('move')

    def draw (self):
        print ('draw')


#objects are instances of a class, the Class creates the blueprint of creating objects and objects are actual instances based on the class

point1 = Point()        
point1.draw()            #all instances listed in the Point class are listed as methods
point1.x= 10           #besides taking methods, objects can take attributes which act like variables that belong to a certain object
point1.y = 20
print (point1.y)

try: 
    point2 = Point () 
    point2.y = 40
    print (point2.y)       #this one is returned
    print (point2.x)       #they are objects of the same class but have different attributes

except AttributeError:
    print ("This attribute has been assigned to object Point1")

####################### CONSTRUCTORS  #################################

# A constructor is a function that is called when creating an object
class Point:
    def __init__(self,x,y):          # __init__ is a special type method called a constructor 'init' means initialise
            self.x = x               #self references the current attribute, .x passes a value to x
            self.y = y

    def move(self):
        print ('move')
    
    def draw (self):
        print ('draw')

point = Point (10,20)
point.x = 11
print (point.x)


##################### Exercise #######################
'''
Create a Class called Person with a name attribute and talk () method
'''

class Person:
    def __init__ (self, FirstName, LastName):
        self.FirstName= FirstName
        self.LastName=LastName

    def talk (self):
        print (f'Hi, i am {self.FirstName} {self.LastName}.')


speak = Person('Milton', 'Simba')
speak.talk()

speak = Person ('Milton', 'Kambarami')
speak.talk()


#################################### INHERITANCE #################################
 
 #Inheritance is a mechanism of reusing code.
'''
class Dog:
    def walk(self):
        print ('walk')

#lets say we have another class Cat with the same method, its unnecessary to re-write the same method as below:

class Cat:
    def walk (self):
        print ('walk')
'''
#this has a disadvantage when you want t modify your code and you have to follow up in every class procedure to fix your code, an alternative would be to modify only source class


class Mammal:
    def walk (self):
        print ('walk')


class Dog (Mammal):
    pass                              #this tells python there is nothing else to add becaise you cant have an empty class
        


class Cat(Mammal):
    def be_annoying (self):
        print ('annoying')                  #or we can add a new method inside the cat class


dog1 = Dog ()
dog1.walk()

cat1 = Cat ()
cat1.walk()
cat1.be_annoying()

