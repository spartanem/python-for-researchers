# Demo: Selective Tour of Pandas

# To run this demo in IPython, use:
#   from IPython.lib.demo import Demo
#   pandas_demo = Demo( path_to_this_file )
#   pandas_demo( )
# where 'path_to_this_file' is the path (as a string) to this file.

# Turning on some forwards-compat with Python 3.
from __future__ import (
    absolute_import     as __FUTURE_absolute_import,
    division            as __FUTURE_division,
    print_function      as __FUTURE_print_function,
)

print( """
    Welcome to Pandas, a Python data analysis package!
""" )

# <demo> --- stop ---

# We'll use the 'numpy' package in this demo.
import numpy as np
# Of course, we'll also be using the 'pandas' package.
import pandas as pd
from pandas import (
    Series,
    DataFrame,
    Panel,
)
# We'll also grab the pretty-printer.
from pprint import pprint

# Alias the numpy random number generator for ease of reference.
randn = np.random.randn

# Note: Much of this demo is adapted from the Pandas documentation.

# <demo> --- stop ---

# A data series with labels automatically generated.
s = Series(
    randn( 5 )
)
pprint( s )

# A data series with labels supplied as a list.
s = Series(
    randn( 5 ),
    index = [ chr( i ) for i in xrange( ord( "a" ), ord( "f" ) ) ]
)
pprint( s )

# A data series, initialized from a scalar, with labels supplied as a list.
s = Series(
    42,
    index = [ chr( i ) for i in xrange( ord( "a" ), ord( "f" ) ) ]
)
pprint( s )

# A data series supplied from a 'dict'.
s = Series( { "a": 42, "b": 42, "c": 42 } )
pprint( s )

# A data series does not have to be of homogeneous type.
# However, many of the manipulation which you'll perform probably assume
# homogeneity.
s = Series( { "a": 42, "b": "foo", "c": 42J } )
pprint( s )

# <demo> --- stop ---

s = Series(
    randn( 5 )
)
pprint( s )

# Data series are not only Python sequences but also act like NumPy 'ndarray'
# objects.
print( s[s > s.median()] )
pprint( np.exp(s) )

# Data series act like Python 'dict' objects as well.
print( 1 in s )

# Labels with no corresponding values use NaN for their missing values.
# This is true both during series initialization and alignment.
pprint( s[ 1 : ] + s[ : -1 ] )

# <demo> --- stop ---

# 'DataFrame' objects are 2D.
# They can be created from a 'dict' of Series objects, a 2D array, etc...

df = DataFrame( { "col1": randn( 4 ), "col2": randn( 4 ) } )
pprint( df )

df = DataFrame( randn( 6, 4 ), columns=[ 'A', 'B', 'C', 'D' ] )
pprint( df )

# A number of selection operations are available.
# For example, you can select a particular row across columns.
pprint( df.xs( 3 ) )

# Series can be used to perform vectorized ("broadcasted") operations
# against DataFrames.
pprint( df - df.ix[ 2 ] )

# The transpose of a DataFrame can easily be found.
pprint( df.T )

# Matrix multiplication can be performed on DataFrames.
pprint( df.T.dot(df) )

# <demo> --- stop ---

# Pandas can directly read CSV files into data frames.
df = pd.read_csv( "demo_data_1.csv" )
pprint( df )

# <demo> --- stop ---

# 'Panel' objects are 3D.

wp = Panel( {
    'Item1' : DataFrame(randn(4, 3)),
    'Item2' : DataFrame(randn(4, 2))
} )
pprint( wp )

# There are also 'TimeSeries', 'SparseSeries', and 'SparsePanel' objects.
# In newer versions, there is experiemental support for higher-dimensional
# panels.

# Stats can also be performed on Pandas objects.
df = DataFrame( randn( 6, 4 ), columns=[ 'A', 'B', 'C', 'D' ] )
pprint( df )

# You can choose which axis number to perform the operation along.
pprint( df.mean( 0 ) )
pprint( df.mean( 1 ) )

# Much more to Pandas, but that's the basic idea.

# For more information, see:
#   http://pandas.pydata.org/pandas-docs/stable/index.html
# Also, definitely have a look at StatsModels:
#   http://statsmodels.sourceforge.net/
#   http://statsmodels.sourceforge.net/stable/

# <demo> --- stop ---
