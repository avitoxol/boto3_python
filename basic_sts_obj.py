import boto3

aws_mgt=boto3.session.Session(profile_name="avitoxol")
sts_con=aws_mgt.client(service_name="sts", region_name="us-east-1")

user=sts_con.get_caller_identity()

print(user)
print(user['UserId'])
