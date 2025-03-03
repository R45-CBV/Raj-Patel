def print_number_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(1, 2 * i):
            print(k, end="")
        print()

rows = 3
print_number_triangle(rows)

