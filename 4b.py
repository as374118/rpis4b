import numpy as np;
import random as rand;
import math;

def f(x):
    if x > 1 or x < -1:
        return -1;
    return 2 * ((1 - x * x) ** 0.5);


def sample(N):
    if N < 0:
        return [];
    res = np.zeros(N);
    
    for i in range(N):
        res[i] = np.random.uniform(-1, 1);
    return res;

def countIntegral(points):
    res = 0;
    points.sort();
    N = len(points);
    for i in range(N - 1):
        length = points[i + 1] - points[i];
        height = (f(points[i + 1]) + f(points[i])) / 2.0;
        res += length * height;
    return res;

def mainFunction(N):
    return countIntegral(sample(N));

print(mainFunction(NTEST));