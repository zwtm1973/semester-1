
import matplotlib.pyplot as plt  # import library
import numpy as np

x = [ k for k in range(30) ]  # create a range for the data
y = [ np.sqrt(k) for k in x ]      # create a simple function y=x^2

plt.plot(x,y)  # create a 2d plot

plt.xlabel('x')
plt.ylabel('y=x^2')  # annotate

plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions

fig, ax = plt.subplots()
plt.bar(x,y, width= 1, edgecolor = "white", linewidth = 0.7)

ax.set(xlim=(0, 10), xticks=np.arange(1, 10),
       ylim=(0, 10), yticks=np.arange(1, 10))

plt.show()