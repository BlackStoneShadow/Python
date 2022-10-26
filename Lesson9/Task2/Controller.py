import Model
import View

class Controller:
    def __init__(self):
        # Выбираем формат хранения
        self.model = Model.PhoneBook('PhoneBook.json')
        #self.model = Model.PhoneBook('PhoneBook.csv')
        self.menu = View.Menu('Menu:')

    def menu_view(self):
        return self.menu.view()

    def menu_all(self):
        return View.Print().data(self.model.get_data())

    def menu_find(self, phone):
        return View.Print().data(self.model.find(phone))

    def menu_add(self, phone, type, name):
        self.model.add((phone, type, name))                        
        return 'Ok'

    def menu_remove(self, phone):
        self.model.delete(phone)                        
        return 'Ok'

    def menu_save(self):
        self.model.save()  
        return 'Ok'