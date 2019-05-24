#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd


class Clean():
    def __init__(self, date):
        self.date = date

        self.df = pd.read_excel('data/{}bb.xlsx'.format(self.date))
        self.df.columns = [col.lower() for col in self.df]

        self.df_xq = pd.read_excel('data/{}xq.xlsx'.format(self.date))
        self.df_xq.columns = [col.lower() for col in self.df_xq]
        self.df = self.df.append(self.df_xq)

        self.students_lib = pd.read_excel('data/兰州理工大学在籍学籍库.xlsx')
        self.students_lib.columns = [col.lower() for col in self.students_lib]

        self.students_list = pd.read_excel('data/在籍在校学生名单.xls')
        self.students_list.columns = [col.lower() for col in self.students_list]
        self.students_list = self.students_list[~self.students_list['籍贯'].isin(['土库曼斯坦', '塔吉克斯坦', '美国'])]

        self.df = pd.merge(self.students_lib, self.df, left_on='sfzh', right_on='zjh')
        self.df = pd.merge(self.df, self.students_list, left_on='sfzh', right_on='身份证号')

    def save2csv(self):
        filename = 'data/{}.csv'.format(self.date)
        self.df.to_csv(filename)


c1 = Clean(201803)
c2 = Clean(201809)
c3 = Clean(201709)

c1.save2csv()
c2.save2csv()
c3.save2csv()
