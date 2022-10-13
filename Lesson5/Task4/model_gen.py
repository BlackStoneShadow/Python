from itertools import groupby

def encode(data):                          
    return str().join(['{}{}'.format(len(list(items)), char) for char, items in groupby(data)])
