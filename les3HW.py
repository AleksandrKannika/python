# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12


def find_odd(some_list):
    found_num = []
    for i in range(len(some_list)):
        if i % 2 != 0:
            found_num.append(some_list[i])
    return found_num


def summ_found_odd(some_list):
    summ = 0
    for i in range(len(some_list)):
        summ += some_list[i]
    return summ


list_some_numbers = [2, 3, 5, 9, 3]
# print(summ_found_odd(find_odd(list_some_numbers)))


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def product(some_list):
    product_list = []
    first_num = 0
    last_num = len(some_list)-1
    while first_num <= last_num:
        product_list.append(some_list[first_num]*some_list[last_num])
        first_num += 1
        last_num -= 1
    return product_list

# print(product(list_some_numbers))

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19


def fraction_numbers(some_list):
    real_list = []
    for i in range(len(some_list)):
        a = float(some_list[i]) - int(some_list[i])
        real_list.append(a)
    return real_list


def find_min_max(some_list):
    found_num = []
    min_num = some_list[0]
    max_num = some_list[0]
    for i in range(len(some_list)):
        if min_num > some_list[i]:
            min_num = some_list[i]
        if max_num < some_list[i]:
            max_num = some_list[i]
    found_num.append(min_num)
    found_num.append(max_num)
    return found_num


def difference(some_list):
    diff = some_list[1] - some_list[0]
    return diff


gg = [3.43, 43.12, 0.327, 5.34, 435.11, 86.34]

# print (round(difference(find_min_max(fraction_numbers(find_min_max(gg)))), 5))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def binary(some_denary):
    binary_num = []
    while int(some_denary) > 0:
        if some_denary % 2 == 0:
            binary_num.insert(0, 0)
        else:
            binary_num.insert(0, 1)
        some_denary //= 2
    return binary_num


def print_bin(some_list):
    for i in some_list:
        print(i, end='')


x_denary = 1
# print_bin(binary(x_denary))


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibo(n):
    if (n == 1) or (n == 2):    
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
fibo_nega_posi_line =[0]

number_of_variabels = int(input("Задайте число для расчета: "))
counter = 1
while counter <= number_of_variabels:
    fibo_nega_posi_line.append(fibo(counter))
    fibo_nega_posi_line.insert(0, fibo(counter) * ((-1) ** (counter + 1)))
    counter += 1

print(fibo_nega_posi_line)