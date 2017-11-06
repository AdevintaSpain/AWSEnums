# AWSenums
Python module that contains a list of enums useful for your applications.

# How To package and distribute:
Based on the [official packaging documentation of python](https://packaging.python.org/tutorials/distributing-packages/#pure-python-wheels):
* ```python setup.py sdist```
* ```python setup.py bdist_wheel```
* ```gpg --detach-sign -a dist/AWSEnums-X.X.Xtar.gz```
* ```twine upload dist/AWSEnums-X.X.X.tar.gz dist/AWSEnums-X.X.X.tar.gz.asc```