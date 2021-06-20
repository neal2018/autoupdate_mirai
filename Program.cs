using System;
using Microsoft.AspNetCore.SignalR.Client;
using System.Net;
using System.Threading.Tasks;
using System.IO;

namespace aspnetcoreapp
{
    public class Program
    {
        static async Task Main()
        {
            var IP = Dns.GetHostEntry("cynthia.ovyno.com").AddressList[0];
            var hub = new HubConnectionBuilder().WithUrl($"http://{IP}:5005/hub/gwent").Build();
            await hub.StartAsync();
            var cardMap = await hub.InvokeAsync<string>("GetCardMap");
            File.WriteAllText($"test.json", cardMap);
        }
    }
}
