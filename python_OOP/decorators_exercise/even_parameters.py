def even_parameters(func):
    def wrapper(*args):
        flag = False
        for arg in args:
            if not isinstance(arg, int) or arg % 2 != 0:
                flag = True
                break
        if flag:
            return "Please use only even numbers!"
        else:
            return func(*args)
    return wrapper


@even_parameters
def add(a, b):
    return a + b
print(add(2, 4))
print(add("Peter", 1))















