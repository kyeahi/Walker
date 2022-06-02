# Kafka

## Installation
`pip install kafka-python`
- Kafka Python API

## Command
### Producer
### Connection
`producer = KafkaProducer(acks, compression_type, bootstrap_servers)`
- acks : 메세지를 보낸 후 요청 완료 전 승인 수
- bootstrap.server : broker 리스트
- compression_type : 데이터 압축 종류
### Send
`producer.send()`
- JSON 형식으로 보낼 것
### Flush
`producer.flush()`
- Send 이후, flush 필요함 > 이전의 값이 남아있음<br><hr>

### Consumer
### Connection
`consumer = KafkaConsumer(topic_name, bootstrap_servers, auto_offset_reset, enable_auto_commit, group_id, value_deserializer, consumer_timeout_ms)`
- bootstrap_servers : broker 리스트
- auto_offset_reset : 오프셋 값 설정
- enable_auto_commit : 주기적으로 오프셋 commint
- group_id : consumer 그룹 이름

<br><br>URL : https://github.com/dpkp/kafka-python



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
