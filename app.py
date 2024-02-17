def addition(a,b):
    return a+b


def multiplication(a,b):
    res = a*b
    return res

def divison(a,b):
    return a/b if b != a else 0

def subtraction(a,b):
    res = a-b
    if res < 0 :
        return 0
    else:
        return res 