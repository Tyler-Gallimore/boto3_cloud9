import boto3

def list_object_keys(client, bucket, prefix = ""):
    keys = []
    response = client.list_objects_v2(Bucket = bucket, Prefix = prefix)
    for content in response["Contents"]:
        keys.append(content["Key"])
    return keys

s3 = boto3.client('s3')


response = list_object_keys(s3, "Placeholderbucket", "/")
