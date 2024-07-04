import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from Tcrawler import Crawler

mpl.rcParams['font.sans-serif'] = ['SimHei']

path1 = "./assets/ev"
path2 = "./assets/fv"
path3 = "./assets/general"

if not os.path.exists(path1):
    os.makedirs(path1)
if not os.path.exists(path2):
    os.makedirs(path2)
if not os.path.exists(path3):
    os.makedirs(path3)

class Draw(Crawler):
    def __init__(self):
        super().__init__()
        print(self.df)
        # print(self.top)
        self.ev_draw_price_and_sales()
        self.fv_draw_price_and_sales()
        self.ev_draw_score()
        self.fv_draw_score()
        self.level()

    def ev_draw_price_and_sales(self):
        ev = self.df[self.df['Type'] == '新能源车']
        ev.reset_index(drop=True, inplace=True)
        ev_sales = ev.loc[:, 'Sales']
        for i in range(self.top):
            ev.loc[i, 'MPrice'] = (float(ev.loc[i, 'LPrice']) + float(ev.loc[i, 'HPrice'])) / 2
        ev_MPrice = ev.loc[:, 'MPrice']
        std = []
        for i in range(self.top):
            x = float(ev.loc[i, 'HPrice']) - float(ev.loc[i, 'MPrice'])
            std.append(x)
        ev_label = ev.loc[:, 'Name']

        fig = plt.figure(figsize=(12, 6),dpi=200)

        ax1 = fig.add_axes((0.1, 0.1, 0.8, 0.8))
        ax2 = ax1.twinx()

        ax1.bar(
            x=ev_label,
            height=ev_MPrice,
            width=0.4,
            color='blue',
            yerr=std,
            ecolor='red',
            capsize=5,
            tick_label=ev_label
        )

        ax2.plot(ev_label, ev_sales,
                 color='green',
                 marker="o"
                 )
        ax2.invert_yaxis()

        ax1.set_xlabel('名称')
        ax1.set_ylabel('价格（单位：万元）')
        ax1.set_title('新能源车报价及销量')
        ax2.set_ylabel('销量')
        ax1.tick_params(axis="x", labelrotation=30)

        fig.savefig('./assets/ev/price_and_sales.png')

        #fig.show()

    def fv_draw_price_and_sales(self):
        fv = self.df[self.df['Type'] == '燃油车']
        fv.reset_index(drop=True, inplace=True)
        fv_sales = fv.loc[:, 'Sales']
        for i in range(self.top):
            fv.loc[i, 'MPrice'] = (float(fv.loc[i, 'LPrice']) + float(fv.loc[i, 'HPrice'])) / 2
        fv_MPrice = fv.loc[:, 'MPrice']
        std = []
        for i in range(self.top):
            x = float(fv.loc[i, 'HPrice']) - float(fv.loc[i, 'MPrice'])
            std.append(x)
        fv_label = fv.loc[:, 'Name']

        fig = plt.figure(figsize=(12, 6),dpi=200)

        ax3 = fig.add_axes((0.1, 0.1, 0.8, 0.8))
        ax4 = ax3.twinx()

        ax3.bar(
            x=fv_label,
            height=fv_MPrice,
            width=0.4,
            color='blue',
            yerr=std,
            ecolor='red',
            capsize=5,
            tick_label=fv_label
        )

        ax4.plot(fv_label, fv_sales,
                 color='green',
                 marker="o"
                 )
        ax4.invert_yaxis()

        ax3.set_xlabel('名称')
        ax3.set_ylabel('价格（单位：万元）')
        ax3.set_title('燃油车报价及销量')
        ax4.set_ylabel('销量')
        ax3.tick_params(axis="x", labelrotation=30)

        fig.savefig('./assets/fv/price_and_sales.png')

        #fig.show()


    def ev_draw_score(self):
        ev = self.df[self.df['Type'] == '新能源车']
        ev.reset_index(drop=True, inplace=True)
        ev_label = ev.loc[:, 'Name']
        ev_score = ev.loc[:, 'Score']
        sorted_indices = np.argsort(ev_score)
        ev_score_sorted = ev_score[sorted_indices]

        fig = plt.figure(figsize=(12, 6),dpi=200)

        ax1 = fig.add_axes((0.1, 0.1, 0.8, 0.8))

        ax1.scatter(ev_label, ev_score_sorted, color='green', marker='o')

        ax1.set_xlabel('名称（销量自左往右从高到低）')
        ax1.set_ylabel('评分')
        ax1.set_title(f'新能源车销量top{self.top}评分')
        ax1.tick_params(axis="x", labelrotation=30)

        fig.savefig('./assets/ev/score.png')

        #fig.show()


    def fv_draw_score(self):
        fv = self.df[self.df['Type'] == '燃油车']
        fv.reset_index(drop=True, inplace=True)
        fv_label = fv.loc[:, 'Name']
        fv_score = fv.loc[:, 'Score']
        sorted_indices = np.argsort(fv_score)
        fv_score_sorted = fv_score[sorted_indices]

        fig = plt.figure(figsize=(12, 6),dpi=200)

        ax1 = fig.add_axes((0.1, 0.1, 0.8, 0.8))

        ax1.scatter(fv_label, fv_score_sorted, color='green', marker='o')

        ax1.set_xlabel('名称（销量自左往右从高到低）')
        ax1.set_ylabel('评分')
        ax1.set_title(f'燃油车销量top{self.top}评分')
        ax1.tick_params(axis="x", labelrotation=30)

        fig.savefig('./assets/fv/score.png')

        #fig.show()

    def level(self):

        fv = self.df[self.df['Type'] == '燃油车']
        fv.reset_index(drop=True, inplace=True)
        fv_level = fv['Level'].value_counts()
        fv_key = list(fv_level.keys())
        fv_value = fv_level.tolist()

        ev = self.df[self.df['Type'] == '新能源车']
        ev.reset_index(drop=True, inplace=True)
        ev_level = ev['Level'].value_counts()
        ev_key = list(ev_level.keys())
        ev_value = ev_level.tolist()

        general = self.df
        general.reset_index(drop=True, inplace=True)
        general_level = general['Level'].value_counts()
        general_key = list(general_level.keys())
        general_value = general_level.tolist()

        fig = plt.figure(figsize=(12, 6), dpi=200)

        fig1=plt.subplot(1,3,1)
        fig1.pie(
            fv_value,
            labels=fv_key,
            # colors=['green','gold','red','blue','orange'],
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 10},
            pctdistance=0.75,
            labeldistance=1.1,
        )
        fig1.set_title('燃油车车型占比')

        fig2 = plt.subplot(1, 3, 2)
        fig2.pie(
            ev_value,
            labels=ev_key,
            # colors=['green', 'gold', 'red', 'blue', 'orange',''],
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 8},
            pctdistance=0.8,
            labeldistance=1.2,
        )
        fig2.set_title('新能源车车型占比')

        fig3 = plt.subplot(1, 3, 3)
        fig3.pie(
            general_value,
            labels=general_key,
            # colors=['green', 'gold', 'red', 'blue', 'orange'],
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 6.5},
            pctdistance=0.8,
            labeldistance=1.2
        )

        fig3.set_title('总车型占比')

        fig.tight_layout()
        #fig.show()
        fig.savefig('./assets/general/level.png')

dr = Draw()
