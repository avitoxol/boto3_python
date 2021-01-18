import boto3

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
ec2_res = aws_mgt.resource(service_name = "ec2", region_name = "us-east-1")
ec2_cli = aws_mgt.client(service_name = "ec2", region_name = "us-east-1")

inst_ids = []

for each inst in ec2_res.instances.all():
    inst_ids.append(inst)

print("Initiating, please wait . . .")

waiter = ec2_cli.get_waiter('instance_running')

ec2_res.instances.start()

waiter.wait(InstanceIds = inst_ids)

dev_serv = []

filter_one = {"Name": "tag:Name", "Values": ['Dev_serv']}

for inst in ec2_res.instances.filter(Filters = [filter_one]):
    dev_serv.append(inst.id)

# for client
dev_ser_cli = []

for inst in ec2_cli.describe_instances(Filters = [filter_one])['Reservations']:
    for i in inst['Instances']:
        dev_serv_cli.append(i['InstanceId'])

#ec2_cli.start_instances(InstanceIds=dev_ser_cli)
#waiter = ec2_cli.get_waiter('instance_running')
#waiter.wait(InstanceIds=dev_ser_cli)

