# Machine learning - Linear Regression
# The term regression is used when you try to find the relationship between variables.
# In Machine Learning, and in statistical modeling, that relationship is used to predict
#the outcome of future events.

# https://www.w3schools.com/python/python_ml_linear_regression.asp


import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, interncept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + interncept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
