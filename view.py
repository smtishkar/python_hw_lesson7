def choose_action():
    print (f"Выберите действие: \nНайти контакт - 1\nСоздать контакт - 2")
    valid = False
    while not valid:
        request = input('\nВведите 1 или 2: ')
        try:
            request = int(request)
            if request >= 1 and request <=2:
                valid = True
            else:
                print("Не корректный ввод, повторите попытку")
        except:
            print("Не корректный ввод, повторите попытку")
            continue
    return request







# def choose_action():
#     print (f"Выберите действие: \nНайти контакт - 1\nСоздать контакт - 2")
#     request = int(input('\nВведите 1 или 2: '))
#     return request