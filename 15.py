try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("could not divide by zero")
except ValueError:
    print("Enter a legal number")
except BaseException as e:
    print("something went wrong")
    print(e.args)

