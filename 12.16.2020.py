#Formatted Strings
first_name = 'John'
last_name = 'Smith'
message = first_name + ' [' + last_name + '] is a coder.'
#above code works but it's too complicated, a formatted string (bottom) = easier to visualize
msg = f'{first_name} [{last_name}] is a coder'
print(message)
print(msg)

#String Methods
course = 'Python for Beginners'
#len is a general purpose fxn built into Py
print(len(course))  #prints 20
#.upper is a fxn specific to Strings - hence a method!
print(course.upper())
print(course) #method doesn't modify the string
print(course.find('P')) #prints index of 0
print(course.find('Beginners')) #prints 11, bc that's the index it starts at
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course) #a boolean expression, in operator, checks if it's in var

#Arithmetic Operators + - * / // %(mod) **(pow)
x = 10
x = x + 3
#augmented(enhanced) assignment operator
x+=3
print(x)

#Operator Precedence --> PEMDAS
y = 10 + 3 * 2
print(y)

#Math Fxns
import math #a module!
a = 2.9
print(round(a))
print(abs(-2.9))
print(math.ceil(2.9))
print(math.floor(2.9))

#can search python 3 math module in Google and see all the fxns

#If Statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day.")
    print("Drink plenty of water.")
#elif = else if
elif is_cold:
    print("It's a cold day.")
    print("Wear warm clothes.")
else:
    print("It's a lovely day!")

print("Enjoy your day!")

#If Statement Exercise
house_price = 1000000
is_good_credit = False

if is_good_credit:
    down_payment = house_price * .10
    print("You need to put down a down payment of 10%:")
else:
    down_payment = house_price*.20
    print("You need to put down a down payment of 20%:")
print(down_payment)
#Could also use a formatted string: print(f"Down payment: ${down_payment}")

#Logical Operators
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

#There's AND, OR, and NOT operators




