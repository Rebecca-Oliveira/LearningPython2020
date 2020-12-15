#Print Statements
print('Rebecca Oliveira')
print('o----')
print(' ||||')
print("*" * 10)

#Data types
price = 10
price = 20 #int
rating = 4.9 #float
name = 'Rebecca' #string
is_published = True #boolean;python is case senisitve
print(price)

#Variable Practice
name = 'John Smith'
age = 20
new_patient = True

#Receiving Input from User
name = input('What is your name? ') # like print(), input() is built into Python
print('Hi ' + name)

#Input Practice
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)

#Type Conversion
birth_year = input('Birth year: ') #need to convert string input into int
print(type(birth_year))  #type() will print the type
age = 2020 - int(birth_year) #int() will convert, same with bool()
print(type(age))
print(age)

#Type Conversion Pracitce
weight_lbs = input("How much do you weigh in lbs.? ")
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

#Strings - what if you have an apostrophe?
course = "Python's Course for Beginners"
course_1= 'Python for "Beginners"'
email = '''
This can be a multi-line string.

Very fancy, yes. 

Best, Rebecca <3
'''
print(course)
print(course_1)
print(email)
print(course[0]) #prints the index, starts at 0, [-1] will print last character
print(course[0:3]) #prints char from index 0,1,2, but not 3
print(course[0:]) #default value for end index would be the lenght of the string
print(course[:]) #this will return everything!

#What will it print?
name = 'Jennifer'
print(name[1:-1])
