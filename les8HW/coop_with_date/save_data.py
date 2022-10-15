

def save_name(x,name):
    
    with open(x, 'a') as cont:
        cont.write(f"{name} ")
    return name

def save_phone(x,phone):

    with open(x, 'a') as cont:
        cont.write(f"{phone}\n")
    return phone


