import boto3

def stope_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds=[instance_id])

    print(response)



stope_instance('i-082c835ff3cfa9078')