Consoles
========

This module has a ``Console`` class for dealing with consoles. It allows you to
read from and write to consoles, as well as kill and start them. The
``get_consoles`` method in the ``User`` object is a generator that yields
``Console`` objects representing all of the consoles the user owns.

Every console on PythonAnywhere is started with an executable name, arguments,
and working directory:

 - The executable name is the command used to start the
   console, and when this executable stops running, the console is closed. For
   example, Bash console have ``bash`` set as the executable.

 - The arguments specify the command line arguments passed to the executable. For
   example, if you want to start a Bash console with verbose mode enabled, you
   can set arguments to ``'--verbose'``.

 - The working directory specifies the initial working directory the console runs
   in. When you start a console using the PythonAnywhere website, this is always
   set to your home directory.


Reading from and writing to consoles
------------------------------------

``Console`` objects have two methods for I/O: ``get_latest_output`` and
``send_input``. According to the official API help page, ``get_latest_output``
gives you approximately the 500 most recent characters of the console's output.
It accepts a boolean argument named ``replace_newlines`` which tells whether or
not to replace ``\r\n`` with ``\n``. It is ``False`` by default. This code plays
back the most recent output from a console::

   >>> import time
   >>> for char in console.get_latest_output(replace_newlines=True):
   ...     print(char, end='')
   ...     time.sleep(0.1)
   ...
   (console output will slowly appear)
