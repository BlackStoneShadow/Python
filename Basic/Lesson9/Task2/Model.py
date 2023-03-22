import json
import csv
from os.path import exists
from os.path import splitext

FORMAT_JSON = 'json'
FORMAT_CSV  = 'csv'

FIELD_NAME   = 'name'
FIELD_TYPE   = 'type'
FIELD_NUMBER = 'number'

class Phone:   

    def __init__(self, data):
        if isinstance(data, Phone):
            item = (data.number, data.type, data.name)
        elif isinstance(data, dict):
            item = (data[FIELD_NUMBER], data[FIELD_TYPE], data[FIELD_NAME])
        else:
            item = tuple(data)
        
        self.number = item[0]
        self.type   = item[1]
        self.name   = item[2]   
    
class PhoneBook:

    def __init__(self, file_name):
       self.file = file_name
       self.data = list()

       self.load_ioc = dict()             
       self.load_ioc[FORMAT_JSON] = self.load_json
       self.load_ioc[FORMAT_CSV]  = self.load_csv

       self.save_ioc = dict()
       self.save_ioc[FORMAT_JSON] = self.save_json
       self.save_ioc[FORMAT_CSV]  = self.save_csv
       
       self.load_ioc.get(self.format())()
    
    def add(self, phone):
        self.data.append(phone)

    def delete(self, phone):
        for item in self.find(phone):
            self.data.remove(item)

    def find(self, phone):
        return filter(lambda item: Phone(item).number == phone, self.data)

    def format(self):
        name, ext = splitext(self.file)
        
        ext = ext[1:]

        if ext not in (FORMAT_JSON, FORMAT_CSV):
            raise Exception('Format not support')
        
        return ext

    def json(self):        
        return json.dumps(self.data, default=vars, sort_keys = False, indent = 4)        

    def load_json(self):
       if exists(self.file):
         with open(self.file) as file:                            
             data = json.load(file)
             for item in data:
                self.add(Phone(item))

    def load_csv(self):
       if exists(self.file):
         with open(self.file) as file:                
             file_csv = csv.reader(file, delimiter=';')             
             for item in file_csv:
                 self.add(Phone(item))
    
    def save(self):
        self.save_ioc.get(self.format())()

    def save_json(self):
        with open(self.file, 'w') as file:
            file.write(self.json())

    def save_csv(self):
        with open(self.file, 'w') as file:
            file_csv = csv.writer(file, delimiter=';', lineterminator='\r')
            for item in self.data:
                file_csv.writerow([item.number, item.type, item.name])           

    def get_data(self):
        return self.data
