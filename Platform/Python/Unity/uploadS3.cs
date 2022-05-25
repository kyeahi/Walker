// UPLOAD
// Install-Package AWSSDK.core
// Install-Package AWSSDK.s3

using Amazon.S3;
using Amazon.S3.Transfer;
using Amazon;

class Program
{
    private const string bucketName = "bucket 이름";
    public static string keyName = "data 이름";           // 받을 데이터 이름
                                                 // Specify your bucket region (an example region is shown).
    private static readonly RegionEndpoint bucketRegion = RegionEndpoint.APNortheast2; # 저장소 지역
    private static IAmazonS3 client;
    public static void Main(string[] args)
    {

        client = new AmazonS3Client(bucketRegion);
        ReadObjectDataAsync().Wait();
        // keyName flush
        keyName = "";
        Console.WriteLine("Download Complete!!");
    }

    static async Task ReadObjectDataAsync()
    {
        try
        {
            using(TransferUtility transferUtility = new Amazon.S3.Transfer.TransferUtility(bucketRegion))
            {
                TransferUtilityUploadRequest uploadRequest = new TransferUtilityUploadRequest
                {
                    BucketName = bucketName,
                    Key = keyName,
                    FilePath = Directory.GetCurrentDirectory()
                };
                transferUtility.Upload(uploadRequest);
            }
        }
        catch (AmazonS3Exception e)
        {
            // If bucket or object does not exist
            Console.WriteLine("Error encountered ***. Message:'{0}' when reading object", e.Message);
        }
        catch (Exception e)
        {
            Console.WriteLine("Unknown encountered on server. Message:'{0}' when reading object", e.Message);
        }
    }
}
