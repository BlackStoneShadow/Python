class Phone:
    
    def __init__(self, type, number, name):
        self.type = type
        self.number = number
        self.name = name

class Phone_(Phone):

    def __init__(self, data):
        item = list(data)
        if len(item) == 3:
            self.type = item[0]
            self.number = item[1]
            self.name = item[2]

class PhoneBook:

    def __init__(self, file_name):
        self.data = list()

    def add(self, phone):
        self.data.append(phone)

    def delete(self, phone):
        for item in self.find(phone):
            self.data.remove(item)

    def find(self, phone):
        return filter(lambda item: Phone_(item).number == phone, self.data)

    def get_data(self):
        return self.data