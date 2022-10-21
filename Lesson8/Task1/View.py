from Model import Employe
from Model import FIELD_SNILS
from os import system

class Menu:
    def __init__(self, caption):
        self.caption = caption
    def view(self):
        system('cls')
        
        print('Menu:')
        print('A_ll')
        print('N_ew')
        print('R_emove')        
        print('F_ind')
        print('S_ave')
        print('E_xit')        

    def items(self):
        return ('A', 'E', 'F', 'N', 'R', 'S')

    def item(self):
        self.view()

        item = str()
        while item not in self.items():
            item = input(self.caption)
        
        return item

class Input:
    def __init__(self):
        system('cls')
    
    def input(self, field):
        return (field, input(field + ':'))

    def snils(self):
        return self.input(FIELD_SNILS) #Key field

    def name(self):
        return self.input('name')

    def date(self):
        return self.input('date')

    def department(self):
        return self.input('department')

    def phone(self):
        return self.input('phone')

    def record(self):    
        return Employe((self.snils(), self.name(), self.date(), self.department(), self.phone()))

class Print:
    def __init__(self):
        system('cls')

    def record(self, item):
        employe = Employe(item)

        for field in employe.fields:
            print(field, employe.fields[field],  sep = ':')
        
        input('Press Enter to continue')

    def data(self, data):        
        for item in data:
            self.record(item)                    
