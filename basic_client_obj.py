import boto3

aws_mgt_con=boto3.session.Session(profile_name="avitoxol")

iam_con=aws_mgt_con.client(service_name="iam",region_name="us-east-1")
ec2_con=aws_mgt_con.client(service_name="ec2",region_name="us-east-1")
s3_con=aws_mgt_con.client(service_name="s3",region_name="us-east-1")

users=iam_con.list_users()
for name in users['Users']:
    print(name['UserName'])


compute=ec2_con.describe_instances()
print(compute)

buckets=s3_con.list_buckets()
print(buckets)
