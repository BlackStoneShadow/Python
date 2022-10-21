import Model
import View

class Controller:
    def __init__(self):
        self.model = Model.Employes('Employes.json')

    def run(self):
        menu = View.Menu('Select menu item:')
        
        item = '_'
        while item not in ('E'):
            item = menu.item()

            if item == 'A':
                View.Print().data(self.model.get_data())
            elif item == 'F':
                View.Print().data(self.model.find(View.Input().snils()))
            elif item == 'N':
                employe = Employe(View.Input().record())
                test = employe[Model.FIELD_SNILS]
                if count(self.model.find(employe[Model.FIELD_SNILS])) == 0:
                    self.model.add()                        
            elif item == 'R':
                self.model.delete(View.Input().snils())
            elif item == 'S':
                self.model.save()
