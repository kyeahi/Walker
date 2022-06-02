import boto3

BUCKET_NAME = 'Bucketname'

s3 = boto3.client(
        service_name='s3',            # Use_service
        region_name='ap-northeast-2', # bucket_region
)

s3.upload_file('local_URL', BUCKET_NAME, 'chanege_name')  # upload_file
s3.download_file(BUCKET_NAME, 'BUCKET_URL', 'LOCAL_URL')  # upload_file
