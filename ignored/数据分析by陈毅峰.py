import pandas as pd  
  
# 示例数据  
data = [  
    {'Name': 'Alice', 'Price': 164500},  # 假设这里的单位是元  
    {'Name': 'Bob', 'Price': 275000},  
    {'Name': 'Charlie', 'Price': 195000},  
    # ... 更多的数据  
]  
  
# 将数据转换为DataFrame  
df = pd.DataFrame(data)  
  
# 定义价格区间的边界，例如每10万一个区间  
bins = [i*100000 for i in range(min(df['Price'])//100000, max(df['Price'])//100000 + 2)]  
  
# 创建一个新的列，为每个价格区间分配中点值作为代表数  
df['RepresentativePrice'] = pd.cut(df['Price'], bins=bins, labels=False, right=False).apply(lambda x: (bins[x] + bins[x+1]) / 2)  
  
# 显示结果  
print(df)  
  
# 计算基于代表数的中位数  
median_rep_price = df['RepresentativePrice'].median()  
print(f"The median representative price is: {median_rep_price}元")  
  
# 计算基于代表数的众数（注意：对于浮点数，众数可能不太准确）  
mode_rep_price = df['RepresentativePrice'].mode().iloc[0]  # 假设只有一个众数，或者选择最常见的值  
print(f"The mode representative price is: {mode_rep_price}元")  
  
# 如果需要，将结果保存到文件  
df.to_csv('output_with_representative_prices.csv', index=False)
