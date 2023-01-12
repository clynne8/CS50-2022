from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break

for i in range(n):
    for j in range(n):
        if i + j >= n - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()
