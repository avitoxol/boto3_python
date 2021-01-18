import boto3

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
ec2_cli = aws_mgt.client(service_name = "ec2", region_name = "us-east-1")

for vol in ec2_cli.describe_volumes()['Volumes']:
    print(vol['VolumeId'], vol['State'])

fil_unused = {"Name": "State", "Values": "available"}

for vol in ec2_cli.describe_volumes()['Volumes']:
    if not "Tags" in vol and vol['State'] == "available":
        print("Terminating")
        print(vol['VolumeId'], vol['State'])
        ec2_cli.delete_volume(VolumeId = vol['VolumeId'])

print("Terminated")
