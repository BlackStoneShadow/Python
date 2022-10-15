import model
from model import encode
from model import decode
from view import read_data
from view import write_data

def run():       
    model.init(model.get())
    write_data('FileEncode.txt', encode(read_data('FileDecode.txt')))
    write_data('FileDecode.txt', decode(read_data('FileEncode.txt')))
