import boto3

#resource object is available only for some of the services
#creating a custom session
aws_mgt=boto3.session.Session(profile_name="avitoxol")

iam_res=aws_mgt.resource(service_name="iam",region_name="us-east-1")
ec2_res=aws_mgt.resource(service_name="ec2",region_name="us-east-1")
s3_res=aws_mgt.resource(service_name="s3",region_name="us-east-1")

#how to list iam users
print(dir(iam_res.users))

users=iam_res.users.all()
for user in users:
    print(dir(user))
    print(user.user_name)

print("--------------")

for user in iam_res.users.limit(1):
    print(user.user_name)

print("------------")

for item in s3_res.buckets.all():
    print(dir(item))
    print(item.name)
