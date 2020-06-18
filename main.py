import numpy as np
import scipy
import matplotlib.pyplot as plt
import random


def func(k, x, y=None):
    error = []
    for x_ in x:
        error += [sum([k_*x_**power_ for k_, power_ in zip(k, range(len(k)))])]
    error = np.array(error)
    if y:
        error = np.abs(error - np.array(y)).mean()
    return error


class KHandler:
    def __init__(self, k, x, y):
        self.k = k
        self.x = x
        self.y = y
        self.error = None

    def calculate(self):
        self.error = func(self.k, self.x, self.y)


class GenAlg:
    def __init__(self, x, y, power_polynom, step=1, tol=0.001, childs=10):
        self.step = step
        self.x = x
        self.y = y
        self.tol = tol
        self.power_polynom = power_polynom
        self.childs = childs
        self.best_k = [0 for i in range(self.power_polynom)]
        self.alpha = None
        self.best_err = None
        self.first_err = None
        self.counter = 0

    def calculate(self):
        def get_first_error():
            tmp = KHandler(self.best_k, self.x, self.y)
            tmp.calculate()
            self.best_err, self.first_err = tmp.error, tmp.error

        get_first_error()
        while True:
            self.counter += 1
            self.alpha = self.best_err / self.first_err
            samples = [KHandler([k_ + random.uniform(-self.step, self.step) * self.alpha
                                 for k_ in self.best_k], self.x, self.y) for k in range(self.childs)]
            for sample in samples:
                sample.calculate()
                # print(sample.error)
                if sample.error < self.best_err:
                    self.best_err = sample.error
                    self.best_k = sample.k
            print('step -', self.counter, 'error -', self.best_err)
            if self.best_err < self.tol:
                print('best error -', self.best_err)
                s = ''
                print('function:', s.join(f'+ {k_}*x**{power_} '
                                          for k_, power_ in zip(self.best_k, range(len(self.best_k)))))
                break

    def plot(self):
        x_new = np.linspace(min(self.x), max(self.x), num=500)
        plt.plot(x_new, func(self.best_k, x_new))
        plt.show()


#x = [0, -1, 1]
#y = [1, 2, 2]
#power_polynom = 3
#cl = GenAlg(x, y, power_polynom)
#cl.calculate()
#cl.plot()
