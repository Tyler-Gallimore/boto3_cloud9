import boto3

def stop_instance(client, instance_id):
    response = client.stop_instances(
        InstanceIds = [
            instance_id
            ],
    )
    print(instance_id, "Stopped")
    
def describe_instance():

    response = ec2.describe_instances()
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(instance["InstanceId"], instance["State"]["Name"])
            
            if "Tags" in instance:
                for tag in instance["Tags"]:
                    if tag["Key"] == "Environment":
                        stop_instance(ec2, instance)

    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    #instance_id = "i-0aebcc42034c6dc79"
    #terminate_instance(ec2, instance_id)
    describe_instance()