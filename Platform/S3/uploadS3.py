# pip install boto3

# csv, pt를 s3에 저장하는 부분
import datetime
import boto3
import os
from config import AWS_ACCESS_KEY, AWS_SECRET_KEY


now = datetime.date.today()
print(now)

# s3 연결
os.environ['AWS_DEFAULT_REGION'] = "ap-northeast-2" # 자신이 설정한 bucket region, 대한민국

s3 = boto3.client('s3',
                 aws_access_key_id = AWS_ACCESS_KEY,
            	   aws_secret_access_key = AWS_SECRET_KEY)
)

bucket_name = 'bucket' # 버켓이름
csvfile = '.csv' # 저장할 csv 파일
ptfile = '.pt' # 저장할 pt 파일

filepath = '/' + str(now)# 현재 시각 위치를 기준
ptfilepath = '/' + ptfile # 저장할 파일 이름
csvfilepath = '/' + csvfile # 저장할 파일 이름


# s3에 얿로드
s3.upload_file(csvfile, bucket_name, filepath + ptfilepath)
s3.upload_file(ptfile, bucket_name, filepath + csvfilepath)
