'''
Descripttion: 东方财富信息爬虫主函数
Author: 
version: v1
Date: 2024-10-23 22:55:39
LastEditors: yang fu ren
LastEditTime: 2024-10-24 01:05:14
'''
import requests 
import re
import pandas as pd

from settings import *

df = pd.DataFrame(columns=list(['代码', '名称', '最新价', '涨跌幅', '涨跌额', '成交量']))
 
response = requests.get('http://54.push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies, verify=False)

if response.status_code == 200:
    try:
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
        
        
        for i in range(20):
                list = [daimas[i], names[i], zuixinjias[i], zhangdiefus[i], zhangdiees[i], chengjiaoliangs[i]]
                df.loc[len(df)] = list
                
        print(df)
    except:
        print("响应内容错误")
else:
    print("请求失败， 状态码：{response.status_code}")