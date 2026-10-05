def is_triangle(a, b, c):
    if a > b + c or b > c + a or c > b + a:
        print("No")
    else:
        print ("Yes")


print(is_triangle(1, 2, 3))
print(is_triangle(12, 1, 1))