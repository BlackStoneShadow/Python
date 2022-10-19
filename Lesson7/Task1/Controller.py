import Model
import View

class Controller:
    def __init__(self):
        self.model = Model.PhoneBook('PhoneBook.json')

    def run(self):
        menu = View.Menu('Select menu item:')
        
        item = 'L'
        while item not in ('E'):
            item = menu.item()

            if item == 'A':
                View.Print().data(self.model.get_data())
            elif item == 'F':
                View.Print().data(self.model.find(View.Input().phone()))
            elif item == 'N':
                self.model.add(View.Input().record())                        
            elif item == 'R':
                self.model.delete(View.Input().phone())
            elif item == 'S':
                self.model.save()