def print_hello(name):
    if name != "michael":
        return f"Hello {name}"


print(print_hello("Yarin"))


def multiply(x, y):
    result1 = x * y
    result2 = x / y
    return result1, result2


bla = multiply(10, 4)
print(bla[0])
print(bla[1])
