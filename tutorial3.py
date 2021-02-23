birth_year = input ('Birth year: ')
print (type(birth_year))
age = 2021 - int (birth_year) #birth year generated an error because 
print (type(age))             # we subtracting a str and int its like 2021-"1992"
                            #however 'int()' converts str to int type in this example.
print (age)
