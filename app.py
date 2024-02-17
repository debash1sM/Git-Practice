def addition(a,b):
    return a+b


def multiplication(a,b):
    if a < 0 or b < 0:
        a = a * 1
        b = b * 1 

    return a*b

def divison(a,b):
    return a/b if b != a else 0

def subtraction(a,b):
    return a-b