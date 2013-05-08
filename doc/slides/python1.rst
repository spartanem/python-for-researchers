Python I: Intro
===============


Expectations
------------

* Previous programming experience recommended. Focus is on using Python as a
  tool, not on teaching programming.

* Will learn language while learning [hopefully] useful tools.

* Python is not the solution to all your problems. (I.e., this seminar is
  informational rather than evangelical in nature. Draw your own conclusions.)

* Python is not a magical gift box; it is a programming language. At least
  some work will be required to reach your goals.


Python Interest Group at MSU?
-----------------------------

* People would meet to help each other install Python and various Python
  packages.

* People would talk about how they use Python at work.

* People would share their experiences with various pieces of Python software.

* Any interest?


Why Python?
-----------

* Popularity. You will likely encounter it. Maybe you already did and maybe
  that is why you are here?

* Compared to many other scripting languages, it has a fairly simple syntax
  which encourages the writing of readable code and may be easier to learn.

* Compared to other scripting languages, it has one of the most
  full-featured sets of tools for scientific computing: NumPy, SciPy,
  pandas, and matplotlib.

* Comparisons and Contrasts

   * Matlab/Octave
      
      * vs NumPy, SciPy, matplotlib, and scikits

   * R
      
      * Can embed in IPython

      * vs pandas, StatsModels, and matplotlib

   * Julia
      
      * Can embed in IPython

   * Perl, Ruby, Scala, Clojure, Haskell, OCaml, etc...

   * Javascript
      
* Consistency

   * Warts in Ruby and Javascript: https://www.destroyallsoftware.com/talks/wat


Interpreters
------------

* Python

   * Python 2 and Python 3

   * CPython, IronPython, Jython, and Stackless Python

* IPython
   
   * IPython Terminal

   * IPython QtConsole

   * IPython Notebook

* Interpreters on the Web

   * repl.it: http://repl.it/languages/Python

   * PythonAnywhere: https://www.pythonanywhere.com/

* Running Programs

   * Pitfall Warning: Explicit ``print`` vs implicit print.

* Compiling Programs
   
   * No explicit compilation. Performed on-the-fly from source into Python VM
     bytecode. (Note presence of ``.pyc`` and ``.pyo`` files.)

   * PyPy and Nuitka

   * Pyrex and Cython

   * Numba


Everything is an Object
-----------------------

* Almost everything is an object.
   
   * Don't worry too much about what an object is. Consider it to be a some
     kind of value which has some associated attributes.
   
   * Attributes, themselves, are generally objects.

   * Objects are created from types. Types themselves are objects.

   * Don't worry about object-oriented programming, if you're not familiar with
     it. Existing types are flexible enough that you usually won't have to 
     create your own. (But, it is easy to do so if you have the need!)

* Information about an object and its attributes can be found.

   * :py:func:`help`


Built-in Types
--------------
   
* :py:class:`object`

* :py:class:`type`

* :py:class:`module`

* :py:class:`NoneType`

* :py:class:`bool`

* :py:class:`function` (named and anonymous)

* :py:class:`int`, :py:class:`long`

* :py:class:`float`

* :py:class:`complex`

* :py:class:`str`, :py:class:`unicode`, :py:class:`bytearray`

* :py:class:`tuple`

* :py:class:`list`

* :py:class:`set`

* :py:class:`dict`


Variables
---------

* Important: Types are associated with values rather than variable names.

* Variable names are references to values.

   * References to values are created by assignment with ``=`` statement.

   * References are likewise changed with ``=`` statement.

   * References are deleted with ``del`` statement.

   * Examples.

* Pitfall Warning: Multiple named references to same sequence or mapping.
   
   * Example.

   * How to make a copy of a sequence? Several ways - more on that later.

* Multiple assignment can be performed using commas as separators.

* Multiple values can be swapped without explicit intermediate variables.

   * Exercise: Try it!


Operators
---------

* ``+``, ``-``, ``*``, ``/``, ``//``, ``%``, ``**``

   * Exercises:

      * What happens if you add strings?

      * What happens if you multiply a string, tuple, or list by an integer?

   * Notes on integer division vs true division.

   * Examples of string interpolation.

   * Examples of the assigning variants of these operators.

* ``==``, ``!=``, ``<``, ``<=``, ``>=``, ``>``

* ``is``, ``is not``, ``in``, ``not in``
   
   * Notes on precedence and alternative keyword orders.

* ``not``, ``and``, ``or``
   
   * Notes on "zeroish" vs "non-zeroish" values.

   * Notes on short-circuiting evaluation.

* ``~``, ``&``, ``|``, ``^``, ``<<``, ``>>``
   
   * Examples of the assigning variants of these operators.


Working with Objects
--------------------

* Objects are instances of types.

   * Instances can be created by calling types or factory functions.

   * Examples.

* :py:func:`dir`

* :py:func:`hasattr`, :py:func:`getattr`, :py:func:`setattr`

* Dot notation (``.``) is used to access attributes.

   * Exercise: Try to add an attribute to an instance of :py:class:`object`.

* The ``class`` statement defines a new type.
   
   * Inheritance. Old-style and new-style classes.

   * Example of simple class.

   * Exercise: Define a new class. Create an instance of it. Then, try to add a
     custom attribute to it. If successful, then try accessing that attribute.

* Note on special methods with double underscores.


Working with Strings
--------------------

* Various kinds of string literals.

* :py:func:`len`

* Indexing

   * Note on zero-based indexing.

   * Exercise: What happens if you use a negative index?

* Slicing
   
   * Colon notation (``:``) for range and stride.

   * Examples.

* :py:meth:`str.strip`

* :py:meth:`str.lower` and :py:meth:`str.upper`

* :py:meth:`str.split` and :py:meth:`str.join`

* :py:meth:`str.replace`

* :py:meth:`str.format`
   
   * Examples.

* :py:meth:`str.__sizeof__`

   * Notes on character width.


Working with Tuples
-------------------

* Creation of tuples.

* Length, indexing, and slicing like strings.

* Pitfall Warning: Syntactic sugar for 1-element tuple.

* Note on multiple assignment and tuples.


Working with Lists
------------------

* Creation of lists.

   * List comprehensions.

   * :py:func:`range` and :py:func:`xrange`

* Length, indexing, and slicing like strings.

* :py:meth:`list.append` and :py:meth:`list.insert`

   * Exercise: Insert an item at the front of a list.

* :py:meth:`list.extend`

* Item removal.

   * Use ``del`` with an index or slice.

   * :py:meth:`list.pop`

   * :py:meth:`list.remove`

* :py:meth:`list.count`

* :py:meth:`list.reverse` and :py:func:`reversed`

* :py:meth:`list.sort` and :py:func:`sorted`


Working with Sets
-----------------

* Creation of sets.

   * Pitfall Warning: The empty set is not ``{ }``!

* Length, but no indexing or slicing.

* :py:meth:`set.add`

* :py:meth:`set.pop`, :py:meth:`set.remove`, :py:meth:`set.discard`

* :py:meth:`set.intersection`, :py:meth:`set.union`
   
   * Updating variants of these methods.

   * Examples.

* :py:meth:`set.difference`, :py:meth:`set.symmetric_difference`
   
   * Updating variants of these methods.

   * Examples.

* Exercise: What do the ``-``, ``&``, ``|``, and ``^`` operators do with sets?

* Exercise: What about the assigning variants of the same?

* :py:class:`frozenset`


Working with Dictionaries
-------------------------

* Creation of dictionaries.

   * From a list of key-value pairs.
      
      :py:func:`enumerate`

      :py:func:`zip`

   * :py:meth:`dict.fromkeys`

   * Dictionary comprehensions.

   * Examples.

   * Exercise: Create a dictionary, using a list of letters as keys and a list
     of numbers as values.

* Indexing by key, but no slicing.

* Value retrieval by indexing vs :py:meth:`dict.get`.

* Manipulating sequences as dictionary values: :py:meth:`dict.setdefault`

* Testing for a key with the ``in`` operator.

* Lists of keys, values, and key-value pairs.

   * Views vs iterators.

* :py:class:`frozendict`


Flow Control and Modularity
---------------------------

* ``pass``

* ``def`` - ``yield`` - ``return``

   * Docstrings.
   
   * Functions can return multiple values.

   * Arbitrary numbers of arguments.

   * Keyword arguments.
   
   * Examples.

* ``if`` - ``elif`` - ``else``
   
   * Examples.

* ``for`` .. ``in`` - ``continue`` - ``break`` - ``else``

   * Really? An ``else`` clause with a loop? Yes.
   
   * Examples.

* ``while`` - ``continue`` - ``break`` - ``else``

   * Examples.

* ``try`` - ``except`` - ``else`` - ``finally``
   
   * The exception hierarchy.
   
   * Examples.

* ``with``
   
   * Examples later.


Functional Programming
----------------------

* ``lambda``

* Biconditional expressions.

* :py:func:`all` and :py:func:`any`

* :py:func:`map`

* :py:func:`filter`

* :py:func:`reduce`

* :py:func:`sum`, :py:func:`min`, :py:func:`max`


Working with Files
------------------

* :py:func:`open` and ``with`` context handler

   * Modes

* Iteration over lines of text file.

* :py:meth:`file.read`, :py:meth:`file.readline`

* :py:meth:`file.write`, :py:meth:`file.writeline`


Miscellany
----------

* :py:func:`int`

   * Number bases.

* :py:func:`float`, :py:func:`complex`

   * Infinities and not-a-number (NaN).

* :py:func:`str`, :py:func:`unicode`, :py:func:`repr`

* :py:func:`raw_input`

* :py:func:`chr`, :py:func:`unichr`, :py:func:`ord`

* :py:func:`eval`

* :py:func:`exec`, :py:func:`execfile`

* :py:mod:`__builtins__`, :py:mod:`__builtin__`, :py:mod:`builtins`

* Decorators

* Properties

* Generator Expressions


Standard Library
----------------

Namespaces, Scopes, and Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :py:func:`vars`

* :py:func:`locals` and :py:func:`globals`

* ``import``

* ``from`` .. ``import`` ..

* Aliasing with ``as``.

* Multiple selective imports.

Back to the Future
~~~~~~~~~~~~~~~~~~

* :py:mod:`__future__`

   * ``division``

   * ``print_function``

   * ``absolute_import``

Python Sundries
~~~~~~~~~~~~~~~

* :py:mod:`sys`
   
   * ``stdin``, ``stdout``, ``stderr``

   * ``version``, ``version_info``

   * ``modules``

* :py:mod:`collections`

   * :py:func:`collections.namedtuple` (type definitions for the lazy)

   * :py:func:`collections.defaultdict`

   * :py:func:`collections.OrderedDict`

Human-Readable Data
~~~~~~~~~~~~~~~~~~~

* :py:mod:`pprint`

Math and Statistics
~~~~~~~~~~~~~~~~~~~

* :py:mod:`math`, :py:mod:`cmath`

   * ``pi`` and ``e``

   * Exercise: Quadruple the arc tangent of 1.

   * Exercise: Investigate the difference between the built-in functions
     :py:func:`int` and :py:func:`round` and the :py:mod:`math` functions
     :py:func:`math.floor`, :py:func:`math.ceil`, and :py:func:`math.trunc`.

* :py:mod:`decimal`
   
   * Examples.

* :py:mod:`fractions`

   * Examples (including classic 1.1 from float and from Decimal)

* :py:mod:`random`

   * :py:func:`random.choice`, :py:func:`random.sample`

   * :py:func:`random.shuffle`

   * Samples from assorted distributions.

   * Examples.

   * Exercise: Generate a list of 10 random samples from a Gaussian
     distribution.

Gathering Data
~~~~~~~~~~~~~~

* :py:mod:`csv`
   
   * Can handle other separators besides commas.

   * Can ignore header lines.

   * Examples.

* :py:mod:`urllib`, :py:mod:`urllib2`

   * FTP and HTTP retrieval of data.

   * Can scrape web pages for data. Use in conjunction with something like 
     BeautifulSoup. For example, see `this Stack Overflow question
     <http://stackoverflow.com/questions/2081586/web-scraping-with-python>`_.

   * Examples.

Data Persistence
~~~~~~~~~~~~~~~~

* :py:mod:`pickle`

   * :py:meth:`pickle.dump`

   * :py:meth:`pickle.load`

   * Exercise: Create a dictionary and set. Dump them to a file. Load them from
     the file.

Raking Data
~~~~~~~~~~~

* :py:mod:`operator`

   * :py:func:`operator.itemgetter`

   * :py:func:`operator.attrgetter`

   * Functional forms of built-in operators.

   * Examples.

* :py:mod:`re`
   
   * :py:func:`re.compile`

   * :py:func:`re.findall`

   * Examples.

Files, Directories, and Subprocesses
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :py:mod:`os`, :py:mod:`subprocess`

   * :py:func:`os.getcwd`

   * :py:func:`os.getpid`

   * :py:class:`subprocess.Popen`

* :py:mod:`os.path`, :py:mod:`glob`, :py:mod:`shutil`

.. vim: set ft=rst ts=3 sts=3 sw=3 et tw=79:
