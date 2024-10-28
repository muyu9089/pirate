#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 上午12:05
# @Author  : 
# @File    : spideruser.py
# @Description :用于爬取东方财富用户持仓信息
import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

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
        # driver = webdriver.Edge()
        driver_edge.get(self.url)
        driver_edge.execute_script("alert('请先登陆账户');")
        time.sleep(10)
        try:
            while driver_edge.window_handles:
                logged_url = driver_edge.current_url

        except:
            print("窗口关闭，程序停止")

        # driver_edge.find_element(By.XPATH, '//*[@id="txt_account"]').send_keys('')


if __name__ == "__main__":

    settings = Settings()
    stock_url = settings.get_login_url()

    user_spider = UserSpider(stock_url)
    user_spider.spider()
