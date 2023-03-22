import Racl as rac
import Komp as kmp

model_name_rac = 'rac'
model_name_kmp = 'kmp'

model_name_sum = 'sum'
model_name_sub = 'sub'
model_name_div = 'div'
model_name_mlt = 'mult'
model_name_int = 'init'

model_ioc = dict()

def init(in_a, in_b, type_num):
    if type_num not in (model_name_rac, model_name_kmp):
        raise Exception('Model not support!')            

    if type_num == model_name_rac:
        model_ioc[model_name_int] = rac.init
        model_ioc[model_name_mlt] = rac.mult
        model_ioc[model_name_div] = rac.div
        model_ioc[model_name_sum] = rac.sum
        model_ioc[model_name_sub] = rac.sub
    else:
        model_ioc[model_name_int] = kmp.init
        model_ioc[model_name_mlt] = kmp.mult
        model_ioc[model_name_div] = kmp.div
        model_ioc[model_name_sum] = kmp.sum
        model_ioc[model_name_sub] = kmp.sub

    model_ioc.get(model_name_int)(in_a, in_b)
            
def mult():
    return model_ioc.get(model_name_mlt)()   # указать функцию

def sum():
    return model_ioc.get(model_name_sum)()   # указать функцию

def div():
    return model_ioc.get(model_name_div)()   # указать функцию

def sub():
    return model_ioc.get(model_name_sub)()   # указать функцию



