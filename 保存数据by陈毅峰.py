import pandas as pd  
  
class Crawler:  
    # ... 之前的代码 ...  
  
    def save_to_file(self, filename, file_format):  
        # 将新能源车和燃油车的数据合并到一个DataFrame中  
        all_cars = self.ev_cars + self.fuel_cars  
        df = pd.DataFrame(all_cars)  
  
        # 将DataFrame保存到文件  
        if file_format == 'xlsx':  
            df.to_excel(filename, index=False)  
        elif file_format == 'csv':  
            df.to_csv(filename, index=False, encoding='utf-8-sig')  # 对于中文文件名和中文列名，可能需要使用utf-8-sig编码  
        else:  
            print(f"Unsupported file format: {file_format}")  
  
# 使用示例  
crawler = Crawler(top=10)  
crawler.crawl()  
crawler.save_to_file('cars_data.xlsx', 'xlsx')  # 保存为Excel文件  
crawler.save_to_file('cars_data.csv', 'csv')  # 保存为CSV文件
