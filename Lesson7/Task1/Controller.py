import Model
import View

class Controller:
    def __init__(self):
        self.model = Model.PhoneBook('PhoneBook.xml')

    def run(self):
        menu = View.Menu('Select menu item:')
        
        item = '_'
        while item not in ('E'):
            item = menu.item()

            if item == 'A':
                View.Print().data(self.model.get_data())
            elif item == 'F':
                View.Print().record(self.model.find(View.Input().phone()))
            elif item == 'R':
                self.model.delete(View.Input().phone())
            elif item == 'N':
                self.model.add(View.Input().record())                        