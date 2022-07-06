import numpy as np
from matplotlib import pyplot as plt
import math

def f(x0):
    return x0 ** 2 - 1 - x0

x = list(np.arange(-3, 3, 0.01))
y = list(map(f, x))
plt.plot(x,y)
x_0 = 10000
x_1 = 1.3
result_analysis = []
idx = 0
while abs(x_0 - x_1) > 1e-10:
    x_0 = x_1
    x_1 = math.sqrt(x_0 + 1)
    result_analysis.append(x_1)
    if idx > 100:
        break
    idx += 1
    print(idx)
plt.plot(result_analysis)
# mark
