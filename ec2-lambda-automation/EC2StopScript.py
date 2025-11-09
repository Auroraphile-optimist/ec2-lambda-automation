# EC2 Stop Script

import boto3

region = 'ap-south-1'
instances = ['i-08760efb3ce7cb26a', 'i-02e88ddf81b2110b9']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print("Stopped your instances: " + str(instances))
