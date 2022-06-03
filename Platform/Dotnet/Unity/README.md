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
`Install-Package AWSSDK.s3`<br>
- AWS S3 Dotnet API

`Install-Package AWSSDK.core`
- .Net AWS SDK

## Command

### Connection
`client = new AmazonS3Client(accesskeyID, accesskeyPW, bucketRegion);`
- accessID, accessPW, bucketRegion 설정 필요
- 보안을 위해 accessID, accessPW는 따로 터미널에서 설정해주는 것을 추천

### Upload
```
using (TransferUtility transferUtility = new Amazon.S3.Transfer.TransferUtility(accesskeyID, accesskeyPW, bucketRegion))
{
    TransferUtilityUploadRequest uploadRequest = new TransferUtilityUploadRequest
    {
        BucketName = bucketName,
        Key = key,
        FilePath = UploadFile
    };
    transferUtility.Upload(uploadRequest);
}
```

### Download
```
using (TransferUtility transferUtility = new Amazon.S3.Transfer.TransferUtility(accesskeyID, accesskeyPW, bucketRegion))
{
    TransferUtilityDownloadRequest downloadRequest = new TransferUtilityDownloadRequest
    {
        BucketName = bucketName,
        Key = Key,
        FilePath = KeyPath
    };
    transferUtility.Download(downloadRequest);
}
```


<br>URL : https://docs.aws.amazon.com/ko_kr/sdk-for-net/v3/developer-guide/quick-start-s3-1-winvs.html
