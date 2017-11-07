import boto3

session = boto3.Session(region_name="us-east-1", profile_name="sch-gov")
pricing = session.client('pricing')


response = pricing.get_attribute_values(ServiceCode='AmazonEC2', AttributeName='instanceType')


path = 'type.py'
python_file = open(path, 'w')
python_file.write("from enum import Enum\n")
python_file.write("\n")
python_file.write("\n")
python_file.write("class Type(Enum):\n")
for instance in response['AttributeValues']:
    if "." in instance['Value']:
        python_file.write("    {} = \"{}\"\n".format(instance['Value'].upper().replace(".", "_"), instance['Value']))
