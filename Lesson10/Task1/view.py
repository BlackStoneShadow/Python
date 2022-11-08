import model
import re

class Menu:
    def __init__(self, caption):
        self.caption = caption
    
    def view(self):        
        return '\n'.join((self.caption, '/eval (expression)', '/plog (print log)', '/clog (clear log)'))        

class Input:
    def __init__(self, text):

        if re.search('^\d+\.?\d*\s*[\+\-\*\/]\s*\d+\.?\d*$', text) != None:            
            self.value_a = re.findall('\d+\.?\d*', text)[0]
            self.value_b = re.findall('\d+\.?\d*', text)[1]
            self.value_o = text.replace(self.value_a, str()).replace(self.value_b, str()).strip()

            self.type_num = model.model_name_rac
        elif re.search('^\d+\s*[/+/-|]\s*\d+i\s*[\+\-\*\/]\s*\d+\s*[/+/-|]\s*\d+i$', text) != None:
            self.value_a = re.findall('\d+\s*[/+/-]\s*\d+i', text)[0]
            self.value_b = re.findall('\d+\s*[/+/-]\s*\d+i', text)[1]
            self.value_o = text.replace(self.value_a, str()).replace(self.value_b, str()).strip()

            self.type_num = model.model_name_kmp
        else:
            self.type_num = None
    
    def get_valua(self):
        return self.value_a

    def get_valub(self):
        return self.value_b

    def get_token(self):
        return self.value_o

    def get_typen(self):
        return self.type_num

class Print:
    def __init__(self, title):
        self.title = title

    def view_data(self, data):                
        return (f'{self.title} = {data}')

    def view_log(self, data):                        
        return (f'{self.title}\n{data}')