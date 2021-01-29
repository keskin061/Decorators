class Decorator(object):
    def __init__(self, function):
        self.function = function

    def __call__(self):
        print(f"first")
        print(self.function)
        print(f"last")


@Decorator
def function_0():
    return "function_0"


function_0()
