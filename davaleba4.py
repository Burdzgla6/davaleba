# Cinema

age = int(input('enter your age: '))
money = int(input('enter money: '))
if age >= 12 and money >= 15:
    print('enjoy the movie')

else:     
    print('access denied ')

#Leap year

year = int(input('enter year: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('leap year')

else:
    print('not a leap year')


# ATM (if)

pin = int(input('enter your pin: '))
balance = 500

if pin == 1234:
    amount = int(input('enter amount'))

    if amount <= 0:
        print('invalid amount')

    elif amount > balance:
        print('not enough money')

    else:
        balance = balance - amount    
        print('take your money:' , amount)
        print('new balance: ' , balance)   

else:
    print('wrong pin')


# ValueError, ZeroDivisionError, TypeError


try:

    name = input('Enter name: ')
    age = int(input('Enter age: '))
    number = int(input('Enter a number to divide 100 by: '))

    print('100 /', number, '=', 100 / number)
    print(f'Hello {name}! Next year you will be {age + 1} years old.') 

except ValueError:
    print('invalid input')

except ZeroDivisionError:
    print('Cannot divide by zero')

except TypeError:
    print('Cannot join text and number')

except Exception as e:
    print(e)        