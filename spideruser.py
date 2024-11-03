#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 上午12:05
# @Author  : 
# @File    : spideruser.py
# @Description :用于爬取东方财富用户持仓信息
import time
import pandas as pd
import threading

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

from settings import Settings
from plottable import PlotTable

edge_options = webdriver.EdgeOptions()
# 'detach' = True 将不会自动关闭
edge_options.add_experimental_option('detach', True)

# 加载驱动
service = Service(executable_path="./msedgedriver.exe")
driver_edge = webdriver.Edge(options=edge_options, service=service)


class UserSpider:

    def __init__(self, url):

        self.url = url

    def login(self):
        """
        @note: 登陆提示
        @return:
        """
        driver_edge.get(self.url)
        driver_edge.execute_script("alert('请先登陆账户');")
        WebDriverWait(driver_edge, 10).until(EC.alert_is_present())  # 等待 alert 出现，最多等10秒
        time.sleep(10)
        # 切换到 alert 对象，并点击“确定”
        alert = Alert(driver_edge)
        alert.accept()  # 点击弹窗的确定按钮

    def spider(self):
        """

        @return:
        """
        html = driver_edge.page_source
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find("div", class_='listtable')

        if table:

            table_head_list = self.get_table_head(table)
            table_body_lists = self.get_table_body(table)
            stock_df = self.build_dataframe(table_head_list, table_body_lists)
            return stock_df

    def show(self, plottable, table, model):

        while True:
            stock_df = self.spider()
            plottable.update(table, model, stock_df)

    def monitor(self, master, plottable, table, model):
        master.after(5000, self.show(plottable, table, model))

    @staticmethod
    def get_table_head(table):
        """
        @note: 获取持仓情况表头内容
        @return: List
        """

        thead = table.find("thead")
        if thead:
            tr = thead.find('tr')
            table_head_list = [table_head.text for table_head in tr.find_all('th') if table_head.text != '操作']
            return table_head_list

    @staticmethod
    def get_table_body(table):
        """
        @note: 获取持仓情况表主体内容
        @return: List
        """
        table_body_lists = []
        tbody = table.find("tbody")
        if tbody:
            for tr in tbody.find_all('tr'):
                table_body_list = []
                for table_body in tr.find_all('td'):
                    if table_body.text != ' 买 卖':
                        table_body_list.append(table_body.text)
                table_body_lists.append(table_body_list)

        return table_body_lists

    @staticmethod
    def build_dataframe(table_head_list, table_body_list):
        """
        @note: 构建DataFrame
        @param table_head_list: 持仓情况表头内容列表
        @param table_body_list: 持仓情况表内容列表
        @return: DataFrame
        """
        stock_df = pd.DataFrame(table_body_list, columns=table_head_list)
        return stock_df


if __name__ == "__main__":
    settings = Settings()
    stock_url = settings.get_login_url()

    user_spider = UserSpider(stock_url)
    user_spider.login()

    target_url = 'https://jywg.18.cn/Trade/Buy'
    while driver_edge.current_url != target_url:
        print("Waiting for logging!")
        time.sleep(30)

    plottable = PlotTable()
    stock_df = user_spider.spider()
    table, model, master = plottable.initialize_table(stock_df)
    table.show()

    # 主进程运行master，子线程运行更新代码
    t1 = threading.Thread(target=user_spider.monitor, args=(master, plottable, table, model))  # 监听数据并修改表格
    t1.start()
    master.mainloop()
