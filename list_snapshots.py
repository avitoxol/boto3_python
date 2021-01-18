import boto3

aws_mgt = boto.session.Session(profile_name = "avitoxol")
ec2_res = aws_mgt.resource(service_name = "ec2", region_name = "us-east-1")

sts_cli = aws_mgt.client(service_name = "sts", region_name = "us-east-1")
response = sts_con.get_caller_id()
myid = response.get('Account')

#list all snapshots

for snap in ec2_res.snapshots.filter(OwnerIds=[myid]):
    print(snap)

#list snapshot based on size

fil_size={"Name": "volume-size", "Values": ['8']}
for snap in ec2_res.snapshots.filter(OwnerIds[myid],Filters=[fil_size]):
    print(snap)
