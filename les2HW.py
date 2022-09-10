# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

x = "0.15"
a = x.split(".")
y = (a[1])
z =0
for i in range(len(y)):
    z+= int(y[i])
print(z)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

f = 4
counter_f = 1
result = 1
while counter_f<=f:
    result *=counter_f
    counter_f+=1
    print(result, end=" ")

# 3. Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = 3
counter_k = 1
result_k = 0
while counter_k<=k:
    result_k+= (1+(1/counter_k))**(counter_k)
    counter_k+=1
print(round(result_k, 4))

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

list_1 = [-6,4,-2,-4,2,8,7,-9,1,-3]
list_2 = input("Введите нужные позиции от 1 до 10 через пробел: ")
list_3 = list_2.split(" ")
result_lists = 1
counter_list_3 = 0
while counter_list_3 < len(list_3):
    result_lists *= list_1[int(list_3[counter_list_3])-1]
    counter_list_3+=1
print(result_lists)


# 5. Реализуйте алгоритм перемешивания списка.

list_mix = [3, 4, 6, 3, 4, 'gfe', 'sd', 4, 53, 'hy']
first_position = 0
last_position = len(list_mix)-1
while first_position < last_position:
    temp = list_mix[first_position]
    list_mix[first_position] = list_mix[last_position]
    list_mix[last_position] = temp
    first_position += 1
    last_position -= 1
print(list_mix)
