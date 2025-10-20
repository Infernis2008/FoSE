x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

if (x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0):
    print("координаты не могут равняться нулю")
if (x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0):
    print("yes, 1")
elif (x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0):
    print("yes, 2")
elif (x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0):
    print("yes, 3")
elif (x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0):
    print("yes, 4")
else:
    print("no")