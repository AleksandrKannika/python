import coop_with_date.read_data
import coop_with_date.save_data
import gui

def pri():
    try:
        choise = int(gui.inp("Выберите что делать с файлом:\n1 - внести данные;\n2 - прочитать файл;\n"))
        while choise:
            if choise == 1:
                file_name = gui.inp("Введите название файла с расширением")
                while file_name:
                    name = gui.inp("Имя")
                    if name == "":
                        name = "none"
                    phone = gui.inp("Телефон")
                    if phone == "":
                        phone = "none"
                    if name == "none" and phone == "none":
                        break
                    else:
                        coop_with_date.save_data.save_name(file_name,name)
                        coop_with_date.save_data.save_phone(file_name,phone)
                break
            elif choise == 2:
                file_name = gui.inp("Введите необходимое название файла с расширением")
                if file_name == "":
                    break
                all_date = coop_with_date.read_data.rd(file_name)
                print(f"\nтелефонный справочник:{file_name}\n")
                print(all_date)
                return pri()
            else:
                print("\n1, 2 или пропустить другого не дано\n")
                return pri()
    except ValueError:
        print("Спасибо за работу")
        
        

    

    