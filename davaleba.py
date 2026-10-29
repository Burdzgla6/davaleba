# type
age = 20
height = 1.75
name ='Giorgi'
is_student = True

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# Math
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(a + b)
print( a - b)
print(a * b)
print( a / b)
print( a // b)
print(a % b)
print(a ** b)


# String
name = input("Enter your name: ")
lastname = input("Enter your lastname: ")

full_name = name + " " + lastname

print(full_name)
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())



# Print
print("Hello", "World", sep="-")

print(1, 2, 3, sep="\t")

print("Hello", end=" ")
print("World")

print("My age is", end=" ")
print(20)



# Comparision
age = 20

print(age == 20)
print(age != 18)
print(age > 18)
print(age < 30)
print(age >= 20)
print(age <= 25)

print(age > 18 and age < 30)
print(age < 18 or age > 15)
print(not age == 20)


#Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))

print("Hello", name)
print("Your age is", age)
print("Your height is", height)