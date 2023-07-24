class store_results:

    logfile = 'results.txt'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        result = self.func(*args)
        log_string = f"Function '{self.func.__name__}' was called. Result: {result}"
        with open(self.logfile, 'a') as file:
            file.write(log_string + "\n")


@store_results
def add(a, b):
    return a + b
@store_results
def mult(a, b):
    return a * b
add(2, 2)
mult(6, 4)