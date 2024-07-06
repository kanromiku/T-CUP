# 导入必要的库
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

from Tcrawler import Crawler

# 设置matplotlib字体为黑体
mpl.rcParams['font.sans-serif'] = ['SimHei']

# 定义三个目录路径用于存储不同类型的图表
path1 = "./assets/ev"
path2 = "./assets/fv"
path3 = "./assets/general"

# 如果目录不存在，则创建目录
if not os.path.exists(path1):
    os.makedirs(path1)
if not os.path.exists(path2):
    os.makedirs(path2)
if not os.path.exists(path3):
    os.makedirs(path3)

class Drawer(Crawler):
    """
    继承自Crawler类，用于绘制和保存各种汽车数据的图表。
    """
    def __init__(self):
        """
        初始化函数，执行数据提取、处理和图表绘制。
        """
        super().__init__()
        # 取消Pandas的链式赋值警告
        pd.options.mode.chained_assignment = None
        # 绘制新能源车和燃油车的价格与销量图
        self.ev_draw_price_and_sales()
        self.fv_draw_price_and_sales()
        # 绘制新能源车和燃油车的评分图
        self.ev_draw_score()
        self.fv_draw_score()
        # 绘制车型级别分布图
        self.level()

    def ev_draw_price_and_sales(self):
        """
        绘制新能源车的价格与销量图。
        """
        # 筛选新能源车数据并重置索引
        ev = self.df[self.df['Type'] == '新能源车']
        ev.reset_index(drop=True, inplace=True)
        # 提取销量数据
        ev_sales = ev.loc[:, 'Sales']
        # 计算中位价格
        for i in range(self.top):
            ev.loc[i, 'MPrice'] = (float(ev.loc[i, 'LPrice']) + float(ev.loc[i, 'HPrice'])) / 2
        ev_MPrice = ev.loc[:, 'MPrice']
        # 计算价格标准差
        std = []
        for i in range(self.top):
            x = float(ev.loc[i, 'HPrice']) - float(ev.loc[i, 'MPrice'])
            std.append(x)
        ev_label = ev.loc[:, 'Name']

        # 创建图表并设置参数
        fig = plt.figure(figsize=(12, 6), dpi=200)
        ax1 = fig.add_axes((0.1, 0.1, 0.8, 0.8))
        ax2 = ax1.twinx()

        # 绘制价格柱状图和销量折线图
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
        # 翻转销量轴
        ax2.invert_yaxis()

        # 设置轴标签和标题
        ax1.set_xlabel('名称')
        ax1.set_ylabel('价格（单位：万元）')
        ax1.set_title('新能源车报价及销量')
        ax2.set_ylabel('销量')
        ax1.tick_params(axis="x", labelrotation=30)

        # 保存图表
        fig.savefig('./assets/ev/price_and_sales.png')

    def fv_draw_price_and_sales(self):
        """
        绘制燃油车的价格与销量图。
        """
        # 筛选燃油车数据并重置索引
        fv = self.df[self.df['Type'] == '燃油车']
        fv.reset_index(drop=True, inplace=True)
        # 提取销量数据
        fv_sales = fv.loc[:, 'Sales']
        # 计算中位价格
        for i in range(self.top):
            fv.loc[i, 'MPrice'] = (float(fv.loc[i, 'LPrice']) + float(fv.loc[i, 'HPrice'])) / 2
        fv_MPrice = fv.loc[:, 'MPrice']
        # 计算价格标准差
        std = []
        for i in range(self.top):
            x = float(fv.loc[i, 'HPrice']) - float(fv.loc[i, 'MPrice'])
            std.append(x)
        fv_label = fv.loc[:, 'Name']

        # 创建图表并设置参数
        fig = plt.figure(figsize=(12, 6), dpi=200)
        ax3 = fig.add_axes((0.1, 0.1, 0.8, 0.8))
        ax4 = ax3.twinx()

        # 绘制价格柱状图和销量折线图
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
        # 翻转销量轴
        ax4.invert_yaxis()

        # 设置轴标签和标题
        ax3.set_xlabel('名称')
        ax3.set_ylabel('价格（单位：万元）')
        ax3.set_title('燃油车报价及销量')
        ax4.set_ylabel('销量')
        ax3.tick_params(axis="x", labelrotation=30)

        # 保存图表
        fig.savefig('./assets/fv/price_and_sales.png')

    def ev_draw_score(self):
        """
        绘制新能源车的评分散点图。
        """
        # 筛选新能源车数据并重置索引
        ev = self.df[self.df['Type'] == '新能源车']
        ev.reset_index(drop=True, inplace=True)
        ev_label = ev.loc[:, 'Name']
        ev_score = ev.loc[:, 'Score']

        # 创建图表并设置参数
        fig = plt.figure(figsize=(12, 6), dpi=200)
        ax1 = fig.add_axes((0.1, 0.1, 0.8, 0.8))

        # 绘制散点图
        ax1.scatter(ev_label, ev_score, color='green', marker='o')

        # 设置轴标签和标题
        ax1.set_xlabel('名称（销量自左往右从高到低）')
        ax1.set_ylabel('评分')
        ax1.set_title(f'新能源车销量top{self.top}评分')
        ax1.tick_params(axis="x", labelrotation=30)

        # 保存图表
        fig.savefig('./assets/ev/score.png')

    def fv_draw_score(self):
        """
        绘制燃油车的评分散点图。
        """
        # 筛选燃油车数据并重置索引
        fv = self.df[self.df['Type'] == '燃油车']
        fv.reset_index(drop=True, inplace=True)
        fv_label = fv.loc[:, 'Name']
        fv_score = fv.loc[:, 'Score']

        # 创建图表并设置参数
        fig = plt.figure(figsize=(12, 6), dpi=200)
        ax1 = fig.add_axes((0.1, 0.1, 0.8, 0.8))

        # 绘制散点图
        ax1.scatter(fv_label, fv_score, color='green', marker='o')

        # 设置轴标签和标题
        ax1.set_xlabel('名称（销量自左往右从高到低）')
        ax1.set_ylabel('评分')
        ax1.set_title(f'燃油车销量top{self.top}评分')
        ax1.tick_params(axis="x", labelrotation=30)

        # 保存图表
        fig.savefig('./assets/fv/score.png')

    def level(self):
        """
        绘制不同车型级别的占比饼图。
        """
        # 筛选并处理燃油车、新能源车和所有车型的数据
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

        # 创建包含三个子图的图表
        fig = plt.figure(figsize=(12, 6), dpi=200)
        fig1 = plt.subplot(1, 3, 1)
        fig2 = plt.subplot(1, 3, 2)
        fig3 = plt.subplot(1, 3, 3)

        # 绘制燃油车、新能源车和所有车型的占比饼图
        fig1.pie(
            fv_value,
            labels=fv_key,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 10},
            pctdistance=0.75,
            labeldistance=1.1,
        )
        fig1.set_title('燃油车车型占比')

        fig2.pie(
            ev_value,
            labels=ev_key,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 8},
            pctdistance=0.8,
            labeldistance=1.2,
        )
        fig2.set_title('新能源车车型占比')

        fig3.pie(
            general_value,
            labels=general_key,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 6.5},
            pctdistance=0.8,
            labeldistance=1.2
        )
        fig3.set_title('总车型占比')

        # 调整子图间距
        fig.tight_layout()
        # 保存图表
        fig.savefig('./assets/general/level.png')

# 实例化Drawer类，执行图表绘制
dr = Drawer()