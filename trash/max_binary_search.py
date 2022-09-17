from typing import List


'''Бинарный поиск'''


def binary_search(numbers: List[int], searched_num: int, start_index: int, end_index: int) -> None:
    # середина - это начало (изначально 0) + половина до конечной точки (изначально n)
    half_index = start_index + ((end_index - start_index) // 2)
    half_value = numbers[half_index]
    
    if (start_index == half_index or end_index == half_index):
        if (half_value == searched_num):
            print(f'Найдено - значение находится на краю массива! (found bounded) - {half_index}')
        else:
            print('Не найдено (not found - all elements checked)')
        return
    # match/case работает только в python версии 3.10 и больше. Можешь переписать на if
    # по сути это выбор из одного кейса
    # https://nuancesprog.ru/p/12097/
    # https://towardsdatascience.com/the-match-case-in-python-3-10-is-not-that-simple-f65b350bb025
    # https://stackoverflow.com/questions/69710333/is-there-a-way-to-match-inequalities-in-python-%E2%89%A5-3-10
    match half_value:
        case _ if searched_num > half_value:
            # идем вправо - значит двигаем начало на середину
            start_index = half_index
        case _ if searched_num < half_value:
            # идем влево - значит двигаем конец на середину
            end_index = half_index
        case _:
            print(f'Нашел число (found) - {half_index}')
            return

    binary_search(numbers, searched_num, start_index, end_index)


numbers: List[int] = [1, 3, 5, 7, 9]
searching_value: int = 1


n = len(numbers)
if (n == 0):
    print('Массив пустой (empty)')
if (n == 1):
    if (numbers[0] == searching_value):
        print('Элемент найден (found - first)')

    else:
        print('Элемент не найден (not found - first)')

binary_search(numbers, searching_value, 0, n)
