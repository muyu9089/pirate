#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 上午12:01
# @Author  : 
# @File    : settings.py
# @Description :

class Settings:

    def __init__(self):

        self.login_url = "https://passport2.eastmoney.com/pub/login?backurl=https%3A//quote.eastmoney.com/center/gridlist.html%23hs_a_board"

    def get_login_url(self):
        """

        @return: String url
        """
        return self.login_url