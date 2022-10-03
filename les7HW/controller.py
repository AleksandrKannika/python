import re
import save_data
import read_data
import gui

def pri():
    a = int(gui.inp("Выберите что делать с файлом:\n1 - внести данные;\n2 - прочитать файл;\n"))
    if a == 1:
        c = gui.inp("Введите название файла с расширением")
        save_data.save_name(c)
        save_data.save_phone(c)
    elif a == 2:
        c = gui.inp("Введите необходимое название файла с расширением")
        f = read_data.rd(c)
        print(f)