import gui

def save_name(x):
    name = gui.inp("Имя")
    with open(x, 'a') as cont:
        cont.write(f"{name} ")
    return name

def save_phone(x):
    phone = gui.inp("Телефон")
    with open(x, 'a') as cont:
        cont.write(f"{phone}\n")
    return phone


