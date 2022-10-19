from Model import Phone
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

    def phone(self):
        return input('Phone:')

    def type(self):
        return input('Type:')

    def name(self):
        return input('Name:')

    def record(self):    
        return Phone((self.phone(), self.type(), self.name()))

class Print:
    def __init__(self):
        system('cls')

    def record(self, item):
        phone = Phone(item)

        print('Phone:', phone.number)
        print('Type:', phone.type)
        print('Name:', phone.name)       
        
        input('Press Enter to continue')

    def data(self, data):        
        for item in data:
            self.record(item)                    