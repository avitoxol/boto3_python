import boto3
import time

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
ec2_res = aws_mgt.resource(service_name = "ec2", region_name = "us-east-1")
ec2_cli = aws_mgt.client(service_name = "ec2", region_name = "us-east-1")

#resource waiter 40 checks every 5 seconds for 200 seconds

my_instance = ec2_res.Instance("i-1234325346324")
print("Starting the instance")
#print(dir(my_instance))
my_instance.start()
my_instance.wait_until_running()
print("Instance has been started")


#checks 40 times every 15 seconds in real time scenario client waiter is better

#print("Starting")
#ec2_cli.start_instances(InstanceIds = ["i-12321353246436f"])
#waiter = ec2_cli.get_waiter('instance_running')
#waiter.wait(InstanceIds = ["i-1232142312351325f"])
#print("Ec2 instance is running")

#Using hybrid approach

#print("Starting")
#my_instance = ec2_res.Instance("i-12412341234")
#my_instance.start()
#waiter = ec2_cli.get_waiter('instance_running')
#waiter.wait(InstanceIds = ["i-1231242341234"])
#print("Ec2 instance is running")

#or the manual approach

#while True:
#    my_inst = ec2_res.Instance("i-123124123412")
#    if my_inst.state['Name'] == "running"
#        break
#    time.sleep(5)
#
#print(my_inst.state['Name'])
#print("The instance is running")
