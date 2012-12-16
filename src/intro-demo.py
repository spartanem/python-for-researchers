# IPython log file

# <demo> silent
from __future__ import (
    division        as __FUTURE_division,
    absolute_import as __FUTURE_absolute_import,
    print_function  as __FUTURE_print_function,
)

print( """

    Welcome to Python!
    
    Python is a general purpose programming language.
    A number of mathematical and scientific software libraries
    have been written in this language.
    We will learn about some of those libraries later.
    
    First, let's familiarize ourselves with the Python language....

    Python is an interpreted language -
    you do not need to compile a source file before running your code.

    Python provides a textual user interface to its interpreter.
    This is very handy for learning the language and for trying out new things,
    because you do not need to edit a file every time you want to do something.
    A good practice is to try things out in an interactive interpreter session
    before putting them into a file.
""" )

# <demo> --- stop ---

### Comments about the Demo ###

# Comments start with the '#' character.
# Python has no special sequence for multi-line comments, like the /* */ of C.
# The only place, in which the '#' character does not start a comment,
# is inside a string. Strings will be formally introduced later in this demo.

# Much of the text for this demo will be delivered as comments,
# such as you are reading now. There are several reasons for this:
#   * Full immersion - get used to looking at Python code and comments.
#   * The demo is actually a Python script being run piece-by-piece.
#     Comments isolate descriptive text from actual code.

# The way this demo will work is that a section, such as this one, will be
# presented. After each section, there will be a prompt which will allow
# any code in the section to be executed. We will execute this code,
# and then show any additional examples in the interactive interpeter
# in which the demo is running.

# Notice the prompt below this comment? If this section contained code,
# pressing the ENTER key would execute the code and you would see any
# printed results beneath the prompt.

# <demo> --- stop ---

### Objects and Console Output, First Glance ###

# Everything in Python is an object.
# We will come to grips with what an object is throughout this demo.
# For now, just think of it as a bundle of various attributes or properties.

# 'print' is a kind of object known as a "callable".
# We will use this callable extensively throughout the demo,
# so let's introduce it now.

# NOTE: If you are trying to follow this demo in a Python 2 interpreter,
#       then execute:
#           from __future__ import print_function
#       Python 2 actually has a 'print' _statement_,
#       but Python 3 uses a built-in 'print' _callable_ instead.
#       To prepare ourselves for the future, we are going to use the
#       'print' callable rather than statement in this demo.
#       Best to develop good habits early - less pain later....

# As expected, the 'print' callable will print output to the console.
# (Look for the output at the end of this demo section.)
print( "Hello, world." )
# Yes, "Hello, world." is a string. We will talk more about strings later.

# <demo> --- stop ---

### Object Types, First Glance ###

# 'type' is another built-in callable.
# It reports the type of a particular value.
# (We will use this callable much in the following sections.)
print( type( "Hello, world." ) )

# NOTE:
# When running a Python script, the interpreter will only
# display output explcitly sent to the console, such as with the
# 'print' callable.
# When using the Python interpreter interactively, a representation of the
# most recently handled object will always be displayed.
# Watch what happens when we type:
#    type( 1 )
# after we have stepped outside this demo section.
# Compare to what [doesn't] happen with the same call below:
type( 1 )

# <demo> --- stop ---

### Data Types: Booleans and Integers ###

## Booleans ##

# There is a 'bool' type for Boolean values.
# This is like a C99 or C++ 'bool' or a Fortran LOGICAL.
print( True, type( True ) )
print( False, type( False ) )

## Integers ##

# An 'int' is 32-bit or 64-bit integer - like a C 'int'.
print( 42, type( 42 ) )

# A 'long' is an arbitrary-precision integer - _unlike_ a C 'long'
print( 42L, type( 42L ) )

# By default, there are no integer types of guaranteed size.
# This is unlike Fortran, which has INTEGER*4, INTEGER*8, etc....
# This is also unlike the C99 standard library <stdint.h> header,
# which provides uint32_t, uint64_t, etc....

# Later, we will discuss the 'numpy' package which provides fixed-size types.
# So, don't be too disconcerted by the lack of fixed-size types.... 

# <demo> --- stop ---

### Data Types: Real and Complex Numbers ###

## Real Numbers ##

# A 'float' is a floating-point real number.
# This is usually 64-bit (like a C 'double' or Fortran REAL*8),
# but is not guaranteed to be.
print( 42.0, type( 42.0 ) )

# By default, there are no floating-point types of guaranteed size either.
# So, no equivalent to Fortran's REAL*4, REAL*8, etc....

# Q: What about an arbitrary-precision real number?
# A: We'll discuss that later.

## Complex Numbers ##

# A 'complex' is a floating-point complex number.
# A lowercase "j" or uppercase "J" may be used to indicate the imaginary part.
print( 42J, type( 42J ) )
print( 42.0j+42.0, type( 42.0j+42.0 ) )

# <demo> --- stop ---

### Data Types: The 'None' Type ###

# The special name 'None' has a type of 'NoneType'.
# If you know Lisp or Scheme, this is like 'nil'.
# If you know Mathematica, this is similar to 'Null'.
# BUT, this is _not_ the same as a C/C++ NULL pointer!
# (Python does not directly provide pointers.)
print( None, type( None ) )

# Note that if just type 'None' in interactive mode,
# nothing will be printed to the console.

# <demo> --- stop ---

### Variables: Creation and Assignment ###

# There are more data types in Python. We look at some of these later.
# For now, let's take a break to talk about variables.

# Unlike most compiled languages,
# Python does not associate types with variable names.
# Instead, values have type.
# (Computer scientists: yes, dynamic versus static typing, among other things.)

# The '=' sign binds (assigns) a particular value to a variable name.
# (If the variable name has not been used before,
#  then it is registered in the symbol table for the current context.
#  We will discuss this more later.)
a = 42

# Except on the left-hand side of an assignment (as above),
# referring to a variable by name will cause its value to be substituted.
# For example, calling 'print' on a variable will display the variable's value.
print( a, type( a ) )

# Unlike most compiled languages,
# Python allows a new value of a _different_ type to be assigned to a variable.
a = None
print( a, type( a ) )

# Q: What happens if we attempt to refer to an unbound variable name?

# <demo> --- stop ---

### Variables: Multiple Assignment ###

# Multiple variable assignments can be done with the same statement.
# (This is a neat feature of Python.)
a, b = 2, 1  # a gets 2, b gets 1
print( a, b )

# Values can be swapped between variables without an explicit intermediate!
a, b = b, a  # a gets 1, b gets 2
print( a, b )

# EXERCISE: (For those following along in a Python interpreter.)
#   (1) Assign 3, 2, 1 to a, b, c respectively.
#   (2) Print the values of these variables.
#   (3) With a single line of code, swap the values such that:
#           a gets 1, b gets 3, c gets 2
#       (Reassigning the values directly is cheating!)
#   (4) Print the values of these variables.

# <demo> --- stop ---

### Introspection of Objects ###

# 'dir' is one of the most useful callables built-in to Python.
# Remember how we earlier defined an object to be a bundle of attributes...?
# Now we are going to display the names of those attributes.
# 'dir' shows a directory of all the attributes associated with an object.
print( dir( 42 ) )
# Note that instances of types will generally have attribute directories
# very similar to their types themselves. There is a good reason for this....
print( dir( int ) )

# Note: There is another form of 'dir', which we will talk about more later.

# 'help' is another built-in callable, perhaps even more useful that 'dir',
# ...if the type of an object is well-documented.
# 'help' is meant to be used in interactive mode. See exercise below.

# EXERCISE:
#   (1) Get help on: 42J
#   (2) Get help on: complex

# Note: There is another way to invoke 'help'. More on that later.

# <demo> --- stop ---

### Strings: Literals ###

# In Python, strings are of variable length.
# You do not need to declare the length of a string in advance.

# There are many different ways to declare string literals.
# If you are familiar with Bourne shells, then you will recognize some of them:
'This is a string.'
'It can contain any number of consecutive double quotes: " "" """ etc...'
"This is also a string."
"It can contain any number of consecutive single quotes: ' '' ''' etc..."

# The following are also string literals.
# These forms are more natural for creating multi-line strings.
'''This is yet another string.
   It can contain any number of consecutive double quotes: " "" """ etc...
   It can also contain up to two consecutive single quotes: ' '' .
   It can also span multiple lines without needing any special characters.'''
"""And, this too is a string.
   It can contain any number of consecutive single quotes: ' '' ''' etc...
   It can also contain up to two consecutive double quotes: " "" .
   It can also span multiple lines without needing any special characters."""

# Anything that looks like a comment inside of a string is part of the string.
'#Not a comment because it is inside a string.' # Comment outside of string.
"#Not a comment because it is inside a string."
'''#Not a comment because it is inside a string.'''
"""#Not a comment because it is inside a string."""

# There are some other kinds of strings - we may discuss those later.

# <demo> --- stop ---

### Strings: Characters and Substrings ###

# Unlike C or Fortran,
# Python does not have the notion of characters as a separate data type.

# Individual characters are just strings of length 1.
'c'
"c"
'''c'''
"""c"""

# Note: An empty string has no characters.
""

# Strings are Python "sequences".
# As such, they support "indexing" and "slicing".

s = "This is a string."
print( s )
print( "first character:", s[ 0 ] )
print( "last character:", s[ 16 ] )
print( "last character (from end):", s[ -1 ] )
print( "first 3 characters:", s[ 0 : 3 ] )
print( "first 3 characters (lower bound implicit):", s[ : 3 ] )
print( "last 3 characters:", s[ 14 : 17 ] )
print( "last 3 characters (upper bound implicit):", s[ 14 : ] )
print( "last 3 characters (UB implicit, from end):", s[ -3 : ] )

# <demo> --- stop ---

### Strings: Length ###

# We want to figure out how to get the length of a string.
# Let's look at the attributes directory for the 'str' type.
print( dir( str ) )

# One of the attributes is named '__len__'.
# EXERCISE: Use 'help' on the 'str' type to find out what '__len__' does.

# The help says: "x.__len__() <==> len(x)"
# but is really not that helpful.
# EXERCISE: Use 'help' on the 'len' callable to find out what it does.

# The help says: "Return the number of items of a sequence or mapping."
# Remember that strings are sequences...?
# Let's try it:
print( len( s ) )

# But, what about that strange dot notation we saw in the original help?
# The dot (".") accesses an attribute of an object.
# Let's try it:
print( s.__len__( ) )

# You now have two methods for getting the length of a string.

# <demo> --- stop ---

### Strings: Size and Character Width ###

# Didn't we just discuss the size of strings?
# Yes, that was one measure of size.
# Now we want to know how many bytes a string object uses in memory.

# EXERCISE: Look at the attributes directory for a string again.

# What is that curiously named '__sizeof__' attribute?
# EXERCISE: Use 'help' on the 'str' type to find out what '__sizeof__' does.

# Let's try it:
print( s.__sizeof__( ) )
# Note that there is no 'sizeof' callable like the 'sizeof' operator in C.

# So, we can get the total size of the object,
# but how much of that is devoted to storage of the characters?
# We are researchers, so let us perform an experiment:
print( "".__sizeof__( ), "a".__sizeof__( ) )

# Good - each character only uses 1 byte.

# Q: Will this always be true? (And do we care?)
# A: See next section of the demo.

# <demo> --- stop ---

### Unicode Strings: Why? ###

# The Python world is slowly but surely moving from Python 2 to Python 3.
# One of the features of Python 3 is that all strings are "Unicode strings"
# by default.

# Unicode is a standard which specifies numbers ("code points") for just
# about every glyph of every known human language in current use...
# plus some historical ones... plus the International Phonetic Alphabet...
# plus some non-linguistic symbols... plus typographic symbols...
# etc....
# One byte can only store 256 unique code points.
# Various encodings exist to map common characters from languages to unique
# values in a byte. Just a few of the many are:
#   ASCII (US standard for English language)
#   ISO 8859-1 (international standard for W. European languages)
#   KOI-8 (Russian standard)
# There exists a scheme, known as UTF-8, which is like ASCII,
# but allows certain values above 127 to "escape" to multi-byte characters.
# This allows one to encode any character with a Unicode code point
# within a string.
# This is also quite messy for several reasons:
#   * If a program does not know that a string is UTF-8,
#     it may try to interpret the string with a wrong single-byte encoding.
#   * The number of characters in a string is not directly related to its size.

# Python 3 solves these issues by using so-called "Unicode strings" by default.
# (This is not just a Python issue, by the way....)

# <demo> --- stop ---

### Byte Arrays and Unicode Strings ###

# Python 2 supports "Unicode strings", but you have to request them explicitly.
# On Windows, these are encoded with UTF-16 (2 bytes minimum per character).
# On most other platforms, UTF-32 is used (4 bytes minimum per character).
u = u"This is a unicode string."
print( type( u ), len( u ) )
print( u"".__sizeof__( ), u"a".__sizeof__( ) ) 

# Some takeaway points:
#   (*) The Python 3 'str' type is like the Python 2 'unicode' type.
#       Because of this, do not bother to use Unicode explicitly in Python 2.
#       Your strings will automatically become Unicode strings in Python 3.
#   (*) If you process large ASCII texts, be aware that your strings will be
#       larger in Python 3 - nearly 4x larger in many cases.
#       Consider using the 'bytearray' type (see below).
#   (*) If you need to use actual arrays of bytes and don't care about
#       character encodings, then use 'bytearray'.

# Python 2.6, 2.7, and 3.x support the 'bytearray' type.
ba = b"This is a bytearray."
print( type( ba ), len( ba ) )
print( b"".__sizeof__( ), b"a".__sizeof__( ) )

# More info about Unicode in Python:
#   http://docs.python.org/2/howto/unicode.html

# <demo> --- stop ---

### Lists ###

# Lists are Python sequences of type 'list'.
print( type( [ ] ) )

# Lists can be created using the square brackets syntax.
print( [ ] )
print( [ 42 ] )
print( [ 1, "a", 3.0J ] )  # Note: Heterogenous types allowed.

# An empty list can also be created using the 'list' callable.
print( list( ) )
# The 'list' callable is actually intended to convert
# from other sequence types to lists.
# EXERCISE: Convert the string "Hello, world!" to a list.

# You can get the length of a list.
ls = [ 1, "a", 3.0J, [ ], "orange", 42.0 ]
print( len( ls ) )

# You can slice and index a list.
print( ls[ 1 ] )
print( ls[ -2 : ] )

# <demo> --- stop ---

### Conversion to Strings ###

# You might think that you can use 'str' to convert a list to a string.
# The answer is, yes, it does convert a list to a string...
# ...but probably not in the way you want.
ls = [ "a", "b", "c" ]
print( str( ls ) )

# As it turns out, 'str' invokes the '__str__' callable attribute of objects.
print( str( 42 ), type( str( 42 ) ) )
print( str( True ), type( str( True ) ) )
print( str( None ), type( str( None ) ) )

# Of course, you can invoke the '__str__' attribute directly.
print( None.__str__( ), type( None.__str__( ) ) )
print( True.__str__( ), type( True.__str__( ) ) )
# ... with the following quirky exception:
# Python will consider 42.__str__ to be an invalid 'float' type.
# (42.0.__str__ and 42L.__str__ are fine, however.)
a = 42
print( a.__str__( ), type( a.__str__( ) ) )

# Useful Tip:
# To convert from a list of strings to a single string,
# use the 'join' callable attribute of the 'str' type.
print( "".join( ls ) )
# If you want comma separators, you can use:
print( ",".join( ls ) )
# If you want space separators, you can use:
print( " ".join( ls ) )

# <demo> --- stop ---

### Sets ###

# Sets are Python sequences of type 'set'.
print( type( set( ) ) )

# In Python 2.7 and 3.x, sets can be created using soem syntactic sugar,
# curly braces:
#    { 1, 2, 3 }
# However, you may want to avoid this as the empty set cannot be { }.
# This is because that notation is already used for an empty 'dict' type.
# (We will discuss the 'dict' type shortly.)
# Instead of using shorthand, we will create sets from other sequences
# using the 'set' callable.
print( set( ) )
print( set( [ ] ) )  # Same as above.
print( set( [ 42 ] ) )
print( set( "Hello, world!" ) )
print( set( [ 1, "a", 3.0J ] ) )

# Sets have the property that they only contain unique elements.
# They are also not order-preserving as you probably noticed above.
print( set( [ 1, 1, "a", 2, 3, 2, 5, 1, 3, "a", None ] ) )

# Python also has a built-in 'frozenset' type.
# You cannot add, replace, or remove elements in fronzen sets.
# This immutability can add safety to your code at the cost of some flexibility.
# EXERCISE: Try some of the above examples using 'frozenset' instead of 'set'.

# The Python standard library provides an 'OrderedSet' type,
# which preserves order. We will discuss this later.

# <demo> --- stop ---

### The Trouble with Tuples ###

# Tuples are Python sequences of type 'tuple'.
print( type( tuple( ) ) )

# Beware: Some members of the Python community get upset if you call them
#         "frozen lists".
# Tuples are present at many places where you find commas (",") in Python code.
# The multiple-variable swaps that we did earlier involved hidden tuples.

# There is syntactic sugar for tuples, but it is _wrong_, _evil_, and _nasty_.
# Let's look at a few examples of it and then rip it to pieces.
print( ( ) ) # Hard to tell the difference from a callable invocation...
print( ( 42, ) )  # That trailing comma is not a typo. Yes, really.
print( ( 1, "a", 3.0J ) )
# Here are non-parenthesized versions of the last two:
tp1 = 42,
print( tp1 )
tp2 = 1, "a", 3.0J
print( tp2 )

# Strong Opinion:
# The syntactic sugar for tuples is _wrong_, _evil_, and _nasty_ because:
#   (*) Parentheses are already used for grouping expressions and for
#       invoking callables. Too many parentheses make code harder to read.
#   (*) There is an ambiguity problem for 1-element tuples. Adding an
#       element to an empty tuple or removing an element from a 2-element
#       tuple can cause bugs in code.
# Note on the 1-Element Tuple Ambiguity Problem:
( 42 ) # is the same as 42 and _not_ a 1-element tuple.
( 42, ) # is a 1-element tuple. Ugly, isn't it?
42, # is also a 1-element tuple. And ugly, just like the parenthesized version.

# EXERCISE: Construct tuples from other sequences such as strings or lists.
#           Hint: Use the 'tuple' built-in callable.

# <demo> --- stop ---

### Dictionaries ###

# Dictionaries are Python maps of type 'dict'.
# Maps associate a key with a value.

print( type( dict( ) ) )

# There is syntactic sugar for dictionaries.
print( { } )
print( { 1: "a" } )
print( { 1: "a", "foo": "bar", None: 42.0J } )

# An empty dictionary can also be created using the 'dict' callable.
print( dict( ) )
# Dictionaries can also be initialized from "keyword arguments".
# The name of each keyword argument will be stored as a string.
d = dict( pi = 3.142, e = 2.718, the_answer = 42 )
print( d )
# Note: Keyword arguments are _not_ variable assignments.
# EXERCISE: After creating the above dictionary, do:
#   print the_answer

# Dictionaries support the indexing operation.
# Given a key (rather than a position as with a sequence),
# the mapped value will be returned.
print( d[ "pi" ] )

# You may have noted above that dictionaries are not order-preserving.
# Later, we will discuss the 'OrderedDict' type, which is order-preserving.

# <demo> --- stop ---

### Addition and Subtraction ###

# Thus far, we've limited ourselves to using a handful of callables
# and introducing the various built-in data types.
# Now, let's look at the various operators available in Python.

## Addition ##
print( 41 + 1 )
print( 41.0 + 1 )
print( complex( 41, 41 ) + complex( 1, 1 ) )
print( "a" + "b" )
print( [ 1, "a" ] + [ 42J ] )
# The 'set' and 'dict' types do not support addition.
# Tip:
#   Look for the "__add__" attribute in a type's attributes directory.

## Subtraction ##
print( 43 - 1 )
print( 43.0 - 1 )
print( complex( 43, 42 ) - complex( 1, 0 ) )
print( set( [ 1, 3, 4 ] ) - set( [ 1 ] ) )
# The 'str', 'list', and 'dict' types do not support subtraction.
# Tip:
#   Look for the "__sub__" attribute in a type's attributes directory.

# Side Note:
#   There are also "reversed" versions of some operator callables,
#   like "__radd__" and "__rsub__". These swap the operands, in case one
#   supports the operation and the other doesn't.
#   As a user, you don't need to worry about this. It happens behind the scenes.

# <demo> --- stop ---

### Multiplication and Exponentiation ###

## Multiplication ##
print( 7 * 6 )
print( 6.0 * 7 )
print( complex( 3, 3 ) * complex( 7, -7 ) )
print( "ab" * 42 )
print( [ 1, "a" ] * 4 )
# The 'set' and 'dict' types do not support multiplication.
# Tip:
#   Look for the "__mul__" attribute in a type's attributes directory.

## Exponentiation ##
print( 4 ** 5 )
print( 4 ** 5.0 )
print( complex( 4, 4 ) ** complex( 5, 5 ) )
# None of the sequence or map types support exponentiation.
# Tip:
#   Look for the "__pow__" attribute in a type's attributes directory.

# <demo> --- stop ---

### Division and True Division ###

## Division ##
print( 84 / 2 )
print( 126 / 3.0 )
print( complex( 84, 84 ) / complex( 2, 2 ) )
# None of the sequence or map types support division.
# Tip:
#   Look for the "__div__" attribute in a type's attributes directory.

# Let's look at division more closely....
# Python 2 follows the C convention for integer division: remainders dropped.
print( 5 / 4 )
# Python 3 will return 1.25 instead of 1 for the above.
# So, if you want integer division, then be explicit about it.
print( 5 // 4 )
a = 5
print( a.__floordiv__( 2 ) )

## True Division ##
# What about "true division" in Python 2.
# In Python 2.6 and 2.7, you can either use the "__truediv__" attribute:
a = 5
print( a.__truediv__( 2 ) )
# or you can issue the following statement:
#   from __future__ import true_division
# and then divide as you might expect.
# Note: If you import something from the '__future__' package in a script,
#       then it must appear before other imports.
#       We will discuss this more later. 

# <demo> --- stop ---

### Modular Arithmetic ###

## Modulo ##
print( 5 % 4 )
print( 5 % -4 )
print( 5 % 4.0 )
print( 5 % 3.5 )
print( 5 % complex( 4, 2 ) )
print( complex( 5, 5 ) % complex( 4, 4 ) )
# Tip:
#   Look for the "__mod__" attribute in a type's attributes directory.

## Quotient and Remainder ##
# Use the 'divmod' built-in callable to quotient and remainder at the same time.
print( divmod( 5, 4 ) )
print( divmod( 5.0, 3.5 ) )
# Tip:
#   Look for the "__divmod__" attribute in a type's attributes directory.

# Q: What about getting the LCD and GCD?
# A: We'll get to that.... They're not built-in functions.

# <demo> --- stop ---

### Rounding and Truncation ###

## Rounding to Nearest ##
print( round( 3.5 ) )
print( round( 3.4999 ) )
print( round( -3.5 ) )
print( round( -3.4999 ) )
print( round( 3.5, -1 ) )
print( round( 11.5, -1 ) )
print( round( 3.5, 1 ) )
print( round( 3.49, 3 ) )

## Truncation ##
print( int( 3.5 ) )
print( int( -3.5 ) )
print( long( 3.5 ) )
print( long( -3.5 ) )
# "__trunc__" is the attribute which supports truncation.
print( 3.5.__trunc__( ) )

## Explicit Conversion ##
print( coerce( 3, 3.5 ) )
print( coerce( 3, 4L ) )

# Q: What about getting the floor and ceiling?
# A: We'll get to that.... They're not built-in functions.

# <demo> --- stop ---

### Operations with Assignment ###

# All of the basic arithmetic operations can be combined with assignment.

a = 41
a = a + 1
# becomes
a = 41
print( "before: a = ", a )
a += 1
print( "after: a = ", a )

a = 43
print( "before: a = ", a )
a -= 1
print( "after: a = ", a )

a = 6
print( "before: a = ", a )
a *= 7
print( "after: a = ", a )

a = 84
print( "before: a = ", a )
a /= 2
print( "after: a = ", a )

a = 84
print( "before: a = ", a )
a //= 2
print( "after: a = ", a )

a = 42
print( "before: a = ", a )
a %= 43
print( "after: a = ", a )

# <demo> --- stop ---

### Bitwise Operations ###

# Python provides the full set of expected bitwise operations.

## Bitwise-And ##
print( 42 & 10 )
a = 42
print( "before: a = ", a )
a &= 10
print( "after: a = ", a )
# Tip: The "__and__" attribute.

## Bitwise-Or ##
print( 42 | 10 )
a = 42
print( "before: a = ", a )
a |= 10
print( "after: a = ", a )
# Tip: The "__or__" attribute.

## Bitwise-Xor ##
print( 42 ^ 10 )
a = 42
print( "before: a = ", a )
a ^= 10
print( "after: a = ", a )
# Tip: The "__xor__" attribute.

# <demo> --- stop ---

### Bitwise Operations ###

## Bitwise-Negation ##
print( ~-43 )
# Tip: The "__invert__" attribute.

## Bitshift-Left ##
print( 10 << 2 )
a = 10
print( "before: a = ", a )
a <<= 2
print( "after: a = ", a )
# Tip: The "__lshift__" attribute.

## Bitshift-Right ##
print( 42 >> 2 )
a = 42
print( "before: a = ", a )
a >>= 2
print( "after: a = ", a )
# Tip: The "__rshift__" attribute.

# <demo> --- stop ---

### Number Bases ###

## Binary (Base-2) ##
print( bin( 42 ) )
print( 0b101010 )
print( int( "101010", 2 ) )
print( int( "0b101010", 2 ) )

## Octal (Base-8) ##
print( oct( 42 ) )  # Uses "__oct__" attribute.
print( 052 )  # Yes, a leading 0 means base-8. Like in C.
print( 0o52 )
print( int( "52", 8 ) )
print( int( "0o52", 8 ) )

## Hexdecimal (Base-16) ##
print( hex( 42 ) )  # Uses "__hex__" attribute.
print( 0x42 )  # A leading 0x means base-16. Like in C.
print( int( "2a", 16 ) )
print( int( "2A", 16 ) )
print( int( "0x2a", 16 ) )
print( int( "0X2A", 16 ) )

## Up to Base-36 Conversions ##
print( int( "z1", 36 ) )
print( int( "Z1", 36 ) )

# <demo> --- stop ---

### String Escape Sequences ###

## Escape Sequences for Terminal Control ##
print( "1\t2" )   # Horizontal Tab - usually equivalent to 8 spaces
print( "1\n2" )   # Newline
print( "1\r2" )   # Carriage Return
print( "1\r\n2" ) # CR+LF is special. Acts like newline. DOS/Windows compatible.
print( "1\a2" )   # Bell - beep! (if terminal supports it and sound is on)
# Go ahead, get it out of your system now...
print( "\a" * 42 )
print( "1\v2" )   # Vertical Tab - terminal may not support
print( "1\f2" )   # Form Feed - terminal may not support
print( "1\b2" )   # Backspace

## Other Escape Sequences ##
print( "1\"2" )   # Double Quote inside double-quoted string.
print( '1\'2' )   # Single Quote inside single-quoted string.
print( "1\\2" )   # Backslash
print( "\042" )   # Octal value for a Double Quote.
print( "\x42" )   # Hexadecimal value for Uppercase Letter 'B'.
print( u"\u0042" ) # 2-byte hexadecimal value of a Unicode code point.
print( u"\U00000042" ) # 4-byte hexadecimal value of a Unicode code point.
print( u"\N{LATIN CAPITAL LETTER B}" ) # Unicode code point by name.
# http://www.fileformat.info/info/unicode/char/42/index.htm
print( u"\N{LATIN CAPITAL LETTER A WITH RING ABOVE}" )
# http://www.fileformat.info/info/unicode/char/00c5/index.htm

# <demo> --- stop ---

### Raw Strings ###

# Python also provides another kind of string known as a "raw string".
# These are useful when you want to ignore escape sequences.

print( r'This is a raw string.\n\r\t' )
print( r"This is a raw string.\n\r\t" )
print( r'''You guessed it...
        this is a raw string.\n\r\t''' )
print( r"""Multi-line support in this too,
another raw string.\n\r\t""" )

# One place where raw strings are very useful is regular expressions.
# Regular expressions use backslash in their own way.
# They are very useful for text searches. We will talk more about them later.

# <demo> --- stop ---

### String Interpolation and Formatting ###

# C programmers will be familiar with much of the following.
print( "%d" % 42 )
print( "%d" % 0x42 )
print( "%x" % 0x42 )
print( "%o" % 42 )
print( "%d" % 2 ** 128 ) # 'long' types are handled transparently
print( "%f" % 3.14159 )
print( "%e" % 3.14159 )
print( "%g" % 3.14159 )
print( "%s" % "abc" )
print( "%s" % 42 ) # %s calls 'str' callable on objects.
print( "%s" % [ "a", 1, 42J ] )
print( "%d%% + %d%% = %d%%" % tuple( [ 40, 60, 100 ] ) ) # %% -> %
d = dict( a = 40, b = 60, c = 100 )
print( "%(a)d + %(b)d = %(c)d" % d ) # Can use keys from dictionaries.

# Python 3 prefers use of the 'format' callable.
# Also available in Python 2.
# Much more powerful. Prefer to use this instead of the above.
print( "The answer is {0}.".format( 42 ) )
print( "{0} + {1} = {2}".format( 40, 60, 100 ) )
print( "{2} - {0} = {0}".format( 40, 60, 100 ) )
print( "'%' is not special here. {0}".format( 42 ) )
print( "{{ is escaped; so is }}. {0}".format( 42 ) )
print( "real part: {0.real}\nimag part: {0.imag}".format( complex( 42, 42 ) ) )
print( "x = {x};\ty = {y}".format( x = 5, y = 4.0 ) )
# For more details, see:
#   http://docs.python.org/2/library/string.html#formatstrings
#   http://docs.python.org/2/library/string.html#formatspec

# <demo> --- stop ---

### Simple User Interaction ###

# At some point, you may write a Python script that takes input from the user.
# Here is a simple way to use the built-in 'raw_input' callable for that:
ans = raw_input( "What is your name?\t" )
print( "Hello, {}. I am pleased to meet you.".format( ans ) )
# 'raw_input' interprets all input from the user as a string.
# If you ask for a number, you will want to use 'int', 'float', etc... on it.

# EXERCISE: Write a few lines of Python code which will prompt for
#           2 floating-point real numbers and then multiply them together.

# If you are interested in doing science, then you probably won't be asking for
# passwords. BUT, if you do want to ask users for passwords, then using
# 'raw_input' is _not_ how you do it. There is a separate Python module
# for that, which provides proper security.

# <demo> --- stop ---

### Arithmetic Comparisons ###

## Exact Equality ##
print( 42 == 42 )
print( 42 == 2 )
print( 42 == 42.0 )
print( [ 42 ] == [ 42 ] )
print( "ab" == "abc" )

## Exact Inequiality ##
print( 42 != 42 )
print( 42 != 2 )
print( 42 != [ 42 ] )
print( "ab" != "abc" )

# <demo> --- stop ---

### Arithmetic Comparisons ###

## Greater-Than-Or-Equals ##
print( 42 >= 42 )
print( 42 >= 2 )
print( "ab" >= "abc" )

## Greater-Than ##
print( 42 > 42 )
print( 42 > 2 )
print( "ab" > "abc" )

# <demo> --- stop ---

### Arithmetic Comparisons ###

## Less-Than-Or-Equals ##
print( 42 <= 42 )
print( 42 <= 2 )
print( "ab" <= "abc" )

## Less-Than ##
print( 42 < 42 )
print( 42 < 2 )
print( "ab" < "abc" )

# <demo> --- stop ---

### Arithmetic Comparisons ###

## Built-in Callable: cmp ##
# Tip: Look at a type's attributes directory for the "__cmp__" attribute.
#      -1 if less than, 0 if equal, 1 if greater than
print( cmp( 42, 42.0 ) )
print( cmp( "ab", "bc" ) )
print( cmp( "bc", "abc" ) )

## Built-in Callable: ord ##
# String comparisons rely on the values of the underlying characters.
print( ord( "a" ) )
print( ord( "b" ) )
# The counterparts to 'ord' are 'chr' and 'unichr'.
# EXERCISE: Print the captial letter 'B' with 'chr'.

# <demo> --- stop ---

### Truth, Falsity, and Negation ###

# Nearly all Python objects have a "zero" value.
# Zero values are associated with falsity.
# Non-zero values are associated with truth.

## Logical Negation ##
# Similar to C/C++ ! or Fortran .not. .
print( not False )
print( not True )
print( not 0 )
print( not 42 )
print( not [ ] )
print( not [ 42 ] )
print( not "" )
print( not "foo" )

# <demo> --- stop ---

### Logical Comparisons ###

## Logical-And ##
# Similar to C/C++ && or Fortran .and. .
# Short circuit evaluation: first false expression ends testing.
# The value of the first false expression is returned.
# If end of test is reached, then last expression is returned.
print( 23 and "me" )
print( 0 and 42 )
print( 23 and "me" and False )
print( 42 and [ ] and 1 )

## Logical-Or ##
# Similar to C/C++ || or Fortran .or. .
# Short circuit evaluation: first true expression ends testing.
# The value of the first true expression is returned.
# If end of test is reached, then last expression is returned.
print( 23 or "me" )
print( 0 or 42 )
print( 23 or "me" or False )
print( 42 or [ ] or 1 )

# <demo> --- stop ---

### Identity and Sameness ###

## Identity ##
# Every object in Python has an identification code.
# The 'id' built-in callable can be used to access this.
a = b = "foo"
print( id( a ) )
print( id( b ) )
print( id( "bar" ) )
# If values are equivalent but of different type, they will have different IDs.
print( id( 42 ) )
print( id( 42.0 ) )
print( 42 == 42.0 )
print( id( 42 ) == id( 42.0 ) )

## Sameness ##
# The 'is' operator is shorthand for comparing IDs.
a = b = "foo"
print( a is b )
print( a is "bar" )
print( a is None )  # There is only one 'None'. Either you're it or you're not.
print( 42 is 42.0 )
# You can negate 'is' tests in one of two ways:
print( not 42 is 42.0 )
print( 42 is not 42.0 ) # Equivalent to above.

# <demo> --- stop ---

### Testing Membership ###

## Sequence Membership ##
# You may have noticed that attribute directories look like lists.
# In fact, they are lists.
# You may have grown tired of scanning their members with your eye.
# Let's let the Python 'in' operator do the work for us.
print( "__add__" in dir( int ) )
print( dir( int ).__contains__( "__add__" ) ) # Equivalent to above.
print( "foo" in dir( int ) )
print( not "foo" in dir( int ) )
print( "foo" not in dir( int ) ) # Equivalent to above.

## Map Membership ##
# The 'in' operator checks a dictionary's keys, not its values.
d = dict( a = 42, b = "foo", c = 42J )
print( "a" in d )
print( "d" in d )
print( 42 in d )
print( "foo" in d )
print( d.has_key( "a" ) )
print( d.has_key( "d" ) )
# Prefer the 'in' operator over the 'has_key' attribute.
# 'in' will work on anything which has the '__contains__' attribute.

# <demo> --- stop ---

### Testing Attribution and Callability ###

## Testing for Attribute Existence ##
# Up until now, we have contented ourselves with getting a list from 'dir'.
# But, we can actually test for attributes directly.
# The 'hasattr' built-in exists for this purpose.
print( hasattr( 42, "__add__" ) )
print( hasattr( int, "__add__" ) )
print( not hasattr( int, "foo" ) )

## Testing Callability ##
# How do we know if something is callable?
# Try calling it...
# or test with the 'callable' built-in callable.
print( callable( int ) )
print( callable( 42 ) )
print( callable( callable ) )

# <demo> --- stop ---

### Flow Control ###

# VERY IMPORTANT NOTE!
# If you forget or ignore everything else from this demo,
# then please remember the following:
#   Python _requires_ indentation inside of flow control structures!
# Curly braces (like in C) or BEGIN..END blocks are not used or allowed.

# IMPORTANT NOTE:
# A best practice is to use 4 _spaces_ per level of indentation.
# Good code editors can be configured to insert 4 spaces with the TAB key.
# Really good code editors can manage "soft tabs",
# which allow a BACKSPACE to backwards delete groups of 4 spaces as well.
# Python 3 is _very picky_ about mixing spaces and horizontal tabs;
# therefore, it is highly recommended that you avoid tabs in your code.

# Python provides the following kinds of flow control:
#   * Acyclic Branching:
#       'if'-'elif'-'else'
#   * Cyclic Branching (Iteration):
#       'while'-'continue'-'break'-'else'
#       'for..in'-'continue'-'break'-'else'
#   * Stacked or Contextual Execution:
#       function call-'raise'-'yield'-'return'
#       'try'-'except'-'else'-'finally'
#       'with..as'

# <demo> --- stop ---

### Acyclic Branching ###

# Python's 'if' is much like Bourne shell's 'if'
# except that you do not need a closing 'fi' statement.

# A simple 'if' block.
if not 42 is 42.0:
    print( "42 and 42.0 have different IDs" )

# A simple 'if'-'else' block.
# Remember the zero/non-zero dichotomy of values.
a = [ ]
if a:
    print( "non-zero value of type {0}".format( type( a ) ) )
else:
    print( "zero value for type {0}".format( type( a ) ) )

# Multiply-branched 'if'-'else' block.
a = [ 42, "foo" ]
b = ord
if   b in a:
    print( "matched first branch" )
elif callable( b ):
    print( "matched second branch" )
    print( "{} is callable".format( b ) )
elif b is None:
    print( "matched third branch" )
else:
    print( "{} didn't match any other branch".format( c ) )

# <demo> --- stop ---

### Acyclic Branching: Biconditionals ###

# If you know C well enough, then you have probably come across something like:
#   x = (a > b) ? a : b;
# This is a biconditional expression.

# Python supports biconditional expressions as well,
# but the syntax is arranged differently.
a = 4
b = 5
print( a if a > b else b )
# As with C, nested conditionals are supported,
# but can be hard to read.
c = 6
print( (a if a > b else b) if b > c else c )

# Note: The above is a contrived example for a 'max' function.
#       Python provides built-in callables for 'max' and 'min'.
print( max( a, b ) )

# Note that Python has no 'switch' or 'case' statement.

# Tip:
#   help( "if" )

# <demo> --- stop ---

### Cyclic Branching (Iteration) ###

## 'while' Loops ##
# Like C/C++ 'while' loops.
# They loop until the termination condition is satisfied.
# If it is met on loop entry, no looping will occur.

# A simple 'while' loop.
s = "a"
while s <= "aaaa":
    print( s )
    s += "a"

# A 'while'-'else' loop.
# The 'else' block is executed when the loop termination condition is satisfied.
ls = [ 1, "a", 42J ]
while ls:
    print( ls )
    ls = ls[ : -1 ]
else:
    print( "List sliced to nothing." )

# Note that Python has no 'do..until' or 'do..while' loops.

# Tip:
#   help( "while" )

# <demo> --- stop ---

### Cyclic Branching (Iteration) ###

## 'for..in' Loops ##
# Python 'for' loops are like Bourne shell 'for' loops,
# and _not_ like C/C++ 'for' loops or Fortran 'DO' loops.
# They iterate over a supplied sequence.

# A simple 'for..in' loop.
for x in [ 1, "a", 42J ]:
    print( x )
# The 'in' here is not an operator but part of the loop syntax.

# A 'for..in'-'else' loop.
# Also an introduction to the 'iteritems' callable attribute of 'dict' types...
# The 'else' block is executed when end of sequence is reached.
d = dict( a = 1, b = "foo", c = [ ] )
for k, v in d.iteritems( ):
    print( k, v )
else:
    print( "No more items in dictionary." )

# Tip:
#   help( "for" )

# <demo> --- stop ---

### Cyclic Branching (Iteration) ###

## 'continue' Statements ##
# Similar to C/C++ 'continue' or Fortran 'CYCLE'.
# Starts next loop iteration immediately without executing remainder of block.

i = 10
while i > 0:
    i -= 1
    if 0 == i % 2:
        continue
    print( "{0} is odd.".format( i ) )

for x in [ 1, "a", 42J ]:
    if "a" == x:
        continue
    print( x )

# Tip:
#   help( "continue" )

# <demo> --- stop ---

### Cyclic Branching (Iteration) ###

## 'break' Statements ##
# Similar to C/C++ 'break' or Fortran 'EXIT'.
# Exits loop immediately without executing remainder of block.
# Any 'else' clause for the loop block will not be executed.

i = 0
while True:
    if i > 100:
        break
    i += 5
else:
    print( "This will never be executed beacause of the 'break'." )

for x in [ 1, "a", 42J ]:
    if "a" == x:
        break
    print( x )
else:
    print( "This will only execute if 'a' is not in the sequence." )

# Tip:
#   help( "break" )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## Functions ##
# The 'def' keyword is like the Fortran 'SUBROUTINE' or 'FUNCTION' keywords,
# or like the 'defun' keyword in Lisp.
# Python functions are callable objects.

# A very simple function.
def foo( ):
    print( "Hello, world!" )
# Python has no concept like a C/C++ 'void function' or Fortran 'SUBROUTINE'.
# All functions return 'None' by default.
x = foo( )
print( x )

# A function with parameters.
# Parameters are just variable names which can take on values of any type.
def bar( x, y ):
    print( x * y )
# If you don't assign the return value of a function to a variable name,
# then the value will be discarded.
bar( 6, 7 )

# EXERCISE: Write a function which has one parameter.
#           Assume that this parameter will be a sequence.
#           Display each element of the sequence.

# Tip:
#   help( "def" )
#   help( "functions" )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## Default Arguments ##
# Python allows parameters to be assigned default arguments,
# if the caller omits the corresponding arguments.
# The '=' sign after a value denotes a default argument.
def add_with_default( x, y = 0 ):
    print( x + y )
add_with_default( 3 )
add_with_default( 4, 5 )

## Keyword Arguments ##
# Python callables can be given arguments in any order by specifying
# their parameter names with assignments when calling them.
def xyz_this( x, y, z ):
    print( x, y, z )
xyz_this( z = 3, x = 5, y = 7 )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## Anonymous Positional Arguments ##
# Python callables can accept an unlimited number of anonymous arguments.
# This is similar to the '...' and 'varargs' machinery of C.
# The acceptance of anonymous arguments is declared with a parameter name,
# which starts with an asterisk ("*").
# The anonymous arguments are presented to the callable as a 'tuple'.
def print_me( *args ):
    for arg in args:
        print( arg )
print_me( 1, "a", 42J )

## Arbitrary Keyword Arguments ##
# If you remember the 'dict' built-in callable from earlier,
# then you have already seen that Python callables can take any number
# of keyword arguments.
# The acceptance of keyword arguments is declared with a parameter name,
# which starts with two asterisks ("**").
# The keyword arguments are presented to the callable as a 'dict'.
def print_arbitrary_dict( **kwargs ):
    print( kwargs )
print_arbitrary_dict( a = 3, b = "foo", c = 42J )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## 'return' Statement ##
# The 'return' keyword is like the C/C++ 'return' keyword.
# The function is immediately exited without executing remaining code.

# Simple function with a single return value.
def the_answer( ):
    return 42
print( the_answer( ) )

# Function with an early return
def early_return( ):
    for el in [ 1, "a", 42J ]:
        if "a" == el:
            return
        print( el )
    print( "If 'a' is in sequence, then this is never executed." )

# Function which returns its arguments multiplied together.
def mul_xy( x, y ):
    return x * y
print( mul_xy( 6, 7 ) )

# Function which returns multiple values.
def multi_return( ):
    return 1, "a", 42J
# Yes, that's actually a tuple.
a, b, c = multi_return( )
print( a, b, c )

# Tip:
#   help( "return" )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## 'yield' Statement ##
# The 'yield' keyword is how Python implements something known as a
# generator.
# If you know enough about C/C++, then you may have encountered
# 'static' variables declared inside of functions.
# Or, if you know enough about Fortran, then you may have encountered
# 'SAVE' variables declared inside of procedures.
# Using 'yield' inside a Python generator takes a snapshot of the state of the
# entire function, not just certain variables. Execution of a generator
# restarts after where it last finished.
# This is different that in the C/C++ or Fortran cases, where only the values
# of certain variables are kept and the procedure must be exited and entered
# at the "proper" points each and every time.

# Simple generator in action.
def count_up_forever( ):
    i = 0
    while True:
        yield i
        i += 1
for j in count_up_forever( ):
    print( j )
    if 10 <= j:
        break

# Tip:
#   help( "yield" )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## 'raise' Statement ##
# Like C++ 'throw' keyword.
# Flags an exception to normal program flow, often due to an error.
# Exception propagates up the call stack until caught and handled.
# Uncaught exceptions will cause the Python interpreter to abort,
# if it is non-interactive. The interactive interpreter will simply
# present a new prompt if it catches anything other than the SystemExit
# exception.

# We aren't going to raise an exception right now,
# because that would be disruptive to this demo without knowing how to
# catch whatever we raise.

# Factoid: The generators used by 'for..in' loops raise StopIteration
#          when they have no more data.

# EXERCISE: Press CTRL-C in your interactive interpreter
#           and discover the exception that it raises.

# Tip:
#   help( "raise" )
#   help( "exceptions" )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## 'try'-'except'-'else'-'finally' Block ##
# Similar to C++ 'catch' keyword but with extra features.
# Attempts to catch exceptions raised within a 'try' block.

# Simple 'try'-'except' block.
# Raises an object of the 'SystemExit' type.
# Catches that object and prints some info about it.
try:
    raise SystemExit( 0 )
except SystemExit as exc:
    print( exc )

# A more sophisticated 'try'-'except'-'else' block.
# Specifically catches division-by-zero.
a = 5
b = 4
try:
    c = a / b
except ZeroDivisionError as exc:
    print( "Ooops! Division by zero occurred." )
    c = 0
except:
    raise
else:
    print( "Division was successful." )
# Note that the 'except' clause without an exception type is a catch-all.
# Any uncaught exception will be caught by that clause.
# The 'raise' without an exception object simply re-raises whatever was caught.

# Tip:
#   help( "try" )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

# A 'try'-'except'-'else'-'finally' block.
# Opens a file and writes to it.
# The 'open' built-in callable can be used to open files
# for reading and writing.
f = None
try:
    f = open( "scratch", "w" )
    f.write( "test" )
except IOError as exc:
    print( "Ooops! There was an I/O error." )
except:
    print( "Some other error occurred. Re-raising." )
    raise
else:
    print( "File operation succeeded." )
finally:
    if f: f.close( )
# The 'finally' clause always executes,
# no matter whether an exception was handled or re-raised.
# It will even execute if a 'return' statement is used inside the blocks.

# Note: Exception handlers are tried in order.
#       A good practice is to make sure the most specific ones are
#       encountered first.
#       See help( "exceptions" ) for the hierarchy of exceptions.
#       Exceptions on the branch tips of the hierarchy are the most specific.

## 'with..as' Blocks ##
# Python has the notion of context handlers.
# We can rewrite the above example using a 'with..as' block.

try:
    with open( "scratch", "w" ) as f:
        f.write( "test" )
        print( "File operation succeeded." )
    # The file is automatically closed at the end of the block,
    # even if an exception occurs.
except IOError as exc:
    print( "Ooops! There was an I/O error." )
except:
    print( "Some other error occurred. Re-raising." )
    raise

# Tip:
#   help( "with" )

# <demo> --- stop ---

### Stacked or Contextual Execution ###

## 'assert' Keyword ##
# Similar to the 'assert' macro used in C programs.
# Raises an AssertionError exception if the tested expression evalues to a
# "zero" value.
# Only works when Python optimization is off.
# Can be useful for high-traffic pieces of code where you don't want the
# test when they have been optimized for production use.
# Usually, though, it is better to raise a proper exception.

a = 43
try:
    assert 42 == a, a
except AssertionError as exc:
    print( exc )

# Tip:
#   help( "assert" )

# <demo> --- stop ---

### Doing nothing for a good cause... ###

## 'pass' keyword ##
# Similar to an empty ';' statement in C/C++.

# A do-nothing function.
# Actually has legitimate uses.
def dummy_function( some_data ):
    pass

# Ignoring an exception.
try:
    1 / 0
except ZeroDivisionError as exc:
    pass

# Tip:
#   help( "pass" )

# <demo> --- stop ---

### Functional Programming ###

# Python supports the notion of functional programming.
# Functional programming involves composing functions with one another
# and applying them to lists of data.
# What we saw the various statements is an example of imperative programming.
# Languages such as Mathematica, Lisp, and Scheme are very oriented
# toward functional programming.

## 'lambda' keyword ##
# C++11 has some support for them via the '[]' keyword.
# Mathematica provides them via the 'Function' function or the '&' shorthand.
# Lisp and Scheme have them.
# They are often called anonymous functions as they have no names.
# They are supposed to be "pure" functions -
# functions without side effects, such as performing I/O or changing global
# variables.
# Python lambda functions cannot contain statements - only function calls.

# The simplest lambda function looks like this:
# It takes no arguments and returns 'None'.
print( type( lambda : None ) )
f = lambda : None
print( callable( f ) )
print( f( ) )

# Tip:
#   help( "lambda" )

# <demo> --- stop ---

### Functional Programming ###

## 'map' Built-in Callable ##
# Applies a callable to every member of one or more sequences.
print( map( ord, "Hello, world!" ) )
print( map( lambda x, y: x << y, [ 6, 5, 4 ], [ 1, 2, 3 ] ) )

## 'filter' Built-in Callable ##
# If given 'None' instead of callable,
# removes all sequence members which are "zero" values.
# Else, applies callable to each sequence member,
# and removes members corresponding to "zero" results.
print( filter( None, [ 0, 1, False, True ] ) )

## 'any' Built-in Callable ##
# Returns 'True' if any element in a sequence is not a "zero" value.
# Returns 'False' otherwise.
print( any( [ 0, 1, False, True ] ) )

## 'all' Built-in Callable ##
# Returns 'True' if all elements in a sequence are not "zero" values.
# Returns 'False' otherwise.
print( all( [ 0, 1, False, True ] ) )

# <demo> --- stop ---

### Functional Programming ###

## 'reduce' Built-in Callable ##
# Reduces a sequence to a scalar by repeatedly applying a callable to
# a pair of operands taken from the sequence.
# The supplied default value will be returned if the sequence is empty.
print( reduce( max, "", "" ) )
# The only element of a 1-element sequence will be returned.
print( reduce( max, "a" ) )
# Otherwise, 'reduce' works as described above.
print( reduce( max, "Hello, world!" ) )

## 'sum' Built-in Callable ##
# Equivalent to:
#   reduce( lambda x, y: x + y, seq, start = 0 )
# but limited to integers.
print( sum( [ ] ) )
print( sum( [ 42 ] ) )
print( sum( [ 1, 4, 9, 16 ] ) )

## 'zip' Built-in Callable ##
# Works like a zipper, interlocking teeth together.
# Can work on single sequences and more than two sequences.
# Takes one element from the same position of each sequence,
# and place them together in a tuple.
# The resulting sequence of tuples is the length of the shortest sequence.
print( zip( [ 1, 4, 9, 16 ] ) )
print( zip( [ 1, 4, 9, 16 ], [ 1, 2, 4, 8, 16 ] ) )
print( zip( "abc", "ABCD", "_" * 42 ) )

# <demo> --- stop ---

### Stacks and Queues ###

## Stacks ##
# Python does not have a built-in stack type.
# But, lists can emulate stacks.

ls = [ ]
print( ls )
ls.append( 4 )
print( "pushed: 4" )
print( ls )
ls.append( 5 )
print( "pushed: 5" )
print( ls )
print( "popped: ", ls.pop( ) )
print( ls )
# Note: You can also manipulate stacks the other way:
#   insert( 0, item ) and pop( 0 )

## Queues ##
# Python does not have a built-in queue type either.
# But, list can emulate queues too.

ls = [ ]
print( ls )
ls.insert( 0, 4 )
print( "enqueued: 4" )
print( ls )
ls.insert( 0, 5 )
print( "enqueued: 5" )
print( ls )
print( "dequeued: ", ls.pop( ) )
print( ls )
# Note: You can also manipulate queues the other way:
#   append( item ) and pop( 0 )

# <demo> --- stop ---

### Efficient Programming ###

# There are various techniques and idioms you can use in Python to
# reduce the amount of code you need to write and to possibly improve
# the efficiency with which it runs.

## 'xrange' Built-in Callable ##
# Supplies a generator over integers with adjustable start, stop, and step.
# Integers on [0,4).
for i in xrange( 4 ):
    print( i )
# Integers on [1,5).
for i in xrange( 1, 5 ):
    print( i )
# Even integers on [2,10).
for i in xrange( 2, 10, 2 ):
    print( i )
# For really large intervals, this is memory-efficient because it generates
# one value at a time rather than the entire sequence.

# <demo> --- stop ---

### Efficient Programming ###

## List Comprehensions ##

# Instead of doing:
ls = [ ]
for i in xrange( 10 ):
    ls.append( i )
# you could do:
ls = [ i for i in xrange( 10 ) ]

# Instead of doing:
def identity_matrix( sz ):
    mat = [ ]
    for idx1 in xrange( sz ):
        mat.append( [ ] )
        for idx2 in xrange( sz ):
            # Kronecker Delta
            mat[ idx1 ].append( 1 if idx1 == idx2 else 0 )
    return mat
# you could do:
def identity_matrix( sz ):
    return [ [ (1 if idx1 == idx2 else 0) for idx1 in xrange( sz ) ]
             for idx2 in xrange( sz ) ]

# You can also use filter expressions in list comprehensions.
# And, you can use multiple generators inside the same comprehension.
print( [ [ x, y ] for x in xrange( 5 ) for y in xrange( 5 ) if x == y ] )

# <demo> --- stop ---

### Efficient Programming ###

## Generator Expressions ##

# List comprehensions create complete lists.
# These can be large and eat up a lot of memory.
# If you are only going to be using the list in one place,
# then a generator expression might suit you better.

for a, b in ([ x, y ] for x in xrange( 5 ) for y in xrange( 5 ) if x == y):
    print( a, b )

# <demo> --- stop ---

### Classes ###

### Miscellany ###

## Line continuations ##

## Parentheses ##

## PEP 8 Style ##

# TODO? Put below into 'stdlib' demo.

### Using Packages and Modules ###

### sys ###

### os.path ###

### collections ###

### math and cmath ###

### fractions ###

### decimal ###

### random ###

### functools and operator ###

### pprint ###

### re ###

### argparse ###

### pickle ###

### hashlib ###

### pdb ###

# <demo> --- stop ---

## Recipe: Implies ##

## Recipe: Exclusive-Or ##
