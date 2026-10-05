def is_between(x, y ,z):
    if x < y < z or z < y < x:
        return True
    else:
        return False

print(is_between(1, 2, 3))
print(is_between(1, 3, 2))
print(is_between(3, 2, 1))