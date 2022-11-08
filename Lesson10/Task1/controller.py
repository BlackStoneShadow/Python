import model
from view import Menu
from view import Input
from view import Print
from os import path
from os import remove
from datetime import datetime 

class Controller:
    def __init__(self):
        self.menu = Menu('Menu:')
        self.name = path.splitext(path.basename(__file__))[0]

    def menu_view(self):
        return self.menu.view()

    def menu_eval(self, text):
        result = str()
        try:                   
            input = Input(text)

            self.value_a = input.get_valua()
            self.value_b = input.get_valub()
            self.value_o = input.get_token()
            self.value_n = input.get_typen()
    
            if self.value_n == None:
                return 'Invalid operands!'

            model.init(self.value_a, self.value_b, self.value_n)

            if self.value_o == '*':
                result = model.mult()
            elif self.value_o == '/':
                result = model.div()
            elif self.value_o == '+':
                result = model.sum()
            elif self.value_o == '-':
                result = model.sub()
            else:
                return 'Invalid operation!'
        except:
            result = 'error'
            
        self.log_write(f'{text}={result}')

        return Print("result").view_data(result)

    def set_user(self, user):
        self.user = user

    def menu_plog(self):
        return Print("history").view_log(self.log_read())

    def menu_clog(self):
        if path.isfile(f'{self.name}.log'):
            remove(f'{self.name}.log')
        
        return Print("history").view_log(str())

    def log_write(self, text):
        with open(f'{self.name}.log', 'a') as data:
            data.writelines(f'{datetime.now()}\t{self.user}\t{text}\n')            

    def log_read(self):
        if path.isfile(f'{self.name}.log'):
            with open(f'{self.name}.log', 'r') as data:
                return data.read()