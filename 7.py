#הוספת else בתנאי שאין breake
for i in range(1, 101):
    if i % 7 == 0 or "7" in str(i):
        continue
    print(i)
else:
    print("loop finished successfully")