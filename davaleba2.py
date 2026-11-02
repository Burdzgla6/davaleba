# Slicing

word= 'programming'
print(word[0])
print(word[-1])
print(word[-3])
print(word[0:4])
print(word[-4:])
print(word[::2])
print(word[::-1])

# Email

mail= input('Please enter your email: ')

position = mail.index('@')
print(position)

username = mail[:position]
print(username)

domain = mail[position + 1:]
print(domain)

dot_position = domain.index('.')
print(dot_position)

first_part = domain[:dot_position]
print(first_part)

#Phone number

phone = input('Please enter your number')
phone = phone.replace(' ' , '').replace('-' , '')
print(phone)

#Slug

title = input('Please enter title: ')
title = title.replace("'", "")
split_text = title.lower().split()
print(split_text)

slug = '-'.join(split_text)
print(slug)

#f-stirng

name = input('enter your name: ')
age = input('enter your age: ')
city = input('enter your city: ')
language= input('enter your favorite language: ')

print(f'name:{name.title()}')
print(f'age:{age}')
print(f'city:{city.title()}')
print(f'favorite language:{language.upper()}')
