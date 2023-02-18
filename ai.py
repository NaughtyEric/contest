import numpy

numdta = [567848, 870465, 1665877, 1897171, 1950325, 2002005, 2048834]
date = [1, 2, 3, 4, 5, 6, 7]
numdta = numpy.array(numdta)
date = numpy.array(date)

# use logistic function to fit the data
def logistic_function(x, a, b, c):
    return a / (1 + b * numpy.exp(-c * x))

# use curve_fit to fit the data
from scipy.optimize import curve_fit
popt, pcov = curve_fit(logistic_function, date, numdta, p0=(2e6, 1, 1))

# estimate 4 ~ 11
future = numpy.arange(4, 11, 1)
future = numpy.array(future)
future_numdta = logistic_function(future, *popt)

# add random noise
future_numdta = future_numdta + numpy.random.normal(0, 25000, future_numdta.shape)

covid_influence = 1.01
for i in range(0, len(future_numdta)):
    future_numdta[i] = future_numdta[i] * covid_influence
    

print(future_numdta)

# plot the data and function
import matplotlib.pyplot as plt
plt.plot(date, numdta, 'o', label='data')
plt.plot(range(1, 20), logistic_function(range(1, 20), *popt) + numpy.random.normal(0, 25000, 19), label='fit')
plt.xlabel('date') 
plt.ylabel('numdta')
plt.legend()
plt.show()
