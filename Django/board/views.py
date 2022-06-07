# pip install dhfs
# pip install kafka-python

import os
from django.shortcuts import render
from config.settings import BASE_DIR
from . import models
from kafka import KafkaProducer
from json import dumps
from hdfs import InsecureClient
import time
import boto3
import environ


num = 0

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

def uploadFile(request):
    global num
    if request.method == "POST":

        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # local로 데이터 저장
        # kafka부분에서 될 경우 지울 예정
        document = models.Document(
            title=fileTitle,
            uploadedFile=uploadedFile
        )

        document.save()

        filepath = './media/result/' + str(uploadedFile)
        os.rename(filepath, './media/result/' + str(num) + '.mp4')

        sendfile()
        os.remove('./media/result/' + str(num) + '.mp4')
        num += 1


    if request.method == "GET":
        return render(request, "upload-file.html")

    documents = models.Document.objects.all()

    return render(request, "upload-file.html", context={
        "files": documents
    })

def sendfile():
    global num
    # 카프카 기본 설정
    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['172.16.1.64:9092'],  # IP주소
        value_serializer=lambda v: dumps(v).encode('utf-8'),
    )

    BUCKET_NAME = 'team4bucket'

    s3 = boto3.client(
        service_name='s3',
        region_name='ap-northeast-2',
    )

    # BUCKET_NAME = 'mycsvpt'
    #
    # s3 = boto3.client(
    #     service_name='s3',
    #     region_name=os.environ['Region_name'],
    #     aws_access_key_id=os.environ['aws_access_key_id'],
    #     aws_secret_access_key=os.environ['aws_secret_access_key'],
    # )

    s3.upload_file('./media/result/' + str(num) + '.mp4', BUCKET_NAME, 'mp4/' + str(num) + '.mp4')
    # client_hdfs = InsecureClient('http://172.30.1.248' + ':9870') # IP 주소 적기
    # client_hdfs.upload('/', './media/result/' + str(num) + '.mp4')



    producer.send('sendvideo', {
        'title': str(num) + '.mp4',
    })
    time.sleep(0.2)  # 부하를 막기 위해 0.2초 쉬기

    producer.flush()  # 데이터 비우기



def result(request):

    return render(request, "result.html")

