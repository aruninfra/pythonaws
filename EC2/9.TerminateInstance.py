import boto3


def terminate_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)




terminate_instance('i-082c835ff3cfa9078')