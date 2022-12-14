from datetime import datetime as dt
from time import time
import model
import csv

def phonebook_logger(name):
    time = dt.now().strftime('%H:%M:%S')
    day = dt.now().strftime('%d.%m.%Y')
    with open ('log.csv', 'a', encoding = 'utf-8') as file:
        log_writer = csv.writer(file)
        log_writer.writerow (['Добавлен пользователь', name, day, time]) 


def phonebook_logger_find(name):
    time = dt.now().strftime('%H:%M:%S')
    day = dt.now().strftime('%d.%m.%Y')
    with open ('log.csv', 'a', encoding = 'utf-8') as file:
        log_writer = csv.writer(file)
        log_writer.writerow (['Поиск пользователя', name, day, time]) 








# def phonebook_logger(name):
#     time = dt.now().strftime('%H:%M:%S; %d.%m.%Y')
#     # current_date = datetime.date.today()
#     # name = model.create_contact()
#     with open ('log.txt', 'a', encoding = 'utf-8') as file:
#         file.write ('\n пользователь {} добавлен {}'.format(name, time))                


# def phonebook_logger_find(name):
#     time = dt.now().strftime('%H:%M:%S; %d.%m.%Y')
#     # current_date = datetime.date.today()
#     # name = model.create_contact()
#     with open ('log.txt', 'a', encoding = 'utf-8') as file:
#         file.write ('\n поиск пользователя {} {}'.format(name, time))     
   