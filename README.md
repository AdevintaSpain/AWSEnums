# AWSenums
Python module that contains a list of enums useful for your applications.

# How To package and distribute:
Based on the [official packaging documentation of python](https://packaging.python.org/tutorials/distributing-packages/#pure-python-wheels):
* ```python setup.py sdist```
* ```python setup.py bdist_wheel```
* ```gpg --detach-sign -a dist/AWSEnums-X.X.Xtar.gz```
* ```twine upload dist/AWSEnums-X.X.X.tar.gz dist/AWSEnums-X.X.X.tar.gz.asc```

# How To build the instances type enum:
Actually we can create it manually with the tool: AWSEnums/tooling/generate_instances_types.py only run the command:

```pipenv run python tooling/generate_instances_types.py -r us-east-1 -p sch-gov```

or if you prefer use the aws environment variables (AWS_DEFAULT_REGION, AWS_PROFILE or AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY) use:

```pipenv run python tooling/generate_instances_types.py```


**NOTE:** Now the aws pricing api only works on us-east-1. 