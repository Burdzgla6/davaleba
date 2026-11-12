# Shopping list

shopping = ['milk' , 'bread' , 'eggs' ]
shopping.append('cheese')
print(shopping)

shopping.insert(0 , 'apples')
print(shopping)

shopping[-1] = 'butter'
print(shopping)

lst = ['tea', 'coffee']
shopping.extend(lst)
print(shopping)

shopping.remove('bread')
print(shopping)

deleted = shopping.pop(1)
print(deleted)
print(shopping)


# Exam scores

scores = [85, 92, 78, 92, 65, 88, 92]

copied_scores = scores.copy()
print(copied_scores.count(92))

print(copied_scores.index(78))

asc_scores = copied_scores.copy()
asc_scores.sort()
print('Ascending: ',asc_scores)

desc_scores = copied_scores.copy()
desc_scores.sort(reverse=True)
print('Descending: ' , desc_scores)

print('highest:', asc_scores[-1])
print('lowest:', asc_scores[0] )

print('original' , scores)


# Matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(matrix))
print(matrix[-1])

print(matrix[1][2])
print(matrix[-2][-1])

print(matrix[-1][-3])

matrix[1][1] = 50
print(matrix)


# Filling a list (while)

numbers = []

while True:
    value = input('Enter a number: ')
    if value == 'stop':
        break

    numbers.append(int(value))

print('List:', numbers)
print('Count:', len(numbers))

if len(numbers) > 0:
    print('First:', numbers[0] , end=' , ')
    print('Last:', numbers[-1])


desc_numbers = numbers.copy()
desc_numbers.sort(reverse=True)

print('Descending:', desc_numbers)    
