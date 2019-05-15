# -*- coding: utf-8 -*-

import pandas as pd


class Analysis():
    def __init__(self, date):
        self.date = date
        self.df = pd.read_csv('data/{}.csv'.format(self.date))

    def pass_rate(self, compute_by=None):

        if compute_by == 'college':
            res = self.df[self.df['cj'] >= 60].groupby('fy').count()['cj'] / \
                  self.df.groupby('fy').count()['cj']
            res = res.dropna()

            return res.round(3)
        elif compute_by == 'major':
            res = self.df[self.df['cj'] >= 60].groupby('专业名称_x').count()['cj'] / \
                  self.df.groupby('专业名称_x').count()['cj']
            res = res.dropna()

            return res.round(3)
        elif compute_by == 'subject':
            self.df['subject'] = self.df['zkzh'].map(lambda x: str(x)[0:2])

            subject = self.df[self.df['cj'] >= 60].groupby('subject').count()['cj'] / \
                  self.df.groupby('subject').count()['cj']

            subject_dict = {'14': '二级C语言', '15': '二级JAva', '16': '三级网络技术', '24': '一级Office', '26': 'a', '28': 'b',
                            '29': 'c', '35': 'd', '36': 'e', '38': 'f', '39': 'g', '41': 'h', '42': 'i', '44': 'g',
                            '45': 'k', '61': 'l', '63': 'm', '64': 'n', '65': 'o'}
            subject.rename(subject_dict, inplace=True)
            subject = subject.dropna()

            return subject.round(3)
        elif compute_by == 'jg':
            res = self.df[self.df['cj'] >= 60].groupby('籍贯').count()['cj'] / \
                  self.df.groupby('籍贯').count()['cj']
            res = res.dropna()

            return res.round(3)
        else:
            res = self.df[self.df['cj'] >= 60]['sfzh'].count() / self.df['sfzh'].count()

            return round(res, 3) * 100
