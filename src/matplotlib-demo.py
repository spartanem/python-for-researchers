# Demo: Selective Tour of NumPy

# To run this demo in IPython, use:
#   from IPython.lib.demo import Demo
#   numpy_demo = Demo( path_to_this_file )
#   numpy_demo( )
# where 'path_to_this_file' is the path (as a string) to this file.

# Turning on some forwards-compat with Python 3.
from __future__ import (
    absolute_import     as __FUTURE_absolute_import,
    division            as __FUTURE_division,
    print_function      as __FUTURE_print_function,
)

print( """
    Welcome to matplotlib, a plotting package for Python.
""" )

# Demo examples adapated from matplotlib documentation.
# In many cases, they are stolen outright.

# <demo> --- stop ---

import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)

plt.show( )

plt.close( )

# A list of plotting commands can be found here:
#   http://matplotlib.org/api/pyplot_summary.html
# Screenshots by plot type with source code.
#   http://matplotlib.org/users/screenshots.html

# <demo> --- stop ---

# 3D plots can be made.

# A list of 3D plot types can be found here:
#   http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#toolkit-mplot3d-tutorial

# Demo of 3D line plot.
execfile( "lines3d_demo.py" )

# <demo> --- stop ---
