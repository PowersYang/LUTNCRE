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

            subject_dict = {'14': '二级C语言', '15': '二级JAva', '16': '三级网络技术', '24': '一级Office', '26': 'VB语言程序设计',
                            '28': 'Java语言程序设计', '29': 'Access数据库程序设计', '35': '网络技术', '36': '数据库技术',
                            '38': '信息安全技术', '39': '嵌入式系统开发技术', '41': '网络工程师', '42': '数据库工程师',
                            '44': '信息安全工程师', '45': '嵌入式系统开发工程师', '61': 'C++语言程序设计', '63': 'MySQL数据库程序设计',
                            '64': 'Web程序设计', '65': 'MS Office', '66': 'Python语言程序设计'}
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

    def pass_rate_fd(self):
        lt60 = self.df[self.df['cj'] < 60]['cj'].count()
        gt60 = self.df[self.df['cj'] < 90]['cj'].count() - lt60
        gt90 = self.df[self.df['cj'] >= 90]['cj'].count()

        data = [lt60, gt60, gt90]
        index = ['不及格', '合格', '优秀']

        return pd.Series(data, index=index)
