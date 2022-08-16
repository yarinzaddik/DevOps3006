is_true = False
a = 2
b = 2.5
strOne = "one"
strThree = "Three"
name = ["channan", "tom", "zack", "aharon"]
print(type(a==b))
if a < b and strOne == "moshe" or strThree == "Three":
    print("a is smaller then b")
elif a == b:
    print("a equals b")
elif b > 1:
    print("blala")
else:
    print("something")

name_to_find = "ariel"
if name_to_find in name:
    print(f"We found {name_to_find}")

other_list = ["Yarin"]
if other_list:
    print("other list has values")

k = 5
f = 5
t = [1, 2, 3]
e = [1, 2, 3]
print(k == f)
print(k is f)
print(t == e)
print(t is e)
