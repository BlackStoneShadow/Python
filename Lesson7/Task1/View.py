from Model import Phone_
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
    def phone(self):
        return input('Phone:')
    def type(self):
        return input('Type:')
    def name(self):
        return input('Name:')

    def record(self):
        system('cls')
        return (self.phone(), self.type(), self.name())

class Print:
    def record(self, item):
        system('cls')

        #Item = Phone_(item)

        print('Phone:', item[0])
        print('Type:', item[1])
        print('Name:', item[2])       
        
        input('Press any key')

    def data(self, data):        
        for item in data:
            self.record(item)                    