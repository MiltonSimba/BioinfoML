#Tuples work like lists but they are immutable, to say you can not edit the contents of the tuple.

numbers = (1,2,3)              #we use () instead of [] for tuples. 
print (numbers[0])

#Tuples are useful when there is an area in your app that you dont want to be changed.


############## Unpacking ##################
coordinates = (1,2,3)
coordinates [0] * coordinates[1] *coordinates [2]      #pretty long huh!

#in python we can make the above statement a lil bit shorter based on the mathematics first

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

#the ultimate Python shortcut would be:

x,y,z = coordinates                      #this is unpacking and can be used with lists too
print (z)



########################################### DICTIONARIES  #########################################################

#we use dictionaries when we want to store pairs of key values eg we have this info

'''Name: John Smith
    Email: john@gmail.com
    Phone: 1234
'''
#dictionaries are defined by using curly brackets
#duplicates are not allowed

customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}       

print (customer ['name'])                       #case sensitive
print (customer.get('name'))                    #same as above
print (customer.get('name'), 'Jan 1 1980')      #adding more char
customer['name'] = 'Jack Smith'                  #Changes 'name' to Jack Smith
print (customer['name'])

customer['Birthdate']= 'Jan 1 1980'              #append an item to the existing list
print (customer.get('Birthdate'))

g

########################### Exercise ##################################

#  Make an app that when you input  phone number in digits it will print it back in letters

'''
phone = input ('Phone: ')

alphanumber= (1,2,3,4,5,6,7,8,9,0)
one,two,three, four, five, six, seven, eight, nine, zero = alphanumber

for item in alphanumber:
    if phone == alphanumber:
        print phone
'''


#Tutor's solution
phone = input('Phone: ')
digits_mapping = {
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four'
}                       #and so on

output = ''
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print (output)






