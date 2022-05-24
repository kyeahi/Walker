// Install-Package Newtonsoft.Json
// Install-Package Confluent.Kafka -Version 1.8.2

using System;
using System.Threading;
using Confluent.Kafka;
using Newtonsoft.Json.Linq;


class Program
{
    public static void Main(string[] args)
    {
        var conf = new ConsumerConfig
        {
            GroupId = "test-consumer-group",
            BootstrapServers = "IP Adress", // broker ip 주소
            AutoOffsetReset = AutoOffsetReset.Earliest
        };

        using (var c = new ConsumerBuilder<Ignore, string>(conf).Build())
        {
            c.Subscribe("topic");            // 토픽 이름

            CancellationTokenSource cts = new CancellationTokenSource();
            Console.CancelKeyPress += (_, e) => {
                e.Cancel = true; // prevent the process from terminating.
                cts.Cancel();
            };

            try
            {
                while (true)
                {
                    try
                    {
                        var cr = c.Consume(cts.Token);
                        JObject json = JObject.Parse(cr.Value);
                        var valuept = json["pt"].ToString(); // pt 파일 다운로드
                        Console.WriteLine(valuept);
                        var valuecsv = json["csv"].ToString();
                        Console.WriteLine(valuecsv);         // csv 파일 다운로드
                    }
                    catch (ConsumeException e)
                    {
                        Console.WriteLine($"Error occured: {e.Error.Reason}");
                    }
                }
            }
            catch (OperationCanceledException)
            {
                // Ensure the consumer leaves the group cleanly and final offsets are committed.
                c.Close();
            }
        }
    }
}
