#from model_rec import encode
#from model_rec import decode
#from model_gen import encode
#from model_gen import decode
import model_rec
import model_gen

model_name_rec = 'rec'
model_name_gen = 'gen'

encode_ioc = dict()
decode_ioc = dict()

model = None

def init(value):
    global model

    if value not in (model_name_rec, model_name_gen):
        raise Exception('Model not support!')        

    model = value

    encode_ioc[model_name_rec] = model_rec.encode
    encode_ioc[model_name_gen] = model_gen.encode

    decode_ioc[model_name_rec] = model_rec.decode
    decode_ioc[model_name_gen] = model_gen.decode

def get():
    result = None   
    while result not in (model_name_rec, model_name_gen):
        result = input('Model({}):'.format(' or '.join((model_name_rec, model_name_gen))))
    
    return result

def encode(data):
    return encode_ioc.get(model)(data)

def decode(data):
    return decode_ioc.get(model)(data)