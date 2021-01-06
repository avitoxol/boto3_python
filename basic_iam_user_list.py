import boto3

aws_mag_con=boto3.session.Session(profile_name="avitoxol")
iam_con=aws_mag_con.resource('iam')

for user in iam_con.users.all():
    print(user)
