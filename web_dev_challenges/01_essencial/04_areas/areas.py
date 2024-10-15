import math

def circle_area(radius):
    pi = 3.14
    area = pi*radius**2
    return(round(area,2))


def square_area(side):
    area = side**2
    return(area)

def rectangle_area(side, base):
    area = side*base
    return(area)

print(circle_area(1),
      circle_area(2),
      circle_area(12),
      circle_area(16))