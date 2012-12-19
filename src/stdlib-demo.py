# Demo: Selective Tour of the Python Standard Library

# To run this demo in IPython, use:
#   from IPython.lib.demo import Demo
#   stdlib_demo = Demo( path_to_this_file )
#   stdlib_demo( )
# where 'path_to_this_file' is the path (as a string) to this file.

# Turning on some forwards-compat with Python 3.
from __future__ import (
    absolute_import     as __FUTURE_absolute_import,
    division            as __FUTURE_division,
    print_function      as __FUTURE_print_function,
)

print( """
    Welcome to the Python standard library!
""" )

# <demo> --- stop ---

### 'sys' Module ###
import sys

# Python version.
print( sys.version_info )
# Python implementation.
# 'CPython' is the standard Python interpreter, written in C.
# There are other implementations out there:
#   Jython (Python on Java VM)
#   IronPython (Python on Microsoft .Net VM)
#   PyPy (Python on LLVM with just-in-time compilation - more on this later)
#   some others (Stackless, etc...) plus extensions (Cython, Numba, etc...)
print( sys.subversion )

# Where is this Python installed?
print( sys.prefix )
print( sys.executable )

# Where does Python look for modules during import?
# Can be augmented with the 'PYTHONPATH' environment variable in your shell.
print( sys.path )

# <demo> --- stop ---

### 'sys' Module ###

# Maximum value of 'int' value before it automatically becomes a 'long'.
# A 32-bit 'int' maxes out at 2147483647.
# A 64-bit 'int' maxes out at 9223372036854775807.
print( sys.maxint )
# Maximum amount of memory which can be addressed,
# largest file which can be fully accessed, etc....
print( sys.maxsize )

# Valuable information on the 'float' type.
# If 'dig' (maximum precision) is 15 digits, then the float is 64-bit.
print( sys.float_info )

# Dictionary of loaded modules with their corresponding paths.
# (Potentially too much information - not showing in the demo.)
#print( sys.modules )

# <demo> --- stop ---

### 'sys' Module ###
from __future__ import print_function

# Standard streams.
# Similar to 'stdin', 'stdout', and 'stderr' from C library's <stdio.h> header.
# They are file stream objects in Python.
print( map( type, [ sys.stdin, sys.stdout, sys.stderr ] ) )
# 'print' writes to 'sys.stdout' be default.
# You can write to 'sys.stderr' instead:
print( "Test output on 'stderr'.", file = sys.stderr )
# A good practice is to write diagnostics, such as errors or traces to 'stderr',
# and the output from normal program execution to 'stdout'.

# Script arguments vector.
# Similar to 'argv' supplied to 'main' in C programs.
# However, no need for 'argc' because 'sys.argv' is a list (has '__len__').
# The argument list for an interactive session is usually not too exciting.
print( sys.argv )
print( len( sys.argv ) )
# Later in this demo, we'll learn a very easy way to parse these arguments.
# If you are used to changing parameters in code and recompiling every time,
# then stop doing that! (You're wasting time.)
# Supplying command-line arguments is flexible and easy in Python.

# Another way to quit Python:
# sys.exit( 0 )
# An exit code of 0 usually indicates succesful completion of program.
# A non-zero exit code indicates a failure of some sort.
# The documentation on the 'os' module provides some common failure codes.
# Look at the 'EX_' things in:
#   http://docs.python.org/2/library/os.html#process-management
# But, there is no true standard in this regard.

# <demo> --- stop ---

### 'pprint' Module ###
# A "pretty printer" for Python.
# Displays complicated data in a generally nicer format than 'print'.
from pprint import pprint, pformat, PrettyPrinter

# A nested list.
ls = [ [ [ i, j ] for j in xrange( 7 ) ] for i in xrange( 6 ) ]
# The nested list displayed with 'print'. Hard to read, isn't it?
print( ls )
# The nested list displayed with the pretty printer.
pprint( ls )
# See: help( pprint )

# You can also capture string representations of pretty printed output...
s = pformat( ls )
print( type( s ) )
# ... and use them later:
print( s )
# See: help( pformat )

# You can create your own pretty printers with default settings.
pp = PrettyPrinter( 4, stream = sys.stderr )
pp.pprint( ls )
# See: help( PrettyPrinter )

# Also see: http://docs.python.org/2/library/pprint.html

# <demo> --- stop ---

### 'os.path' Module ###
# Platform-independent file path handling.
# (Additional functions are added to module depending on platform,
#   but the core is platform-independent.)
# There is really no reason why your code should be limited to one platform,
# such as Linux, MacOS X, or Windows. No extra work is required in most cases.
from os.path import (
    abspath     as path_absolute,
    relpath     as path_relative,
    curdir      as path_curdir,
    pardir      as path_pardir,
    extsep      as path_extsep,
    join        as path_join,
)

# Transform to the absolute path to the current directory.
print( path_absolute( path_curdir ) )
# Transform to the relative path to the parent directory.
print( path_relative( path_pardir ) )

# Join various elements together into a path.
# Is like p1 + os.path.dirsep + p2 etc....
print( path_join( path_curdir, "stdlib-demo" + path_extsep + "py" ) )

# <demo> --- stop ---

### 'os.path' Module ###
from os.path import(
    expanduser  as path_expand_user,
    dirname     as path_dirname,
    basename    as path_basename,
)

# Discover the path to a home directory.
# Performs Unix shell-like "tilde expansion". (Works on Windows too.)
print( path_expand_user( "~" ) )
# Useful for finding a user's configuration files.

# Find the directory name portion of a path.
# Like Unix 'dirname' command.
print( path_dirname( path_expand_user( "~" ) ) )
# Find the file name portion of a path.
# Like Unix 'basename' command, but doesn't filter extensions.
print( path_basename( path_join(
    path_curdir,
    "stdlib-demo" + path_extsep + "py"
) ) )

# <demo> --- stop ---

### 'os.path' Module ###
from os.path import(
    exists      as path_exists,
)

# Test for the existence of a file.
# Note: If you need to check permissions on a file,
#       then use the 'os.access' or 'os.stat' callables or the 'stat' module,
#       some pieces of which are in the 'os.path' module.
print( path_exists( path_join(
    path_curdir,
    "stdlib-demo" + path_extsep + "py"
) ) )

# Tip:
#   If you need to search a directory tree, then take a look at 'os.path.walk'.
#   Also recommended:
#       http://docs.python.org/2/library/glob.html
#       http://docs.python.org/2/library/fnmatch.html

# See also:
#   dir( os.path )
#   http://docs.python.org/2/library/os.path.html

# <demo> --- stop ---

### 'os' Module ###
# Wrapper for many common Unix system calls and C library functions.
# In this demo, we will ignore most of them and briefly mention only a few of
# the module's attributes.
from os import (
    getcwd,
    environ     as envvars,
    devnull     as os_devnull,
    linesep     as os_linesep,
)
from os.path import pathsep as path_pathsep

# Absolute path to current working directory.
print( getcwd( ) )

# Dictionary-like container for environment variables.
print( "path" in envvars )
pprint( envvars[ "path" ].split( path_pathsep ) )
# You can also use the 'os.getenv' and 'os.putenv' callables.

# Name of the platform's "bit bucket".
# 'nul' on DOS/Windows; '/dev/null' most everywhere else.
print( os_devnull )

# Text line terminators for the platform.
# '\r\n' on DOS/Windows; '\r' on old MacOS (pre-X); '\n' most everywhere else.
print( os_linesep )
# Python generally writes text files using the line separator for the
# platform it is running on and so you do not usually have to be aware of
# a particular line separtor.

# <demo> --- stop ---

### 'collections' Module ###
# Contains various sequence and map types, which are not built-in to Python.
# Also provides a type hierarchy, which can be useful with
# 'issubclass' and 'isinstance'.
import collections
from collections import (
    Counter,
)

# Instances and subclasses of abstract types.
# (For more about abstract types, see:
#   http://docs.python.org/2/library/abc.html )
print( isinstance( "abc", collections.Sequence ) )
print( isinstance( ls, collections.Sequence ) )
print( isinstance( list, collections.Callable ) )
print( issubclass( list, collections.Mapping ) ) # false
print( issubclass( dict, collections.Mapping ) )

# Counting objects, the harder way.
ls = [ 1, 1, 3, 4, 1, 3, 2 ]
d = { }
for k in ls:
    if k in d:
        d[ k ] += 1
    else:
        d[ k ] = 1
print( d[ 3 ] )
# Counting objects, the easier way.
d = Counter( ls )
print( d.most_common( ) )
print( d[ 3 ] )

# <demo> --- stop ---

### 'collections' Module ###
from collections import (
    defaultdict,
    OrderedDict,
)

# What happens if you access a 'dict' with a non-existent key?
d = { }
try:
    print( d[ 42 ] )
except KeyError as exc:
    print( exc )
# You could use the 'get' method to be safe (by providing a default value),
# but that can also get old after awhile.
print( d.get( 42, 0 ) )
# Or you could use a 'defaultdict'.
# Note: You must supply a callable. This allows for dynamic behavior.
d = defaultdict( lambda: 0 )
print( d[ 42 ] )

## OrderedDict ##
s = "Hello, world!"
ls = zip( s, map( ord, s ) )
pprint( ls )
d = dict( ls )
# Side Note: Python 2 'items' method creates an entire list.
#            Python 2 'iteritems' method iterates element-by-element.
#            Only use 'items' when you know your memory requirements are low.
#            Python 3 only provides 'items', which acts like 'iteritems'.
pprint( d.items( ) )
d = OrderedDict( ls )
pprint( d.items( ) )

# <demo> --- stop ---

### 'collections' Module ###
from collections import namedtuple

# Named tuples are a great alternative to anonymous tuples in most cases.
# The 'namedtuple' callable is a "class factory".
# It creates classes of named tuples, which you can then use to create
# named tuples.
TruthTableRow = namedtuple( "TruthTableRow", "p q v" )
print( type( TruthTableRow ) )
ttrow = TruthTableRow( 0, 1, 0 )
print( type( ttrow ) )
pcol = [ 0, 0, 1, 1 ]
qcol = [ 0, 1, 0, 1 ]
# Truth table for 'and'.
pprint( map( lambda p, q: TruthTableRow( p, q, p and q ), pcol, qcol ) )
# Truth table for 'or'.
pprint( map( lambda p, q: TruthTableRow( p, q, p or q ), pcol, qcol ) )

# The elements of named tuples can be accessed by either name or position.
print( ttrow[ 0 ] == ttrow.p )

# See also: http://docs.python.org/2/library/collections.html
    
# <demo> --- stop ---

### 'math' Module ###
# Mathematical functions on floating-point real numbers.
import math
from math import (
    floor, ceil, trunc,
    factorial, sqrt, hypot,
    log, log10, exp,
    sin, cos, tan, sinh, cosh, tanh,
    asin, acos, atan, atan2,
)

pprint( dir( math ) )

# EXERCISE:
#   (1) Convert 77.2913 degrees to radians.
#   (2) Then display the cosine of that value.
#   Hint: Look at the attributes listing and use the 'help' built-in as needed.

# EXERCISE:
#   (1) Calculate the arctangent of 1.
#   (2) Multiply that value by 4 and compare the result to pi.
#   Hint: 'pi' and 'e' are constants in the 'math' module.

# Hypoteneuses from pairs of successive integers.
pprint( map( hypot, xrange( 1, 10 ), xrange( 2, 11 ) ) )

## Floor, Ceiling, and Trunction ##
ls = [ -3.5, -3.49, 3.49, 3.5 ]
print( map( round, ls ) )
print( map( trunc, ls ) )
print( map( floor, ls ) )
print( map( ceil, ls ) )

# See also: http://docs.python.org/2/library/math.html

# <demo> --- stop ---

### 'math' Module ###

# Python can construct special floating-point numbers.
# 'math.isnan' (Not-a-Number) and 'math.inf' (Infinity) can test for them.
x = float( "inf" )  # "+inf" works too
print( x, type( x ), math.isinf( x ) )
x = float( "-inf" )
print( x, type( x ), math.isinf( x ) )
x = float( "nan" )
print( x, type( x ), math.isnan( x ) )

# See also:
#   http://en.wikipedia.org/wiki/IEEE_floating_point
#   Unix only: http://docs.python.org/2/library/fpectl.html

# <demo> --- stop ---

### 'cmath' Module ###
# Mathematical functions for floating-point complex numbers.
import cmath

# Callables from 'math' module do not work with complex numbers.
angle = complex( 0, math.pi / 4 )
try:
    sin( angle )
except TypeError as exc:
    print( exc )
# Callables from 'cmath' module will, however.
print( cmath.sin( angle ) )

## 'polar', 'rect', 'phase' ##
some_cplx = complex( 42, 42 )
print( cmath.polar( some_cplx ) )
print( cmath.rect( *cmath.polar( some_cplx ) ) )
print( cmath.phase( some_cplx ) )

# See also: http://docs.python.org/2/library/cmath.html

# <demo> --- stop ---

### decimal ###
# _Arbitrary-precision_, _exact_ floating-point real numbers.
import decimal
from decimal import Decimal

# Show useful information about current context for Decimals.
# Works on a per-thread basis, so you can have a different context per thread.
# (If you don't know what a thread is, then don't worry.)
# (If you do, then rejoice.)
print( decimal.getcontext( ) )
# See also: help( decimal.setcontext )

# Regular IEEE 754 floating numbers are "inexact" underneath.
# Converting one to a higher-precision Decimal deonstrates this.
print( Decimal( 3.14159 ) )
# Compare this to constructing a Decimal directly.
print( Decimal( "3.14159" ) )

# Decimals can be constructed to arbitrary precision:
print( Decimal( "1" ) / Decimal( "7" ) )
decimal.getcontext( ).prec = 100
print( Decimal( "1" ) / Decimal( "7" ) ) 
decimal.getcontext( ).prec = 28

## 'sqrt', 'log', etc... ##
print( Decimal( "2" ).sqrt( ) )

# Much, much more....
# For more information, see: http://docs.python.org/2/library/decimal.html

# <demo> --- stop ---

### 'fractions' Module ###
# Rational numbers.
import fractions
from fractions import Fraction

# A side trip back to floating-point numbers.
print( 42.0.is_integer( ) )
print( 42.0.as_integer_ratio( ) )
print( 3.5.is_integer( ) )
print( 3.5.as_integer_ratio( ) )
# Almost have fractions, but not quite.

# Can construct from a pair of integers.
print( Fraction( *3.5.as_integer_ratio( ) ) )
# Can construct from a string.
print( Fraction( "1/2" ) )
# Can construct from a float. (But beware of inexactness.)
print( Fraction( 1.1 ) )
# Can construct from a Decimal!
print( Fraction( Decimal( "1.1" ) ) )

# Can do arithmetic with them.
print( Fraction( "7/2" ) + Fraction( "1/4" ) )

# For more information, see:
#   http://docs.python.org/2/library/fractions.html
#   http://docs.python.org/2/library/numbers.html#module-numbers

# <demo> --- stop ---

### 'random' Module ###
# Pseudorandom number generation.
# Random choice and sampling from sequences.
# Random sampling of well-known statistical distributions.
# Random shuffling of sequences.
import random

# Roll a six-sided die 10 times.
print( [ random.randint( 1, 6 ) for i in xrange( 10 ) ] )
# Big random number.
print( random.getrandbits( 256 ) )
# Random real number on interval [0,1).
print( random.random( ) )

# Random choice from sequences.
print( random.choice( [ 1, "a", 42J ] ) )
print( random.choice( "Hello, world!" ) )
# Random sampling of sequences.
print( random.sample( xrange( 42 ), 6 ) )
# Random permutations of sequences.
ls = range( 10 )
print( ls )
random.shuffle( ls )
print( ls )

# Random sampling of statistical distributions.
print( random.gauss( 0, 1 ) )
print( random.lognormvariate( 0, 1 ) )
# And others....

# For more information, see: http://docs.python.org/2/library/random.html

# <demo> --- stop ---

### 'functools' Module ###
# Wrappers for functions.
import functools
from functools import partial as partial_function

# One of the nice things about classes is that the objects they create
# can have attributes which allow for persistent state to be carried between
# uses. Sometimes, it is nice to have a similar property for functions and
# methods.
# (We will see some examples of this later, if you are doubtful.)
# 'functools.partial' allows you to hard-wire some of a callable's parameters,
# while leaving other free for arguments to be supplied later.
my_sum = partial_function( reduce, lambda x, y: x + y )
print( my_sum( xrange( 10 ) ) )
# In this case, we hard-wired the 'function' parameter of 'reduce'
# to create our own summation function.

# For more information, see: http://docs.python.org/2/library/functools.html

# Also, have a look at: http://docs.python.org/2/library/itertools.html

# <demo> --- stop ---

### 'operator' Module ###
# Function equivalents of most Python operators.
# Plus, partial functions for extracting specific elements of sequences
# or attributes of objects.
# (This is a very useful module - don't underrate it.
#  If programming efficiency is gold, then this is a gold mine.)
import operator
from operator import (
    itemgetter,
    attrgetter,
)

# Let's define a dot product function without using any explicit loops.
v1 = [ random.randint( 1, 6 ) for i in xrange( 10 ) ]
v2 = [ random.randint( 1, 6 ) for i in xrange( 10 ) ]
def dot_product( x, y ):
    return sum( map( operator.mul, x, y ) )
print( dot_product( v1, v2 ) )

# 'itemgetter' works with elements at specific positions in a sequence.
some_set = set( zip( v1, v2 ) )
# A set's elements are unordered.
print( some_set )
# By default, they are sorted by the first value in each pair.
print( sorted( some_set ) )
# Let's sort a copy of the pairs in this set by the second value in each pair.
print( sorted( some_set, key = itemgetter( 1 ) ) )
# 'itemgetter' can work with multiple positions at the same time, by the way.

# 'attrgetter' works with specific attributes.
# Let's create a vector of complex numbers and get their imaginary parts.
vc = map( complex, v1, v2 )
print( map( attrgetter( "imag" ), vc ) )

# For more information, see:
#   dir( operator )
#   http://docs.python.org/2/library/operator.html

# <demo> --- stop ---

### 'heapq' Module ###
# Heaps (Binary Trees)
# Implemented on top of standard Python lists.
import heapq
from heapq import (
    heapify,
    heappop, heappush,
)

# Let's transform a list of die rolls into a heap.
h = [ random.randint( 1, 6 ) for i in xrange( 10 ) ]
print( h )
heapify( h ) # heapify sorts the list in place
print( h )
# Sorting a list will maintain the heap invariant.
# (Note: Sorting is slower than [re]heaping.
#   If you don't need a sorted list, then don't sort it.)
h.sort( )
print( h )
# Let's perform operations which maintain the heap property.
# (Note: Regular 'insert' won't, unless done _very judiciously_.) 
print( "popped from heap:", heappop( h ) )
print( h )
heappush( h, 15 )
heappush( h, -3 )
print( "pushed onto heap: 15, -3" )
print( h )

# For more information, see:
#   http://docs.python.org/2/library/heapq.html

# <demo> --- stop ---

### 'time' Module ###
# Python times and timers.
import time
from time import (
    sleep,
    time        as epoch_time,
    localtime,
    gmtime,
    tzname,
    asctime,
    strftime,
)

# Sleep for 500 ms.
sleep( 0.5 )

# Number of seconds since midnight on 1 Jan 1970.
# Can use as a random number generator seed.
# Combine with 'os.getpid' for a more unique seed.
print( epoch_time( ) )

# Local Timezone (if computer is configured correctly)
print( tzname )

# Local Time
print( localtime( ) )
# Time on the Greenwich Meridian
print( gmtime( ) )
# Local time as a string.
print( asctime( ) )
# GMT as a string.
print( asctime( gmtime( ) ) )
# Just the current year as a string.
print( strftime( "%Y", gmtime( ) ) )

# For more information, see: http://docs.python.org/2/library/time.html

# <demo> --- stop ---

### 'datetime' Module ###
import datetime
from datetime import (
    datetime,
    timedelta,
)

# Two days from now.
print( datetime.now( ) + timedelta( 2 ) )

# For more information, see: http://docs.python.org/2/library/datetime.html

# <demo> --- stop ---

### 're' Module ###
# Regular expressions are very useful for many kinds of text processing.
# Many languages, such as Mathematica, Perl, Ruby, have them.
# Also, several common Unix utilities, such as 'grep' and 'sed' use them.
import re

# Regular expressions are written using a miniature pattern language.
# We are not going to go over all aspects of this,
# but show some examples of more commonly-used features.

s = "If the answer is 42, then what was the question?"
print( re.findall( r"42", s ) )
# OK, so that was a somewhat underwhelming example,
# because you can technically do something similar with substring matching.
print( "42" in s )
print( s.find( "42" ) )
# Let's do something slightly more interesting.
print( re.findall( r"\d+", s ) )  # Match 1 or more digits.
s = s.replace( "42", "43" )
print( re.findall( r"\d+", s ) )  # Match 1 or more digits.
s = "1 + 100 == 101"
print( re.findall( r"\d+", s ) )  # Match 1 or more digits.

# <demo> --- stop ---

### 're' Module ###

# Tired of typing of regular expression over and over?
# "Compile" it and assign the compiled expression to a variable.
re_digits = re.compile( r"\d+" )
print( re_digits.findall( "42 is being used 2 much in the demo." ) )
# Now you apply the same regular expression over and over again to
# various strings. Can be useful if you are processing a text file
# line-by-line, for example.

# You can also perform string substitutions with regular expressions.
# Note the use of 'functools.partial' to hard-wire the substitution,
# so that we can re-use it without typing it over and over again.
dot_to_underscore = partial_function( re.sub, r"\.{1,1}", "_" )
s = "version 3.0.5.19"
print( dot_to_underscore( s ) )

# Other useful features:
#   * matching across multiple lines; see re.MULTILINE
#   * iterator version of find for large texts; see re.finditer

# For more information, see: http://docs.python.org/2/library/re.html

# <demo> --- stop ---

### csv ###
import csv

# CSV readers (and writers) sit on top of regular file streams.
# A list is returned per each record read.
with open( "demo_data_1.csv", "rb" ) as csv_file:
    csv_reader = csv.reader( csv_file )
    for row in csv_reader:
        print( row )

# The header row can be used to supply dictionary keys.
# A dictionary will then be returned per each record read.
first_names = [ ]
dobs = [ ]
with open( "demo_data_1.csv", "rb" ) as csv_file:
    csv_dreader = csv.DictReader( csv_file )
    for row in csv_dreader:
        first_names.append( row[ "First Name" ] )
        dobs.append( time.strptime( row[ "DOB" ], "%m/%d/%y" ) )
pprint( first_names )
pprint( dobs )                     

# For more information, see: http://docs.python.org/2/library/csv.html

# <demo> --- stop ---

### cPickle ###
# Object persistence (serialization/deserialization).
# Save values in memory to a file and then restore them later.
import cPickle 

ls = [ 1, "a", 42J ]
with open( "test.pypickle", "wb" ) as pickle_file:
    cPickle.dump( ls, pickle_file )
with open( "test.pypickle", "rb" ) as pickle_file:
    ls_new = cPickle.load( pickle_file )
print( ls == ls_new )

# For more information, see:
#   http://docs.python.org/2/library/pickle.html
#   http://docs.python.org/2/library/pickle.html#module-cPickle
# In partciular:
#   http://docs.python.org/2/library/pickle.html#what-can-be-pickled-and-unpickled
#   http://docs.python.org/2/library/pickle.html#the-pickle-protocol       

# <demo> --- stop ---

### argparse ###
import argparse

# Example shamelessly adapted from the 'argparse' documentation.
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

# Normally, we would leave the call to 'parse_args' empty,
# so that it would sys.argv. However, for the sake of the demo,
# we are passing a contrived argument list.
args = parser.parse_args(['--sum', '7', '-1', '42'])
print args.accumulate(args.integers)

# See how easy that was?
# You can use 'argparse' to specify simulation parameters, operating mode,
# etc... without editing your code.

# For more information, see: http://docs.python.org/2/library/argparse.html

# <demo> --- stop ---

### Other Useful Modules ###
# The following are modules not covered by the demo,
# but deserve honorable mentions.

## 'struct' Module ##
# Parse binary data. (Can come from files, network connections, etc....)

## 'hashlib' Module ##
# Generate cryptograpy-grade hashes of objects.
# Useful for managing large digital repositories.
# Cryptographic hashes are very different from one another,
# if even one bit of their inputs is different.

## 'StringIO' Module ##
# Read and write to strings as if they were files.
# Can be useful for capturing output, for example.
# (Bonus points for parsing captured output with 're'.)

## 'mmap' Module ##
# Modify the contents of files as they were giant strings.
# Can be much more efficient (and easier) than parsing files line-by-line,
# especially if you need to parse structure from multiple lines.
# Also useful for amortizing write-out costs of large files over a the
# duration of a process rather than do everything at the end.

## 'timeit' Module ##
# Measure the performance of your code in action.

## 'pdb' Module ##
# Debug your code.
# Basic debugger commands are similar to those of 'gdb'.

### Concluding Remarks ###

# The Python library is _large_.
# We only just scratched the surface.
# The documentation index for the entire library can be found at:
#   http://docs.python.org/2/library/index.html

# Thanks for working through this demo.

# <demo> --- stop ---
