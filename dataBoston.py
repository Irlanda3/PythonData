import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd

from sklearn.datasets import load_boston

df = pd.read_csv('transplantsInUSAByAge.csv')
# print(df)
boston = load_boston()

print(type(boston))

x = np.array(boston.data[:, 5])  # we take all filas from columna 5
y = np.array(boston.target)
print(type(x))

slope, interncept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + interncept


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

print(r)  # Value 0.695359947071539
