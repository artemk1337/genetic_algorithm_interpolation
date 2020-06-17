import numpy as np
import scipy
import matplotlib.pyplot as plt
import random


# k: [1, 2, 3, 4...] => 1 + 2x + 3x^2 + 4x^3 + ...

# k = [0, 1]


def func(k, x, y=None):
    error = []
    for x_ in x:
        error += [sum([k_*x_**power_ for k_, power_ in zip(k, range(len(k)))])]
    error = np.array(error)
    if y:
        error = np.abs(error - np.array(y)).mean()
    return error


#print(func(k, x, y))

#x_new = np.linspace(min(x), max(x), num=500)
#plt.plot(x_new, func(k, x_new))
#plt.show()


class KHandler:
    def __init__(self, k, x, y):
        self.k = k
        self.x = x
        self.y = y
        self.error = None

    def calculate(self):
        self.error = func(self.k, self.x, self.y)


x = [1, 2, 3]
y = [8, 6, 4]
best_k = [0, 0]
best_err = np.inf
tol = 0.001
counter = 0
while True:
    counter += 1
    samples = [KHandler([k_ + random.uniform(-1, 1) for k_ in best_k], x, y) for k in range(10)]
    for sample in samples:
        sample.calculate()
        #print(sample.error)
        if sample.error < best_err:
            best_err = sample.error
            best_k = sample.k
    print(counter, best_err)
    if best_err < tol:
        print(best_err)
        print(best_k)
        break

x_new = np.linspace(min(x), max(x), num=500)
plt.plot(x_new, func(best_k, x_new))
plt.show()
