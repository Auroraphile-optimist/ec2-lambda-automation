import boto3

# EC2 Start Script for Mumbai Region
region = 'ap-south-1'
instances = ['i-08760efb3ce7cb26a', 'i-02e88ddf81b2110b9']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('✅ Started your instances: ' + str(instances))
