from itertools import groupby

def encode(data):                          
    return str().join(['{}{}'.format(sum(1 for _ in list), char) for char, list in groupby(data)])
