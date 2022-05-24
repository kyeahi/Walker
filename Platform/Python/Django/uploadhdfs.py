def sendfile():
    global num
    # 카프카 프로듀서 기본 설정
    producer = KafkaProducer(
        acks=0,
        compression_type='gzip',
        bootstrap_servers=['Ip Adress:9092'],  # IP주소
        value_serializer=lambda v: dumps(v).encode('utf-8'),
    )

    client_hdfs = InsecureClient('http://Ip Adress' + ':50070') # IP 주소 적기
    client_hdfs.upload('/', './media/result/' + str(num) + '.mp4')

    producer.send('video', {
        'title': str(num) + '.mp4',
    })
    time.sleep(0.2)  # 부하를 막기 위해 0.2초 쉬기

    producer.flush()  # 데이터 비우기

    num += 1
