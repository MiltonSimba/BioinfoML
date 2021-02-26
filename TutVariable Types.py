birth_year = input ('Birth year: ')
print (type(birth_year))
age = 2021 - int (birth_year) #birth year generated an error because 
print (type(age))             # we subtracting a str and int its like 2021-"1992"
                            #however 'int()' converts str to int type in this example.
print (age)




################# Exercise using Variant Types###################
#divide the mass value by 2.20462262
weight = input ('What is your weight in kg? ')
weight_lbs = float(weight)*2.20462262
print ('Your weight in pounds is ' + str (weight_lbs))
