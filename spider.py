'''
Descripttion: 
Author: yang fu ren
version: 
Date: 2024-10-23 22:55:39
LastEditors: yang fu ren
LastEditTime: 2024-10-25 00:05:35
'''
'''
Descripttion: 东方财富信息爬虫主函数
Author: 
version: v1
Date: 2024-10-23 22:55:39
LastEditors: yang fu ren
LastEditTime: 2024-10-24 23:40:34
'''
import requests 
import re
import pandas as pd

from settings import Settings

class Spider:
    
    def __init__(self, url, headers, params, cookies, verify, stock_df):
         self.url = url
         self.headers = headers
         self.params = params
         self.cookies = cookies
         self.verify = verify
         self.stock_df = stock_df
         
    def get_respones_from_url(self):
        try:
            response = requests.get(url=self.url, headers=self.headers, params=self.params, cookies=self.cookies, verify=self.verify)
        
            return response
        except requests.exceptions.RequestException as e:
            print(f"请求错误，错误信息：{e}")
    
    def get_stock_info_from_respones(self):
        
        response = self.get_respones_from_url()
        
         # 正则获取相关信息
        daimas = re.findall('"f12":(.*?),',response.text)
        names = re.findall('"f14":"(.*?)"',response.text)
        zuixinjias = re.findall('"f2":(.*?),',response.text)
        zhangdiefus = re.findall('"f3":(.*?),',response.text)
        zhangdiees = re.findall('"f4":(.*?),',response.text)      
        chengjiaoliangs = re.findall('"f5":(.*?),',response.text)       
        chengjiaoes = re.findall('"f6":(.*?),',response.text)
        zhenfus = re.findall('"f7":(.*?),',response.text)       
        zuigaos = re.findall('"f15":(.*?),',response.text)        
        zuidis = re.findall('"f16":(.*?),',response.text)        
        jinkais = re.findall('"f17":(.*?),',response.text)        
        zuoshous = re.findall('"f18":(.*?),',response.text)       
        liangbis = re.findall('"f10":(.*?),',response.text)        
        huanshoulvs = re.findall('"f8":(.*?),',response.text)       
        shiyinglvs = re.findall('"f9":(.*?),',response.text)
        
        if response.status_code == 200:
                for i in range(20):
                        list = [daimas[i], names[i], zuixinjias[i], zhangdiefus[i], zhangdiees[i], chengjiaoliangs[i]]
                        self.stock_df.loc[len(self.stock_df)] = list
        else:
            print("请求失败， 状态码：{response.status_code}")


if __name__ == "__main__":
    
    columns = ['代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量']
    stock_df = pd.DataFrame(columns=columns)
    
    for page in range(1, 20):
        
        settings = Settings(page)
    
        spider = Spider(settings.url, settings.headers, settings.params, settings.cookies, False, stock_df)
        spider.get_stock_info_from_respones()

    print(f"stock_df: {stock_df}")