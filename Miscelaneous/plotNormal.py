import numpy as np
s = np.random.binomial(100, .5, 100000)

from scipy.stats import norm
import matplotlib.pyplot as plt

# Generate some data for this demonstration.
data = s
# Fit a normal distribution to the data:
avg, standard_dev = norm.fit(data)

# Plot the histogram.
plt.hist(data, bins=20, normed=True, alpha=0.6, color="blue")

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, avg, standard_dev)
plt.plot(x, p, 'k', linewidth=2)
title = "Fit results: Average = %.2f,  Standard Deviation = %.2f" % (avg, standard_dev)
plt.title(title)

plt.show()