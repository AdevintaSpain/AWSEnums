import boto3
import argparse

from typing import List

parser = argparse.ArgumentParser(description='Generate a aws instance type enum.')

parser.add_argument('-r', '--region',
                    help="AWS region, now only works with us-east-1",
                    type=str,
                    default="us-east-1",
                    required=False)
parser.add_argument('-p', '--profile', help="AWS profile", type=str, required=False)

params = vars(parser.parse_args())

session = boto3.Session(region_name=params["region"], profile_name=params["profile"])
pricing = session.client('pricing')


def get_instances(next_token: str=None) -> List[str]:
    if next_token:
        response = pricing.get_attribute_values(ServiceCode='AmazonEC2',
                                                AttributeName='instanceType',
                                                NextToken=next_token)
    else:
        response = pricing.get_attribute_values(ServiceCode='AmazonEC2', AttributeName='instanceType')
    instances: List[str] = [instance['Value'] for instance in response['AttributeValues'] if "." in instance['Value']]
    if "NextToken" in response.keys():
        instances.extend(get_instances(next_token=response["NextToken"]))

    return instances


instance_types: List[str] = get_instances()

path = 'type.py'
python_file = open(path, 'w')
python_file.write("from enum import Enum\n")
python_file.write("\n")
python_file.write("\n")
python_file.write("class Type(Enum):\n")
for instance_type in instance_types:
    python_file.write("    {} = \"{}\"\n".format(instance_type.upper().replace(".", "_"), instance_type))
