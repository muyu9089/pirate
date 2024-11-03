#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/10/31 下午11:48
# @Author  : 
# @File    : plottable.py
# @Description : 绘制持仓情况动态展示表格
from tkintertable import TableCanvas, TableModel
from tkinter import *
import tkinter
import time


class PlotTable:

    def initialize_table(self, stock_df):
        """
        @note: 初始化表格
        @param stock_df:
        @return:
        """
        # 初始化字典并添加第一行
        table_data = {
            '0': {'证券代码': '', '证券名称': '', '持仓数量': '', '可用数量': '', '成本价': '', '当前价': '', '最新市值': '', '持仓盈亏': '', '持仓盈亏比例': '', '当日盈亏': '', '当日盈亏比例': ''}
        }

        # 根据DataFrame的行数添加后续行
        for i in range(len(stock_df) - 1):
            row_key = f'{i + 1}'  # 从 'row2' 开始
            table_data[row_key] = {
                '证券代码': '',
                '证券名称': '',
                '持仓数量': '',
                '可用数量': '',
                '成本价': '',
                '当前价': '',
                '最新市值': '',
                '持仓盈亏': '',
                '持仓盈亏比例': '',
                '当日盈亏': '',
                '当日盈亏比例': ''
            }

        master = tkinter.Tk()  # 主窗口
        master.geometry('600x400')

        tframe = Frame(master)  # 子窗口
        tframe.pack()  # 布局

        model = TableModel()
        model.importDict(table_data)

        table = TableCanvas(tframe, model=model)  # table组件挂载到frame子窗口上
        return table, model, master

    def update(self, table, model, stock_df):
        """
        @note: 更新表格数据
        @param stock_df:
        @param model:
        @param table:
        @return:
        """
        time.sleep(5)
        table_data = {}
        for i in range(len(stock_df)):
            table_data[f'{i}'] = {
                '证券代码': stock_df.iloc[i, 0],
                '证券名称': stock_df.iloc[i, 1],
                '持仓数量': stock_df.iloc[i, 2],
                '可用数量': stock_df.iloc[i, 3],
                '成本价': stock_df.iloc[i, 4],
                '当前价': stock_df.iloc[i, 5],
                '最新市值': stock_df.iloc[i, 6],
                '持仓盈亏': stock_df.iloc[i, 7],
                '持仓盈亏比例': stock_df.iloc[i, 8],
                '当日盈亏': stock_df.iloc[i, 9],
                '当日盈亏比例': stock_df.iloc[i, 10]
            }

        model.importDict(table_data)
        table.redraw()

