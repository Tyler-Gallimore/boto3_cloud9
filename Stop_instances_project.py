import boto3

def stop_instance(client, instance_id):
    response = client.stop_instances(
        InstanceIds = [
            instance_id
            ],
    )
    print(instance_id, "Stopped")
    
def stop_dev_instance():
    response = ec2.describe_instances()    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Environment":
                        if tag["Value"] == "Dev":
                            stop_instance(ec2, instance["InstanceId"])

    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    stop_dev_instance()
