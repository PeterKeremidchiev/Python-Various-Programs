def multiply(times):
    def decorator(function):
        def wrapper(*args):
            result = 0
            for i in range(times):
                result += function(*args)
            return result
        return wrapper
    return decorator


@multiply(5)
def add_ten(number):
 return number + 10
print(add_ten(6))