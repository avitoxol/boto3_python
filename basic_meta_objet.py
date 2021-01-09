import boto3

# You can enter into client object from resource obj

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
ec2_res = aws_mgt.resource(service_name = "ec2")

print(dir(ec2_res))
print(dir(ec2_res.meta))
print(ec2_res.meta.client.describe_regions()['Regions'])

for item in ec2_res.meta.client.describe_regions()['Regions']:
    print(item['RegionName'])
