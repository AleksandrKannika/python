# 1. Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141

import math

a = math.pi
d = 5
print(round(a,d))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#    "20" -> [2, 2, 5]

n = 63
c = 2
list1 = []
while c <= n:
    if n%c == 0:
        n = n/c
        list1.append(c)
    else:
        c += 1

print(list1)


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
#    неповторяющихся элементов исходной последовательности.
#    [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

x = [1, 1, 2, 3, 4, 5, 5]
c = []
i = 0
while i < len(x)-1:
    if x[i] == x[i+1]:
        i += 2
    else:
        c.append(x[i])
        i += 1
print(c)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#    (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#    Пример:
#    k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

extent = 4
couner = 0
list_poly_coeff = []
while couner < extent+1:
    rnd_num = random.randint(0,100)
    list_poly_coeff.insert(0, rnd_num)
    couner+=1

couner = 0
list_poly_extent = []
while couner < extent+1:
    if couner > 1:
        list_poly_extent.insert(0,f"x^{couner}")
    elif couner == 1:
        list_poly_extent.insert(0,"x")
    else:
        list_poly_extent.insert(0,"0")
    couner+=1

print(list_poly_coeff)
print(list_poly_extent)

for i in range(len(list_poly_coeff)):
    if list_poly_coeff[i] == 0:
        list_poly_coeff[i] = "del" + list_poly_extent[i]
    elif list_poly_coeff[i] == 1:
        list_poly_coeff[i] = list_poly_extent[i]
        if list_poly_extent[i] == "0":
            list_poly_coeff[i] = 1
    elif list_poly_extent[i] == "0":
        list_poly_coeff[i] = str(list_poly_coeff[i])
    else:
        list_poly_coeff[i] = str(list_poly_coeff[i]) + list_poly_extent[i]

print(list_poly_coeff)
text_find = "del"
correct_list = [item for item in list_poly_coeff if text_find not in item]
print(correct_list)

result = " + ".join(correct_list)
result = result + " = 0"
print(result)

# 5. Даны два файла, в каждом из которых находится запись многочлена.
#    Задача - сформировать файл, содержащий сумму многочленов.




