#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 上午12:01
# @Author  : 
# @File    : settings.py
# @Description :

class Settings:

    def __init__(self):

        self.login_url = "https://jywg.18.cn/Login?el=1&clear=1"

    def get_login_url(self):
        """

        @return: String url
        """
        return self.login_url