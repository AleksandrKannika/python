# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

week_check = ["Будний день","Будний день","Будний день","Будний день","Будний день","Выходной","Выходной"]
week_day = int(input("Введите день недели: "))
print(week_check[week_day-1])

if week_day == 6 or week_day ==7:
    print("Выходной")
else:
    print("Будний день")

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = 0
y = 0
z = 0
if (not ( x or y or z)) == (not x) and (not y) and (not z):
    print(True)
else:
    print(False)

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите координату x: "))
y = int(input("Введите координату y: "))
if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input("Введите номер четверти"))
if quarter_number == 1:
    print(f'диапазон {quarter_number} четверти - от 0 до x и от 0 до y')
elif quarter_number == 2:
    print(f'диапазон {quarter_number} четверти - от -x до 0 и от 0 до y')
elif quarter_number == 3:
    print(f'диапазон {quarter_number} четверти - от -x до 0 и от -y до 0')
else:
    print(f'диапазон {quarter_number} четверти - от 0 до x и от -y до 0')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xa = 3
ya = 6
xb = 2
yb = 1
v = ((xb-xa)**2 + (yb-ya)**2)**(0.5)
print(v)