import model
import re

class Menu:
    def __init__(self, caption):
        self.caption = caption
    
    def view(self):        
        return '\n'.join((self.caption, '/eval'))        

    def item(self):
        self.view()

        item = str()
        while item not in self.items():
            item = input(self.caption)
        
        return item

class Input:
    def __init__(self, arg1, arg2, oper):
        self.value_a = arg1
        self.value_b = arg2
        self.value_o = oper

        if 'i' in str(self.value_a) and 'i' in str(self.value_b):
            self.type_num = model.model_name_kmp
        elif self.try_cast(self.value_a, int) != None and self.try_cast(self.value_b, int) != None:
            self.type_num = model.model_name_rac
        else:
            self.type_num = None

    def try_cast(self, value, type):   
        try:
            return type(value)
        except:
            return None
    
    def get_valua(self):
        return self.value_a

    def get_valub(self):
        return self.value_b

    def get_opera(self):
        return self.value_o

    def get_typen(self):
        return self.type_num

class Print:
    def __init__(self, title):
        self.title = title

    def view_data(self, data):                
        return (f'{self.title} = {data}')