import boto3



ec2_resource = boto3.resource('ec2')

response = ec2_resource.create_instances(
    ImageId='ami-00fa32593b478ad6e',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='mykey',
    SecurityGroups=[
        'pygroup'
    ]
)

print(response)