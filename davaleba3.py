# # Even or Odd

number = int(input('enter your number: '))
if number % 2 == 0:
    print('your number is Even')

else:
    print('your number is Odd')


# Age restriction

age = int(input('enter your age: '))
if  age <= 0:
    print('Invalid age')

elif 0 < age <= 12:
    print('Child')

elif 13 <= age <= 17:
    print('Teenager')

elif 18 <= age <= 64:             
    print('Adult')

else:
    print('Senior')    


# Grades 

grade = int(input('enter your grade: '))
if grade < 0:
    print('Invalid grade')

elif grade > 100:
    print('Invalid grade')


elif 90 <= grade <= 100:
    print('A')

elif 80 <= grade <=89:
    print('B')

elif 70 <= grade <= 79:
    print('C')

elif 60 <= grade <= 69:
    print('D')

elif 50 <= grade <= 59:
    print('E')

else:
    print('F') 


# Yes\No


answer = input('Do you like python?: ').strip().lower()

if answer == 'yes':
    print('Great!')

elif answer == 'no':
    print('Maybe you will like it later')

else:
    print('Please answer yes or no')    


# Calculator

fisrt_number =float(input('enter first number: '))

operation = input('enter operation: ')

second_number = float(input('enter second number: '))

if operation == '+':
    print(first_number + second_number)

elif operation == '-':
    print(fisrt_number - second_number)  

elif operation == '*':
    print(fisrt_number * second_number)

elif operation == '/':
    print(fisrt_number / second_number) 

else: 
    print('Unknown operation')     