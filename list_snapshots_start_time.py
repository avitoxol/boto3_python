import boto3
import datetime

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
ec2_res = aws_mgt.resource(service_name = "ec2", region_name = "us-east-1")
ec2_cli = aws_mgt.client = (service_name = "ec2", region_name = "us-east-1")

sts_cli = session.client("sts")
myid = sts_cli.get_caller_identity().get('Account')
today = datetime.datetime.now()

start_time = str(datetime.datetime(today.year,today.month,today.day,6,00,00))
print(start_time)

for snap in ec2_res.snapshots.filter(OwnerIds=[myid]):
    if snap.start_time.strftime("%Y-%m-%d %H:%M:%S") == start_time:
        print (snap.id, snap.start_time.strftime("%Y-%m-%d %H:%M:%S")


