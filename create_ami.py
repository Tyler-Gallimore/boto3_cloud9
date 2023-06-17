import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    InstanceId = "PlaceHolder",
    Name = "Go to Ami"
)

print(response["ImageId"])