import boto3

#List ec2 instances using client obj

aws_mgt=boto3.session.Session(profile_name="avitoxol")
ec2_cli=aws_mgt.client(service_name="ec2", region_name="us-east-1")

instances=ec2_cli.describe_instances()['Reservations']

print(instances)

for inst in instances:
    for i in inst['Instances']:
        print(i['InstanceId'])
