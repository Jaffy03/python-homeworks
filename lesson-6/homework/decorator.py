def check(func):
    def wrapper(a, b):
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

try:   
    a=float(input("Enter a nominator: "))
    b=float(input("Enter a denominator: "))
    print(div(a, b))
except:
    print("Invalid input type")
