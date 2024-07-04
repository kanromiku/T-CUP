def find_price_range_intersection(price_range_strings):  
    # 将字符串转换为（min, max）元组  
    def convert_range(range_str):  
        parts = range_str.replace('万', '').split('-')  
        return (float(parts[0]) * 10000, float(parts[1]) * 10000)
    
    intersection = convert_range(price_range_strings[0])  
  
    # 遍历剩余的价格区间  
    for range_str in price_range_strings[1:]:  
        # 转换当前价格区间为（min, max）元组  
        current_range = convert_range(range_str)  
  
        # 当前区间与交集的交集  
        new_intersection = (  
            max(intersection[0], current_range[0]),    
            min(intersection[1], current_range[1])  
        )  
  
        # 检查新的交集是否有效  
        if new_intersection[0] > new_intersection[1]:  

            return None  
  
        # 更新交集  
        intersection = new_intersection  
   
    return intersection  
