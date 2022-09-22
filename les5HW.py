# # 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".



# # 2. Создайте программу для игры с конфетами человек против человека.
# #    Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# #    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# #    Все конфеты оппонента достаются сделавшему последний ход. 
# #    Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# #    a) Добавьте игру против бота
# #    b) Подумайте как наделить бота ""интеллектом""
# import random

# total = 2021
# was_taken = 0
# player1 = 1
# player2 = 0
# mode = int(input("Выберите режим игры: \n 1 - если с другим игроком \n 2 - если с ботом \n:"))
# if mode == 1:
#     while was_taken < total:
#         move = 0
#         if player1 > player2:
#             move = int(input("1 игрок: "))
#             if move <= 28 and move != 0:
#                 was_taken += move
#                 player1 -= 1
#                 player2 += 1
#             else:
#                 print("Число не должно быть меньше 1 и превышать 28!")
#         else:
#             move = int(input("2 игрок: "))
#             if move <= 28 and move != 0:
#                 was_taken += move
#                 player2 -= 1
#                 player1 += 1
#             else:
#                 print("Число не должно быть меньше 1 и превышать 28!")
#         print(was_taken)
# elif mode == 2:
#     lavel = int(input("Введите уровень сложности: \n 1 - легкий \n 2 - удачи!!!\n:"))
#     if lavel == 1:
#         while was_taken < total:
#                 move = 0
#                 if player1 > player2:
#                     move = int(input("Игрок: "))
#                     if move <= 28 and move != 0:
#                         was_taken += move
#                         player1 -= 1
#                         player2 += 1
#                     else:
#                         print("Число не должно быть меньше 1 и превышать 28!")
#                 else:
#                     move = random.randint(1,28)
#                     print(f"Компуктер: {move}")
#                     was_taken += move
#                     player2 -= 1
#                     player1 += 1
#                 print(was_taken)
#     if lavel == 2:
#         while was_taken < total:
#                 move = 0
#                 if player1 > player2:
#                     move = int(input("Игрок: "))
#                     if move <= 28 and move != 0:
#                         was_taken += move
#                         player1 -= 1
#                         player2 += 1
#                     else:
#                         print("Число не должно быть меньше 1 и превышать 28!")
#                 else:
#                     move = (total - was_taken) % 29 
#                     if move == 0:
#                         move = random.randint(1,28)
#                     print(f"Компуктер: {move}")
#                     was_taken += move
#                     player2 -= 1
#                     player1 += 1
#                 print(was_taken)

#     # 3. Создайте программу для игры в ""Крестики-нолики"".

import re


a = "| 1 | 2 | 3 |\n-------------\n| 4 | 5 | 6 |\n-------------\n| 7 | 8 | 9 |"


c ='1'
if c == "1":
    c = re.sub("1","x",a)
print(re.sub(r"\d+", "-", c))

#     # 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#     # **Входные и выходные данные хранятся в отдельных текстовых файлах.**
