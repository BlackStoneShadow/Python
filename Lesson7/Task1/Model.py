import json
from os.path import exists

class Phone:   

    def __init__(self, data):
        if isinstance(data, Phone):
            item = (data.number, data.type, data.name)
        elif isinstance(data, dict):
            item = tuple(data.values())
        else:
            item = tuple(data)
        
        self.number = item[0]
        self.type = item[1]
        self.name = item[2]   

class PhoneBook:

    def __init__(self, file_name):
       self.file = file_name

       self.data = list()
       if exists(file_name):
         with open(self.file) as file:                            
             data = json.load(file)['data']
             for item in data:
                self.add(Phone(item))

    def json(self):
        return json.dumps(self, default=lambda item: item.__dict__, sort_keys = False, indent = 4)

    def add(self, phone):
        self.data.append(phone)

    def delete(self, phone):
        for item in self.find(phone):
            self.data.remove(item)

    def find(self, phone):
        return filter(lambda item: Phone(item).number == phone, self.data)
    
    def save(self):
        with open(self.file, 'w') as file:
            file.write(self.json())

    def get_data(self):
        return self.data