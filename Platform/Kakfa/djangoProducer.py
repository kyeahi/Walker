# pip install dhfs
# pip install kafka-python

from kafka import KafkaProducer
from json import dumps
from hdfs import InsecureClient

def sendfile():
    global num
    
    # 카프카 기본 설정
    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=[':9092'],  # IP주소
        value_serializer=lambda v: dumps(v).encode('utf-8'),
    )

    client_hdfs = InsecureClient('http://192.168.66.143' + ':9870') # IP 주소 적기
    client_hdfs.upload('/', './media/result/' + str(num) + '.mp4') # 저장한 mp4 파일 

    producer.send('video', {
        'title': str(num) + '.mp4',
    })
    time.sleep(0.2)  # 부하를 막기 위해 0.2초 쉬기

    producer.flush()  # 데이터 비우기

    num += 1
