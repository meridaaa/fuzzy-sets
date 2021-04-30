import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
import math


def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


def TrapezidoalMf(X, a, b, c, d):
    Y = []
    crossover = []
    cross = []
    y = -1
    for x in X:
        y = max(min(min(((x - a) / (b - a)), 1), ((d - x) / (d - c)), 1), 0)
        if (y >= 0 and y < 1):
            cross.append([y, x])
        Y.append(y)
    a = closest([i[0] for i in cross], 0.5)
    for i in cross:
        if (i[0] == a):
            crossover.append(a)
            crossover.append(i[1])
    return Y, crossover


X = [(i / 700) for i in range(-7000, 7000)]
print('Maghadire a, b, c, d ra vared koind.')
a, b, c, d = float(input('a: ')), float(input('b: ')), float(input('c: ')), float(input('d: '))
y, crossover = TrapezidoalMf(X, a, b, c, d)

plt.plot(X, y, '-b')
plt.scatter(crossover[1], crossover[0])
plt.show()  