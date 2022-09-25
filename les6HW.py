# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
#    неповторяющихся элементов исходной последовательности.
#    [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

follower_list = [1, 1, 2, 3, 4, 5, 5]
res = list(filter(lambda x: follower_list.count(x) == 1, follower_list))
unique_num = [i for i in follower_list if follower_list.count(i) == 1]
# count_item = 0
# while count_item < len(follower_list)-1:
#     if follower_list[count_item] == follower_list[count_item+1]:
#         count_item += 2
#     else:
#         unique_num.append(follower_list[count_item])
#         count_item += 1
print(unique_num)
print(res)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# list_1 = [-6,4,-2,-4,2,8,7,-9,1,-3]
# list_2 = input("Введите нужные позиции от 1 до 10 через пробел: ")
# list_3 = list_2.split(" ")
# result_lists = 1
# counter_list_3 = 0
# while counter_list_3 < len(list_3):
#     result_lists *= list_1[int(list_3[counter_list_3])-1]
#     counter_list_3+=1
# print(result_lists)

from random import randint
count_element = 10
new_method = [randint(-count_element,count_element) for i in range(count_element)]
print(new_method)


# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

list_some_numbers = [2, 3, 5, 9, 3]

# def find_odd(some_list):
#     found_num = []
#     for i in range(len(some_list)):
#         if i % 2 != 0:
#             found_num.append(some_list[i])
#     return found_num


# def summ_found_odd(some_list):
#     summ = 0
#     for i in range(len(some_list)):
#         summ += some_list[i]
#     return summ

# print(summ_found_odd(find_odd(list_some_numbers)))



res = [list_some_numbers[i] for i in range(len(list_some_numbers)) if i%2 != 0]
sum = 0
for i in res:
    sum += i
print(sum) 




# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import math


# f = 4
# counter_f = 1
# result = 1
# while counter_f<=f:
#     result *=counter_f
#     counter_f+=1
#     print(result, end=" ")

num_fac = 5
fac = [math.factorial(i) for i in range(1,num_fac + 1)]
print(fac)




