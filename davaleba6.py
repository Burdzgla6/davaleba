# for , ramge()

for i in range(1, 11):
    print(i, 'squeared =' ,  i ** 2)

  
for i in range(10 , 0 , -1):
    print(i)
print('Go!')    

total = 0
for i in range(2 , 101 , 2):
    total = total + i
print(total)    


# Counting vowels

text = input('enter text: ').lower()

count = 0

for ch in text:
    if ch in 'aeiou':
        count += 1
print('vowles' , count)


# Sum of numbers (continue) 

total = 0
count = 0
num = ''
while True:

    num = (input('enter your number: '))

    if num == 'stop' :
        break

    num =int(num)

    if num < 0:
        print('Negative numbers are not allowed')
        continue

    total += num
    count += 1
    
print("Sum:", total)
print("Count:", count)


# Triangle (nested cycles)

n = int(input('enter n: '))

for i in range(1 ,n + 1):
    for j in range(i):
        print('*' , end = '')
    print()


for i in range(n ,0 , -1):
    for j in range(i):
        print('*' , end = '')
    print()    