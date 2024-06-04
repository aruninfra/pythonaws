import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.delete_security_group(
    GroupId='sg-0df3d9a9524c6620f'
)

print(response)