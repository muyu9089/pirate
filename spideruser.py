#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 上午12:05
# @Author  : 
# @File    : spideruser.py
# @Description :用于爬取东方财富用户持仓信息
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup

from settings import Settings

edge_options = webdriver.EdgeOptions()
# 'detach' = True 将不会自动关闭
edge_options.add_experimental_option('detach', True)

# 加载驱动
service = Service(executable_path="./msedgedriver.exe")
driver_edge = webdriver.Edge(options=edge_options, service=service)


class UserSpider:

    def __init__(self, url):

        self.url = url

    def spider(self):
        """

        @return:
        """

        driver_edge.get(self.url)
        driver_edge.execute_script("alert('请先登陆账户');")
        time.sleep(10)
        while (True):
            if driver_edge.current_url == 'https://jywg.18.cn/Trade/Buy':
                time.sleep(10)
                html = driver_edge.page_source
                soup = BeautifulSoup(html, 'html.parser')

                table = soup.find("div", class_='listtable')

                if table:

                    table_head_list = self.get_table_head(table)
                    table_body_list = self.get_table_body(table)
                    self.build_dataframe(table_head_list, table_body_list)

    def get_table_head(self, table):
        """
        @note: 获取持仓情况表头内容
        @return: List
        """

        thead = table.find("thead")
        if thead:
            tr = thead.find('tr')
            table_head_list = [table_head.text for table_head in tr.find_all('th') if table_head.text != '操作']
            return table_head_list

    def get_table_body(self, table):
        """
        @note: 获取持仓情况表主体内容
        @return: List
        """

        tbody = table.find("tbody")
        if tbody:
            for tr in tbody.find_all('tr'):
                table_body_list = [table_body.text for table_body in tr.find_all('td') if table_body.text != ' 买 卖']
                return table_body_list

    # def build_dataframe(self, table_head_list, table_body_list):
    #     """
    #
    #     @param table_head_list: 持仓情况表头内容列表
    #     @param table_body_list: 持仓情况表内容列表
    #     @return: DataFrame
    #     """
    #     stock_df = pd.DataFrame(table_body_list, columns=table_head_list)
    #     print(stock_df)


if __name__ == "__main__":
    settings = Settings()
    stock_url = settings.get_login_url()

    user_spider = UserSpider(stock_url)
    user_spider.spider()
