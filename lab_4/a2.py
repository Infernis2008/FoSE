def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()

def draw_right_triangle(n, ch):
    for i in range(1, n + 1):
        for j in range(i):
            print(ch, end='')
        print()

def draw_frame(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print(ch, end='')
            else:
                print(' ', end='')
        print()

n = int(input("введите n: "))
m = int(input("введите m: "))
char = input("введите символ: ")

print(f"ПРЯМОУГОЛЬНИК {n}x{m}:")
draw_rectangle(n, m, char)

print("ПРАВЫЙ ТРЕУГОЛЬНИК:")
draw_right_triangle(n, char)

print(f"РАМКА {n}*{m}:")
draw_frame(n, m, char)
