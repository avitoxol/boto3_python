import boto3

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
ec2-res = aws_mgt.resource(service_name = "ec2", region_name = "us-east-1")

print(dir(ec2_res.instances))

for instance in ec2_res.instances.all():
    print(instance)

fil_one = {"Name": "instance-state-name", "Values": ['running']}
fil_two = {"Name": "instance-type", "Values": ['t2.micro']}

for instance in ec2_res.instances.filter(Filters = [fil_one, fil_two]):
    print(instance)


