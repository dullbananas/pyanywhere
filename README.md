![Read the Docs](https://img.shields.io/readthedocs/pyanywhere)
![PyPI](https://img.shields.io/pypi/v/pyanywhere)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyanywhere)

# pyanywhere
This is a wrapper for the PythonAnywhere API that is currently in alpha stage of development. Here is an example showing how it works:

```python3
from pyanywhere.users import User
user = User('username', token='XXXXXXXX')

# Print names of all consoles
for console in user.get_consoles():
    print(console.name)
```

## Links
  * GitHub: https://github.com/dullbananas/pyanywhere
  * Documentation: https://pyanywhere.readthedocs.io/en/latest/
  * PyPI: https://pypi.org/project/pyanywhere/
