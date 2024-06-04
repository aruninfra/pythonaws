import boto3


def get_instances():
    ec2_client = boto3.client('ec2')

    reservations = ec2_client.describe_instances().get('Reservations', [])

    for reservation in reservations:
        for instance in reservation.get('Instances', []):
            instance_id = instance.get('InstanceId')
            instance_type = instance.get('InstanceType')
            public_ip = instance.get('PublicIpAddress', 'No Public IP')
            private_ip = instance.get('PrivateIpAddress', 'No Private IP')

            print(f"{instance_id}, {instance_type}, {public_ip}, {private_ip}")


get_instances()
