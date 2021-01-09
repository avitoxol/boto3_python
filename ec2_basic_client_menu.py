import boto3
import sys

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
aws_cli = aws_mgt.client(service_name = "ec2", region_name = "us-east-1")

while True:
    print("Please choose one of the following actions")
    print("""
        Start
        Stop
        Terminate
        Exit
        """)

    action = input("Please choose your option: ")

    if action.lower() == "start":
        instance = input("Please provide your EC2 Instance ID: ")
        print("Starting EC2 instance")
        desired_instance = aws_cli.start_instances(InstanceIds = [instance])
    elif action.lower() == "stop":
        instance = input("Please provide your EC2 Instance ID: ")
        print("Stopping EC2 instance")
        desired_instance = aws_cli.stop_instances(InstanceIds = [instance])
    elif action.lower() == "terminate":
        instance = input("Please provide your EC2 Instance ID: ")
        print("EC2 has been TERMINATED")
        desired_instance = aws_cli.terminate_instances(InstanceIds = [instance])
    elif action.lower() == "exit":
        print("Thank you for your troubles ! ! !")
        sys.exit()
    else:
        print("You have chosen an incorrect option")
