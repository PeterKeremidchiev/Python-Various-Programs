
operators = {
    '/': lambda x, y: x / y,
    '*': lambda x, y: x * y,
    '-': lambda x, y: x - y,
    '+': lambda x, y: x + y,
    '^': lambda x, y: x ** y,
}

def math_operation(a):
    num_1, operator, num_2 = a.split()
    return operators[operator](float(num_1), float(num_2))

