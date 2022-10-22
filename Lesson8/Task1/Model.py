import json
from os.path import exists
from os.path import splitext

FORMAT_JSON = 'json'
FIELDS_NAME = 'fields'
FIELD_SNILS = 'snils'
FIELD_NAMES = 'name'
FIELD_DATES = 'date'
FIELD_DEPAR = 'department'
FIELD_PHONE = 'phone'

class Employe:   

    def __init__(self, data):
        self.fields = dict()

        if isinstance(data, Employe):
            for field in data.fields:
                self.fields[field] = data.fields[field]
        elif isinstance(data, dict):
            data = data[FIELDS_NAME]
            for field in data:
                self.fields[field] = data[field]
        elif isinstance(data, tuple):
            for item in data:
                self.fields[item[0]] = item[1]

    def __getitem__(self, item):
        return self.fields[item]

    def __setitem__(self, item, value):
        self.fields[item] = value
    
class Employes:

    def __init__(self, file_name):
       self.file = file_name
       self.data = list()

       self.load_ioc = dict()             
       self.load_ioc[FORMAT_JSON] = self.load_json

       self.save_ioc = dict()
       self.save_ioc[FORMAT_JSON] = self.save_json
       
       self.load_ioc.get(self.format())()
    
    def add(self, item):        
        self.data.append(item)

    def delete(self, snils):
        for item in self.find(snils):
            self.data.remove(item)

    def find(self, snils):                
        return filter(lambda item: Employe(item)[FIELD_SNILS] == snils, self.data)

    def format(self):
        name, ext = splitext(self.file)
        
        ext = ext[1:]

        if ext not in (FORMAT_JSON):
            raise Exception('Format not support')
        
        return ext

    def json(self):        
        return json.dumps(self.data, default=vars, sort_keys = False, indent = 4)        

    def load_json(self):
       if exists(self.file):
         with open(self.file) as file:                            
             data = json.load(file)
             for item in data:
                self.add(Employe(item))

    def save(self):
        self.save_ioc.get(self.format())()

    def save_json(self):
        with open(self.file, 'w') as file:
            file.write(self.json())

    def get_data(self):
        return self.data
