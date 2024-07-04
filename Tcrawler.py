import pandas as pd
import requests
from lxml import etree


def find_price_range_intersection(price_range):
    # 将字符串转换为（min, max）元组

    intersection = price_range[0]

    # 遍历剩余的价格区间
    for current_range in price_range[1:]:

        # 当前区间与交集的交集
        new_intersection = (
            max(intersection[0], current_range[0]),
            min(intersection[1], current_range[1])
        )

        # 检查新的交集是否有效
        if new_intersection[0] > new_intersection[1]:
            continue

            # 更新交集
        intersection = new_intersection

    return intersection


class Crawler:
    def __init__(self, top=20):

        pd.options.mode.chained_assignment = None
        self.ev_cars = []
        self.fuel_cars = []
        self.all_cars = []

        self.top = top

        self.df = pd.DataFrame()
        self.merged_df = pd.DataFrame()
        self.ev_df = pd.DataFrame()
        self.fc_df = pd.DataFrame()

        self.crawl()
        self.to_df()

        self.ev_price_range = [(float(self.ev_df.loc[_, 'LPrice']), float(self.ev_df.loc[_, 'HPrice'])) for _ in
                               range(self.top)]
        # print(self.ev_price_range)
        self.fc_price_range = [(float(self.fc_df.loc[_, 'LPrice']), float(self.fc_df.loc[_, 'HPrice'])) for _ in
                               range(self.top)]
        # print(self.ev_price_range)
        self.ev_intersection = find_price_range_intersection(self.ev_price_range)
        self.fc_intersection = find_price_range_intersection(self.fc_price_range)
        # print(self.ev_intersection)
        # print(self.fc_intersection)

    def crawl(self):
        # 爬取新能源车排行榜前self.top的相关数据
        session = requests.Session()  # 使用Session优化爬取速度
        headers_1 = {
            'Cookie': 'fvlid=1716013576861KOtAec71nT; sessionid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18'
                      '+14%3A26%3A06.790%7C%7C0; autoid=efc2d15769498f97fd8076ec436543f3; cookieCityId=110100; '
                      '__ah_uuid_ng=c_C6117FE6-D242-4853-9E44-38F3EAA90481; area=310120; '
                      'sessionuid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18+14%3A26%3A06.790%7C%7C0; '
                      'wwwjbtab=0%2C0; pvidlist=5d1bb3c7-35e5-42e1-9c33-e1ec416c1f153:631328:980272:0:1:5072904; '
                      'ASP.NET_SessionId=gsmxvlyrrd3i5nhgkngdvhk0; ahsids=5761_5964; historyseries=5761%2C5964; '
                      'sessionip=61.165.108.8; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1719028355,1719039011,'
                      '1719071065; ahpvno=70; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1719072085; v_no=21; '
                      'visit_info_ad=C6117FE6-D242-4853-9E44-38F3EAA90481||B1ECA9E0-678B-4FCE-B7DC-4EC0A8CD1A07||-1'
                      '||-1||21; ref=0%7C0%7C0%7C0%7C2024-06-23+00%3A01%3A25.523%7C2024-05-18+14%3A26%3A06.790',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/126.0.0.0 Safari/537.36',
        }
        url_1 = 'https://www.autohome.com.cn/rank/9-2305-0-0_9000-x-x-x/2024-05.html'
        html_1 = session.get(url_1, headers=headers_1).text
        et_1 = etree.HTML(html_1)
        for i in range(1, self.top + 1):
            temp_dict = {}
            MZ_1 = et_1.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[1]/text()')
            JG_1 = et_1.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[3]/text()')
            XL_1 = et_1.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[4]/div[1]/span/text()')
            PF_1 = et_1.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(
                    i) + ']/div[3]/div[2]/span/strong/text()')
            ID_1 = et_1.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/button/@data-series-id')

            MZ_1 = ','.join(MZ_1)  # 新能源车名字
            JG_1 = ','.join(JG_1)  # 新能源车价格
            XL_1 = ','.join(XL_1)  # 新能源车销量
            PF_1 = ','.join(PF_1)  # 新能源车评分
            ID_1 = ','.join(ID_1)  # 新能源车在汽车之家的ID

            url_t = 'https://www.autohome.com.cn/' + ID_1
            html_t = session.get(url_t, headers=headers_1).text
            et_t = etree.HTML(html_t)
            LVL_1 = et_t.xpath('/html/body/div[2]/div[3]/div[4]/div[1]/div[1]/div[2]/dl[1]/dd[3]/span[1]/text()')
            LVL_1 = ','.join(LVL_1)  # 新能源车的级别

            high = 0
            low = 0

            if JG_1 != '暂无报价':
                tlis = ''.join(JG_1.split("万")).split('-')
                high = tlis[1]
                low = tlis[0]

            temp_dict['Type'] = '新能源车'
            temp_dict['Name'] = MZ_1.strip()
            temp_dict['LPrice'] = low
            temp_dict['HPrice'] = high
            temp_dict['Sales'] = XL_1.strip()
            temp_dict['Score'] = PF_1.strip()
            temp_dict['Level'] = LVL_1.strip()

            # print(str(i), MZ_1, JG_1, XL_1, PF_1, LVL_1)
            self.ev_cars.append(temp_dict)

        # 爬取燃油车排行榜前self.top的相关数据
        headers_2 = {
            'Cookie': 'fvlid=1716013576861KOtAec71nT; sessionid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18'
                      '+14%3A26%3A06.790%7C%7C0; autoid=efc2d15769498f97fd8076ec436543f3; cookieCityId=110100; '
                      '__ah_uuid_ng=c_C6117FE6-D242-4853-9E44-38F3EAA90481; area=310120; '
                      'sessionuid=C6117FE6-D242-4853-9E44-38F3EAA90481%7C%7C2024-05-18+14%3A26%3A06.790%7C%7C0; '
                      'wwwjbtab=0%2C0; pvidlist=5d1bb3c7-35e5-42e1-9c33-e1ec416c1f153:631328:980272:0:1:5072904; '
                      'ASP.NET_SessionId=gsmxvlyrrd3i5nhgkngdvhk0; '
                      'Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1719028355,1719039011,1719071065; '
                      'Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1719072085; sessionip=61.165.109.24; '
                      'ahsids=5769_5761_5964; historyseries=5769%2C5761%2C5964; ahpvno=77; '
                      'sessionvid=E6B929E8-CA56-4575-BEBC-950912D2EA3C; v_no=5; '
                      'visit_info_ad=C6117FE6-D242-4853-9E44-38F3EAA90481||E6B929E8-CA56-4575-BEBC-950912D2EA3C||-1'
                      '||-1||5; ref=0%7C0%7C0%7C0%7C2024-06-23+13%3A27%3A10.675%7C2024-05-18+14%3A26%3A06.790; '
                      'ahrlid=1719120431078YZ5GMSXZrY-1719120446160',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/126.0.0.0 Safari/537.36',
        }
        url_2 = 'https://www.autohome.com.cn/rank/1-1-0-0_9000-x-1-x/2024-05.html'
        html_2 = session.get(url_2, headers=headers_2).text
        et_2 = etree.HTML(html_2)

        for i in range(1, self.top + 1):
            temp_dict = {}
            MZ_2 = et_2.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[1]/text()')
            JG_2 = et_2.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[3]/div[3]/text()')
            XL_2 = et_2.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/div[4]/div[1]/span/text()')
            PF_2 = et_2.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(
                    i) + ']/div[3]/div[2]/span/strong/text()')
            ID_2 = et_2.xpath(
                '/html/body/main/div/div[2]/div[3]/div[1]/div[2]/div/div/div[' + str(i) + ']/button/@data-series-id')

            MZ_2 = ','.join(MZ_2)  # 燃油车名字
            JG_2 = ','.join(JG_2)  # 燃油车价格
            XL_2 = ','.join(XL_2)  # 燃油车销量
            PF_2 = ','.join(PF_2)  # 燃油车评分
            ID_2 = ','.join(ID_2)  # 燃油车在汽车之家的ID

            url_t = 'https://www.autohome.com.cn/' + ID_2
            html_t = session.get(url_t, headers=headers_2).text
            et_t = etree.HTML(html_t)
            LVL_2 = et_t.xpath('/html/body/div[2]/div[3]/div[4]/div[1]/div[1]/div[2]/dl[1]/dd[3]/span[1]/text()')
            LVL_2 = ','.join(LVL_2)  # 燃油车的级别

            high = 0
            low = 0

            if JG_2 != '暂无报价':
                tlis = ''.join(JG_2.split("万")).split('-')
                high = tlis[1]
                low = tlis[0]

            temp_dict['Type'] = '燃油车'
            temp_dict['Name'] = MZ_2.strip()
            temp_dict['LPrice'] = low
            temp_dict['HPrice'] = high
            temp_dict['Sales'] = XL_2.strip()
            temp_dict['Score'] = PF_2.strip()
            temp_dict['Level'] = LVL_2.strip()

            # print(str(i), MZ_2, JG_2, XL_2, PF_2, LVL_2)
            self.fuel_cars.append(temp_dict)

    def to_df(self):
        # 将新能源车和燃油车的数据合并到一个DataFrame中
        self.all_cars = self.ev_cars + self.fuel_cars
        self.df = pd.DataFrame(self.all_cars)
        self.ev_df = pd.DataFrame(self.ev_cars)
        self.fc_df = pd.DataFrame(self.fuel_cars)
        # self.merged_df = self.df.groupby(['Type']).apply(lambda x:x[:], include_groups=False)
        # print(self.merged_df)

    def save_to_file(self, filename, file_format):

        # 将DataFrame保存到文件
        if file_format == 'xlsx':
            self.df.to_excel(filename, index=False)
        elif file_format == 'csv':
            self.df.to_csv(filename, index=False, encoding='utf-8-sig')  # 对于中文文件名和中文列名，可能需要使用utf-8-sig编码
        else:
            print(f"Unsupported file format: {file_format}")


cr = Crawler()
cr.save_to_file('./assets/cars_data.xlsx', 'xlsx')  # 保存为Excel文件
cr.save_to_file('./assets/cars_data.csv', 'csv')  # 保存为CSV文件
