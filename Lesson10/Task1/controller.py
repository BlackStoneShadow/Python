import model
from view import Menu
from view import Input
from view import Print

class Controller:
    def __init__(self):
        self.menu = Menu('Menu:')

    def menu_view(self):
        return self.menu.view()

    def menu_eval(self, arg1, arg2, oper):
        self.value_a = Input(arg1, arg2, oper).get_valua()
        self.value_b = Input(arg1, arg2, oper).get_valub()
        self.value_o = Input(arg1, arg2, oper).get_opera()
        self.value_n = Input(arg1, arg2, oper).get_typen()
    
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

        return Print("result").view_data(result)