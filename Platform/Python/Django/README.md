# Hdfs

## Installation
`pip install hdfs`
- hdfs Python API

## Command

### Connection
`hdfs.client.Client(url, root=None, proxy=None, timeout=None, session=None)`

### Upload
`upload(hdfs_path, local_path, n_threads=1, temp_dir=None, chunk_size=65536, progress=None, cleanup=True, **kwargs)`

### Download
`download(hdfs_path, local_path, overwrite=False, n_threads=1, temp_dir=None, **kwargs)`
<br><br><br>URL : https://hdfscli.readthedocs.io/en/latest/api.html



# S3
## Installation
`pip install boto3`<br>
- Python AWS SDK > AWS 서비스 연동 및 실행

`pip install awscli`
- aws 명령줄 인터페이스 > 설치 후 aws configure > AccessID, AccessPW, Bucket_Region 등 설정

## Command

### Connection
`s3 = boto3.client(accessID, accessPW, service_name, region_name)`
- accessID, accessPW, service_name는 보안을 위해 awscli를 통해 설정해주는 것을 추천
- 참고 URL : https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html

### Upload
`s3.upload(local_URL, Bucket_NAME, Object_Name)`

### Download
`s3.download(Bucket_NAME, Bucket_URL, local_URL)`


<br>URL : https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html
