import boto3

def stop_instance(client, instance_id):
    response = client.stop_instances(
        InstanceIds = [
            instance_id
            ],
    )
    print(instance_id, "Stopped")

def start_instance(client, instance_id):
    response = client.start_instances(
        InstanceIds = [
            instance_id
            ],
    )
    print(instance_id, "Started")
    
def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds = [
            instance_id
            ],
    )
    print(instance_id, "Terminated")
    
if __name__ == '__main__':
    ec2 = boto3.client('ec2')
    instance_id = "i-0aebcc42034c6dc79"
    terminate_instance(ec2, instance_id)