import math


def circle_area(r, pai=math.pi):
    area = pai * (r ** 2)
    return area


print('{:.2f}'.format(circle_area(5)))