# Removing duplicates

numbers = [4, 8, 15, 8, 16, 23, 4, 42, 15, 8]
unique_numbers = list(set(numbers))

print(unique_numbers)
print(len(unique_numbers))
print(23 in unique_numbers)


# Set operations

ana = {'python', 'java', 'c', 'sql'}
nika = {'python', 'javascript', 'sql', 'go'}

print(ana.union(nika))
print(ana.intersection(nika))
print(ana.difference(nika))
print(ana.symmetric_difference(nika))


# voting

votes = ['Ana', 'Nika', 'Ana', 'Mari', 'Nika', 'Ana', 'Mari', 'Ana']

votes_count = {}
for name in votes:
    if name in votes_count:
        votes_count[name] += 1
    else :   
        votes_count[name] = 1
for name, count in votes_count.items():
    print(f"{name}: {count}")


# Store inventory

total = 0
inventory = {
    'laptop': {'price': 2500, 'quantity': 5},
    'mouse': {'price': 40, 'quantity': 0},
    'keyboard': {'price': 120, 'quantity': 12},
    'monitor': {'price': 800, 'quantity': 0},
}
total = 0

for name, count in inventory.items():
    price = count['price']
    quantity = count['quantity']

    total += price * quantity

print("Total value:", total)
for name, count in inventory.items():
    if count['quantity'] == 0:
        print("This product is out of stock:", name)

product = input("Enter the product name: ")

if product in inventory:
    amount = int(input('Enter quantity: '))

    if inventory[product]['quantity'] >= amount:
        inventory[product]['quantity'] -= amount

        cost = inventory[product]['price'] * amount

        print("Purchase cost:", cost)
        print("Purchase successful!")

    else:
        print('Supply is insufficient')

else:
    print('Product not found')    


#  Comprehension
 
  
words = ['python', 'java', 'ai', 'sql', 'go', 'python']

numbers = [i ** 2 for i in range(1, 11)]
print("Squares:", numbers)

words_length = {word: len(word) for word in words}
print("Word lengths:", words_length)

first_letters = {word[0] for word in words}
print("First letters:", first_letters)
