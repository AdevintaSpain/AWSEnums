import requests

r = requests.get("https://raw.githubusercontent.com/boto/botocore/develop/botocore/data/ec2/2016-04-01/service-2.json")
r.status_code

path = 'type.py'
python_file = open(path, 'w')


python_file.write("from enum import Enum\n")
python_file.write("\n")
python_file.write("\n")
python_file.write("class Type(Enum):\n")
for instance_type in r.json()["shapes"]["InstanceType"]["enum"]:
    python_file.write("    {} = \"{}\"\n".format(instance_type.upper().replace(".", "_"), instance_type))

