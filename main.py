from pyDatalog import pyDatalog
import random

pyDatalog.create_terms('X, Z, Y, Sm, div, Average, y, SumRand')

# Сумма
(y[X] == running_sum_(Y, for_each=Y)) <= ((Y._in(range_(X + 1))))
print(y[999999] == Sm)

# Среднее
(div[X, Y] == Z) <= (X // Y == Z)
print(div[y[99999], 99999] == Average)

# Медиана
H = sorted([random.choice(range(99999)) for i in range(100)])
print("Median: ", (H[49] + H[50]) / 2)

# Произведение
import functools
print (functools.reduce(lambda a, b : a * b, [random.choice(range(99999)) for i in range(100)]))