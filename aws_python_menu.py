#!/usr/bin/python3
import boto3
from botocore.exceptions import ClientError

def aws_status():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    print(response)

def aws_start():
    print('Enter instance id')
    instance_id = input()
    ec2 = boto3.client('ec2')
    try:
        ec2.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, run start_instances without dryrun
    try:
        response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

def aws_stop():
    print('Enter instance id')
    instance_id = input()
    ec2 = boto3.client('ec2')
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, call stop_instances witout dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

def aws_restart():
    print('Enter instance id')
    instance_id = input()
    ec2 = boto3.client('ec2')
    # Do a dryrun first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, call stop_instances witout dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)

def aws_create_instance():
    ec2 = boto3.resource('ec2')
    try:
        instance = ec2.create_instances(ImageId='ami-785db401',InstanceType='t2.micro',MaxCount=1,MinCount=1)
        print(instance)
    except ClientError as e:
        print(e)

def menu():
    while True:
        print('1. Get information about instances')
        print('2. Start instance')
        print('3. Stop instance')
        print('4. Restart instance')
        print('5. Create new instance')
        print('6. Quit')
        reply = int(input())

        if reply == 1:
            aws_status()
        elif reply == 2:
            aws_start()
        elif reply == 3:
            aws_stop()
        elif reply == 4:
            aws_restart()
        elif reply == 5:
            aws_create_instance()
        elif reply == 6:
            break
        else:
             print('pew')

print('Welcome to Amazon Control')
print('Select action:')


menu()
