Introduction
============

This module is a wrapper of the PythonAnywhere API. Like the Discord.py library,
it defines classes for everything, such as users and consoles.

The ``User`` class is very important because you have to use it to access
anything else. If you are running this module on PythonAnywhere, you can use the
``get_current_user`` to create a ``User`` object that represents your user::

   >>> from pyanywhere.users import get_current_user
   >>> user = get_current_user()
   >>> user.name
   'joe_mama'

Every ``User`` object needs an API token. When you call ``get_current_user``, it
gets the token using the ``API_TOKEN`` environment variable. If you are running
this module outside of PythonAnywhere, or you want to access the API through a
different user, you can manually create a ``User`` object. The constructor
accepts two arguments: the username and the API token::

   >>> from pyanywhere.users import User
   >>> user = User('username', 'XXXXXXX')

This is how you access your consoles::

   >>> for console in user.get_consoles():
   ...     print(console.name)
   ...
   Bash console 14000012
   Bash console 14042069
