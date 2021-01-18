import boto3

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
ec2_res = aws_mgt.resource(service_name - "ec2", region_name = "us-east-1")

for vol in ec2_res.volumes.all():
    print(vol.id, vol.state)

fil_unused = {"Name": "status", "Values": [available]}

for vol in ec2.res.volumes.filter(Filters = [fil_unused])
    print(vol.id, vol.state, vol.tags)
    if not vol.tags:
        print(vol.id, vol.state, vol.tags)
        print("Unused vols and untagged vols to be deleted")
        vol.delete()

print("Deleted")
