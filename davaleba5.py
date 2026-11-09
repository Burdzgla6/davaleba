# Even number

num = 1 
while num <= 50:
    if num % 2 == 0:
        print(num)
    num += 1


# Sum from 1 to N

n = int(input('enter N:'))

total = 0
number = 1

while number <= n:
    total += number
    number += 1
print('Sum:', total)    


# Factorial

n = int(input('enter n: '))

factorial = 1
number = 1

while number <= n:
    factorial *= number
    number += 1
print(factorial)    


# Arithmetic mean

total = 0
count = 0
num = int(input('enter number: '))

while num != 0:
    total += num 
    count += 1

    num = int(input('enter number: '))
if count > 0:
    average = total / count
    print(average)
else: 
    print('No numbers were entered')


# Guessing Game

secret = 7
attempts = 0
guessed = False

while attempts < 5 and guessed == False:
    guess =int(input('guess: '))
    attempts += 1
    if guess > secret:
        print('too high')
    elif guess < secret:
        print('too low')
    else:
        print('you win!')
        guessed = True
if guessed == False:
    print('You lose! The number was', secret)        