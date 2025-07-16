import boto3, os, configparser

def upload_attachments_to_s3(attachments, sender_email, bucket_name, s3_prefix="emails/"):
    config = configparser.ConfigParser()
    config.read('config.config')

    aws_access_key = config['AWS']['aws_access_key']
    aws_secret_access_key = config['AWS']['aws_secret_access_key']
    region_name = config['AWS']['region_name']

    s3 = boto3.client("s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    folder_name = sender_email.replace("@", "_at_")
    s3_folder_url = f"s3://{bucket_name}/{s3_prefix}{folder_name}/"

    for local_file in attachments:
        try:
            filename = os.path.basename(local_file)
            s3_key = f"{s3_prefix}{folder_name}/{filename}"
            print(f"Uploading {local_file} to S3 as {s3_key}...")
            s3.upload_file(local_file, bucket_name, s3_key)
        except Exception as e:
            print(f"Failed to upload {local_file} to S3: {e}")

    return s3_folder_url