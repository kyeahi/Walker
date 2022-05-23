# pip install kafka-python
# pip install hdfs
# pip install opencv-python
# pip install awscli
# pip install boto3
# 액세스 키 ID : 
# 액세스 키 PW : 

import subprocess
from hdfs import InsecureClient
from kafka import KafkaConsumer
from json import loads
import cv2
import os

# Kafka Consumer 셋팅
consumer = KafkaConsumer(
    'video',
    bootstrap_servers=['브로커주소:포트번호'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    consumer_timeout_ms=1000
)


# 통신한 hdfs 주소
client_hdfs = InsecureClient('http://hdfs_ip:50070')
client_hdfs.download('경로(hdfs)', '다운받을 장소(spark)', overwrite=False, threads=1,temp_dir=None)


filepath = '/' + str(consumer.title)
video = cv2.VideoCapture(filepath) #'' 사이에 사용할 비디오 파일의 경로 및 이름을 넣어주도록 함

fps = video.get(cv2.CAP_PROP_FPS)
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))


# 비디오 데이터 확인
print('********************')
print('filepath', filepath)
print('fps', fps)
print('length', length)
print('width', width)
print('height', height)
print('********************')


# 디렉토리 생성
try:
    if not os.path.exists('/' + filepath[:-4]):
        subprocess.call('mkdir' + filepath[:-4])

except OSError:
    print ('Error: Creating directory. ' + filepath[:-4])


# 동영상파일 이미지로 자르기
count = 0
while(video.isOpened()):
    # 이미지 회색으로 변경
    try:
        ret, image = video.read()
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        image = cv2.resize(image, (800, 400))  # 이미지 800*400으로 변경

    except:
        break;
        video.release()

    if(int(video.get(1)) % num == 0): # num의 숫자마다 저장됨
        cv2.imwrite('/'+filepath[:-4] + "/" + filepath[:-4] + "%d.jpg" % count, image)
        # print('Saved frame number :', str(int(video.get(1))))
        count += 1
video.release()

# 이미지 압축
subprocess.call('tar -zcvf' + filepath[:-4] + '*' + '.jpg', shell=True)

# 이미지 hadoop으로 업로드
client_hdfs = InsecureClient('http://192.168.66.143' + ':9870') # IP 주소 적기
client_hdfs.upload('/', '/' + filepath[:-4] + '.tar.gz') # 이미지 파일 압축해서 저장

# spark 모델 부분

# spark 모델 부분 끝


# csv, pt를 s3에 저장하는 부분
import datetime
import boto3
import os

now = datetime.date.today()
print(now)

# s3 연결
os.environ['AWS_DEFAULT_REGION'] = "ap-northeast-2" # 자신이 설정한 bucket region

s3 = boto3.client('s3')

bucket_name = 'mycsvpt'
csvfile = 'ChatbotData.csv' # 저장할 데이터
ptfile = 'checkpoint.pt' # 저장할 데이터

filepath = '/' + str(now)# 현재 시각 위치를 기준
ptfilepath = '/' + ptfile # 저장할 파일 이름
csvfilepath = '/' + csvfile # 저장할 파일 이름


# s3에 얿로드
s3.upload_file(csvfile, bucket_name, filepath + ptfilepath)
s3.upload_file(ptfile, bucket_name, filepath + csvfilepath)
