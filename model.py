def find_right_contant():                           
    with open ('phonebook.txt', 'r', encoding = 'utf-8') as f:
        lst = f.readlines()
        find = input("Кого ищеи?: ")
        for i in lst:
            if find in i:
                print(i)
                break
        if find not in i:
            print ("Контакт не найден")
    return find    

book = {}
def create_contact():
    with open ('phonebook.txt', 'a', encoding = 'utf-8') as f:
        name = input("Введите имя: ")
        tel = input("Введите номер: ")
        book[name] = tel
        f.write (f"{name} {tel}\n")
    return name



# def find_right_contant():
#     with open ('phonebook.txt', 'r', encoding = 'utf-8') as f:
#         lst = f.readlines()
#         find = input("Кого ищеи?: ")
#         for i in lst:
#             if find in i:
#                 print(i)
#                 break
#             elif find not in i:
#                 print ("Контакт не найден")
#     return find    


# def find_right_contant():                           
#     with open ('phonebook.txt', 'r', encoding = 'utf-8') as f:
#         lst = f.readlines()
#         find = input("Кого ищеи?: ")
#         for i in lst:
#             if find in i:
#                 print(i)
#                 break
#         if find not in lst:
#             print ("Контакт не найден")
#     return find    