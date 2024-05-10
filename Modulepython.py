def funmath(x):
    from math import sin, cos
    y = sin(x) - cos(x) + sin(x) * cos(x)
    print(y)
    return y


funmath(60)
