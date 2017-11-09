import boto3
import argparse


parser = argparse.ArgumentParser(description='Generate a aws instance type enum.')

parser.add_argument('-r', '--region', help="AWS region, now only works with us-east-1", type=str, default="us-east-1")
parser.add_argument('-p', '--profile', help="AWS profile", type=str)

params = vars(parser.parse_args())


session = boto3.Session(region_name=params["region"], profile_name=params["profile"])
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
