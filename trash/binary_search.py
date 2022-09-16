import math
numbers = [i for i in range(1, 101)]
num = 117

def binary_search(numbers, num):
    n = len(numbers)
    if len(numbers) == 1 and numbers[0] != num:
        print('Искомого числа нет в списке')
        return 'Число найдено'
    if num < numbers[n // 2]:
        print(f'Предполагается, что число {num} расположено в 1-ой половине списка numbers')
        numbers = numbers[0 : n // 2]
    elif num > numbers[n // 2]:
        print(f'Предполагается, что число {num} расположено во 2-ой половине списка numbers')
        numbers = numbers[n // 2 : n]
    elif num == numbers[n // 2]:
        print(f'Загаданное число - {numbers[len(numbers) // 2]}')
        return 'Число найдено'
    binary_search(numbers, num)

binary_search(numbers, num)


