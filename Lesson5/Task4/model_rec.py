def encode(data):    
    result = str()

    if len(data) == 0:
        return result

    char = data[0]
    for i in range(1, len(data)):
        result = str(i) + char
        if data[i] != char:
            result += encode(data[i:])
            break
    else:
        result = str(i + 1) + char
                    
    return  result