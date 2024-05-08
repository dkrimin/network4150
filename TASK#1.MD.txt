PS C:\itmo> ping ya.ru

Pinging ya.ru [5.255.255.242] with 32 bytes of data:
Reply from 5.255.255.242: bytes=32 time=12ms TTL=54
Reply from 5.255.255.242: bytes=32 time=30ms TTL=54
Reply from 5.255.255.242: bytes=32 time=15ms TTL=54
Reply from 5.255.255.242: bytes=32 time=14ms TTL=54

Ping statistics for 5.255.255.242:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 12ms, Maximum = 30ms, Average = 17ms
PS C:\itmo> netstat

Active Connections

  Proto  Local Address          Foreign Address        State
  TCP    192.168.168.105:1797   xiva-daria:https       ESTABLISHED
  TCP    192.168.168.105:1816   20.54.37.73:https      ESTABLISHED
  TCP    192.168.168.105:2245   lt-in-f188:5228        ESTABLISHED
  TCP    192.168.168.105:2251   ec2-34-224-118-116:https  ESTABLISHED
  TCP    192.168.168.105:2258   cdn-185-199-108-154:https  ESTABLISHED
  TCP    192.168.168.105:2377   cdn-185-199-109-133:https  ESTABLISHED
  TCP    192.168.168.105:2388   lb-140-82-113-25-iad:https  ESTABLISHED
  TCP    192.168.168.105:2409   a95-101-10-163:https   CLOSE_WAIT
  TCP    192.168.168.105:2411   152.199.19.161:https   CLOSE_WAIT
  TCP    192.168.168.105:2412   152.199.19.161:https   CLOSE_WAIT
  TCP    192.168.168.105:2414   a87-245-209-240:https  CLOSE_WAIT
  TCP    192.168.168.105:2416   149.154.167.41:https   ESTABLISHED
  TCP    192.168.168.105:2417   68.220.193.245:https   CLOSE_WAIT
  TCP    192.168.168.105:2418   68.220.193.245:https   CLOSE_WAIT

PS C:\itmo\network4150> nslookup ya.ru
Server:  UnKnown
Address:  192.168.168.1

Non-authoritative answer:
Name:    ya.ru
Addresses:  2a02:6b8::2:242
          77.88.55.242
          5.255.255.242

PS C:\itmo\network4150>


PS C:\itmo\network4150> tracert ya.ru

Tracing route to ya.ru [5.255.255.242]
over a maximum of 30 hops:

  1    19 ms    10 ms     6 ms  192.168.168.1
  2    11 ms     2 ms     7 ms  10.200.0.23
  3    11 ms     6 ms     1 ms  spb-r2-cr1.ae54-1417.rascom.as20764.net [80.64.102.128]
  4     *        *        *     Request timed out.
  5    57 ms     9 ms    12 ms  yandex-pni.rascom.as20764.net [81.27.254.74]
  6     *        *        *     Request timed out.



   50  44.029305 Intel_64:b4:37 → MercusysTech_a9:73:a9 ARP 42 192.168.168.105 is at 04:56:e5:64:b4:37
   51  54.062056 MercusysTech_a9:73:a9 → Broadcast    ARP 42 Who has 192.168.168.106? Tell 192.168.168.1
   52  54.985567 MercusysTech_a9:73:a9 → Broadcast    ARP 42 Who has 192.168.168.105? Tell 192.168.168.1
   53  54.985567 MercusysTech_a9:73:a9 → Broadcast    ARP 42 Who has 192.168.168.106? Tell 192.168.168.1
   54  54.985595 Intel_64:b4:37 → MercusysTech_a9:73:a9 ARP 42 192.168.168.105 is at 04:56:e5:64:b4:37
   55  56.006817 MercusysTech_a9:73:a9 → Broadcast    ARP 42 Who has 192.168.168.105? Tell 192.168.168.1
   56  56.006842 Intel_64:b4:37 → MercusysTech_a9:73:a9 ARP 42 192.168.168.105 is at 04:56:e5:64:b4:37
   57  57.033091 MercusysTech_a9:73:a9 → Broadcast    ARP 42 Who has 192.168.168.101? Tell 192.168.168.1


