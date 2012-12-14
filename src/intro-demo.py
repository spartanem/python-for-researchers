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

# <demo> --- stop ---

### Dictionaries ###

# <demo> --- stop ---

# Python also provides another kind of string known as a "raw string".
# The reason for these may be discussed later.

r'This is a raw string.'
r"This is a raw string."
r'''You guessed it... this is a raw string.'''
r"""Yes, this is also a raw string."""

# <demo> --- stop ---


