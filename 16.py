def get_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("age can not be negative")

try :
    get_age()
except ValueError as e:
    if len(e.args) > 0:
        if e.args[0] == "age can not be negative":
            print("blablabla")
        else:
            print(e.args)

