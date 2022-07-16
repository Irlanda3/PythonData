import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd


df = pd.read_csv('transplantsInUSAByAge.csv')


x = np.array(df.columns)  # we take all filas from columna 5
y = np.array(df)
row_count = len(x)
print(row_count)  # It says that we have 10 rows
column_count = len(y)
print(column_count)

slope, interncept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + interncept


mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# print(r)  # Value 0.695359947071539 for boston data
