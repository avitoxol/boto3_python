import boto3
import sys

aws_mgt = boto3.session.Session(profile_name = "avitoxol")
aws_res = aws_mgt.resource(service_name = "ec2", region_name = "us-east-1")
while True:
    print("Please choose one of the following actions")
    print("""
        Start
        Stop
        Terminate
        Exit
        """)

#    def inst_id():
#        instance = input("Provide Instance Id: ")
#        return instance

    action = input("Please choose your option: ")

    if action.lower() == "start":
        instance = input("Please provide your EC2 Instance ID: ")
        print("Starting EC2 instance")
        desired_instance = aws_res.Instance(instance)
        desired_instance.start()
    elif action.lower() == "stop":
        instance = input("Please provide your EC2 Instance ID: ")
        print("Stopping EC2 instance")
        desired_instance = aws_res.Instance(instance)
        desired_instance.stop()
    elif action.lower() == "terminate":
        instance = input("Please provide your EC2 Instance ID: ")
        print("EC2 has been TERMINATED")
        desired_instance = aws_res.Instance(instance)
        desired_instance.terminate()
    elif action.lower() == "exit":
        print("Thank you for your troubles ! ! !")
        sys.exit()
    else:
        print("You have chosen an incorrect option")
