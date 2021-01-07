import boto3

aws_mgt=boto3.session.Session(profile_name="avitoxol")
ec2_res=aws_mgt.resource(service_name="ec2", region_name="us-east-1")

instance=ec2_res.instances.all()

for inst in instance:
    print(inst.tags)

