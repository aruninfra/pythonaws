import boto3

def get_all_regions():
    ec2 = boto3.client('ec2')
    response = ec2.describe_regions()
    return [region['RegionName'] for region in response['Regions']]

def list_instances():
    regions = get_all_regions()
    for region in regions:
        print(f"Region: {region}")
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                instance_state = instance['State']['Name']
                print(f"Instance ID: {instance_id}, State: {instance_state}")

def stop_running_instances():
    regions = get_all_regions()
    for region in regions:
        print(f"Stopping instances in Region: {region}")
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                print(f"Stopping instance: {instance_id}")
                ec2.stop_instances(InstanceIds=[instance_id])

def start_stopped_instances():
    regions = get_all_regions()
    for region in regions:
        print(f"Starting instances in Region: {region}")
        ec2 = boto3.client('ec2', region_name=region)
        response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                print(f"Starting instance: {instance_id}")
                ec2.start_instances(InstanceIds=[instance_id])

if __name__ == "__main__":
     list_instances()
#    stop_running_instances()
#    start_stopped_instances()
