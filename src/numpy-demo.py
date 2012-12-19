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
    Welcome to NumPy, an efficient linear algebra package for Python.
""" )

# <demo> --- stop ---

# For this demo, we'll be using a number of pieces from the 'numpy' package.
from numpy import *
# The pretty-printer from the Python standard library might also be useful.
from pprint import pprint

# Note: Most pieces of this demo are adapted from the NumPy documentation.

# Arrays are bread-and-butter of NumPy.
# They can be created in various ways, including from Python iterators.
a = array( xrange( 10 ) )
print( a )
print( type( a ) )

# NumPy is known for its memory efficiency and speed.
# This is because it stores efficient arrays of the raw data,
# as opposed to arrays of Python objects, each wrapping a piece of raw data.
# This is also because operations are performed on the raw data directly
# without the overhead of accessing it trhough Python objects.
# NumPy arrays much be homogeneous to obtain these benefits.
# Thus, each numpy array has a type associated with it.
print( a.dtype )

# <demo> --- stop ---

# Arrays of purely zeroes or ones can be easily created.
# Specific data types can also be specified for the generated data.
pprint( zeros( [ 3, 4 ] ) )
pprint( ones( [ 4, 3 ] ,dtype = complex64 ) )

# 'arange' is imilar to 'range', except that it creates 'ndarray' types
# and it can take floatig-point reals as arguments.
pprint( arange( 0, 2, 0.3 ) )
# 'linspace' allows for an array to be created which has numbers spaced at
# uniform intervals from one another without knowing the interval in
# advance - only the number of divisions.
pprint( linspace( 0, 2, 9 ) )

# Lower dimensional arrays can be reshaped into higher dimensional ones.
pprint( arange( 24 ).reshape( 2, 3, 4 ) )

# <demo> --- stop ---

# Many operations have a vectorized form available.
pprint( a ** 2 )
pprint( sin( a ) )
pprint( a < 4 )

# Both dot products and pairwise multiplications are supported.
b = array( a )
pprint( a * b )
pprint( dot( a, b ) )

# Arrays can be sliced as sequences.
pprint( a[ 2 : 5 ] )
pprint( a[ : : 3 ] ) # every 3rd element between start and end

# Arrays can be transposed.
a.shape = 5, 2
pprint( a )
pprint( a.transpose( ) )

# <demo> --- stop ---

## Linear Algebra ##
from numpy,linalg import *

a = array( [ [ 1, 3 ], [ 5, 7] ] )
pprint( a )
b = array( xrange( 3, 1, -1 ) )
pprint( b )

# "eye"-dentity matrix
pprint( eye( 4 ) )
# Inverse of a matrix
pprint( inv( a ) )

# Trace
pprint( trace( a ) )
# Determinant
pprint( det( a ) )
# Norm
pprint( norm( a ) )

# Linear Solver
pprint( solve( a, b ) )

# Eigenvalues and eigenvectors.
pprint( eig( a ) )

# <demo> --- stop ---

# Much more in this package.
# For more details, see:
#   http://www.scipy.org/Tentative_NumPy_Tutorial
#   http://docs.scipy.org/doc/numpy/reference/

# <demo> --- stop ---
