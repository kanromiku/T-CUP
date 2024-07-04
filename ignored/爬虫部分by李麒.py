import requests
from lxml import etree

headers_1 = {
    'Cookie': 'fvlid=1716013576861KOtAec71nT; sessionid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18+14%3A26%3A06.790%7C%7C0; autoid=efc2d15769498f97fd8076ec436543f3; cookieCityId=110100; __ah_uuid_ng=c_C6117FE6-D242-4853-9E44-38F3EAA90481; area=310120; sessionuid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18+14%3A26%3A06.790%7C%7C0; wwwjbtab=0%2C0; pvidlist=5d1bb3c7-35e5-42e1-9c33-e1ec416c1f153:631328:980272:0:1:5072904; ASP.NET_SessionId=gsmxvlyrrd3i5nhgkngdvhk0; ahsids=5761_5964; historyseries=5761%2C5964; sessionip=61.165.108.8; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1719028355,1719039011,1719071065; ahpvno=70; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1719072085; v_no=21; visit_info_ad=C6117FE6-D242-4853-9E44-38F3EAA90481||B1ECA9E0-678B-4FCE-B7DC-4EC0A8CD1A07||-1||-1||21; ref=0%7C0%7C0%7C0%7C2024-06-23+00%3A01%3A25.523%7C2024-05-18+14%3A26%3A06.790',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
url_1 = 'https://www.autohome.com.cn/rank/9-2305-0-0_9000-x-x-x/2024-05.html'
html_1 = requests.get(url_1, headers=headers_1).text
et_1 = etree.HTML(html_1)
for i in range(21):
    MZ_1 = et_1.xpath(
        '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[1]/text()')
    JG_1 = et_1.xpath(
        '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[3]/text()')
    XL_1 = et_1.xpath(
        '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[4]/div[1]/span/text()')
    MZ_1 = ','.join(MZ_1)  # 新能源车名字
    JG_1 = ','.join(JG_1)  # 新能源车价格
    XL_1 = ','.join(XL_1)  # 新能源车销量
    print(str(i), MZ_1, JG_1, XL_1)

headers_2 = {
    'Cookie': 'fvlid=1716013576861KOtAec71nT; sessionid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18+14%3A26%3A06.790%7C%7C0; autoid=efc2d15769498f97fd8076ec436543f3; cookieCityId=110100; __ah_uuid_ng=c_C6117FE6-D242-4853-9E44-38F3EAA90481; area=310120; sessionuid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18+14%3A26%3A06.790%7C%7C0; wwwjbtab=0%2C0; pvidlist=5d1bb3c7-35e5-42e1-9c33-e1ec416c1f153:631328:980272:0:1:5072904; ASP.NET_SessionId=gsmxvlyrrd3i5nhgkngdvhk0; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1719028355,1719039011,1719071065; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1719072085; sessionip=61.165.109.24; ahsids=5769_5761_5964; historyseries=5769%2C5761%2C5964; ahpvno=77; sessionvid=E6B929E8-CA56-4575-BEBC-950912D2EA3C; v_no=5; visit_info_ad=C6117FE6-D242-4853-9E44-38F3EAA90481||E6B929E8-CA56-4575-BEBC-950912D2EA3C||-1||-1||5; ref=0%7C0%7C0%7C0%7C2024-06-23+13%3A27%3A10.675%7C2024-05-18+14%3A26%3A06.790; ahrlid=1719120431078YZ5GMSXZrY-1719120446160',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}
url_2 = 'https://www.autohome.com.cn/rank/1-1-0-0_9000-x-1-x/2024-05.html'
html_2 = requests.get(url_2, headers=headers_2).text
et_2 = etree.HTML(html_2)

for i in range(21):
    MZ_2 = et_2.xpath(
        '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[1]/text()')
    JG_2 = et_2.xpath(
        '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[3]/text()')
    XL_2 = et_2.xpath(
        '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[4]/div[1]/span/text()')
    MZ_2 = ','.join(MZ_2)  # 燃油车名字
    JG_2 = ','.join(JG_2)  # 燃油车价格
    XL_2 = ','.join(XL_2)  # 燃油车销量
    print(str(i), MZ_2, JG_2, XL_2)
