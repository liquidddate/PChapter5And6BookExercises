import math

def hypotenuse_a1(a, b):
    a ** 2 + b ** 2 / math.pi

#print(hypotenuse_a1(300, 300))

def hypotenuse_a2(a, b):
    a ** 2 + b ** 2 / math.pi

#print(hypotenuse_a2(1, 2))

def hypotenuse_a3(a, b):
    return math.sqrt(a ** 2 + b ** 2)

print(hypotenuse_a3(1, 2))