// Install-Package aws.core
// Install-Package aws.s3

using Amazon;
using Amazon.S3;
using Amazon.S3.Model;
using Amazon.S3.Transfer;
using System;
using System.IO;
using System.Threading.Tasks;

namespace Amazon.DocSamples.S3
{
    class GetObjectTest
    {
        private const string bucketName = "zzz";
        private const string keyName = "";           // 받을 데이터 이름
        // Specify your bucket region (an example region is shown).
        private static readonly RegionEndpoint bucketRegion = RegionEndpoint.APNortheast2; // 대한민국 지역
        private static IAmazonS3 client;

        public static void Main()
        {
            client = new AmazonS3Client(bucketRegion);
            ReadObjectDataAsync().Wait();
        }

        static async Task ReadObjectDataAsync()
        {
            string responseBody = "";
            try
            {
                GetObjectRequest request = new GetObjectRequest
                {
                    BucketName = bucketName,
                    Key = keyName
                };
                using (GetObjectResponse response = await client.GetObjectAsync(request))
                using (Stream responseStream = response.ResponseStream)

                // 파일이 유무 확인
                using (StreamReader reader = new StreamReader(responseStream))
                {
                    string title = response.Metadata["x-amz-meta-title"]; // Assume you have "title" as medata added to the object.
                    string contentType = response.Headers["Content-Type"];
                    Console.WriteLine("Object metadata, Title: {0}", title);    // 파일 이름
                    Console.WriteLine("Content type: {0}", contentType);        // 파일 확장자

                    responseBody = reader.ReadToEnd(); // Now you process the response body.
                }

                // 다운로드 받는 코드 
                using (TransferUtility transferUtility = new Amazon.S3.Transfer.TransferUtility(bucketRegion))
                {
                    TransferUtilityDownloadRequest downloadRequest = new TransferUtilityDownloadRequest
                    {
                        BucketName = bucketName,
                        Key = keyName,
                        FilePath = keyName
                    };
                    transferUtility.Download(downloadRequest);
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
}
