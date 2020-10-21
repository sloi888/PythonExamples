def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def double(a):
    return a * 2
def square(a):
    return a ** 2
def quadratic(a, b, c):
    x1 = ((b * -1) + ((b * b - 4 * a * c)) ** 0.5) / (2 * a)
    x2 = ((b * -1) - ((b * b - 4 * a * c)) ** 0.5) / (2 * a)
    return x1, x2
def quadraticExact(a, b, c):
    x1 = f"{(b * -1)} + √{(b * b - 4 * a * c)} over {(2 * a)}"
    x2 = f"{(b * -1)} - √{(b * b - 4 * a * c)} over {(2 * a)}"
    return x1, x2
def circleArea(radius):
    area = 3.14159 * (radius ** 2)
    return area

print(add(1, 2))  # 3
print(multiply(2, 5))  # 20
print(double(20))  # 40
print(square(9))  # 81
print(quadratic(1, 5, 6))  # x = -2, -3
print(quadraticExact(1, 5, 6))  # x = -5 + √1 over 2, -5 - √1 over 2
print(circleArea(5))  # 78.539
print(double(square(add(multiply(2, 3), 2))))
# multiply 2 * 3 = 6
# add 6 + 2 = 8
# square 8^2 = 64
# double 64 * 2 = 128
print(double(add(5, 10) + multiply(2, 5)))
# add 5 + 10 = 15
# multiply 2 * 5 = 10
# + operator 15 + 10 = 25
# double 25 * 2 = 50