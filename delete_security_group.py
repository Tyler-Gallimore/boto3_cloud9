import boto3

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupID = 'PlaceHolder',
)

print(response)