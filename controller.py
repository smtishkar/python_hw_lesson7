import view
import model
from logger import phonebook_logger as logc
from logger import phonebook_logger_find as logf


def button_click():
    user_request = view.choose_action()
    if user_request == 1:
        res = model.find_right_contant()
        logf(res)
    elif user_request == 2:
        res = model.create_contact()
        logc(res)
