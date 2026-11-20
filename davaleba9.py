 # Ticket Printing

def print_ticket(name, destination, ticket_class):
    print('--- TICKET ---')
    print('Passenger:', name)
    print('Destination:', destination)
    print('Class:', ticket_class)

print_ticket('Nika', 'Batumi', 'Economy')
print_ticket(name='Mari', destination='Kutaisi',ticket_class='Business')
print_ticket('Luka', 'Batumi', ticket_class='Economy')


# Temperature

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

temp1 = celsius_to_fahrenheit(0)
temp2 = celsius_to_fahrenheit(37)
temp3 = celsius_to_fahrenheit(100)

print('37C =', temp2, 'F')
print('0C =', temp1, 'F')
print('100C =', temp3, 'F')

def is_warm(celsius, limit=20):
    return celsius > limit

print(is_warm(25))
print(is_warm(25, 30))
print(is_warm(limit=10, celsius=15))


# Analysis of Numbers

def analyze_numbers(numbers):
    smallest = min(numbers)
    largest = max(numbers)
    average = sum(numbers) / len(numbers)

    return smallest, largest, average

numbers = [12, 7, 25, 3, 18]
minimum, maximum, average = analyze_numbers([12, 7, 25, 3, 18])

result = analyze_numbers([12, 7, 25, 3, 18])
print(result)


# Group List


def add_student(name, group=None):
    if group is None:
        group = []

    if name not in group:
        group.append(name)

    return group

group_a = add_student('Ana')
group_b = add_student('Nika')
group_a = add_student('Mari', group_a)
group_a = add_student('Ana', group_a)

print(group_a)
print(group_b)    


# Password Strength

def check_password(password):
    if len(password) < 6:
        return 'Too short'

    if password.isdigit():
        return 'Weak'

    if not any(char.isdigit() for char in password) or not any(char.isalpha() for char in password):
        return 'Medium'

    return 'Strong'

passwords = ['abc', '1234567', 'qwerty', 'python3', 'Tbilisi2024']

for password in passwords:
    result = check_password(password)
    print(password, '->', result)


    