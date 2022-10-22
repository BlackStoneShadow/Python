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
                View.Print().data(self.model.find(View.Input().snils_value()))
            elif item == 'R':
                self.model.delete(View.Input().snils_value())
            elif item == 'N':
                employe = Model.Employe(View.Input().record())
                if len(list(self.model.find(employe[Model.FIELD_SNILS]))) == 0:
                    self.model.add(employe)                        
            elif item == 'T':
                employe = list(self.model.find(View.Input().snils_value()))
                if len(employe) == 1:
                    employe = employe[0]

                    View.Print().record(employe)
                    employe[Model.FIELD_DEPAR] = View.Input().department_value()
                    View.Print().record(employe)
            elif item == 'S':
                self.model.save()
