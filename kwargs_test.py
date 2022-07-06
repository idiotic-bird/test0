import numpy as np


def process2(T, theta, delta):
    sum0 = 0
    sum1 = 0
    num1 = 0
    k = 1
    visual_list = np.zeros(T // delta + 1)
    while sum0 < T:
        tau = np.random.exponential(theta)
        sum1 += tau
        num1 += 1
        if sum1 > delta * k:
            while sum1 > delta * k:
                visual_list[k] = num1
                k += 1
        sum0 = sum1
    print(visual_list)
    return visual_list

process2(10, 1, 1)