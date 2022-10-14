model = None

def init():
    global model
    while model not in ('rec', 'gen'):
        model = input('Model(rec or gen):')

if model == 'rec':
    from model_rec import encode
    from model_rec import decode
else:
    from model_gen import encode
    from model_gen import decode