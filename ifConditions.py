####################################### If Statement #############################################
is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print ('Drink plenty of water')
elif is_cold:
    print ("Its a cold day")
    print('Wear warm clothes')
else:
    print ('Its a lovely day')
    
print ("Enjoy your day")

########################## Exercise ####################################
price = 1000000
good_credit=True
if good_credit:
    price= price * 0.1
    print (f'Downpayment = ${price}')   #Here i used the formatted string approach, since price is int
else:
    price = price *0.2
    print ('Downpayment = $' + str(price))    #Same approach as above but using string concatenations.


##################  Logical Operators    ##################
#Logical Operators are used when we have a number of conditions

#if applicant has high income AND good credit, is eligible for loan. Let's put it in code form.

high_income = True
good_credit = True
criminal_record= False

if  high_income and good_credit:      #Both of the statements should be true
    print ('Eligible for loan')

#if applicant has high income OR good credit, is eligible for loan. Let's put it in code form.
if high_income or good_credit:
    print ('Eligible for loan:OR')    #At least one statement has to be true

#if applicant has high income and good credit and does not have a criminal record, is eligible for loan. Let's put it in code form.
if high_income and good_credit and not criminal_record:    
  print ('Eligible for loan:not')           #Not negates the given condition



################### Comparison Operators  ############################
# Comparison Operators compare a variable to a value

Example = ''' if temperature is greater then 30
                 it's a hot day
              otherwise if its less than 10
                 it's a cold day
              otherwise
                 its neither hot nor cold'''

##Solution

temperature=35

if temperature > 30:
    print ("Its a hot day")
else:
    print ('Its not a hot day')

### other operators include < -less than, >= - greater than or equal to, <= - less than or equal too
### == -Equal to, one = is assignment, != -not equal to

############################  Exercise   #################################
Exercise = '''if name is less than 3 characters long
        name must be at least 3 characters
  otherwise if its more 50 characters long
        name can be a max of 50 characters
  otherwise
        name looks good!'''

name = input ('Enter your name ')
name_length = len (name)

if name_length < 3:
       print('Name must be at least 3 characters')
elif name_length > 50:
       print ('Name can be a maximum of 50 characters')
else:
       print ('name looks good')

################################ Project: Weight Converter ########################################

weight = int(input ('Enter your Weight: '))
unit = input ('(L)bs or (K)g: ')

if unit.upper() == 'L':   #dont forget () in variable methods
    convert = weight * 0.45
    print (f'You are {convert} kg')
else:
    convert = weight / 0.45
    print (f'You are {convert} lbs')
#ConditionEnd









