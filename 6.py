print(list(range(3)))
print(list(range(1, 17)))
print(list(range(17, 2, -3)))
for i in range(7):
    print("Hello World")
names = ["1", "2", "3"]
for name in names:
    print(name, end=" ")

for i in range(len(names)):
    names[i] = "dotan"

a = 0
while a < 5:
    print(a)
    a = a + 1
for name in names:
    if name == "zack":
        break
    print(name)
for name in names:
    if name == "zack":
        continue
    else:
        pass
    print(name)