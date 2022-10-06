import random

def generate_superscript(x, n):
    if n == 0:
        return str(x)
    if n == 1:
        return str(x)+"x"
    superscript = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    result = str(x)
    if x != 0:
        result += "x"
    for i in str(n):
        result += superscript[int(i)]
    return result

def generate_polynomial(k):
    result = []
    for i in range(k, -1, -1):
        coefficient = random.randint(0, 100)
        if coefficient != 0:
            result.append(generate_superscript(coefficient, i))
    return "+".join(result)


print(generate_polynomial(10))
