import boto3, configparser

def move_to_archive(bucket_name, source_key):
    config = configparser.ConfigParser()
    config.read(r'C:\Users\Sravani\Documents\mongoDB_task_2\config.ini')

    aws_access_key = config['AWS']['aws_access_key']
    aws_secret_access_key = config['AWS']['aws_secret_access_key']
    region_name = config['AWS']['region_name']

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    dest_key = source_key.replace("resumes/", "archive/")
    s3.copy_object(Bucket=bucket_name, CopySource={'Bucket': bucket_name, 'Key': source_key}, Key=dest_key)
    s3.delete_object(Bucket=bucket_name, Key=source_key)