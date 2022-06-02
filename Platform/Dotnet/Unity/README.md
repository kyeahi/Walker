# Kafka

## Installation
`Install-Package Newtonsoft.Json`
- Dotnet Json
`Install-Package Confluent.Kafka -Version 1.8.2`
- Kafka Dotnet API

## Command
### Consumer
### Connection
```
var conf = new ConsumerConfig
{
    GroupId, 
    BootstrapServers,
    AutoOffsetReset
};
```
- GroupID : Consumer 그룹 아이디 설정
- BootstrapServers : broker 리스트
- AutoOffsetReset : 오프셋

### Subscribe
```
using (var c = new ConsumerBuilder<Ignore, string>(conf).Build())
{
    c.Subscribe("Bucket_Name");
    CancellationTokenSource cts = new CancellationTokenSource();
    Console.CancelKeyPress += (_, e) => {
    e.Cancel;
    cts.Cancel();
};
```
- 구독할 토픽 이름 설정


<br><br>URL : https://docs.confluent.io/kafka-clients/dotnet/current/overview.html



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
