Python Distributions
====================

A Python distribution is a software bundle, which contains a Python interpreter
and the Python standard library. Installer programs for common operating
systems are a frequent mode of distribution. Many Python distributions also
have package managers so that you can install or upgrade various Python
packages.

Some of the most popular distributions are listed below. Distributions which
are marked as "scientific" are ones which come with :ref:`IPython <IPython 
Python Package>`, :ref:`numpy <numpy Python Package>`, :ref:`pandas <pandas 
Python Package>`, and :ref:`matplotlib <matplotlib Python Package>`, at a 
minimum. All of the distributions provide at least one integrated development
environment (IDE) for free. A Python IDE provides a Python-aware code editor
integrated with the ability to run code from that editor.


.. _ActiveState Python Distribution:

ActiveState ActivePython
------------------------

   Scientific: No, but many scientific packages can be added via the package
   manager

   Platform: AIX, HP-UX, Linux, MacOS X, Solaris, Windows

   Overview: http://www.activestate.com/activepython

   Downloads: http://www.activestate.com/compare-editions

   Package List: too many to list - use search page:
   http://code.activestate.com/pypm/search:/?tab=name

   Package Manager: `PyPM <http://code.activestate.com/pypm/>`_

   IDE: :ref:`IDLE <IDLE IDE>`, :ref:`Komodo <Komodo IDE>` (must be purchased
   separately from ActiveState)

   Note: ActivePython is one of the oldest Python distributions, but is not
   particularly geared towards science.


.. _Anaconda Python Distribution:

Continuum Analytics Anaconda
----------------------------
   
   Scientific: Yes

   Platform: Linux, MacOS X, Windows

   Overview: https://store.continuum.io/

   Downloads: [Note: Complete distribution is available for free, but requires
   registration first. Also, academics can get several powerful commercial
   add-on products for free with proof of affiliation with an educational
   institution.]

   Package List: http://docs.continuum.io/anaconda/pkgs.html

   Package Manager: `conda <http://docs.continuum.io/conda/>`_

   IDE: :ref:`Spyder <Spyder IDE>`
   
   Note: Continuum provides a Python compiler, called `Numba
   <http://numba.pydata.org/>`_, as part of its distribution. This can compile
   Python code down to machine code and is aware of how to optimize with
   special consideration for the popular :ref:`numpy <numpy Python Package>`.

   Note: Commercial add-on tools are linked against the Intel Math Kernel
   Library (MKL) for improved numerical performance.


.. _Enthought Python Distribution:

Enthought Canopy
----------------

   Scientific: Yes

   Platform: Linux, MacOS X, Windows

   Overview: https://www.enthought.com/products/canopy/

   Downloads: [Note: Academics can get the professional version for free by
   registering for an academic license at
   https://www.enthought.com/products/canopy/academic/ .]

   Package List: https://www.enthought.com/products/canopy/package-index/

   Package Manager: `Canopy Package Manager
   <http://docs.enthought.com/canopy/quick-start/package_manager.html>`_
   
   IDE: :ref:`IDLE <IDLE IDE>`, :ref:`SciTE <SciTE IDE>`

   Note: Professional version is linked against the Intel Math Kernel Library
   (MKL) for improved numerical performance.


.. _Python(x,y) Python Distribution:

Python(x,y)
-----------

   Scientific: Yes

   Platform: Windows
   
   Overview: https://code.google.com/p/pythonxy/

   Downloads: https://code.google.com/p/pythonxy/wiki/Downloads

   Package List: https://code.google.com/p/pythonxy/wiki/StandardPlugins
   
   IDE: :ref:`SciTE <SciTE IDE>`, :ref:`Spyder <Spyder IDE>`

   Other Tools: Console (enhanced Windows command line window), WinMerge
   (differencing and merging of files on Windows)

   Note: A variant of this distribution is also available for Linux; please see
   `pythonxy-linux <https://code.google.com/p/pythonxy-linux/>`_.


.. _WinPython Python Distribution:

WinPython
---------
   
   Scientific: Yes

   Platform: Windows
   
   Overview: https://code.google.com/p/winpython/

   Downloads: https://code.google.com/p/winpython/downloads/list

   Package List: https://code.google.com/p/winpython/wiki/PackageIndex

   Package Manager: `WinPython Package Manager (WPPM)
   <https://code.google.com/p/winpython/wiki/ControlPanel>`_
   
   IDE: :ref:`SciTE <SciTE IDE>`, :ref:`Spyder <Spyder IDE>`

   Other Tools: TortoiseHG (Mercurial version control system integrated into
   Windows Explorer)


Additional Python Packages
==========================

Some Python packages may not be a part of some distributions, but contain 
files which must be compiled (i.e., they are not "pure Python"). As it can 
be difficult to compile these files, especially on Windows, there exist
third-party repositories of precompiled packages.


Christoph Gohlke's Windows Binaries
-----------------------------------

   Overview: http://www.lfd.uci.edu/~gohlke/pythonlibs/

   Downloads: http://www.lfd.uci.edu/~gohlke/pythonlibs/

   Package List: http://www.lfd.uci.edu/~gohlke/pythonlibs/

   Platform: Windows


.. vim: set ft=rst ts=3 sts=3 sw=3 et tw=79:
