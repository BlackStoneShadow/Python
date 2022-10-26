from Model import Phone

class Menu:
    def __init__(self, caption):
        self.caption = caption
    def view(self):
        
        return '\n'.join((self.caption, '/All', '/New Phone Type Name', '/Remove Phone', '/Find Phone', '/Save'))        

    def item(self):
        self.view()

        item = str()
        while item not in self.items():
            item = input(self.caption)
        
        return item

class Print:
    def record(self, item):
        phone = Phone(item)

        return '\n'.join((f'Phone:{phone.number}', f'Type:{phone.type}', f'Name:{phone.name}', '\n'))                   

    def data(self, data):        
        result = str()
        for item in data:
            result += self.record(item)                            
        
        return result
