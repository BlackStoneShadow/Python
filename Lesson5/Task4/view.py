def read_data(file_name):
    with open(file_name, 'r') as data:
        return data.readline()

def write_data(file_name, text):
    with open(file_name, 'w') as data:
        return data.write(text)

